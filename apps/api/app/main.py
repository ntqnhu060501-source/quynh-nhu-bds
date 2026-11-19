from __future__ import annotations

import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, field_validator

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = Path(os.getenv("DB_PATH", str(BASE_DIR / "quynh_nhu_bds.sqlite3")))
DB_PATH.parent.mkdir(parents=True, exist_ok=True)


@contextmanager
def db() -> Iterator[sqlite3.Connection]:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def init_db() -> None:
    with db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS properties (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                area_m2 REAL,
                price_text TEXT,
                location TEXT NOT NULL DEFAULT 'Cam Lâm, Khánh Hòa',
                status TEXT NOT NULL DEFAULT 'draft',
                description TEXT NOT NULL DEFAULT '',
                verified_at TEXT,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS leads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                need TEXT NOT NULL DEFAULT '',
                source TEXT NOT NULL DEFAULT 'website',
                consent INTEGER NOT NULL DEFAULT 0,
                status TEXT NOT NULL DEFAULT 'new',
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )
        """)


app = FastAPI(
    title="Quỳnh Như BDS API",
    version="0.1.0",
    description="API nền tảng website và tiếp nhận khách hàng Quỳnh Như BDS.",
)

origins = [x.strip() for x in os.getenv("CORS_ORIGINS", "http://127.0.0.1:8000,http://localhost:8000").split(",") if x.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


class LeadIn(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    phone: str = Field(min_length=8, max_length=20)
    need: str = Field(default="", max_length=2000)
    source: str = Field(default="website", max_length=100)
    consent: bool

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, value: str) -> str:
        normalized = "".join(ch for ch in value if ch.isdigit() or ch == "+")
        if len(normalized) < 9:
            raise ValueError("Số điện thoại chưa hợp lệ")
        return normalized


@app.on_event("startup")
def startup() -> None:
    init_db()


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "quynh-nhu-bds-api", "version": "0.1.0"}


@app.get("/api/properties")
def list_properties() -> list[dict]:
    # Public endpoint only returns explicitly published records.
    with db() as conn:
        rows = conn.execute(
            """SELECT id, title, area_m2, price_text, location, description
               FROM properties WHERE status = 'published'
               ORDER BY created_at DESC"""
        ).fetchall()
    return [dict(row) for row in rows]


@app.post("/api/leads", status_code=201)
def create_lead(payload: LeadIn, request: Request) -> dict[str, str]:
    if not payload.consent:
        raise HTTPException(status_code=400, detail="Cần xác nhận đồng ý để được liên hệ.")
    with db() as conn:
        conn.execute(
            """INSERT INTO leads (name, phone, need, source, consent)
               VALUES (?, ?, ?, ?, ?)""",
            (payload.name.strip(), payload.phone, payload.need.strip(), payload.source, 1),
        )
    return {"status": "received", "message": "Thông tin đã được tiếp nhận."}
