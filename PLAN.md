# PLAN — Lab 13 · Nhóm TamKa (L3A) · 3 thành viên: Trung · Hùng · Khánh

Kế hoạch làm bài Lab 13 (Định giá agent và lập kế hoạch pilot, Gate 2a) cho nhóm **3 người**, chia việc để **ba người chạy song song**, chỉ gặp nhau ở vài điểm đồng bộ ngắn. Đọc file này 5 phút trước 14:00.

Nguồn: [README.md](README.md), [CHECKPOINTS.md](CHECKPOINTS.md), [RUBRIC.md](RUBRIC.md), [RULES.md](RULES.md), [SUBMISSION.md](SUBMISSION.md), [docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md](docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md), [docs/du_lieu_va_cong_thuc.md](docs/du_lieu_va_cong_thuc.md), `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`.

---

## 1. Bài này chấm gì (để biết dồn sức vào đâu)

| Tiêu chí | Điểm | Nhiệm vụ | File bằng chứng | Người chịu trách nhiệm chính |
| --- | ---: | --- | --- | --- |
| C1 · Mô hình chi phí | 20 | A | `src/lab13.py`, `report/team/bang_chi_phi.md` (A1–A4) | Trung |
| C2 · Bảng độ nhạy | 15 | B | `report/team/bang_chi_phi.md` (B1–B4) | Trung (code) · Hùng (kiểm số, B3/B4) |
| C3 · Bảng lỗi | 10 | C | `report/team/bang_loi.md` | Hùng + Khánh (gắn nhãn) |
| C4 · pilot_plan.yaml | 15 | D | `report/team/pilot_plan.yaml` | Khánh |
| C5 · Chỉ số, event, rủi ro, hồ sơ | 10 | E | `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md` | Hùng (chỉ số) · Trung (rủi ro) · Khánh (hồ sơ) |
| C6–C8 · Hội đồng chấm | 30 | E + duyệt chéo | `ho_so_launch_v0.md`, `pilot_plan.yaml` | Khánh trình bày, cả 3 chuẩn bị số |

Số được nhận nếu lệch ≤ 2% so với đáp án. Ba phép thử A1 phải ĐẠT trước khi làm gì tiếp.

---

## 2. Phân vai: 4 vai của lab chia cho 3 người

Lab thiết kế cho 4 vai. Nhóm 3 người gộp như sau (ghi đúng vào `TEAM.md`, dòng STT 4 để trống và ghi chú "nhóm 3 người, vai gộp"):

| Thành viên | Vai chính | Vai kiêm | Sở hữu file (chỉ người này sửa) |
| --- | --- | --- | --- |
| **Trung** | Người viết code (trước giải lao) | Người phụ trách B3/B4 + rủi ro kinh tế E2 | `src/lab13.py` (khung + phần A, B), `report/team/bang_chi_phi.md` |
| **Hùng** | Người kiểm số | Người gắn nhãn 1; người phụ trách chỉ số E1 + event | `report/team/bang_loi.md`, `report/team/nhan_c_nguoi1_Hung.md`, `report/team/chi_so.md` |
| **Khánh** | Người gắn nhãn 2 kiêm giữ hồ sơ | Người viết code sau giải lao (phần D1); người trình bày Gate 2a | `report/team/pilot_plan.yaml`, `report/team/ho_so_launch_v0.md`, `report/team/nhan_c_nguoi2_Khanh.md`, `TEAM.md`, `report/team/group_report.md` |

Vì sao chia vậy:
- **Hai người gắn nhãn (Hùng, Khánh) không phải người viết code A/B**, nên lúc 15:35 họ gắn nhãn còn Trung hoàn thiện B — đúng như đề yêu cầu.
- **Quy tắc "đổi người viết code sau giải lao"** được đáp ứng: Khánh viết phần cỡ mẫu D1 trong `lab13.py`, Hùng tự tay tính lại chi phí (bản kiểm số độc lập) → có ít nhất 2 người tự tính được chi phí.
- **Mỗi file chỉ có một chủ** → ba người commit song song không đụng nhau.

