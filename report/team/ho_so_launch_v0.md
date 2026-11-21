# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

<!-- ===== Cả file do KHÁNH sửa. Trung, Hùng gửi số cho Khánh, không sửa trực tiếp. ===== -->

Nhóm: TamKa · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated], gấp 16,3 lần hóa đơn token + tool (274,7 đ). Phạm vi pilot gồm phí cố định 40 tr/tháng là 4.599 đ (0,38×) ở quy mô đầy đủ và 5.784 đ (0,48×) ở nửa quy mô | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Ca làm lại (+51,8%), 2. Tỉ lệ xem lại (+40,7%), 3. Lương nhân viên (+23,1%). Giá token chỉ ảnh hưởng +5,6% | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Chi phí cả hệ thống: 5.865 đ/yêu cầu = 0,49× so với 12.000 đ nhân viên tự làm (đã tính bù 222 việc trợ lý không xong); trong phạm vi pilot là 0,38× - 0,48× [simulated] | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chính: 82,83% (đóng trong 24h và không mở lại 7 ngày); Dùng: 27,12% (tỉ lệ bỏ qua sửa/bỏ); An toàn: 4,25% (mở lại 7 ngày, trong phạm vi là 3,97%). 10 event có `trace_id` | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca lỗi phân loại vào 5 nhóm Google PAIR (đồng thuận 100%); 5 ca đại diện có đo lường cụ thể bằng event/ngưỡng/tần suất và 1 vai trò chịu trách nhiệm | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo 20 nhân viên can thiệp - 20 đối chứng (c = 20 cụm), MDE 6 điểm (859 yc/nhóm, m ≥ 299, DE = 6,96); 3 luật dừng NẾU-TRONG-THÌ-KHÔNG THÌ; rollback 30 phút | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Xem lại 100% kéo dài làm chi phí lên 11.743 đ (0,98×) đến 12.414 đ (1,03×) [simulated]; số ca làm lại tăng gấp đôi đội chi phí lên 6.787 đ [simulated]. Có cơ chế giảm bậc | Giả lập | Kế toán trưởng |

**Đề xuất:** Go có điều kiện

- **Điều kiện 1:** Chỉ triển khai trong phạm vi `noi_dia` và `hang_nang`; loại bỏ hoàn toàn `quoc_te` (1,88× so với tự làm) và `doi_tac` (0,85×). Người phụ trách: PM trợ lý hoàn phí. Ngày kiểm tra: 2026-12-08.
- **Điều kiện 2:** Áp dụng trần tối đa 2 lần chạy cho mỗi yêu cầu để tối ưu chi phí toàn hệ thống (6.901.220 đ). Người phụ trách: Kỹ sư trưởng agent. Ngày kiểm tra: 2026-12-08.
- **Điều kiện 3:** Giảm tỷ lệ xem lại theo bậc (100% → 50% → 20%) khi tỷ lệ sửa + bỏ < 15% trong 1 tuần nhằm tránh nguy cơ xem lại 100% hòa vốn hoặc đắt hơn người làm (11.743 đ - 12.414 đ [simulated]). Người phụ trách: Trưởng nhóm CSKH. Ngày kiểm tra: 2026-12-15.
- **Điều kiện 4:** Chấp nhận đánh đổi MDE 6 điểm; nếu tác động thực tế chỉ là 5 điểm (power giảm còn 64,2%), kéo dài pilot thêm 2 tuần để gom đủ m ≥ 299 yêu cầu/nhân viên trước khi ra quyết định. Người phụ trách: Giám đốc vận hành. Ngày kiểm tra: 2027-01-05.
