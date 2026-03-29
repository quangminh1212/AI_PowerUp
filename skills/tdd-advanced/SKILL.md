---
name: tdd-advanced
description: Vòng lặp Đỏ-Xanh-Tái cấu trúc (Red-Green-Refactor) bắt buộc trước mọi đoạn code nhằm loại bỏ rủi ro tạo rác trong hệ thống và bảo hành tính năng chạy mãi mãi.
---

# TDD Advanced (Test-Driven Development Nâng Cao)

## Mục đích
Khi một tính năng sinh ra mà không có cách chống đứt, tính năng đó có xu hướng trở thành "bom nổ chậm" mỗi lần nâng cấp (Update v2). Kỹ năng này đóng chặt tư duy: "Code không có Test thì Không Phải Là Code, mà chỉ là bản dáp." 

## Quy trình ép buộc (Mandatory Process)

### Bước 1: RED (Viết Failed Test Trc Tiên)
- AI không được viết Code Chạy, BẮT BUỘC phải viết Kịch bản Test sai trước.
- Assert cái gì sẽ xảy ra? Cái gì là đầu vào (Input) và đầu ra lỗi (Expected Error).
- Chạy thử cho đến khi màn hình báo Vàng/Đỏ (Failed test! - Bởi vì hàm chưa được code!).

### Bước 2: GREEN (Viết Code Để Đạt Màu Xanh)
- Quay lại hiện trường viết hàm cần xử lý, với logic ngu ngốc nhất và đơn giản nhất (Hardcode cũng được) - Làm sao để Test chuyển sang Đỏ thành Xanh Lục.
- Hoàn thành Minimal Viable Logic.

### Bước 3: REFACTOR (Tối Ưu & Thu Dọn Bãi Rác)
- Khi code đã bảo đảm đỗ test, AI phải tiến hành chẻ logic ra làm 3 phần sạch sẽ nhất.
- Kiểm tra lại các biến dư thừa. Đổi tên hàm củ chuối (Naming Convesion) thành tên rành mạch.
- Lợi ích lớn nhất là lúc này Code dù đổi bao nhiêu lớp thuật toán, Test vẫn tự check màu Xanh thay cho bộ não AI. Không phải lo phá vỡ tính năng.

### Bước 4: Tự Định Bản Update (Maintainability Test) 
- Mất bao lâu nếu dev khác mở cái test case này ra đọc hiểu? Nhanh nhất có thể.

## Khi nào sử dụng
- Khi viết các function/utilities cốt lõi của Backend, các hàm xử lý Payment, Parsing Date/Time, Password.
- Khi user bảo: *"Viết hàm này cực kĩ cho tao, đảm bảo bug free."*
