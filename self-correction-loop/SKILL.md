---
name: self-correction-loop
description: Vòng lặp tự kiểm điểm và chéo hóa phản biện code trước khi đưa ra cho người dùng.
---

# Self-Correction Loop (Tự Kiểm Điểm & Sửa Sai)

## Mục đích
Hạn chế tối đa những lỗi ngớ ngẩn do "nhắm mắt code", ép AI phải chạy bộ não trong chế độ: "Mình vừa code cái này, liệu nó có đúng thực sự không, hay nó sẽ gây lỗi?".

## Quy trình ép buộc (Mandatory Process)

Khi bật kỹ năng này, trước khi commit code hoặc in ra kết quả, AI cần tự hỏi và ghi ra một Checklist kiểm tra như sau:

### 1. Phản biện tính toàn vẹn (Integrity Check)
- Có thực sự giải quyết đúng vấn đề gốc chưa hay chỉ là một mẹo hack?
- Đoạn mã vừa thay đổi có làm hỏng các phần khác đang chạy ổn định không (Hậu quả liên đới)?

### 2. Edge Cases (Trường hợp Góc)
- Bắt buộc liệt kê 3 trường hợp xấu nhất (worst-case scenarios): giá trị null, thời gian timeout, dữ liệu bất thường. Code hiện tại đã bao phủ các trường hợp này chưa? 
- **Nếu chưa, quay lại sửa code NGAY!**

### 3. Hiệu năng & Bảo mật (Performance & Security)
- Có loop nào lồng nhau dư thừa không (O(n^2))? Có bộ nhớ nào rò rỉ không?
- Thay đổi này có tạo ra lỗ hổng SQL Injection hay XSS nào không?

## Khi nào sử dụng
- Sau khi fix xong một chuỗi bug dai dẳng.
- Trước khi chốt một PR (Pull Request) hoặc commit cuối ngày.
- Khi người dùng phàn nàn "Mã mày đưa chạy toàn lỗi!".
