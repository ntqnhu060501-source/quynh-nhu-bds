# QUỲNH NHƯ BDS

Nền tảng kinh doanh bất động sản Cam Lâm: website giới thiệu sản phẩm, tiếp nhận khách hàng, quản trị dữ liệu và các mô-đun AI.

## Nguyên tắc
- Ưu tiên chi phí vận hành 0 đồng ở giai đoạn đầu.
- Không đăng thông tin lô đất, giá, pháp lý hoặc tiến độ nếu chưa được xác minh.
- Dữ liệu khách hàng và thông tin nội bộ không đưa vào mã nguồn.
- Xây từng giai đoạn, kiểm thử trước khi phát hành.

## Kiến trúc khởi đầu
- `apps/web`: giao diện website responsive.
- `apps/api`: REST API Python/FastAPI.
- SQLite ở local; thiết kế để chuyển PostgreSQL khi triển khai nhiều người dùng.
- AI là mô-đun tùy chọn; không phụ thuộc dịch vụ trả phí để website cơ bản hoạt động.

## Chạy local
Yêu cầu Python 3.11+.

```bash
cd apps/api
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Mở API docs tại http://127.0.0.1:8000/docs.

Website tĩnh hiện ở `apps/web/index.html`. Trong giai đoạn kế tiếp sẽ nối website với API, hoàn thiện quản trị, xác thực và quy trình triển khai.

## Trạng thái
- [x] Repository và kiến trúc ban đầu.
- [x] API nền: health check, danh sách bất động sản, tiếp nhận khách hàng.
- [ ] Quản trị đăng nhập và CRUD đầy đủ.
- [ ] CRM, phân quyền, nhật ký hoạt động.
- [ ] Kho tri thức Cam Lâm có trích dẫn nguồn.
- [ ] AI Creative Studio.
- [ ] Bản đồ, lưu trữ ảnh/tài liệu và triển khai production.

## Bảo mật
Không commit `.env`, database, token, mật khẩu, dữ liệu khách hàng hoặc giấy tờ pháp lý cá nhân. Xem `.env.example`.
