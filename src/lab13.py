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
    # Lần chạy thứ i chỉ xảy ra khi i-1 lần trước đều sai: tổng (1-p)^(i-1), i=1..k = (1-(1-p)^k)/p
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # Tiền trả cho mọi lần chạy (tử số) chia cho xác suất thành công (mẫu số) → luôn bằng 1/p
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


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
    reqs = reqs.copy()
    # Chỉ giữ lần chạy thuộc các yêu cầu đang xét (để A3/A4 gọi với reqs đã lọc theo loại)
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        # Bỏ lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn giới hạn → chuyển nhân viên,
        # không còn phút xem lại/làm lại của trợ lý
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    # Tử số: MỌI lần chạy, kể cả status == 'loi'. Giá token tính cho 1.000 token.
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai   # simulated
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai   # simulated
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    # Mẫu số: chỉ yêu cầu thành công
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong if thanh_cong else float('nan'),
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


# =====================================================================
# ===== VÙNG TRUNG · A2–A4, B (in bảng) ===============================
# =====================================================================

def in_bang_A(runs, reqs):
    """In bảng A2 (9 dòng), A3 (4 loại + tỉ lệ ok theo attempt), A4 (chi phí cố định)."""
    print('\n=== A2 · Mô hình chi phí từ trace ===')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:16s} {gia_tri:>14,.1f}')
    tong = ket_qua['tong']
    print(f'Phút xem lại [sim]: {reqs.phut_xem_lai_simulated.sum():,} · phút làm lại [sim]: '
          f'{reqs.phut_lam_lai_simulated.sum():,} · số lần gọi tool: {runs.tool_calls.sum():,}')
    print(f'cps / hoá đơn mỗi yêu cầu = {ket_qua["cps"] / ket_qua["hoa_don_moi_yc"]:.1f} lần')
    for khoan in ('token', 'tool', 'xem_lai', 'lam_lai'):
        print(f'  tỉ trọng {khoan:8s} {ket_qua[khoan] / tong * 100:5.1f}%')
    print(f'  giờ nhân viên (xem lại + làm lại) {(ket_qua["xem_lai"] + ket_qua["lam_lai"]) / tong * 100:5.1f}%')
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_thong = (tong + BASELINE * khong_tc) / len(reqs)
    print(f'Chi phí cả hệ thống / yêu cầu [sim] = ({tong:,.0f} + {khong_tc} × {BASELINE:,}) / {len(reqs):,} '
          f'= {he_thong:,.0f} đ = {he_thong / BASELINE:.2f}× của {BASELINE:,} đ')

    # ---------- A3 · tách theo loại ----------
    print('\n=== A3 · Tách theo loại yêu cầu ===')
    print(f'{"loai":10s} {"so_yc":>6s} {"ti_le_tc":>9s} {"chay/yc":>8s} {"cps [sim]":>10s} {"so 12k":>7s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs.loai == loai]
        kq = mo_hinh(runs, r)
        so_chay = runs.request_id.isin(r.request_id).sum()
        print(f'{loai:10s} {len(r):6d} {kq["thanh_cong"] / len(r) * 100:8.1f}% {so_chay / len(r):8.2f} '
              f'{kq["cps"]:10,.0f} {kq["cps"] / BASELINE:6.2f}×')
    # Chạy lại có giúp không: tỉ lệ ok theo từng lần thử, theo loại
    gop = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    gop['ok'] = (gop.status == 'ok').astype(float)
    bang_ok = gop.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean') * 100
    so_run = gop.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='count')
    print('Tỉ lệ lần chạy ok (%) theo attempt (số lần chạy trong ngoặc):')
    for loai in bang_ok.index:
        o = '  '.join(f'lần {a}: {bang_ok.loc[loai, a]:5.1f}% ({int(so_run.loc[loai, a])})'
                      for a in bang_ok.columns)
        print(f'  {loai:10s} {o}')

    # ---------- A4 · cộng chi phí cố định, phạm vi noi_dia + hang_nang ----------
    print('\n=== A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ===')
    pv = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    kq = mo_hinh(runs, pv)
    print(f'Phạm vi: {len(pv)} yêu cầu, {kq["thanh_cong"]} thành công, tổng {kq["tong"]:,.0f} đ, '
          f'cps {kq["cps"]:,.0f} đ [sim]')
    for nhan, khoi_luong in [('45.000 yc/tháng', KHOI_LUONG_THANG), ('một nửa khối lượng', KHOI_LUONG_THANG / 2)]:
        viec_tc = khoi_luong * kq['thanh_cong'] / len(reqs)
        co_dinh = CO_DINH_THANG / viec_tc
        tong_viec = kq['cps'] + co_dinh
        print(f'  {nhan:20s} việc TC/tháng {viec_tc:9,.0f} · cố định/việc {co_dinh:6,.0f} đ · '
              f'cps + cố định {tong_viec:6,.0f} đ = {tong_viec / BASELINE:.2f}× [sim]')


