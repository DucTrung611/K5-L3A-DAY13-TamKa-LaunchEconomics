# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

<!-- ===== Cả file do KHÁNH sửa; Trung, Hùng góp nội dung qua Khánh. ===== -->

- Tên nhóm: TamKa
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm TamKa xây dựng bộ hồ sơ launch v0 nhằm trả lời 4 câu hỏi cốt lõi trước hội đồng thẩm định Gate 2a cho trợ lý hoàn phí LogiX-VN:
1. **Hiệu quả kinh tế:** Xác định chi phí thật sự cho mỗi việc thành công (Cost-of-Pass) thay vì chỉ nhìn vào hóa đơn token bề nổi.
2. **Hành vi sử dụng:** Đo lường tỷ lệ can thiệp/bỏ qua của nhân viên CSKH và thiết kế hệ thống telemetry ghi nhận sự kiện (events).
3. **Quản trị rủi ro & lỗi:** Phân loại 20 ca lỗi thực tế theo khung chuẩn Google PAIR, thiết lập cơ chế phát hiện và quy trách nhiệm rõ ràng.
4. **Thiết kế Pilot khoa học:** Xây dựng thử nghiệm ngẫu nhiên theo cụm (Cluster RCT), tính toán cỡ mẫu hiệu dụng, xác định đánh đổi thống kê và thiết lập luật dừng an toàn viết trước.

## 3. Giải pháp

