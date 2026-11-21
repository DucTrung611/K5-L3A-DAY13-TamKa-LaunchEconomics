# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

<!-- ===== Cả file do TRUNG sửa (Hùng đọc chấm cùng, đọc số cho Trung ghi). ===== -->

- Nhóm chấm (hội đồng): TamKa
- Nhóm được chấm: HongSac (L3A) · https://github.com/hoang2k3ai/K5-L3A-DAY13-HongSac-LaunchEconomics · bản chấm: commit `29c9b91`
- File đã đọc: `ho_so_launch_v0.md`, `pilot_plan.yaml`, `bang_chi_phi.md`, `chi_so.md`, `bang_loi.md`, `group_report.md`

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | "Go có điều kiện" khớp số: cả hệ thống 5.864,65 đ = 0,489× [simulated]. Nêu rõ hai con số bất lợi: xem lại 100% làm CPS lên 11.743 đ (0,979×) đến 12.415 đ (1,035×, đắt hơn tự làm), và power chỉ 64,18% nếu tác động thật là +5 điểm. Có cách xử lý cho từng số: giảm xem lại theo bậc (cần ≥ 100 yêu cầu trưởng thành, sửa + bỏ < 15%), COO ký đánh đổi MDE +6. 4 điều kiện, mỗi điều kiện có vai trò và ngày kiểm tra. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Thu hẹp về noi_dia + hang_nang (982/1.200 yêu cầu) có lý do bằng số: quoc_te 22.515 đ = 1,876×, doi_tac chỉ 54,41% thành công. Nhãn đầy đủ: mục 1, 2, 3, 7 của hồ sơ ghi trạng thái "Giả lập"; tiêu đề cột các bảng A4, B1, B3 trong `bang_chi_phi.md` và cả bảng E2 đều ghi simulated; `pilot_plan.yaml` có 7 dòng `simulated_inputs`. Chỉ một sót nhỏ, không trừ điểm: `group_report.md` dòng 29 ghi 11.743–12.415 đ không kèm nhãn. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Tách được tác động: ngẫu nhiên theo nhân viên 20 + 20, phân tầng depot, seed 13; đối chứng chạy cùng lúc; đủ 20 cụm mỗi nhóm. Đủ mẫu cho MDE +6 đã khai báo trước: m = 299, DE 6,96, 5.980 yêu cầu/nhánh, hiệu dụng ≈ 859. 4 luật dừng đủ 4 vế, có ngưỡng (chênh ≥ 2 điểm hoặc > 6% mở lại, CPS > 8.000 đ, sửa + bỏ > 40%, 1 ca hoàn trùng), có thời hạn, và Giám đốc vận hành có quyền tắt cờ trong 30 phút. Ngưỡng an toàn đặt sau khi nhìn tỉ lệ hiện tại 3,97% nên không dừng ngay tuần đầu. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Đồng ý với đề xuất của nhóm. Trong phạm vi noi_dia + hang_nang, chi phí thấp hơn nhân viên tự làm: 4.599 đ = 0,38× ở 45.000 yêu cầu/tháng [simulated]. Pilot tách được tác động và có luật dừng cụ thể. Tuy vậy, kết luận chỉ đứng vững khi giảm được xem lại, vì xem lại 100% cho 0,979–1,035× [simulated], và khi COO chấp nhận power 64,18% ở mức +5 điểm, nên chưa thể Go không điều kiện. Hai điểm hội đồng ghi nhận thêm:

- Luật dừng chi phí (CPS > 8.000 đ) chỉ áp dụng ở pha ổn định 50%. Trong pha xem lại 100% ở bước 10–25%, CPS dự kiến đã là 11.743–12.415 đ [simulated], tức vượt 8.000 đ, nhưng không có luật nào giới hạn thời gian của pha này.
- `ho_so_launch_v0.md` mục 5 ghi "Nhãn TV3 và TV4 đều có AI hỗ trợ", trong khi RULES yêu cầu hai người gắn nhãn độc lập và không dùng AI để tạo nhãn lỗi. Phần này không thuộc thang 30 điểm hội đồng, nhưng giảng viên nên xem lại khi chấm tiêu chí C.

**Một câu hỏi cho đội trình:** Pha xem lại 100% ở bước 10% tốn 11.743–12.415 đ/việc [simulated], vượt ngưỡng dừng chi phí 8.000 đ của chính nhóm. Nếu hết tuần thứ hai tỉ lệ sửa + bỏ vẫn ≥ 15%, nên không được giảm xem lại, thì nhóm làm gì: kéo dài pha này, dừng pilot, hay thu hẹp về noi_dia? Ai quyết định, và quyết định trước ngày nào?

**Câu trả lời của đội trình (ghi lại tại buổi):** (Trung ghi lại câu trả lời của HongSac lúc 17:25)
Nếu hết tuần 2 (06/12/2026), tỷ lệ sửa + bỏ vẫn ≥ 15%, nhóm không giảm xem lại, không kéo dài pha 100% vô thời hạn và không chuyển lên 50% ngày 07/12; đề xuất dừng pilot hiện tại, tắt trợ lý cho yêu cầu mới và chuyển lại cho nhân viên tự xử lý, do CPS 11.743–12.415 đ/việc [simulated] vượt mốc 8.000 đ.
PM trợ lý hoàn phí và Kế toán trưởng đối chiếu CPS với phút đo thật, tính lại phương án chỉ noi_dia; Giám đốc vận hành (COO) là người quyết định dừng và phê duyệt hướng xử lý chậm nhất ngày 06/12/2026, trước lịch nâng bước 07/12.
Chỉ xem xét một pilot noi_dia mới khi có mô hình chi phí, kinh phí và ngưỡng dừng được duyệt lại; không tự thu hẹp phạm vi rồi tiếp tục dùng kết quả của pilot cũ để kết luận hiệu quả.