def in_bang_B(runs, reqs):
    """In B1 (9 kịch bản), B2 (đổi một cặp), B3 (giới hạn 1/2/3 lần), B4 (xem lại 100%)."""
    print('\n=== B1 · Đổi từng yếu tố (cps, simulated) ===')
    goc = mo_hinh(runs, reqs)['cps']
    kich_ban = {
        'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':            dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':       dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':            dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':       dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':             dict(luong_phut=2500),
        'Tối đa 2 lần chạy':          dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':             dict(max_lan_chay=1),
    }
    print(f'{"Gốc (A2)":26s} {goc:8,.0f}')
    thay_doi = {}
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        thay_doi[ten] = (cps / goc - 1) * 100
        print(f'{ten:26s} {cps:8,.0f} {thay_doi[ten]:+6.1f}%')
    # Tự kiểm: mô hình tuyến tính → "giảm một nửa" = −½ × "gấp đôi"
    for a, b in [('Giá token gấp đôi', 'Giá token giảm một nửa'), ('Xem lại gấp đôi', 'Xem lại giảm một nửa'),
                 ('Làm lại gấp đôi', 'Làm lại giảm một nửa')]:
        assert abs(thay_doi[b] + thay_doi[a] / 2) < 1e-6, f'{b} phải bằng −½ × {a}'
    print('Tự kiểm "giảm một nửa = −½ × gấp đôi": ĐẠT')

    print('\n=== B2 · Đổi một cặp và xếp hạng ===')
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    tong_rieng = thay_doi['Giá token gấp đôi'] + thay_doi['Xem lại gấp đôi']
    print(f'Token ×2 + xem lại ×2: {cap:,.0f} đ ({(cap / goc - 1) * 100:+.1f}%) · '
          f'tổng hai tác động riêng {tong_rieng:+.1f}%')
    xep_hang = sorted(['Giá token gấp đôi', 'Xem lại gấp đôi', 'Làm lại gấp đôi', 'Lương tăng 25%'],
                      key=lambda t: -abs(thay_doi[t]))
    print('Xếp hạng: ' + ' > '.join(f'{t} ({thay_doi[t]:+.1f}%)' for t in xep_hang))

    print('\n=== B3 · Giới hạn chạy lại: chi phí cả hệ thống (simulated) ===')
    print(f'{"giới hạn":>8s} {"tổng trợ lý":>12s} {"không TC":>8s} {"cả hệ thống":>12s} {"cps":>7s}')
    he_thong = {}
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']
        he_thong[k] = kq['tong'] + BASELINE * khong_tc
        print(f'{k:8d} {kq["tong"]:12,.0f} {khong_tc:8d} {he_thong[k]:12,.0f} {kq["cps"]:7,.0f}')
    print(f'Rẻ nhất cho công ty: giới hạn {min(he_thong, key=he_thong.get)} lần')

    print('\n=== B4 · Xem lại 100% (phạm vi noi_dia + hang_nang, simulated) ===')
    pv = reqs[reqs.loai.isin(['noi_dia', 'hang_nang'])]
    r_pv = runs[runs.request_id.isin(pv.request_id)]
    co_ok = r_pv.loc[r_pv.status == 'ok', 'request_id'].nunique()
    so_lam_lai = int((pv.ket_qua == 'lam_lai').sum())
    tc = int((pv.ket_qua == 'thanh_cong').sum())
    token_tool = (r_pv.tokens_in / 1000 * GIA_VAO + r_pv.tokens_out / 1000 * GIA_RA
                  + r_pv.tool_calls * GIA_TOOL).sum()
    phut_lam_lai_tb = reqs.loc[reqs.ket_qua == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print(f'{co_ok} yc có ≥1 lần chạy ok × 5 phút · {so_lam_lai} ca làm lại · token+tool {token_tool:,.0f} đ · '
          f'{tc} việc thành công')
    for phut_ll in [9, phut_lam_lai_tb]:
        tong = co_ok * 5 * LUONG_PHUT + so_lam_lai * phut_ll * LUONG_PHUT + token_tool
        cps = tong / tc
        hoa_von = (BASELINE * tc - token_tool - so_lam_lai * phut_ll * LUONG_PHUT) / (co_ok * LUONG_PHUT)
        print(f'  làm lại {phut_ll:4.1f} phút/ca: tổng {tong:,.0f} đ → cps {cps:,.0f} đ = {cps / BASELINE:.2f}× · '
              f'hoà vốn khi xem lại ≤ {hoa_von:.1f} phút/ca')


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
    n_tong = len(reqs)
    n_chinh = int(((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).sum())
    chinh = n_chinh / n_tong

    xem = reqs[reqs['duoc_xem_lai'] == 1]
    n_xem = len(xem)
    n_bo_qua = int(xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum())
    bo_qua = n_bo_qua / n_xem

    n_an_toan = int((reqs['mo_lai_trong_7_ngay'] == 1).sum())
    an_toan = n_an_toan / n_tong

    pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    n_pv = len(pham_vi)
    n_mo_lai_pv = int((pham_vi['mo_lai_trong_7_ngay'] == 1).sum())
    mo_lai_pv = n_mo_lai_pv / n_pv

    print(f'Chỉ số chính (đóng 24h & không mở lại 7 ngày): {chinh:.2%} ({n_chinh}/{n_tong})')
    print(f'Chỉ số dùng (bỏ qua gợi ý sua+bo / được xem lại): {bo_qua:.2%} ({n_bo_qua}/{n_xem})')
    print(f'Chỉ số an toàn (mở lại trong 7 ngày - toàn bộ): {an_toan:.2%} ({n_an_toan}/{n_tong})')
    print(f'Tỉ lệ mo_lai_trong_7_ngay (noi_dia + hang_nang): {mo_lai_pv:.2%} ({n_mo_lai_pv}/{n_pv})')


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
