# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

<!-- ===== VÙNG TRUNG — chỉ TRUNG sửa phần dưới ===== -->

## A1 · Ba phép thử đáp án biết trước

`python lab13.py A` in `Ba phép thử đáp án biết trước: ĐẠT`.

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 (= (1 − 0,2²) / 0,8) |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 (= 1 / 0,8) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (= 1,248 / 0,992; k triệt tiêu, luôn bằng 1/p) |

## A2 · Mô hình chi phí từ trace

Tử số cộng **mọi** lần chạy (1.624 lần, kể cả lần `loi`); mẫu số chỉ đếm `ket_qua == thanh_cong`.

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 (5.600 lần gọi × 15 đ) | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 (890 phút × 2.000 đ) | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 (1.132 phút × 2.000 đ) | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,3 lần** "hoá đơn chia số yêu cầu" (4.472 / 274,7) [simulated]: phần lớn chi phí là giờ nhân viên, không phải token.
- Khoản lớn nhất là **làm lại, 51,8%** tổng chi phí [simulated], tiếp theo là xem lại 40,7% [simulated]; giờ nhân viên cộng lại chiếm 92,5%, token + tool chỉ 7,5%.
- So với 12.000 đ phải dùng chi phí cả hệ thống, cộng phần nhân viên làm thay 222 yêu cầu không thành công: (4.373.585 + 222 × 12.000) / 1.200 = **5.865 đ/yêu cầu = 0,49×** [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× |

Tỉ lệ lần chạy `ok` theo lần thử (đo từ trace, số lần chạy trong ngoặc):

| Loại | Lần 1 | Lần 2 | Lần 3 |
| --- | ---: | ---: | ---: |
| noi_dia | 91,0% (824) | 75,7% (74) | 38,9% (18) |
| hang_nang | 70,9% (158) | 39,1% (46) | 17,9% (28) |
| quoc_te | 30,0% (150) | 11,4% (105) | 2,2% (93) |
| doi_tac | 51,5% (68) | 18,2% (33) | 14,8% (27) |

- **quoc_te** không đáng để trợ lý xử lý: 22.515 đ = 1,88× [simulated], chỉ 27,3% thành công. Chạy lại không giúp: lần 2 chỉ đúng 11,4%, lần 3 chỉ 2,2%, lỗi lặp lại trên cùng yêu cầu nên chạy lại chỉ tốn thêm tiền.
- **doi_tac** sát ngưỡng (0,85× [simulated], 54,4% thành công) và có điều khoản riêng → cũng loại khỏi phạm vi pilot. Phạm vi pilot: **noi_dia + hang_nang** (982 yêu cầu, 900 thành công, 3.414 đ/việc [simulated]).

<!-- ===== VÙNG HÙNG — chỉ HÙNG sửa phần dưới ===== -->

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ (simulated) | 0,38× |
| Một nửa khối lượng (22.500) | 16.875 | 2.370 đ | 5.784 đ (simulated) | 0,48× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Ở quy mô đầy đủ (45.000 yêu cầu/tháng), chi phí cố định 1.185 đ/việc đưa tổng lên **4.599 đ = 0,38×** [simulated], không đổi kết luận. Khi giảm một nửa khối lượng (22.500/tháng), cố định tăng gấp đôi lên 2.370 đ/việc (**5.784 đ = 0,48×** [simulated]) và sẽ đội mạnh nếu khối lượng pilot quá nhỏ.

<!-- ===== VÙNG TRUNG — chỉ TRUNG sửa phần dưới ===== -->

## B1 · Đổi từng yếu tố

Gốc (A2): 4.472 đ [simulated]. Mỗi dòng là một lần gọi `mo_hinh` với một tham số đã đổi (`python lab13.py B`). Mọi số trong bảng là simulated.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 | −8,1% |

Tự kiểm (code có `assert`): mỗi kịch bản "giảm một nửa" giảm đúng nửa mức tăng của "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9) vì mô hình cộng tuyến tính.

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated], đúng bằng tổng hai tác động riêng (+5,6% + 40,7%) vì mô hình tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **số ca làm lại** (+51,8%) · 2. **tỉ lệ xem lại** (+40,7%) · 3. **lương nhân viên** (+23,1% khi tăng 25%); giá token chỉ +5,6% khi gấp đôi.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay). Mọi số là simulated.

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 | 319 | 7.449.781 | 4.111 (thấp nhất) |
| 2 lần | 4.093.220 | 234 | **6.901.220 (rẻ nhất)** | 4.237 |
| 3 lần | 4.373.585 | 222 | 7.037.585 | 4.472 |

- **Giới hạn 2 lần** rẻ nhất cho công ty (6.901.220 đ [simulated]), **không trùng** với giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ). Tối ưu riêng chi phí mỗi việc thành công đẩy thêm 85 việc sang nhân viên (319 so với 234), làm cả hệ thống đắt hơn 548.561 đ.

<!-- ===== VÙNG HÙNG — chỉ HÙNG sửa phần dưới ===== -->

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: Với 9 phút làm lại/ca, chi phí là **11.743 đ = 0,98×** [simulated] (hoà vốn nếu xem lại ≤ 5,1 phút); dùng trung bình 15,3 phút/ca từ dữ liệu thì lên **12.415 đ = 1,03×** [simulated] (hoà vốn ≤ 4,8 phút), đắt hơn nhân viên tự làm.
- Kết quả này nói gì về thứ pilot cần học được? Vì tiền xem lại chiếm ~90% tổng chi phí nên xem lại 100% gần như không tiết kiệm được gì; pilot phải học được tỉ lệ xem lại có thể giảm an toàn xuống mức nào và mỗi lần xem lại có rút ngắn dưới 5 phút được không.
