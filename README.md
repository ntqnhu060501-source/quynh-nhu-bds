# QUỲNH NHƯ BDS

Nền tảng kinh doanh bất động sản Cam Lâm: website giới thiệu sản phẩm, tiếp nhận khách hàng và các mô-đun quản trị/AI theo từng giai đoạn.

## Nguyên tắc triển khai
- Ưu tiên chi phí 0 đồng ở giai đoạn đầu; các dịch vụ có giới hạn miễn phí phải được kiểm tra trước khi dùng production.
- Không đăng lô đất, giá, pháp lý hoặc tiến độ nếu chưa được xác minh.
- Không đưa dữ liệu khách hàng, giấy tờ cá nhân, mật khẩu hoặc khóa bí mật vào Git.
- Mỗi giai đoạn phải có kiểm thử và tiêu chí nghiệm thu.

## Kiến trúc hiện tại
- `apps/web`: website thương hiệu responsive bằng HTML/CSS/JavaScript.
- `apps/api`: REST API FastAPI.
- SQLite: cơ sở dữ liệu local cho giai đoạn phát triển.
- AI: mô-đun tùy chọn; website cơ bản không phụ thuộc AI.

## Chạy API local
Yêu cầu Python 3.11+.

```bash
cd apps/api
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

- Health: http://127.0.0.1:8000/api/health
- API docs: http://127.0.0.1:8000/docs
- Danh sách sản phẩm đã duyệt: http://127.0.0.1:8000/api/properties
- Kiểm thử: `pytest -q` trong `apps/api`.

Xem [hướng dẫn chạy local](docs/LOCAL_DEVELOPMENT.md) và [kiến trúc](docs/ARCHITECTURE.md).

## Trạng thái đã xác minh trong mã nguồn
- [x] Website giới thiệu thương hiệu.
- [x] API health check.
- [x] API công khai chỉ trả sản phẩm có trạng thái `published`.
- [x] API tiếp nhận khách hàng, yêu cầu đồng ý liên hệ.
- [x] Kiểm thử khói cho health, danh mục và consent.
- [ ] Admin đăng nhập, CRUD bất động sản và xác thực an toàn.
- [ ] CRM giao diện, lịch sử chăm sóc, phân quyền và audit log.
- [ ] Kho tri thức Cam Lâm có trích dẫn tài liệu.
- [ ] AI Creative Studio và quy trình sản xuất nội dung.
- [ ] Bản đồ, lưu trữ media, backup và triển khai production.

## Giới hạn bảo mật
Bản hiện tại chưa phải production. Chưa nhập dữ liệu khách hàng thật; chưa mở API lead ra Internet trước khi hoàn thiện xác thực, rate limit/chống spam, HTTPS, backup và quy trình bảo vệ dữ liệu.
