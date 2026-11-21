# Nhiệm vụ C · Nhãn độc lập — Người gắn nhãn 1: Trần Mạnh Hùng

Chỉ Hùng sửa file này. Gắn trong 8 phút, **không trao đổi**, **không mở mục Nhiệm vụ C của `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`** trước khi commit.
Commit file này **trước** khi so nhãn (message: `C: nhan doc lap nguoi 1`). Sau khi đã so, **không sửa** bảng nhãn bên dưới.

Năm loại (Google PAIR): Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm. Gắn theo nguyên nhân gốc, không theo chỗ cần sửa.
20 ca: `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, mục "Hai mươi ca lỗi".

| Ca | Nhãn | Lý do ngắn |
| --: | --- | --- |
| 1 | Do người dùng | Khách nhập số tài khoản nhận hoàn tiền thiếu hai chữ số |
| 2 | Hệ thống | Trợ lý truyền sai tham số loại hàng khi gọi tool tra bảng giá |
| 3 | Ngữ cảnh | Hệ thống hoàn đúng về ví LogiX theo thiết kế nhưng khách chờ tiền về ngân hàng |
| 4 | Giới hạn hệ thống | Không có dữ liệu chặng hãng nước ngoài giao nên trợ lý không tra cứu được |
| 5 | Ngầm | Hoàn thừa tiền mã giảm giá, không khách nào báo và không có cảnh báo |
| 6 | Do người dùng | Khách chọn nhầm mục "Hoàn phí giao trễ" cho đơn hàng bị vỡ |
| 7 | Hệ thống | API sổ cái trả lỗi 503 nhưng trợ lý vẫn báo hoàn tiền thành công |
| 8 | Hệ thống | Trợ lý bịa "Điều 7.2" không tồn tại trong chính sách hiện hành |
| 9 | Do người dùng | Khách nhập mã đơn sàn TMĐT thay vì mã vận đơn LogiX |
| 10 | Ngữ cảnh | Từ chối đúng chính sách bất khả kháng nhưng app vẫn hiện cam kết giao 24h |
| 11 | Giới hạn hệ thống | Hệ thống không hỗ trợ xử lý đầu vào dạng tin nhắn thoại |
| 12 | Ngầm | Tool depot D05 thiếu trường làm token tăng gấp 3 suốt 3 tuần mà không ai thấy |
| 13 | Giới hạn hệ thống | Hoàn phí bảo hiểm đối tác nằm ngoài phạm vi xử lý của trợ lý |
| 14 | Do người dùng | Khách bấm nhầm nút "Xác nhận đã nhận tiền" khi chưa nhận |
| 15 | Hệ thống | Trợ lý tính hoàn 100% thay vì 50% theo chính sách trễ 24–48 giờ |
| 16 | Ngữ cảnh | Gửi thông báo đúng thiết kế "gửi ngay" nhưng rơi vào 2:14 sáng gây phiền |
| 17 | Ngầm | Cache bảng giá cũ làm lệch 1.000–2.000 đ trên 212 đơn suốt 9 ngày không ai mở lại |
| 18 | Ngữ cảnh | Tính đúng 50% nhưng tin nhắn không kèm công thức khiến khách tưởng hoàn thiếu |
| 19 | Giới hạn hệ thống | Dữ liệu hệ thống chỉ truy cập được 12 tháng, đơn 14 tháng trước ngoài giới hạn |
| 20 | Hệ thống | Thiếu khoá chống trùng (idempotency) khiến trợ lý hoàn hai lần cùng một đơn |
