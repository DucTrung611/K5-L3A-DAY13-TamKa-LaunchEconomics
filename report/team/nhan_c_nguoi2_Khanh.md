# Nhiệm vụ C · Nhãn độc lập — Người gắn nhãn 2: Nguyễn Khắc Khánh

Chỉ Khánh sửa file này. Gắn trong 8 phút, **không trao đổi**, **không mở mục Nhiệm vụ C của `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`** trước khi commit.
Commit file này **trước** khi so nhãn (message: `C: nhan doc lap nguoi 2`). Sau khi đã so, **không sửa** bảng nhãn bên dưới.

Năm loại (Google PAIR): Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm. Gắn theo nguyên nhân gốc, không theo chỗ cần sửa.
20 ca: `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, mục "Hai mươi ca lỗi".

| Ca | Nhãn | Lý do ngắn |
| --: | --- | --- |
| 1 | Do người dùng | Khách nhập thiếu 2 chữ số tài khoản ngân hàng nhận hoàn tiền |
| 2 | Hệ thống | Trợ lý gọi tool tra bảng giá tham số hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ |
| 3 | Ngữ cảnh | Hoàn về ví LogiX đúng thiết kế nhưng không giải thích khiến khách tưởng chưa nhận |
| 4 | Giới hạn hệ thống | Chặng do hãng nước ngoài giao không có dữ liệu để xử lý |
| 5 | Ngầm | Hoàn thừa tiền theo giá trước giảm, âm thầm không ai phát hiện cho tới khi kiểm tra mẫu |
| 6 | Do người dùng | Khách chọn nhầm lý do giao trễ trong khi mô tả hàng bị vỡ |
| 7 | Hệ thống | API sổ cái trả lỗi 503 nhưng trợ lý vẫn báo khách đã hoàn tiền thành công |
| 8 | Hệ thống | Trợ lý bịa (hallucination) điều 7.2 không tồn tại trong chính sách hiện hành |
| 9 | Do người dùng | Khách nhập mã đơn của sàn thương mại điện tử thay vì mã vận đơn LogiX |
| 10 | Ngữ cảnh | Từ chối do bão đúng điều khoản bất khả kháng nhưng mâu thuẫn cam kết 24h trên app |
| 11 | Giới hạn hệ thống | Không hỗ trợ xử lý tin nhắn thoại |
| 12 | Ngầm | Tool thiếu trường làm tốn token gấp 3 suốt 3 tuần mà không ai phát hiện |
| 13 | Giới hạn hệ thống | Khách hỏi hoàn phí bảo hiểm hàng hóa, sản phẩm của đối tác ngoài phạm vi trợ lý |
| 14 | Do người dùng | Khách bấm nhầm xác nhận đã nhận tiền khi chưa nhận |
| 15 | Hệ thống | Trễ 26 giờ thuộc khung hoàn 50% nhưng trợ lý tính hoàn 100% |
| 16 | Ngữ cảnh | Gửi tin nhắn lúc 2:14 sáng đúng thiết kế gửi ngay nhưng làm phiền khách ban đêm |
| 17 | Ngầm | Cache bảng giá cũ gây lệch tiền 212 đơn suốt 9 ngày mà không ai mở lại |
| 18 | Ngữ cảnh | Tính đúng tiền hoàn nhưng tin nhắn không kèm công thức làm khách tưởng hoàn thiếu |
| 19 | Giới hạn hệ thống | Dữ liệu đơn từ 14 tháng trước vượt quá giới hạn 12 tháng hệ thống truy cập được |
| 20 | Hệ thống | Thiếu khóa chống trùng (idempotency key) dẫn đến hoàn tiền hai lần cho cùng một đơn |

## Hai dòng bảng khắc phục do Khánh soạn (Hùng chép vào `bang_loi.md`)

Chỉ điền **sau** khi đã so nhãn (S4). Cách phát hiện đo được (event, ngưỡng, tần suất), người phụ trách là một vai trò.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 18 | Ngữ cảnh | Tỉ lệ khách mở lại ticket thắc mắc số tiền hoàn theo tuần | Mẫu tin nhắn gửi khách luôn ghi rõ cách tính: 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với lý do `thieu_du_lieu`, thống kê theo loại yêu cầu | Giữ luồng chuyển nhân viên kèm bản tóm tắt; đưa đơn quốc tế ra khỏi phạm vi pilot | PM trợ lý hoàn phí |
