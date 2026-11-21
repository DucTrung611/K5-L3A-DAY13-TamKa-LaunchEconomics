# Báo cáo cá nhân — ThanDucTrung-2A202603449

File của **Thân Đức Trung**. Chỉ Trung sửa file này.

## 1. Thông tin thành viên

- Họ tên: Thân Đức Trung
- MSSV: 2A202603449
- Email: thanductrung123@gmail.com
- Vai trong nhóm: Người viết code (A, B), nhóm trưởng; kiêm luật dừng D3 và rủi ro kinh tế E2

## 2. Phần việc phụ trách

- `src/lab13.py`: vùng A1, A2 (`mo_hinh`), `in_bang_A` (A2, A3, A4), `in_bang_B` (B1–B4).
- `report/team/bang_chi_phi.md`: A1, A2, A3, B1, B2, B3.
- `report/team/pilot_plan.yaml`: chú thích tỉ lệ mở lại hiện tại + `stop_rules`.
- `report/team/chi_so.md`: E2 rủi ro kinh tế.
- `report/team/phieu_cham.md`: chấm nhóm n + 1 ở Gate 2a (cùng Hùng).

## 3. Đóng góp cụ thể

- **A1.** Ba hàm theo công thức E[lần chạy] = (1 − (1 − p)^k) / p, P = 1 − (1 − p)^k, hệ số = E / P. Ba phép thử in ĐẠT. Hệ số chi phí luôn bằng 1/p vì (1 − (1 − p)^k) triệt tiêu ở tử và mẫu.
- **A2.** `mo_hinh` lọc lần chạy theo `request_id` của tập yêu cầu đang xét (để A3, A4 dùng lại), cộng token/tool của **mọi** lần chạy kể cả `loi`, chia giá token cho 1.000, và chỉ chia cho yêu cầu `thanh_cong`. Kết quả: tổng 4.373.585 đ, 978 việc thành công, **4.472 đ/việc** [simulated], gấp 16,3× hoá đơn 274,7 đ/yêu cầu. Làm lại chiếm 51,8%, xem lại 40,7% [simulated].
- **So với nhân viên.** Thêm dòng chi phí cả hệ thống (cộng 12.000 đ × 222 yêu cầu không thành công): 5.865 đ/yêu cầu = 0,49× [simulated], để không so 4.472 đ trực tiếp với 12.000 đ.
- **A3.** noi_dia 0,22×, hang_nang 0,69×, quoc_te 1,88×, doi_tac 0,85× [simulated]. Bảng tỉ lệ ok theo lần thử cho thấy quoc_te lần 2 chỉ 11,4%, lần 3 chỉ 2,2% → chạy lại không giúp; đề xuất phạm vi pilot noi_dia + hang_nang.
- **B1–B3.** 9 kịch bản bằng một dict gọi lại `mo_hinh`; thêm `assert` tự kiểm "giảm một nửa = −½ × gấp đôi". Cặp token×2 + xem lại×2 = +46,3% đúng bằng tổng hai tác động riêng. B3: giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ) dù giới hạn 1 lần có cps thấp nhất (4.111 đ) [simulated].
- **D3.** Trước khi đặt ngưỡng, tính tỉ lệ mở lại hiện tại 3,97% trong phạm vi (4,25% toàn bộ) → không dùng ngưỡng tuyệt đối 3% (sẽ dừng ngay tuần đầu) mà dùng chênh ≥ 2 điểm so với đối chứng + trần 6%. Ba luật đủ 4 vế, mỗi luật có thời hạn và một vai trò có quyền dừng.
- **E2.** 5 dòng rủi ro, mỗi dòng có tác động bằng số từ B1/B3/B4/A4, dấu hiệu theo dõi gắn với event, hành động và một vai trò.

## 4. Bằng chứng

- Lệnh: `cd src && python lab13.py A B` in toàn bộ số A2, A3, A4, B1–B4; mọi số khớp số đối chiếu trong hướng dẫn (lệch 0%, riêng B4 biến thể 15,3 phút ra 12.415 đ so với 12.414 đ do làm tròn phút trung bình).
- File: `src/lab13.py` (vùng Trung), `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml` (stop_rules), `report/team/chi_so.md` (E2).
- Commit: xem lịch sử git của các file trên (tác giả DucTrung611).

## 5. Công cụ AI đã dùng

- **Claude Code (Claude)**: gợi ý và viết code cho `mo_hinh`, `in_bang_A`, `in_bang_B`; soạn câu chữ cho bảng trong `bang_chi_phi.md`, luật dừng và bảng E2.
- **Cách tự kiểm tra:**
  - Ba phép thử A1 (`kiem_tra_dap_an_biet_truoc`) phải in ĐẠT trước khi chạy tiếp.
  - So từng số A2, A3, A4, B1, B2, B3, B4 với bảng số đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (yêu cầu lệch ≤ 2%).
  - `assert` trong `in_bang_B` kiểm tính tuyến tính của mô hình (giảm một nửa = −½ gấp đôi); B2 kiểm cặp = tổng hai tác động riêng.
  - Tính tay lại một số: 4.373.585 / 978 = 4.472; (4.373.585 + 222 × 12.000) / 1.200 = 5.865; 7.449.781 − 6.901.220 = 548.561.
  - Đối chiếu ở điểm đồng bộ S2 với bản kiểm số độc lập của Hùng (script riêng, không gọi `mo_hinh`) cho A2, A4, B4.
  - Mọi số trong hồ sơ là do `lab13.py` in ra hoặc tính tay ở trên; AI không được dùng để tạo số hay nhãn lỗi.

## 6. Tự đánh giá

- Làm tốt: số A, B khớp đáp án; nắm được vì sao tử số tính mọi lần chạy còn mẫu số chỉ đếm việc thành công, và vì sao phải so chi phí cả hệ thống chứ không chỉ cps.
- Cần cải thiện: (Trung tự bổ sung sau buổi học.)
