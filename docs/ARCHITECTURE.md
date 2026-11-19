# Kiến trúc nền tảng Quỳnh Như BDS

## Mục tiêu sản phẩm
Một hệ thống thống nhất phục vụ hai mục tiêu: xây dựng thương hiệu chuyên môn tại Cam Lâm và chuyển đổi khách quan tâm thành cơ hội mua bất động sản.

## Phân hệ đích
1. Website công khai: giới thiệu thương hiệu, bất động sản, bài phân tích, biểu mẫu liên hệ.
2. CMS/BĐS: quản lý lô đất, hình ảnh, giá, trạng thái, hồ sơ pháp lý và lịch sử cập nhật.
3. CRM: khách hàng, nhu cầu, nguồn khách, người phụ trách, lịch sử chăm sóc, nhắc việc.
4. Trung tâm nội dung: chủ đề, kịch bản, lịch đăng, thư viện media, hiệu quả nội dung.
5. Kho tri thức Cam Lâm: tài liệu quy hoạch/pháp lý, metadata nguồn, ngày ban hành, cơ quan ban hành, trạng thái hiệu lực, trích dẫn.
6. AI: trợ lý tra cứu có dẫn nguồn; hỗ trợ viết kịch bản; quy trình sản xuất video; không tự kết luận pháp lý.
7. Bản đồ: vị trí tài sản và lớp thông tin quy hoạch có nguồn xác minh.
8. Quản trị: tài khoản, vai trò, nhật ký, sao lưu, quyền truy cập.

## Kiến trúc kỹ thuật
- Frontend: HTML/CSS/JS giai đoạn nền; có thể nâng cấp React/Next khi nhu cầu thực tế yêu cầu.
- Backend: FastAPI, REST API, Pydantic.
- CSDL: SQLite cho phát triển một máy; PostgreSQL cho production/multi-user.
- Media: local trong phát triển; object storage khi triển khai.
- AI: adapter độc lập, ưu tiên mô hình local/Ollama; website vẫn hoạt động khi AI tắt.

## Nguyên tắc dữ liệu
- Phân biệt dữ liệu đã xác minh, đang kiểm tra và do người dùng cung cấp.
- Không tự tạo giá, diện tích, pháp lý, quy hoạch, tiến độ dự án.
- Lưu nguồn và thời điểm kiểm chứng cho mọi tuyên bố quan trọng.
- Không đưa thông tin khách hàng lên website công khai.
- Chưa đưa dữ liệu thật vào hệ thống cho đến khi có quy trình sao lưu và bảo vệ phù hợp.

## Các giai đoạn
- G0: repository, cấu trúc, quy tắc kỹ thuật và bảo mật.
- G1: website công khai + API tiếp nhận lead + danh mục tài sản.
- G2: admin, CRM, xác thực, phân quyền, audit log.
- G3: kho tri thức và tra cứu tài liệu có trích dẫn.
- G4: AI nội dung và Creative Studio.
- G5: bản đồ, media, tìm kiếm nâng cao.
- G6: kiểm thử bảo mật, backup, monitoring, triển khai production.