`report/team/phieu_cham.md` (chấm nhóm khác) do Trung + Hùng điền lúc 17:10. Mỗi người tự viết báo cáo cá nhân của mình.

---

## 3. Nguyên tắc để làm song song không giẫm chân nhau

### 3.1 Bản đồ sở hữu file (khung đã tạo sẵn trong repo)

Khung các file đã được tạo và đánh dấu vùng bằng comment `===== VÙNG <TÊN> =====` (trong `.md` là comment HTML ẩn, không hiện khi xem). **Chỉ sửa trong vùng mang tên mình.** Git tự gộp được các thay đổi ở những vùng khác nhau của cùng một file; xung đột chỉ xảy ra khi hai người sửa cùng một chỗ.

| File | Trung | Hùng | Khánh |
| --- | --- | --- | --- |
| `src/lab13.py` | vùng A1–A2 (`mo_hinh`…), `in_bang_A`, `in_bang_B` | `in_chi_so_E1` | `co_mau`, `in_bang_D1` |
| `report/team/bang_chi_phi.md` | A1, A2, A3, B1, B2, B3 | A4, B4 | — |
| `report/team/nhan_c_nguoi1_Hung.md` | — | cả file | — |
| `report/team/nhan_c_nguoi2_Khanh.md` | — | — | cả file (nhãn + 2 dòng khắc phục) |
| `report/team/bang_loi.md` | — | cả file (chép 2 bộ nhãn + 2 dòng của Khánh vào) | — |
| `report/team/pilot_plan.yaml` | chú thích tỉ lệ mở lại + `stop_rules` | chú thích D2 | D1, đánh đổi, mọi trường còn lại |
| `report/team/chi_so.md` | E2 rủi ro kinh tế | E1 chỉ số + event + kiểm tra chéo | — |
| `report/team/ho_so_launch_v0.md` | — | — | cả file (Trung, Hùng gửi số cho Khánh) |
| `report/team/group_report.md` | — | — | cả file |
| `report/team/phieu_cham.md` | cả file | đọc chấm cùng, báo số cho Trung | — |
| `TEAM.md` | mục cá nhân của Trung | mục cá nhân của Hùng | phần chung + mục cá nhân của Khánh |
| Báo cáo cá nhân | `2A202603449_ThanDucTrung.md` | `2A202603496_TranManhHung.md` | `2A202603472_NguyenKhacKhanh.md` |
| `PLAN.md`, `.gitattributes`, file trong `docs/`, 2 file CSV, `lab13_starter.py` | không ai sửa | | |

**`src/lab13.py`:** khối `if __name__ == '__main__':` ở cuối đã gọi sẵn 4 hàm `in_bang_A`, `in_bang_B`, `in_bang_D1`, `in_chi_so_E1` → **không ai sửa khối này, phần hằng số và các import ở đầu file**. Cần import thêm thì đặt trong thân hàm của mình. Chạy riêng phần của mình, không cần chờ A1 xong:

```bash
cd src
python lab13.py D1     # Khánh
python lab13.py E1     # Hùng
python lab13.py A B    # Trung (cần A1 ĐẠT)
python lab13.py        # chạy tất cả, dùng khi chốt bài
```

### 3.2 Git: quy trình làm chung một repo

Lần đầu (Hùng, Khánh): Trung vào GitHub → Settings → Collaborators, mời 2 bạn. Hai bạn clone:

```bash
git clone https://github.com/DucTrung611/K5-L3A-DAY13-TamKa-LaunchEconomics.git
cd K5-L3A-DAY13-TamKa-LaunchEconomics
```

Mỗi lần làm xong một phần nhỏ (một bảng, một hàm):

