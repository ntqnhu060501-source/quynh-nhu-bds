# Chạy thử trên máy cá nhân

## API
Cài Python 3.11+, mở terminal:

```bash
cd apps/api
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS/Linux
# source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Kiểm tra:
- Health: http://127.0.0.1:8000/api/health
- API docs: http://127.0.0.1:8000/docs
- Danh sách sản phẩm đã duyệt: http://127.0.0.1:8000/api/properties

Chạy kiểm thử: `pytest -q`.

## Website
Mở `apps/web/index.html` để xem giao diện tĩnh. Biểu mẫu gửi dữ liệu cần API chạy tại cùng origin hoặc cấu hình reverse proxy. Ở bản hiện tại API chưa phục vụ trực tiếp thư mục frontend; không coi việc mở file HTML là website đã triển khai công khai.

## Trạng thái và giới hạn hiện tại
Đây là nền móng kỹ thuật giai đoạn đầu, chưa phải hệ thống production:
- Chưa có đăng nhập admin, phân quyền hoặc CRUD quản trị.
- Chưa có CRM giao diện; lead hiện được lưu trong SQLite phía API.
- Chưa cấu hình hosting/domain/HTTPS.
- Chưa có sao lưu tự động, giám sát hoặc quy trình xóa dữ liệu theo yêu cầu.
- Chưa đưa bất kỳ sản phẩm bất động sản thật nào lên website vì chưa có bộ dữ liệu được xác minh và duyệt.

Không nhập dữ liệu khách hàng thật cho tới khi hoàn tất xác thực, bảo mật, sao lưu và triển khai HTTPS.
