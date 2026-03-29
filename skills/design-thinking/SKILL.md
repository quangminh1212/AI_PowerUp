---
name: design-thinking
description: Áp dụng quy trình Design Thinking (Thấu hiểu - Xác định - Lên ý tưởng - Prototype - Kiểm tra) để tạo ra sản phẩm hoàn hảo, tập trung vào người dùng trước khi viết code.
---

# Design Thinking (Tư Duy Thiết Kế Lấy Người Dùng Làm Trung Tâm)

## Mục đích
Hạn chế việc AI tạo ra những ứng dụng "chạy được nhưng xấu" hoặc "đúng tính năng nhưng khó dùng" (Poor UX). Design thinking ép AI phải sống trong đầu người dùng cuối trước khi gõ phím.

## 5 Bước Bắt Buộc (Mandatory 5-Step Process)

### Bước 1: Empathize (Thấu Hiểu Người Dùng)
- Đặt câu hỏi: Ai là người trực tiếp bấm vào nút này? Họ đang ở tâm trạng bực bội, vội vàng chờ load, hay thoải mái lướt web?
- Device (Mobile chạm tay hay Desktop click chuột).

### Bước 2: Define (Định Nghĩa Vấn Đề)
- Gói gọn mục tiêu vào một câu (Ví dụ: "Người ta vào trang này chỉ để tìm BẢNG GIÁ thật nhanh, không phải để đọc giới thiệu 1000 chữ").

### Bước 3: Ideate (Lên Ý Tưởng Siêu Tốc)
- Liệt kê 3 Option giao diện:
  + Option 1 (Đơn giản nhất, an toàn nhất).
  + Option 2 (Đẹp, dùng Animation trơn tru Glassmorphism/Tailwind hiện tại).
  + Option 3 (Đột phá về UX). 
- Chọn Option tốt nhất chốt lại với User.

### Bước 4: Prototype (Bản Nháp Nhanh)
- In ra một Cấu trúc Khung xương Markdown/ASCII thay vì Code dài loằng ngoằng. Hoặc viết nhanh 1 đoạn HTML/CSS Tailwind giả lập để người dùng xem trước bộ form/hiệu ứng. 

### Bước 5: Test (Kiểm Soát Lỗi UX)
- Nhấn thử button trên điện thoại ảo (Mobile viewport). Chữ có quá bé không? Màu có tương phản kém không (Contrast Ratio)?
- Đã chuẩn bị sẵn Loading Spinner và Empty State chưa?

## Khi nào sử dụng
- Khi user yêu cầu: *"Thiết kế giúp tao trang Web mới"* hoặc *"UI cũ xấu quá, vẽ lại đi."*