```bash
git pull --rebase                       # lấy bài của 2 bạn về trước
git add <chỉ các file của mình>         # KHÔNG dùng "git add ." để khỏi đẩy nhầm file nháp, .venv
git commit -m "A2: mo_hinh + bang A2"   # message ghi rõ nhiệm vụ
git pull --rebase
git push
```

- Làm thẳng trên `main`, commit nhỏ và thường xuyên. Vì mỗi vùng chỉ một chủ, `pull --rebase` gần như không bao giờ xung đột.
- Nếu vẫn xung đột: mở file, giữ phần trong vùng của **cả hai** người (không xoá vùng của bạn), `git add <file>` → `git rebase --continue`. Không chắc thì gọi chủ vùng kia, đừng tự quyết.
- `.gitattributes` đã ép dấu xuống dòng LF → máy Windows và macOS không tạo diff cả file.
- Không force-push, không sửa commit cũ (RULES).
- **Bằng chứng gắn nhãn độc lập (C):** Hùng commit `nhan_c_nguoi1_Hung.md`, Khánh commit `nhan_c_nguoi2_Khanh.md` **trước** khi so nhãn; thời gian commit chứng minh hai người không trao đổi. Sau khi so, không sửa hai bảng nhãn này.

### 3.3 Điểm đồng bộ (chỉ 6 lần, mỗi lần ≤ 5 phút)

| Giờ | Điểm đồng bộ | Ai | Nội dung |
| --- | --- | --- | --- |
| 14:10 | S1 · Khung code | Cả nhóm | Khung đã có sẵn trong repo; ai cũng `git pull`, chạy `python lab13.py D1 E1` in ra TODO là được |
| ~14:53 | S2 · Chốt số A | Trung + Hùng | So số A2/A3/A4 của code với bản tính tay của Hùng và slide chữa; lệch > 2% thì dừng sửa |
| ~15:20 | S3 · Chốt số B + D1 | Cả nhóm | B1 đủ 9 dòng, xếp hạng 3 yếu tố; D1 a–e của Khánh khớp; chốt phạm vi pilot từ A3 |
| ~15:46 | S4 · So nhãn C | Hùng + Khánh (Trung chứng kiến) | Đếm đồng thuận, thống nhất ca lệch |
| ~16:30 | S5 · Chốt pilot | Cả nhóm | Cách chia, mức chênh, ngưỡng luật dừng; YAML qua 2 lệnh kiểm tra |
| ~16:55 | S6 · Chốt đề xuất | Cả nhóm | Go / Go có điều kiện / No-go, có nêu con số bất lợi |

Ngoài 6 điểm này, **không chờ nhau**: ai xong trước thì làm việc kế tiếp trong luồng của mình (xem mục 4).

---

## 4. Lịch làm song song (swimlane)

