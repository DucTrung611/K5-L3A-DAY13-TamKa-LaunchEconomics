# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

<!-- ===== VÙNG HÙNG — chỉ HÙNG sửa phần dưới ===== -->

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) (phạm vi `noi_dia` + `hang_nang`: 3,97%, 39/982) |
| Dùng | Tỉ lệ nhân viên mở trợ lý ở nhóm can thiệp | Số yêu cầu nhóm can thiệp có `agent_suggestion_shown` ÷ tổng yêu cầu nhóm can thiệp | Không cần tính |
| An toàn | % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần | Số đơn kiểm mẫu có `so_tien_da_hoan != so_tien_dung` ÷ tổng đơn kiểm mẫu hằng tuần | Không cần tính |

Chỉ số chính trong đợt chạy thử là **82,83%** (không viết "trợ lý đã nâng chỉ số", vì đợt chạy thử không có nhóm đối chứng).

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy, kể cả lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id`, `so_tien_de_xem`, `trace_id` | Khi gợi ý trợ lý hiện ra |
| `staff_review_decision` | Nhân viên | `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai`, `trace_id` | Khi bấm giữ/sửa/bỏ |
| `staff_rework_completed` | Nhân viên | `phut_lam_lai`, `ly_do`, `trace_id` | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi sổ hoàn tiền |
| `handoff_to_staff` | Agent | `reason`, `tom_tat`, `trace_id` | Khi chuyển cho nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at`, `trace_id` | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | `reopened_at`, `reason`, `trace_id` | Khi khách mở lại |
| `audit_sample_checked` | Kế toán / Người kiểm số | `so_tien_da_hoan`, `so_tien_dung`, `trace_id` | Kiểm tra mẫu hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (% đóng 24h & không mở lại 7 ngày):** tính từ `refund_request_created` (tổng yêu cầu), `ticket_closed` (đóng trong 24h) và `ticket_reopened` (không mở lại trong 7 ngày) nối qua `trace_id` → **Đo được**.
- **Chỉ số dùng (% bỏ qua gợi ý):** tính từ `staff_review_decision` (`sua` + `bo` ÷ tổng số quyết định xem lại) → **Đo được**.
- **Chỉ số an toàn (% lỗi lọt đến khách):** tính từ `ticket_reopened` (trong 7 ngày) ÷ `refund_request_created` → **Đo được**.
- **Chỉ số dùng đề xuất (% mở trợ lý ở nhóm can thiệp):** tính từ `agent_suggestion_shown` ÷ `refund_request_created` (lọc `arm = treatment`) → **Đo được**.
- **Chỉ số an toàn đề xuất (% hoàn sai tiền kiểm mẫu):** tính từ `audit_sample_checked` (`so_tien_da_hoan != so_tien_dung` ÷ tổng mẫu kiểm) → **Đo được**.

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