- **Nhiệm vụ A (Mô hình chi phí):** Xây dựng hàm `mo_hinh` trong `src/lab13.py` tính toán trên toàn bộ 1.624 lần chạy và 1.200 yêu cầu. Chi tiết tại [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ B (Phân tích độ nhạy):** Khảo sát 9 kịch bản biến động chi phí, xác định trần 2 lần chạy là tối ưu cho toàn hệ thống và phân tích kịch bản xem lại 100%. Chi tiết tại [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (Bảng lỗi Google PAIR):** Hai thành viên (Hùng và Khánh) gắn nhãn độc lập 20 ca lỗi, đạt đồng thuận 100%, chọn 5 ca đại diện xây dựng giải pháp khắc phục có đo lường. Chi tiết tại [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (Kế hoạch pilot):** Thiết kế Cluster RCT phân bổ theo nhân viên (20 can thiệp, 20 đối chứng), chấp nhận đánh đổi MDE 6 điểm ($n=859, m \ge 299, DE=6,96$), thiết lập 3 luật dừng chuẩn cú pháp NẾU-TRONG-THÌ-KHÔNG THÌ. Chi tiết tại [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E (Chỉ số & Hồ sơ Launch v0):** Đo lường 3 chỉ số trong đợt chạy thử, đặc tả 10 event telemetry có `trace_id`, lập bảng 5 rủi ro kinh tế và tổng hợp hồ sơ 1 trang tại [ho_so_launch_v0.md](ho_so_launch_v0.md).

## 4. Kết quả

- **Chi phí mỗi việc thành công:** Đạt **4.472 đ [simulated]**, gấp **16,3 lần** hóa đơn token + tool (274,7 đ). Giờ làm việc của nhân viên chiếm **92,5%** tổng chi phí (làm lại 51,8%, xem lại 40,7%) [simulated].
- **Chi phí cả hệ thống:** Đạt **5.865 đ/yêu cầu = 0,49×** [simulated] mức 12.000 đ nhân viên tự làm (đã tính chi phí nhân viên xử lý thay 222 yêu cầu trợ lý không hoàn thành).
- **Phạm vi pilot:** Khuyến nghị chỉ chạy `noi_dia` (0,22×) và `hang_nang` (0,69×); loại bỏ hoàn toàn `quoc_te` (1,88×) và `doi_tac` (0,85×) [simulated]. Khi cộng chi phí cố định 40 triệu đ/tháng, CPS trong phạm vi pilot đạt **4.599 đ (0,38×)** ở quy mô đầy đủ và **5.784 đ (0,48×)** ở nửa quy mô [simulated].
- **Ba yếu tố nhạy nhất:** 1. Số ca làm lại (+51,8%), 2. Tỉ lệ xem lại (+40,7%), 3. Lương nhân viên (+23,1%). Giá token chỉ ảnh hưởng +5,6% [simulated].
- **Chỉ số đợt chạy thử:** Tỷ lệ đóng 24h & không mở lại 7 ngày đạt **82,83%**; tỷ lệ bỏ qua gợi ý đạt **27,12%**; tỷ lệ mở lại 7 ngày đạt **4,25%** (trong phạm vi pilot là 3,97%).
- **Đề xuất cuối cùng:** **GO CÓ ĐIỀU KIỆN** (giới hạn 2 lần chạy, giảm bậc xem lại, theo dõi chặt chẽ ngưỡng mở lại 6% và rủi ro power 64,2%).

## 5. Khó khăn và cách xử lý

1. **Vấn đề cỡ mẫu cụm:** Với quy mô 40 nhân viên và ICC = 0,02, trần cỡ mẫu hiệu dụng tối đa chỉ đạt $c / ICC = 20 / 0,02 = 1.000 < 1.251$ yêu cầu, không đủ để phát hiện mức chênh 5 điểm với power 80%.
   - *Cách xử lý:* Nhóm quyết định chấp nhận đánh đổi nâng MDE lên 6 điểm ($n=859$), yêu cầu mỗi nhân viên xử lý $m \ge 299$ đơn ($DE=6,96$). Đồng thời tính toán và công khai con số bất lợi: nếu tác động thực tế chỉ đạt 5 điểm, power sẽ giảm xuống 64,2%, từ đó đưa vào điều kiện kiểm tra kéo dài thời gian pilot thêm 2 tuần nếu cần.
2. **Sự cố môi trường ban đầu:** Môi trường ảo Python ban đầu bị tạo nhầm từ MSYS2/MinGW dẫn tới lỗi SSL và không thể cài các wheel tiền biên dịch của pandas/scipy/statsmodels.
   - *Cách xử lý:* Tái cấu trúc môi trường ảo sạch sẽ bằng Python 3.12 chuẩn của Windows (`C:\Python312\python.exe`), cài đặt thành công 100% requirements mà không cần biên dịch từ mã nguồn.

## 6. Tổng hợp đóng góp

Nhóm 3 thành viên làm việc song song, sở hữu vùng riêng biệt để tránh xung đột mã nguồn:
- **Thân Đức Trung (Nhóm trưởng):** Viết code A1, A2, in bảng A, in bảng B trong `src/lab13.py`; hoàn thiện phần A & B trong `bang_chi_phi.md`; soạn thảo 3 luật dừng `stop_rules` trong `pilot_plan.yaml`; xây dựng bảng rủi ro kinh tế E2 trong `chi_so.md`.
- **Trần Mạnh Hùng:** Kiểm số độc lập A2, A4, B4; viết code E1; gắn nhãn độc lập Người 1 ở nhiệm vụ C; hoàn thiện `bang_loi.md`; đặc tả chỉ số và 10 event có `trace_id` trong `chi_so.md`; trả lời 5 câu hỏi D2 trong `pilot_plan.yaml`.
- **Nguyễn Khắc Khánh:** Viết code D1 (`co_mau`, `in_bang_D1`) trong `src/lab13.py`; hoàn thiện phần D1, đánh đổi và các trường YAML trong `pilot_plan.yaml`; gắn nhãn độc lập Người 2 ở nhiệm vụ C; tổng hợp toàn bộ hồ sơ `ho_so_launch_v0.md`; viết `group_report.md`; đại diện nhóm thuyết trình và trả lời phản biện Gate 2a.

## 7. Hạn chế và hướng cải thiện

- **Hạn chế:** Số liệu thời gian xem lại và làm lại là dữ liệu giả lập (`_simulated`), chưa phản ánh hoàn toàn áp lực tâm lý và thao tác thực tế của nhân viên. Đợt chạy thử 2 tuần chưa có nhóm đối chứng chạy song song nên con số 82,83% chỉ mang tính tham khảo kỹ thuật.
- **Hướng cải thiện:** Trong tuần đầu của pilot, cần đo lường thời gian xem lại thực tế qua event `staff_review_decision` để kiểm chứng giả định 5 phút; nếu thời gian xem lại kéo dài > 5 phút thì phải nhanh chóng tối ưu giao diện hỗ trợ CSKH.

## 8. Tài liệu tham khảo

1. Erol et al., *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arXiv:2504.13359, 2025.
2. Google PAIR, *People + AI Guidebook: Errors + Graceful Failure*, pair.withgoogle.com.
3. Statsmodels Developers, *Power and Sample Size Calculations (`statsmodels.stats.power.NormalIndPower`)*.