| Giờ | Trung (code A/B) | Hùng (kiểm số · nhãn 1 · chỉ số) | Khánh (nhãn 2 · hồ sơ · code D1) |
| --- | --- | --- | --- |
| **13:50–14:00** | Fork/đổi tên repo nhóm (nếu chưa), mời 2 bạn | Cài `.venv` theo [src/README.md](src/README.md), chạy lệnh kiểm tra `san sang` | Cài `.venv`, chạy lệnh kiểm tra `san sang` |
| **14:00–14:10** | Kiểm tra 2 bạn đã clone + pull được; đọc mục A trong hướng dẫn chi tiết | Đọc [docs/du_lieu_va_cong_thuc.md](docs/du_lieu_va_cong_thuc.md), mở 2 CSV xem cột | Điền `TEAM.md` (tên nhóm TamKa, L3A, vai); mở `ho_so_launch_v0.md` |
| **14:10–14:20** | **A1**: 3 hàm → `python lab13.py` in `ĐẠT` (1,20 · 1,25 · 1,25) | **Kiểm số độc lập** (script nháp ngoài repo hoặc notebook): tổng token, tool, lần chạy attempt > 1, phút xem lại/làm lại, số `thanh_cong` | **D1**: viết `co_mau()` + tính a, b, c, d, e trong vùng của mình |
| **14:20–14:40** | **A2**: `mo_hinh` + bảng A2 (9 dòng, 2 dòng `simulated`) | Tiếp kiểm số: **A4** (phạm vi noi_dia + hang_nang, cố định 40 tr/tháng, 2 mức khối lượng) | D1: thêm power khi chênh thật chỉ 5 điểm mà thiết kế cho 6 điểm (NormalIndPower, n = 859); ghi D1 vào chú thích đầu `pilot_plan.yaml` |
| **14:40–14:53** | **A3**: gọi `mo_hinh` theo từng `loai` + tỉ lệ ok theo attempt (trả lời "chạy lại có giúp không") | **E1**: viết `in_chi_so_E1` — 3 chỉ số + tỉ lệ `mo_lai_trong_7_ngay` (toàn bộ và trong phạm vi) | Điền sẵn phần YAML không phụ thuộc số: `owner`, `assignment`, `rollback`, `identifiability`, `interim_looks` |
| 14:53 | **S2 · chốt số A** (Trung + Hùng), đối chiếu slide chữa | ← | Khánh điền mục 1, 3 của hồ sơ bằng số A vừa chốt |
| **14:55–15:20** | **B1, B2**: 9 kịch bản + cặp (token×2 & xem lại×2) + xếp hạng; **B3**: giới hạn 1/2/3 lần, chi phí cả hệ thống | **B4** tính tay/độc lập: xem lại 100% noi_dia + hang_nang (5 phút/ca ok, 9 phút/ca làm lại), thêm biến thể 15,3 phút và mức hoà vốn; tự kiểm "giảm một nửa = nửa mức tăng gấp đôi" trên bảng B1 của Trung | **Không mở phần C của hướng dẫn chi tiết** (có nhãn đáp án). Điền mục 2 hồ sơ khi B1 có; soạn sẵn D2 nháp |
| 15:20 | **S3 · chốt B + D1 + phạm vi pilot** (2 phút), rồi giải lao | ← | ← |
| **15:35–15:43** | Hoàn thiện câu trả lời B3, B4 trong `bang_chi_phi.md` (≤ 3 dòng, có số, nhãn `simulated`) | **C · gắn nhãn độc lập 20 ca** (8 phút, ngồi tách, không trao đổi) → commit | **C · gắn nhãn độc lập 20 ca** (8 phút, ngồi tách, không trao đổi) → commit |
| **15:43–15:51** | Soạn nháp **E2 rủi ro kinh tế** (≥ 2 dòng, số từ B1/B4/A4) | **S4**: so nhãn, đồng thuận = trùng/20; thống nhất ca lệch + 1 câu quy tắc mỗi ca | **S4** cùng Hùng |
| **15:51–16:05** | Review bảng khắc phục: mỗi dòng có event/ngưỡng/tần suất + 1 vai trò | Bảng khắc phục: 3 dòng (Do người dùng, Hệ thống, Ngầm) | Bảng khắc phục: 2 dòng (Ngữ cảnh, Giới hạn hệ thống); điền mục 5 hồ sơ |
| 16:05–16:08 | Đối chiếu slide chữa C | ← | ← |
| **16:08–16:30** | **D3 luật dừng**: 3 luật NẾU–TRONG–THÌ–KHÔNG THÌ (an toàn, chi phí, mức độ sử dụng), ngưỡng dựa trên tỉ lệ mở lại hiện tại và chi phí A/B | **D2**: 5 câu "tách được tác động" vào chú thích YAML; liệt kê `simulated_inputs` | **D**: chọn cách chia, điền `primary_metric`, `scope` (theo A3), `decision_date`, ghép luật dừng của Trung; chạy 2 lệnh kiểm tra YAML |
| 16:30 | **S5 · chốt pilot** + đối chiếu slide chữa D | ← | ← |
| **16:36–16:55** | Chốt **E2** vào `chi_so.md` (bảng rủi ro); mục 2, 7 hồ sơ cho Khánh | **E1** vào `chi_so.md`: 3 chỉ số tính thử + 2 chỉ số tự đề xuất + ≥ 6 event có `trace_id` + kiểm tra chéo chỉ số ↔ event | **E3** hồ sơ: hoàn thiện 7 mục (con số · trạng thái · vai trò phụ trách); viết nháp đề xuất |
| 16:55–17:00 | **S6 · chốt đề xuất** + `grep -rni production ../report/team` không in gì → push | ← | ← |
| **17:00–17:10** | Nhận hồ sơ nhóm n+1 | Nhận hồ sơ nhóm n+1 | Gửi hồ sơ nhóm mình cho hội đồng; luyện câu trả lời 1 phút |
| **17:10–17:25** | Chấm nhóm n+1 vào `phieu_cham.md` (C6, C7) | Chấm nhóm n+1 (C8: pilot), viết 1 câu hỏi | Chuẩn bị trả lời 3 câu hội đồng hay hỏi (mục 7) |
| **17:25–17:45** | Công bố kết quả chấm (1 phút) | Ghi câu trả lời của đội trình vào phiếu | Trình bày (1 phút) + trả lời (1 phút) |
| **17:45–18:00** | Chạy `python lab13.py` trên **máy Hùng** (checklist "máy khác"); push cuối | Báo cáo cá nhân + đóng góp trong `TEAM.md` | `group_report.md` (ghi kết quả hội đồng nhóm nhận); báo cáo cá nhân |
| **Sau giờ học → 23:59** | Soát chính tả số, nhãn `simulated` | Soát `bang_loi.md`, `chi_so.md` | Soát checklist nộp (mục 8); **cả 3 tự nộp link repo trên LMS** |

