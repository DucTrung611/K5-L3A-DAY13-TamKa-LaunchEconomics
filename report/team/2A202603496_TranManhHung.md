# Báo cáo cá nhân — TranManhHung-2A202603496

File của **Trần Mạnh Hùng**. Chỉ Hùng sửa file này.

## 1. Thông tin thành viên

- Họ tên: Trần Mạnh Hùng
- MSSV: 2A202603496
- Email: hungmochi003@gmail.com
- Vai trong nhóm: Người kiểm số; người gắn nhãn 1

## 2. Phần việc phụ trách

- `src/lab13.py` (vùng Hùng): viết `in_chi_so_E1(reqs)` tính 3 chỉ số E1 và tỉ lệ `mo_lai_trong_7_ngay` cho luật dừng D3.
- `report/team/bang_chi_phi.md` (vùng Hùng): kiểm số độc lập và hoàn thiện mục A4, B4.
- Nhiệm vụ C: gắn nhãn độc lập 20 ca lỗi vào `report/team/nhan_c_nguoi1_Hung.md`; tổng hợp bảng nhãn và bảng khắc phục vào `report/team/bang_loi.md`.
- `report/team/pilot_plan.yaml` (vùng Hùng): trả lời 5 câu kiểm tra D2 ("tách được tác động").
- `report/team/chi_so.md` (vùng Hùng): hoàn thiện bảng chỉ số E1, danh sách event có `trace_id` và kiểm tra chéo.

## 3. Đóng góp cụ thể

- Hoàn thiện `in_chi_so_E1` và chạy kiểm chứng trên `logix_requests.csv`.
- Tính đối chiếu từ CSV cho A4 (quy mô 45.000 và 22.500 yêu cầu/tháng) và B4 (xem lại 100% ở mức 9 phút và 15,3 phút làm lại/ca), đảm bảo gắn nhãn `simulated` cho các số từ cột `_simulated`.
- Đọc 20 ca lỗi từ đề bài gốc và gắn nhãn độc lập theo 5 loại Google PAIR dựa trên nguyên nhân gốc; soạn 3 dòng khắc phục (`Do người dùng`, `Hệ thống`, `Ngầm`) có event, ngưỡng và vai trò phụ trách.
- Hoàn thiện 5 câu D2 cho phương án chia 20 nhân viên mỗi nhóm phân tầng theo depot, kiểm tra hợp lệ file YAML bằng `yaml.safe_load`.
- Đặc tả 5 chỉ số E1 và 10 event có `trace_id`, kiểm tra chéo khả năng đo lường của từng chỉ số.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- `src/lab13.py` (`python lab13.py E1`): chính `82.83% (994/1200)`, dùng `27.12% (48/177)`, an toàn `4.25% (51/1200)`, `noi_dia + hang_nang` mở lại `3.97% (39/982)`.
- `report/team/bang_chi_phi.md`: A4 (`4.599 đ = 0,38×` ở 45.000/tháng; `5.784 đ = 0,48×` ở 22.500/tháng `[simulated]`), B4 (`11.743 đ = 0,98×` với 9 phút làm lại; `12.415 đ = 1,03×` với 15,3 phút làm lại `[simulated]`).
- `report/team/nhan_c_nguoi1_Hung.md` (20 ca gắn nhãn độc lập), `report/team/bang_loi.md`, `report/team/pilot_plan.yaml` (mục D2), `report/team/chi_so.md` (mục E1 & event).

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- Có sử dụng trợ lý AI trong IDE để hỗ trợ viết hàm `in_chi_so_E1`, soạn nháp bảng báo cáo và kiểm tra cú pháp YAML.
- Tự kiểm tra kết quả bằng cách chạy trực tiếp script Python trên `logix_runs.csv` và `logix_requests.csv`, đối chiếu lại từng công thức trong `docs/du_lieu_va_cong_thuc.md` và xác nhận các giới hạn quy tắc (nhãn `simulated`, tuân thủ quy tắc 5 về Gate 2a trong `README.md`, không chạm vào vùng của thành viên khác).

## 6. Tự đánh giá

- Hoàn thành đầy đủ các vùng được giao đúng cấu trúc phân công của nhóm, đảm bảo không gây conflict với Trung và Khánh. Phần so nhãn và 2 dòng khắc phục còn lại trong `bang_loi.md` sẵn sàng ghép ngay sau khi Khánh commit `nhan_c_nguoi2_Khanh.md`.
