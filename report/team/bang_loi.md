# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

<!-- ===== Cả file do HÙNG sửa. Nhãn độc lập: mỗi người điền file riêng nhan_c_nguoi1_Hung.md / nhan_c_nguoi2_Khanh.md, commit trước khi so; sau S4 Hùng chép hai cột vào bảng dưới. Hai dòng khắc phục của Khánh lấy từ file nhan_c_nguoi2_Khanh.md. ===== -->

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Trần Mạnh Hùng · Người gắn nhãn 2: Nguyễn Khắc Khánh (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Không có ca nào không trùng (đồng thuận 20/20 = 100%, đạt ngưỡng ≥ 80%).

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `refund_ledger_write` trả lỗi sai định dạng STK ngân hàng > 2% đơn/ngày (theo dõi hằng ngày) | Kiểm tra độ dài và định dạng STK ngay trên form trước khi gửi; hiển thị hướng dẫn sửa tại chỗ | Kỹ sư giao diện |
| 7 | Hệ thống | Event `refund_ledger_write` thất bại (HTTP 503) nhưng vẫn gửi xác nhận hoàn tiền > 0 ca/giờ (cảnh báo thời gian thực) | Chỉ báo thành công sau khi sổ cái xác nhận ghi thành công; hết số lần thử lại thì chuyển `handoff_to_staff` | Kỹ sư backend |
| 18 | Ngữ cảnh | Tỉ lệ khách mở lại ticket thắc mắc số tiền hoàn theo tuần | Mẫu tin nhắn gửi khách luôn ghi rõ cách tính: 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với lý do `thieu_du_lieu`, thống kê theo loại yêu cầu | Giữ luồng chuyển nhân viên kèm bản tóm tắt; đưa đơn quốc tế ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked` kiểm tra mẫu 50 đơn/tuần phát hiện lệch số tiền hoàn > 1% số đơn kiểm | Tự động xoá bộ nhớ đệm (cache) khi cập nhật bảng giá và kiểm tra phiên bản bảng giá trước khi tính | Người kiểm số |
