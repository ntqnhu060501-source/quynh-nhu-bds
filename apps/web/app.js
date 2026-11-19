const API_BASE = window.QUYNH_NHU_API_BASE || "";
const year = document.querySelector("#year");
if (year) year.textContent = new Date().getFullYear();

async function loadProperties() {
  const container = document.querySelector("#property-list");
  if (!container) return;
  try {
    const response = await fetch(`${API_BASE}/api/properties`);
    if (!response.ok) throw new Error("Không tải được danh mục");
    const properties = await response.json();
    if (!properties.length) return;
    container.replaceChildren(...properties.map((item) => {
      const card = document.createElement("article");
      card.className = "property-card";
      const title = document.createElement("h3");
      title.textContent = item.title;
      const meta = document.createElement("p");
      meta.textContent = [item.area_m2 ? `${item.area_m2} m²` : "", item.location, item.price_text || ""].filter(Boolean).join(" · ");
      const desc = document.createElement("p");
      desc.textContent = item.description || "";
      card.append(title, meta, desc);
      return card;
    }));
  } catch {
    // The static website remains usable while the API is offline.
  }
}

const form = document.querySelector("#lead-form");
form?.addEventListener("submit", async (event) => {
  event.preventDefault();
  const status = document.querySelector("#form-status");
  const data = new FormData(form);
  const payload = {
    name: String(data.get("name") || "").trim(),
    phone: String(data.get("phone") || "").trim(),
    need: String(data.get("need") || "").trim(),
    consent: data.get("consent") === "on",
    source: "website"
  };
  const button = form.querySelector("button[type=submit]");
  button.disabled = true;
  status.textContent = "Đang gửi thông tin…";
  try {
    const response = await fetch(`${API_BASE}/api/leads`, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(payload)
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.detail || "Chưa gửi được thông tin.");
    form.reset();
    status.textContent = "Như đã nhận được thông tin. Cảm ơn anh/chị!";
  } catch (error) {
    status.textContent = error.message || "Chưa kết nối được máy chủ. Anh/chị vui lòng thử lại sau.";
  } finally {
    button.disabled = false;
  }
});

loadProperties();
