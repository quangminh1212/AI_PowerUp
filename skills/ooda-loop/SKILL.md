---
name: ooda-loop
description: Vòng lặp OODA (Quan sát - Định hướng - Quyết định - Hành động) dùng để xử lý sự cố khẩn cấp, gỡ lỗi (debug) nhanh hoặc đối phó với các vấn đề liên tục thay đổi.
---

# OODA Loop (Vòng lặp Phản ứng Nhanh)

## Mục đích
Được khởi xướng bởi Không lực Hoa Kỳ, OODA Loop giúp AI xử lý những tình huống "Mã đang chạy tự nhiên lỗi, log mù mờ, không biết lỗi ở đâu" cực kỳ nhanh, vượt qua giới hạn của tư duy phản xạ thông thường. Giúp tác chiến nhanh nhất có thể.

## Quy trình ép buộc (Mandatory Process)

Khi bật kỹ năng này, AI sẽ lặp đi lặp lại 4 bước siêu tốc này cho đến khi diệt xong Bug:

### 1. Observe (Quan sát)
- Thu thập mọi log lỗi, stack trace mới nhất.
- Đọc lại mã nguồn hiện hành và trạng thái môi trường. KHÔNG LÀM GÌ CẢ ngoài nhìn và nhặt data.

### 2. Orient (Định hướng & Liên kết)
- Phân tích data vừa nhặt: Lỗi này giống lỗi nào từng gặp? 
- Tổng hợp lại bối cảnh (Ví dụ: Server vừa update package phụ thuộc (dependency) -> lỗi).

### 3. Decide (Quyết định Giả thuyết)
- Đưa ra 1 (và chỉ 1) giả thuyết khả thi nhất ngay lúc này. 
- Đề xuất 1 bản sửa lỗi thử nghiệm nhỏ nhất (MVP Fix) hoặc 1 lệnh kiểm tra (probe).

### 4. Act (Hành động & Phản hồi)
- Chạy lệnh test hoặc áp dụng sửa lỗi ngay.
- Quay lại Bước 1 (Observe) ngay lập tức với kết quả mới (Thành công hay ra log lỗi mới?). Lặp lại vòng OODA trong tích tắc!

## Khi nào sử dụng
- Khi hệ thống bị sập (Production Down) cần cứu nguy.
- Lỗi biên dịch (Compile Error)/Lỗi Runtime xảy ra liên tục mà không hiểu tại sao.
- Khi người dùng bảo: *"Tự sửa cái bug củ chuối này đi, dùng OODA loop!"*
