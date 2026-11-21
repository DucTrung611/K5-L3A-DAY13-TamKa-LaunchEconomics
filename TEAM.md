# Team

> Quy ước tránh conflict: phần "Thông tin nhóm" và bảng "Thành viên" do **Khánh** (giữ hồ sơ) sửa. Mỗi thành viên **chỉ sửa mục cá nhân của mình** ở cuối file.

## Thông tin nhóm

- Tên nhóm: TamKa
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-TamKa-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/DucTrung611/K5-L3A-DAY13-TamKa-LaunchEconomics · `main` · (điền hash commit chốt khi nộp)
- Ghi chú: nhóm 3 người, bốn vai của lab được gộp như bảng dưới.

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Thân Đức Trung | 2A202603449 | thanductrung123@gmail.com | DucTrung611 | Nhóm trưởng · Người viết code (A, B) |
|   2 | Nguyễn Khắc Khánh | 2A202603472 |       |        | Người gắn nhãn 2 kiêm giữ hồ sơ · Người viết code sau giải lao (D1) |
|   3 | Trần Mạnh Hùng | 2A202603496 |       |        | Người kiểm số · Người gắn nhãn 1 |
|   4 | (nhóm 3 người) | | | | |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên có báo cáo riêng:

- `report/team/2A202603449_ThanDucTrung.md`
- `report/team/2A202603472_NguyenKhacKhanh.md`
- `report/team/2A202603496_TranManhHung.md`

<!-- ===== MỤC CỦA TRUNG — chỉ Trung sửa ===== -->

## ThanDucTrung-2A202603449

### Phần việc phụ trách

- `src/lab13.py` vùng A1, A2, A3, A4, B; `report/team/bang_chi_phi.md` (A1–A3, B1–B3); luật dừng trong `pilot_plan.yaml`; E2 rủi ro kinh tế trong `report/team/chi_so.md`.

### Đóng góp cụ thể

- A1: viết 3 hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong` → ba phép thử in ĐẠT (1,20 · 1,25 · 1,25).
- A2: viết `mo_hinh` (tử số mọi lần chạy, mẫu số chỉ việc thành công, hỗ trợ `max_lan_chay`) → 4.472 đ/việc thành công [simulated], gấp 16,3× hoá đơn chia số yêu cầu; chi phí cả hệ thống 5.865 đ/yêu cầu = 0,49× [simulated].
- A3: tách 4 loại + bảng tỉ lệ ok theo lần thử → loại quoc_te (1,88×) và doi_tac (0,85×) khỏi phạm vi pilot.
- A4, B4 trong code (`in_bang_A`, `in_bang_B`) để Hùng đối chiếu với bản tính tay.
- B1–B3: 9 kịch bản, cặp token×2 + xem lại×2 (+46,3%), xếp hạng làm lại > xem lại > lương; giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ) [simulated].
- D3: 3 luật dừng NẾU–TRONG–THÌ–KHÔNG THÌ (an toàn, chi phí, mức độ sử dụng) đặt ngưỡng từ tỉ lệ mở lại hiện tại 3,97% trong phạm vi.
- E2: 5 dòng rủi ro kinh tế lấy số từ B1, B3, B4, A4.

### Bằng chứng

- `src/lab13.py` (vùng Trung) · lệnh `cd src && python lab13.py A B`.
- `report/team/bang_chi_phi.md` (A1, A2, A3, B1, B2, B3).
- `report/team/pilot_plan.yaml` (chú thích tỉ lệ mở lại + `stop_rules`).
- `report/team/chi_so.md` (E2).

<!-- ===== MỤC CỦA KHÁNH — chỉ Khánh sửa ===== -->

## NguyenKhacKhanh-2A202603472

### Phần việc phụ trách

- `src/lab13.py` vùng D1; `report/team/pilot_plan.yaml`; `report/team/ho_so_launch_v0.md`; `report/team/group_report.md`; `TEAM.md` (phần chung); nhãn độc lập người 2 ở nhiệm vụ C; trình bày Gate 2a.

### Đóng góp cụ thể

- Viết hàm `co_mau()` và hàm `in_bang_D1()` trong `src/lab13.py` (vùng Khánh); tính đúng 5 câu cỡ mẫu D1 a–e và power khi thiết kế cho 6 điểm mà tác động thật là 5 điểm.
- Hoàn thiện phần chú thích D1, đánh đổi chấp nhận và các trường YAML chính trong `report/team/pilot_plan.yaml`.
- Gắn nhãn độc lập 20 ca lỗi chuẩn Google PAIR trong `report/team/nhan_c_nguoi2_Khanh.md` và soạn 2 dòng khắc phục (Ca 18 Ngữ cảnh và Ca 4 Giới hạn hệ thống).
- Tổng hợp toàn bộ hồ sơ launch v0 một trang tại `report/team/ho_so_launch_v0.md` với đề xuất Go có điều kiện (4 điều kiện rõ ràng).
- Viết báo cáo nhóm `report/team/group_report.md`, quản lý phần chung `TEAM.md`, đại diện nhóm thuyết trình và trả lời phản biện Gate 2a.

### Bằng chứng

- `src/lab13.py` (vùng Khánh) · lệnh `cd src && python lab13.py D1`.
- `report/team/pilot_plan.yaml` (D1, đánh đổi, các trường YAML).
- `report/team/nhan_c_nguoi2_Khanh.md` (bảng nhãn 20 ca độc lập + 2 giải pháp khắc phục).
- `report/team/ho_so_launch_v0.md` (bảng 7 mục + 4 điều kiện đề xuất).
- `report/team/group_report.md` và báo cáo cá nhân `report/team/2A202603472_NguyenKhacKhanh.md`.

<!-- ===== MỤC CỦA HÙNG — chỉ Hùng sửa ===== -->

## TranManhHung-2A202603496

### Phần việc phụ trách

- Kiểm số độc lập (A2, A4, B4) trong `report/team/bang_chi_phi.md`; `src/lab13.py` vùng E1; `report/team/bang_loi.md`; E1 + danh sách event trong `report/team/chi_so.md`; câu D2 trong `pilot_plan.yaml`; nhãn độc lập người 1 ở nhiệm vụ C.

### Đóng góp cụ thể

-

### Bằng chứng

-
