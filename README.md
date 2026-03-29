# AI Advanced Cognitive Skills Repository

Đây là bộ sưu tập các kỹ năng tư duy bậc cao (Advanced Cognitive Skills Framework) dành cho Trí Tuệ Nhân Tạo (AI). Bộ kỹ năng này ép AI phải sử dụng các vùng "tư duy rành mạch" thay vì dựa vào kinh nghiệm cũ mơ hồ hoặc dự đoán sai số, nhằm giúp AI đưa ra kết quả thông minh hơn và tiệm cận với 0 lỗi (zero-defect).

## Cấu trúc Hệ Sinh Thái
Dự án được phân chia theo chuẩn quốc tế nhằm module hóa các năng lực của AI:

### 1. Kỹ năng tư duy cốt lõi (`skills/`)
Mô phỏng các vùng "tư duy rành mạch" thay vì dựa vào kinh nghiệm cũ mơ hồ hoặc dự đoán sai số:
- `first-principles-thinking`: Tư duy Sơ nguyên.
- `self-correction-loop`: Vòng lặp Tự Đánh Giá & Phản Biện.
- `system-impact-analyzer`: Tư duy Phân tích Hậu Quả Hệ Thống.
- `devil-advocate`: Đóng vai Ác Quỷ Phản Biện Tìm Lỗi.
- `ooda-loop`: Quy trình Phản Ứng Nhanh Kỹ Thuật (Quan sát - Hướng - Quyết - Hành).
- `design-thinking`: Góc nhìn Thấu hiểu UX/Người dùng khi Thiết kế UI.
- `tdd-advanced`: Viết Code không hỏng bằng Vòng lặp Test Đỏ/Xanh khắt khe.

### 2. Khung điều phối & Phương pháp luận (`frameworks/`)
Các nền tảng Orchestration và luận điểm phát triển phần mềm được tinh tuyển:
- `superpowers`: An agentic skills framework & software development methodology.
- `ccpm`: Project management skill system cho Agents qua GitHub Issues và Git worktrees.

### 3. Vùng nhớ lưu trữ (`memory/`)
Các hệ thống Memory layer cấp cho AI bộ nhớ dài hạn và quản lý Session:
- `mem0`: Universal memory layer cho AI Agents.
- `cipher`: Bộ nhớ mã nguồn mở tối ưu riêng cho nhóm coding agents.

### 4. Máy chủ giao thức ngữ cảnh (`mcp-servers/`)
Các Model Context Protocol (MCP) servers cung cấp APIs mở rộng và Integration tools:
- `MCPRules`: Quản lý lập trình guidelines và rules logic.
- `context7`: Up-to-date doc queries cho AI editors (Upstash).
- `github-mcp-server`: Quản trị GitHub CI/CD, Issues, Pull Requests trực tiếp.
- `mcp-chrome` / `playwright-mcp` / `chrome-devtools-mcp`: Mở rộng năng lực kiểm thử UI và Web interaction.
- `cli-mcp-server`: Tương tác qua Command Line với Security Policies khắt khe.
- `mcp-feedback-enhanced`: Nhận command execution + user interaction.

## Hướng dẫn cài đặt cho AI Agent
1. **Phục hồi toàn bộ Submodules (Frameworks, Servers, Memory):**
   Chạy lệnh sau tại thư mục gốc để tải trọn bộ sinh thái mã nguồn mở:
   ```bash
   git submodule update --init --recursive
   ```
2. **Kích hoạt Skills nội bộ:**
   Yêu cầu Agent copy (hoặc symlink) toàn bộ thư mục bên trong `skills/` vào thư mục `~/.agent/skills/` để kích hoạt tính năng **Auto Skill Discovery**.
   Sau đó Agent sẽ tự động phân tích và import các MCP/Framework theo ngữ cảnh công việc.