---

## 5. Chi tiết từng nhiệm vụ

### A · Mô hình chi phí (Trung code · Hùng kiểm số)

**Quy tắc cốt lõi:** tử số tính **mọi** lần chạy (kể cả `status == 'loi'`), mẫu số chỉ đếm `ket_qua == 'thanh_cong'`. Giá token chia 1.000 trước khi nhân. Đọc CSV yêu cầu với `keep_default_na=False`.

- **A1** — `E[lần chạy] = (1 − (1 − p)^k) / p` (k=None → 1/p); `P(thành công) = 1 − (1 − p)^k` (k=None → 1); hệ số = E / P.
- **A2** — `mo_hinh` trả về: `token, tool, chay_lai (attempt > 1), xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc`. Hỗ trợ `max_lan_chay` (bỏ run có attempt > giới hạn; yêu cầu có `so_lan_chay` > giới hạn → `chuyen_nhan_vien`, phút xem lại/làm lại = 0) để B gọi lại.
- **A3** — `mo_hinh(runs, reqs[reqs.loai == x])` cho 4 loại; thêm bảng tỉ lệ ok theo `attempt` × `loai` để chứng minh chạy lại không giúp loại kém.
- **A4** — chỉ noi_dia + hang_nang: số việc thành công/tháng = 45.000 × (thành công trong phạm vi / 1.200); cố định/việc = 40.000.000 / số đó; làm cho 45.000 và một nửa khối lượng.
- **Lưu ý khi so với 12.000 đ:** chi phí mỗi việc thành công chưa tính phần nhân viên làm thay các ca không thành công → khi so "có rẻ hơn nhân viên không" phải dùng **chi phí cả hệ thống / yêu cầu** (cộng 12.000 đ × số ca không thành công).

**Việc của Hùng (kiểm số):** tính lại bằng script nháp riêng, **không gọi `mo_hinh`** — ít nhất: tổng token, tổng tool, chi phí mỗi việc thành công, chi phí trong phạm vi A4, B4. Ghi cách tính vào báo cáo cá nhân (bằng chứng "tự tay tính").

