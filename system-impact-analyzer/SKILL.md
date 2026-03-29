---
name: system-impact-analyzer
description: Phân tích đánh giá vòng đời và hậu quả kéo theo (Ripple Effect) trước khi thay đổi bất kì file/tính năng quan trọng nào.
---

# System Impact Analyzer (Phân Tích Tác Động Hệ Thống)

## Mục đích
Khi một tính năng được phát triển hoặc điều chỉnh, AI thường chỉ nhìn dưới góc độ hẹp của một file/cái module. Kỹ năng này bắt buộc cái nhìn bao quát (Bird-eye View) để tránh sửa cái này hỏng ba cái khác.

## Quy trình ép buộc (Mandatory Process)

### Bước 1: Dependency Mapping
- Hãy list ra mọi thành phần, module, hay API trực tiếp liên quan đến điểm thay đổi định làm. Mãi cho đến Front-end, Back-end, DB.

### Bước 2: Liệt kê Nguy Cơ Rủi Ro Dây Chuyền (Ripple Effects)
- Thay đổi này trong module auth có lỡ làm sập luồng đăng nhập của legacy system hay token cũ chưa hết hạn không?
- Thay đổi schema ở DB có tương thích lùi (backward compatibility) không?
- Thay đổi UI, màu sắc này có phá vỡ tiêu chuẩn quốc tế và nguyên tắc responsive hiện tại không?

### Bước 3: Actionable Mít Gation (Kế hoạch phòng trừ)
- Trước khi code file này, hãy liệt kê 3 test case tự động hoặc test-local cụ thể để xác nhận rằng những "Ripple Effect" ở trên đã được thử nghiệm và vô hiệu hóa.

## Khi nào sử dụng
- Khi bảo trì hoặc Refactor các chức năng cốt lõi (Core Logic).
- Bắt tay vào sửa API, Database models hoặc các file tiện ích `utils`, `helpers`.
- Người dùng cần một sự cẩn thận cực lớn trước khi nâng cấp.
