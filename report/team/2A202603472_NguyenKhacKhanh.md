# Báo cáo cá nhân — NguyenKhacKhanh-2A202603472

File của **Nguyễn Khắc Khánh**. Chỉ Khánh sửa file này.

## 1. Thông tin thành viên

- Họ tên: Nguyễn Khắc Khánh
- MSSV: 2A202603472
- Email: khackhanh120104@gmail.com
- Vai trong nhóm: Người gắn nhãn 2 kiêm giữ hồ sơ; người viết code sau giải lao (D1)

## 2. Phần việc phụ trách

- **Nhiệm vụ D1:** Viết hàm `co_mau()` và hàm `in_bang_D1()` trong `src/lab13.py` để tính toán cỡ mẫu cho 3 cách chia (theo yêu cầu, theo nhân viên, theo depot) và giải phương trình tìm cỡ mẫu cho mức chênh 6 điểm.
- **Kế hoạch Pilot:** Hoàn thiện các trường thông tin trong `report/team/pilot_plan.yaml` (D1, đánh đổi, owner, scope, assignment, rollout, primary_metric, identifiability, rollback, simulated_inputs).
- **Nhiệm vụ C (Gắn nhãn độc lập):** Gắn nhãn độc lập 20 ca lỗi theo Google PAIR trong `report/team/nhan_c_nguoi2_Khanh.md` và soạn 2 dòng khắc phục (Ca 18 Ngữ cảnh và Ca 4 Giới hạn hệ thống).
- **Hồ sơ Launch v0:** Giữ hồ sơ và hoàn thiện toàn bộ file `report/team/ho_so_launch_v0.md` (7 mục và đề xuất Go có điều kiện).
- **Báo cáo nhóm & Thuyết trình:** Viết `report/team/group_report.md`, quản lý phần chung của `TEAM.md`, đại diện nhóm thuyết trình và trả lời phản biện trước hội đồng Gate 2a.

## 3. Đóng góp cụ thể

- Tự viết hàm `co_mau()` bằng phân phối chuẩn `statistics.NormalDist`, cho ra cỡ mẫu chính xác $n = 1.251$ yêu cầu/nhóm (5 điểm) và $n = 859$ yêu cầu/nhóm (6 điểm).
- Giải phương trình thiết kế cụm với $c = 20$ nhân viên/nhóm và $ICC = 0,02$, chứng minh cần $m \ge 299$ yêu cầu/người ($DE = 6,96$) để đạt mức chênh 6 điểm.
- Tính toán mức suy giảm power từ 0,80 xuống 0,642 (64,2%) khi tác động thực tế chỉ đạt 5 điểm bằng thư viện `statsmodels.stats.power.NormalIndPower`.
- Hoàn thiện 20/20 nhãn lỗi độc lập, giải thích nguyên nhân gốc cho từng ca; xây dựng giải pháp khắc phục có đo lường cụ thể bằng event/ngưỡng/tần suất.
- Tổng hợp toàn bộ các con số tài chính và kỹ thuật từ các thành viên vào bản hồ sơ launch v0 một trang ngắn gọn, logic, chặt chẽ để bảo vệ tại Gate 2a.

## 4. Bằng chứng

- **Mã nguồn:** Hàm `co_mau` và `in_bang_D1` tại VÙNG KHÁNH trong [`src/lab13.py`](file:///c:/vinuni/K5-L3A-DAY13-TamKa-LaunchEconomics/src/lab13.py); lệnh chạy độc lập `python lab13.py D1` in ra kết quả đạt 100%.
- **File nộp:**
  - [`report/team/pilot_plan.yaml`](file:///c:/vinuni/K5-L3A-DAY13-TamKa-LaunchEconomics/report/team/pilot_plan.yaml) (đạt chuẩn cú pháp YAML, không còn dấu `?`).
  - [`report/team/nhan_c_nguoi2_Khanh.md`](file:///c:/vinuni/K5-L3A-DAY13-TamKa-LaunchEconomics/report/team/nhan_c_nguoi2_Khanh.md) (đủ 20 ca lỗi độc lập và 2 giải pháp khắc phục).
  - [`report/team/ho_so_launch_v0.md`](file:///c:/vinuni/K5-L3A-DAY13-TamKa-LaunchEconomics/report/team/ho_so_launch_v0.md) (đủ 7 mục, trạng thái và 4 điều kiện Go).
  - [`report/team/group_report.md`](file:///c:/vinuni/K5-L3A-DAY13-TamKa-LaunchEconomics/report/team/group_report.md).
- **Git commits:**
  - `662bddf D1: hoan thanh co mau va pilot_plan vung Khanh`
  - Merge commit `c81fb48 Merge branch 'khackhanh'` vào nhánh `main`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (Gemini 3.8 Flash High).
- **Mục đích:**
  - Hỗ trợ giải phương trình toán học và kiểm tra cú pháp phân phối chuẩn cho hàm `co_mau()` trong Python.
  - Rà soát các quy tắc phân biệt của Google PAIR để đảm bảo gắn nhãn chuẩn xác theo nguyên nhân gốc chứ không theo triệu chứng bề ngoài.
  - Soát lỗi cú pháp YAML (`yaml.safe_load`) và kiểm tra các từ bị cấm (theo quy tắc 5 của lab) trên toàn bộ hồ sơ nhóm.
- **Cách tự kiểm tra:** Chạy lệnh `python lab13.py D1` để đối chiếu kết quả cỡ mẫu với slide bài giảng; dùng lệnh `yaml.safe_load` để xác thực file YAML; tự đọc lại từng ca lỗi để bảo đảm tính logic.

## 6. Tự đánh giá

- Hoàn thành đầy đủ 100% các phần việc được phân công đúng tiến độ thời gian quy định.
- Phối hợp nhịp nhàng với 2 thành viên trong nhóm, tuân thủ nghiêm ngặt quy tắc phân vùng file để không gây xung đột Git.
- Đóng góp tích cực vào việc thiết kế kế hoạch thử nghiệm có tính khả thi thực tế và bảo vệ thành công hồ sơ trước hội đồng Gate 2a.
- Đánh giá: Hoàn thành xuất sắc nhiệm vụ.