### B · Độ nhạy (Trung code · Hùng kiểm tra)

- B1: 9 kịch bản = 9 lần gọi `mo_hinh` với một tham số đổi (dict kịch bản).
- B2: một lần gọi đổi cặp; kiểm tra = tổng 2 tác động riêng (mô hình tuyến tính). Xếp hạng 3 yếu tố theo % thay đổi khi "gấp đôi".
- B3: với giới hạn 1/2/3: tổng trợ lý, số yêu cầu không thành công, chi phí cả hệ thống = tổng + 12.000 × không thành công, cps. Trả lời: giới hạn rẻ nhất cho công ty có trùng giới hạn cps thấp nhất không.
- B4 (Hùng tính): phạm vi noi_dia + hang_nang; yêu cầu có ≥ 1 run `ok` × 5 phút; ca `lam_lai` × 9 phút; + token/tool mọi run của phạm vi; ÷ số thành công trong phạm vi. Ghi thêm biến thể dùng phút làm lại trung bình thật từ cột `phut_lam_lai_simulated` và mức hoà vốn phút xem lại.

### C · Bảng lỗi (Hùng + Khánh gắn nhãn · Trung review)

- 20 ca nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, mục "Hai mươi ca lỗi". 5 loại PAIR: Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm.
- **Liêm chính:** Hùng và Khánh **không đọc mục "Nhiệm vụ C" trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` trước khi gắn và commit nhãn** (mục đó có nhãn tham khảo). Không sửa bộ nhãn độc lập sau khi đã so.
- Gắn theo **nguyên nhân gốc**, không theo chỗ cần sửa. Phân biệt Hệ thống (sai đã lộ ra, có người thấy) với Ngầm (không ai nhận ra cho tới khi kiểm tra mẫu).
- Đồng thuận < 16/20 → viết lại định nghĩa trước khi đi tiếp.
- Bảng khắc phục 5 ca (mỗi loại 1 ca): "phát hiện bằng gì" phải có **event + ngưỡng + tần suất**; "ai phụ trách" là **một vai trò** (PM trợ lý hoàn phí, Kỹ sư trưởng agent, Trưởng nhóm CSKH, Kế toán trưởng…), không ghi "cả đội".

### D · pilot_plan.yaml (Khánh chủ · Trung luật dừng · Hùng D2)

- **D1** (Khánh, viết từ 14:10 vì không phụ thuộc A/B): baseline 0,70, +5 điểm, α 0,05, power 0,8, ICC 0,02.
  - a) chia theo yêu cầu: `co_mau(0.70, 0.75)`.
  - b) theo nhân viên m = 75: DE = 1 + 74 × 0,02; n × DE; số nhân viên mỗi nhóm; so với 40 người.
  - c) 20 nhân viên/nhóm: trần cỡ mẫu hiệu dụng = c / ICC.
  - d) 6 depot/nhóm: c / ICC.
  - e) chênh 6 điểm (859/nhóm), 20 người/nhóm: giải 20m / (1 + (m − 1) × 0,02) ≥ 859.
- **Chọn cách chia** sau khi có D1: so sánh theo yêu cầu / nhân viên / depot (đủ mẫu? tách được tác động? ≥ 20 cụm?). Nếu chưa đủ mẫu ở 5 điểm → ghi rõ **đánh đổi đã chấp nhận** và con số bất lợi (power khi tác động thật chỉ 5 điểm).
- **D2** (Hùng): 5 câu, mỗi câu 1 dòng trong phần chú thích.
- **D3 luật dừng** (Trung): tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại **trước** khi đặt ngưỡng (ngưỡng tuyệt đối thấp hơn tỉ lệ hiện tại sẽ dừng pilot ngay tuần đầu → nên so với nhóm đối chứng + trần tuyệt đối). Đủ 4 vế NẾU – TRONG – THÌ – KHÔNG THÌ, có ngưỡng, thời hạn, người có quyền dừng.
- `scope` lấy từ A3 (loại nào > hoặc sát 12.000 đ thì loại ra, ghi lý do bằng số, nhãn `simulated`).
- **Kiểm tra trước khi push** (chạy trong `src/`):
  ```bash
  python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml', encoding='utf-8'))"
  grep -v '^ *#' ../report/team/pilot_plan.yaml | grep -n '?'     # không được in gì
  ```

### E · Chỉ số, rủi ro, hồ sơ (Hùng E1 · Trung E2 · Khánh E3)

- **E1** (Hùng): 3 chỉ số tính thử (chính · dùng · an toàn) bằng `in_chi_so_E1`; tự đề xuất thêm 1 chỉ số dùng + 1 chỉ số an toàn (không cần tính); ≥ 6 event, mỗi event có `trace_id`; kiểm tra chéo: mỗi chỉ số tính từ event nào. Viết "chỉ số trong đợt chạy thử là …", **không** viết "trợ lý đã nâng chỉ số".
- **E2** (Trung): ≥ 2 dòng rủi ro, tác động lấy thẳng từ bảng B1/B4/A4 (ví dụ: làm lại gấp đôi; xem lại 100% kéo dài; khối lượng thấp làm phí cố định/việc tăng), mỗi dòng có dấu hiệu theo dõi + hành động + vai trò.
- **E3** (Khánh, điền dần từ 14:00): 7 mục, mỗi mục có con số chính · trạng thái (**Xong, có bằng chứng · Chưa · Giả lập**; mục dựa trên cột `_simulated` ghi Giả lập) · vai trò phụ trách. Dòng cuối: **Go / Go có điều kiện / No-go**. Nếu Go có điều kiện: mỗi điều kiện có vai trò + ngày kiểm tra. Đề xuất **phải nêu con số bất lợi** (vd. xem lại 100% gần hoà vốn; power thấp nếu tác động thật chỉ 5 điểm) và cách xử lý — đây là chỗ ăn 10 điểm C6.

### Duyệt chéo Gate 2a

- Nhóm n chấm nhóm n + 1 vào `report/team/phieu_cham.md`. Chấm theo bằng chứng, mỗi ô điểm có lý do kèm số.
- Câu hỏi gợi ý cho nhóm bạn: chi phí khi tuần đầu xem lại 100%? cách chia có ≥ 20 cụm mỗi nhóm không? ngưỡng an toàn có làm pilot dừng ngay tuần đầu với tỉ lệ mở lại hiện tại không?

---

## 6. Số để tự đối chiếu (từ hướng dẫn chi tiết, lệch ≤ 2% là đạt)

Dùng để **kiểm**, không chép thay cho code: mọi số trong hồ sơ phải do `lab13.py` in ra hoặc có cách tính tay (RULES).

| Mục | Số đối chiếu |
| --- | --- |
| A1 | 1,20 · 1,25 · 1,25 |
| A2 | token 245.585 · tool 84.000 · lần chạy 2–3: 93.804 · xem lại 1.780.000 [sim] · làm lại 2.264.000 [sim] · tổng 4.373.585 · thành công 978 · cps 4.472 [sim] · hoá đơn/yc 274,7 · gấp 16,3× · làm lại 51,8% lớn nhất |
| A3 | noi_dia 2.696 (0,22×) · hang_nang 8.221 (0,69×) · quoc_te 22.515 (1,88×) · doi_tac 10.215 (0,85×) |
| A4 | 33.750 việc/tháng · cố định 1.185 đ/việc · 4.599 đ (0,38×) · nửa khối lượng 5.784 đ (0,48×) |
| B1 | token×2 +5,6% · xem lại×2 +40,7% · làm lại×2 +51,8% · lương +25% → +23,1% · tối đa 2 lần −5,2% · 1 lần −8,1% |
| B2/B3 | cặp +46,3% · xếp hạng: làm lại > xem lại > lương · rẻ nhất cho công ty: giới hạn 2 lần (6.901.220 đ) |
| B4 | 11.743 đ = 0,98× (9 phút) · 12.414 đ = 1,03× (15,3 phút) [sim] |
| D1 | a 1.251 · b DE 2,48 → 3.103/nhóm, 42 người/nhóm (không đủ) · c ≤ 1.000 · d ≤ 300 · e m ≥ 299 |
| E1 | chính 82,83% · bỏ qua gợi ý 27,12% · mở lại 7 ngày 4,25% (trong phạm vi 3,97%) |

(Nhãn C cố ý **không** ghi ở đây để giữ hai bộ nhãn độc lập.)

---

## 7. Rủi ro của chính nhóm và cách xử lý

| Rủi ro | Cách xử lý |
| --- | --- |
| Chỉ có 3 người, lab thiết kế cho 4 | Gộp vai như mục 2; D1 và E1 kéo lên làm sớm (không phụ thuộc A/B) để giải phóng 16:08–17:00 |
| A1 không ĐẠT làm chặn mọi thứ | Trung ưu tiên A1 trong 10 phút đầu; Hùng/Khánh vẫn làm được phần độc lập (kiểm số thô, D1) |
| Xung đột git trên `lab13.py` | Khung vùng riêng ở 14:10; mỗi người chỉ sửa hàm của mình; `git pull --rebase` trước push |
| Máy ai đó cài thư viện lỗi | Cài từ 13:50; nếu lỗi, người đó làm việc tài liệu trên máy mình và chạy code trên máy bạn; ghi lỗi + bằng chứng vào mục 5 `group_report.md` |
| Thiếu nhãn `simulated` / lọt từ bị cấm | 16:55 Khánh chạy `grep -rni production ../report/team` và soát mọi số từ cột `_simulated` |
| Người phụ trách ghi "cả đội" | Danh sách vai trò dùng chung: Giám đốc vận hành, PM trợ lý hoàn phí, Kỹ sư trưởng agent, Trưởng nhóm CSKH, Kế toán trưởng |
| Một thành viên quên nộp link LMS | Trước 23:00 Khánh nhắn nhóm xác nhận cả 3 đã nộp |

---

## 8. Checklist nộp (Khánh giữ, cả nhóm tick)

- [ ] Repo tên `K5-L3A-DAY13-TamKa-LaunchEconomics`, public hoặc đã mời giảng viên.
- [ ] `TEAM.md`: tên nhóm, lớp, URL repo, commit chốt, 3 thành viên + vai gộp + đóng góp.
- [ ] 3 báo cáo cá nhân `report/team/MSSV_HoTen.md` (copy từ mẫu, giữ nguyên file mẫu), có mục công cụ AI đã dùng và cách tự kiểm tra.
- [ ] `cd src && python lab13.py` chạy hết trên máy khác (máy Hùng); A1 in ĐẠT.
- [ ] Đủ 6 file hồ sơ đúng tên trong `report/team/` + `group_report.md`.
- [ ] Mọi số từ cột `_simulated` có nhãn `simulated`.
- [ ] `pilot_plan.yaml` qua `yaml.safe_load`, không còn `?` ngoài chú thích, ≥ 3 luật dừng đủ 4 vế.
- [ ] Mỗi mục hồ sơ có người phụ trách là một vai trò.
- [ ] Đề xuất là một trong ba: Go / Go có điều kiện / No-go.
- [ ] `grep -rni production report/team` không in gì.
- [ ] Không commit `.venv/`, `.env`, không sửa 2 file CSV.
- [ ] Push trước 23h59 GMT+7; **cả 3 người** tự nộp link repo trên LMS.
