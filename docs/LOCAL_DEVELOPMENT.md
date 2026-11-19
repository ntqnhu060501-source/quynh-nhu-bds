# Chạy website Quỳnh Như BDS trên Windows

## Cách nhanh nhất
1. Tải mã nguồn từ nhánh `phase-1/website-api-hardening` hoặc clone repo.
2. Cài Python 3.11+ nếu máy chưa có.
3. Mở thư mục `apps/api`.
4. Nhấp đúp `run-local.bat`. Lần đầu chương trình tạo môi trường Python và cài thư viện cần thiết.
5. Khi cửa sổ máy chủ hiện thông báo Uvicorn đang chạy, mở trình duyệt tại http://127.0.0.1:8000.
6. Giữ cửa sổ máy chủ mở khi sử dụng. Nhấn Ctrl+C để dừng.

## Chạy bằng terminal
```bash
cd apps/api
python -m venv .venv
```
Windows PowerShell:
```powershell
.venv\\Scripts\\Activate.ps1
```
macOS/Linux:
```bash
source .venv/bin/activate
```
Cài và chạy:
```bash
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

## Địa chỉ kiểm tra
- Website: http://127.0.0.1:8000/
- API health: http://127.0.0.1:8000/api/health
- API docs: http://127.0.0.1:8000/docs
- Danh sách bất động sản đã duyệt: http://127.0.0.1:8000/api/properties

Chạy kiểm thử trong `apps/api`: `pytest -q`.

## Giới hạn và an toàn dữ liệu
Đây là bản chạy local, chưa phải website công khai trên Internet:
- Chưa có đăng nhập admin, phân quyền hoặc CRUD quản trị.
- Chưa có CRM giao diện; lead hiện lưu trong SQLite local.
- Chưa cấu hình hosting/domain/HTTPS hoặc sao lưu tự động.
- Chưa đưa bất kỳ sản phẩm thật nào lên website vì chưa có bộ dữ liệu đã xác minh và duyệt.
- Không nhập dữ liệu khách hàng thật cho tới khi hoàn tất xác thực, chống spam, HTTPS, backup và quy trình bảo vệ dữ liệu.
