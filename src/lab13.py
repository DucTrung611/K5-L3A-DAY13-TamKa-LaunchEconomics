"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm TamKa (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.

QUY ƯỚC LÀM SONG SONG (tránh conflict khi merge)
- File chia thành 3 VÙNG, mỗi vùng chỉ một người sửa:
    VÙNG TRUNG : A1, A2 (mo_hinh), in_bang_A (A2, A3, A4), in_bang_B (B1–B4)
    VÙNG KHÁNH : co_mau, in_bang_D1 (D1 a–e, power)
    VÙNG HÙNG  : in_chi_so_E1 (3 chỉ số E1, tỉ lệ mo_lai_trong_7_ngay cho D3)
- Không ai sửa phần hằng số, khối __main__ và dòng đánh dấu ===== VÙNG ... =====.
  Cần thêm import thì đặt ngay trong thân hàm của mình, không thêm lên đầu file.
- Chạy riêng phần của mình:  python lab13.py A | B | D1 | E1   (không truyền gì = chạy tất cả)
"""
import math
import sys

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CO_DINH_THANG = 40_000_000   # chi phí cố định của trợ lý, đồng / tháng (A4)
KHOI_LUONG_THANG = 45_000    # yêu cầu hoàn phí / tháng (A4)


# =====================================================================
# ===== VÙNG TRUNG · A1, A2 ===========================================
# =====================================================================

# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    raise NotImplementedError('VIẾT Ở ĐÂY')


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    raise NotImplementedError('VIẾT Ở ĐÂY')


# =====================================================================
# ===== VÙNG TRUNG · A2–A4, B (in bảng) ===============================
# =====================================================================

def in_bang_A(runs, reqs):
    """In bảng A2 (9 dòng), A3 (4 loại + tỉ lệ ok theo attempt), A4 (chi phí cố định)."""
    print('\n=== A2 · Mô hình chi phí từ trace ===')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:16s} {gia_tri:>14,.1f}')
    # TODO CP1 · A3: gọi mo_hinh(runs, reqs[reqs.loai == loai]) cho từng loai.
    # TODO CP1 · A4: phạm vi noi_dia + hang_nang, cộng CO_DINH_THANG.


def in_bang_B(runs, reqs):
    """In B1 (9 kịch bản), B2 (đổi một cặp), B3 (giới hạn 1/2/3 lần), B4 (xem lại 100%)."""
    print('\n=== B · Bảng độ nhạy ===')
    print('TODO CP2')


# =====================================================================
# ===== VÙNG KHÁNH · D1 cỡ mẫu ========================================
# =====================================================================

def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm để so hai tỉ lệ p1, p2 (làm tròn lên)."""
    from statistics import NormalDist
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    n = (za * math.sqrt(2 * pb * (1 - pb)) + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2
    return math.ceil(n)


def in_bang_D1():
    """In D1 a–e: baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02.
    Thêm: power khi thiết kế cho 6 điểm (859/nhóm) mà tác động thật chỉ 5 điểm."""
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower

    print('\n=== D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02) ===')
    
    # a) Chia theo yêu cầu
    n_yc = co_mau(0.70, 0.75)
    print(f'a) Chia theo yêu cầu: {n_yc:,} yêu cầu mỗi nhóm')

    # b) Theo nhân viên, m = 75
    m_b = 75
    icc = 0.02
    de_b = 1 + (m_b - 1) * icc
    n_b = math.ceil(n_yc * de_b)
    staff_per_arm_b = math.ceil(n_b / m_b)
    total_staff_b = staff_per_arm_b * 2
    print(f'b) Theo nhân viên (m = 75): DE = {de_b:.2f} -> {n_b:,} yêu cầu mỗi nhóm -> {staff_per_arm_b} nhân viên mỗi nhóm (tổng {total_staff_b} > 40: KHÔNG ĐỦ NGƯỜI)')

    # c) 20 nhân viên mỗi nhóm
    max_c = math.floor(20 / icc)
    print(f'c) 20 nhân viên mỗi nhóm: trần hiệu dụng c/ICC = {max_c:,} < {n_yc:,} (KHÔNG ĐẠT)')

    # d) 6 depot mỗi nhóm
    max_d = math.floor(6 / icc)
    print(f'd) 6 depot mỗi nhóm: trần hiệu dụng c/ICC = {max_d:,} < {n_yc:,} (KHÔNG ĐẠT)')

    # e) Mức chênh 6 điểm (859 mỗi nhóm), 20 nhân viên mỗi nhóm
    n_6pt = co_mau(0.70, 0.76)
    m_req = (0.98 * n_6pt) / (20 - 0.02 * n_6pt)
    m_val = math.ceil(m_req)
    de_e = 1 + (m_val - 1) * icc
    print(f'e) Mức chênh 6 điểm ({n_6pt:,} mỗi nhóm), 20 nhân viên: cần m >= {m_val} yêu cầu/người (DE = {de_e:.2f})')

    # Power khi thiết kế cho 6 điểm (859/nhóm) mà tác động thật chỉ 5 điểm
    es = proportion_effectsize(0.75, 0.70)
    power_actual = NormalIndPower().power(effect_size=es, nobs1=n_6pt, alpha=0.05)
    print(f'   Power khi tác động thật chỉ 5 điểm (nobs1={n_6pt}): {power_actual:.2f} (khoảng {power_actual*100:.1f}%)')


# =====================================================================
# ===== VÙNG HÙNG · E1 chỉ số + số cho D3 =============================
# =====================================================================

def in_chi_so_E1(reqs):
    """In 3 chỉ số tính thử (chính, dùng, an toàn) trên 1.200 yêu cầu,
    và tỉ lệ mo_lai_trong_7_ngay: toàn bộ và trong phạm vi noi_dia + hang_nang (dùng cho luật dừng D3)."""
    print('\n=== E1 · Chỉ số tính thử ===')
    print('TODO CP5')


# =====================================================================
# ===== KHÔNG SỬA PHẦN DƯỚI (khối chạy chung) =========================
# =====================================================================

if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')   # console Windows mặc định cp1252, không in được tiếng Việt
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    chon = set(a.upper() for a in sys.argv[1:]) or {'A', 'B', 'D1', 'E1'}
    if chon & {'A', 'B'}:
        kiem_tra_dap_an_biet_truoc()
    if 'A' in chon:
        in_bang_A(runs, reqs)
    if 'B' in chon:
        in_bang_B(runs, reqs)
    if 'D1' in chon:
        in_bang_D1()
    if 'E1' in chon:
        in_chi_so_E1(reqs)
