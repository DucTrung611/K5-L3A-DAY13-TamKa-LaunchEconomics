# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

<!-- ===== VÙNG HÙNG — chỉ HÙNG sửa phần dưới ===== -->

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | ... |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | ... |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | ... |
| Dùng | Nhóm tự đề xuất: ... | ... | Không cần tính |
| An toàn | Nhóm tự đề xuất: ... | ... | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- ...

<!-- ===== VÙNG TRUNG — chỉ TRUNG sửa phần dưới ===== -->

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi (yếu tố nhạy nhất, B1/B2) | +51,8%: 4.472 → 6.787 đ/việc thành công [simulated] | Tỉ lệ `lam_lai` theo tuần (event `staff_rework_completed`) > 7%; đợt chạy thử 4,9% trong phạm vi | Thu hẹp về noi_dia + giới hạn 2 lần chạy (luật dừng 2); rà 20 trace làm lại trong 3 ngày | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài (B4) | 11.743 đ = 0,98× của 12.000 đ (12.414 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu) [simulated]; hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (≤ 4,8 phút) | % yêu cầu được xem lại còn > 50% ở cuối bước rollout 0.25; phút xem lại trung vị đo thật (event `staff_review_decision`) > 5 phút | Giảm xem lại theo bậc (100% → 50% → 20%) khi tỉ lệ sửa + bỏ < 15% trong 1 tuần; rút gọn màn hình xem lại | Trưởng nhóm CSKH |
| Tỉ lệ xem lại gấp đôi so với đợt chạy thử (B1) | +40,7%: 4.472 → 6.292 đ [simulated] | Số phút xem lại / yêu cầu theo tuần cao hơn 2 lần mức chạy thử | Không giảm bậc xem lại thì cũng không mở rộng phạm vi; tìm loại yêu cầu gây xem lại nhiều | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến (A4) | Cố định 40 triệu/tháng: +1.185 đ/việc ở 45.000 yc/tháng (tổng 4.599 đ = 0,38×), +2.370 đ/việc nếu còn một nửa (5.784 đ = 0,48×) [simulated] | Số việc thành công theo tuần (event `ticket_closed`) < 50% kế hoạch | Không mở rộng pilot; đàm phán lại hợp đồng chi phí cố định theo khối lượng | Kế toán trưởng |
| Tối ưu sai chỉ tiêu khi giới hạn chạy lại (B3) | Giới hạn 1 lần cho cps thấp nhất (4.111 đ) nhưng cả hệ thống đắt hơn giới hạn 2 lần 548.561 đ trên 1.200 yêu cầu (+85 việc chuyển nhân viên) [simulated] | Số `handoff_to_staff` theo tuần tăng > 20% sau khi đổi giới hạn | Báo cáo chi phí cả hệ thống / yêu cầu (gồm 12.000 đ × ca chuyển nhân viên), không chỉ cps | Kỹ sư trưởng agent |
