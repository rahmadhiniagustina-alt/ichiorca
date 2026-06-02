import streamlit as st
import time

# ==========================================
# 1. MANAGEMENT HALAMAN & THEME CYBERPUNK
# ==========================================
st.set_page_config(
    page_title="EnvironForensic Pro v4.5",
    page_icon="🧪",
    layout="wide"
)

# CSS Kustom untuk Tampilan Premium Gelap ala OrganIQ
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=400;600;700&family=JetBrains+Mono:wght=400;700&display=swap');
    
    [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #0A0E17 !important;
        color: #E2E8F0 !important;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    [data-testid="stSidebar"] {
        background-color: #111827 !important;
        border-right: 2px solid #1F2937;
    }
    
    .app-brand {
        font-size: 32px;
        font-weight: 800;
        background: linear-gradient(135deg, #10B981 0%, #06B6D4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .lab-card {
        background-color: #161E2E;
        border: 1px solid #1F2937;
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 15px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    }
    
    .stTextInput input, .stNumberInput input {
        background-color: #1F2937 !important;
        color: #38BDF8 !important;
        border: 1px solid #374151 !important;
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #06B6D4 0%, #0891B2 100%);
        color: white !important;
        font-weight: 600;
        border-radius: 12px;
        padding: 12px;
        border: none;
        box-shadow: 0 4px 14px rgba(6, 182, 212, 0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #22D3EE 0%, #06B6D4 100%);
        box-shadow: 0 6px 20px rgba(6, 182, 212, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. INISIALISASI STATE UTAMA (DIPERBAIKI)
# ==========================================
if "hp" not in st.session_state:
    st.session_state.hp = 3
if "score" not in st.session_state:
    st.session_state.score = 100
if "collected_sample" not in st.session_state:
    st.session_state.collected_sample = ""
if "lab_step" not in st.session_state:
    st.session_state.lab_step = "INPUT_REAGEN"
if "do_calculated" not in st.session_state:
    st.session_state.do_calculated = 0.0

def apply_penalty(reason):
    st.session_state.hp -= 1
    st.session_state.score -= 20
    st.toast(f"❌ Kesalahan: {reason}! HP berkurang.", icon="🚨")

def reset_game():
    st.session_state.hp = 3
    st.session_state.score = 100
    st.session_state.collected_sample = ""
    st.session_state.lab_step = "INPUT_REAGEN"
    st.session_state.do_calculated = 0.0

# ==========================================
# 3. SIDEBAR MONITOR
# ==========================================
with st.sidebar:
    st.markdown("<div class='app-brand'>🕵️‍♂️ STATUS</div>", unsafe_allow_html=True)
    st.write("---")
    c_hp, c_sc = st.columns(2)
    c_hp.metric(label="❤️ Sisa HP", value=f"{st.session_state.hp} / 3")
    c_sc.metric(label="⭐ Skor Reputasi", value=st.session_state.score)
    
    st.write("---")
    st.markdown("### 📖 Buku Rumus Analisis Kimia")
    with st.expander("Rumus DO (Titrasi Winkler) 🧪"):
        st.write("Untuk mencari kadar DO Air, gunakan rumus penyederhanaan berikut:")
        st.code("DO (mg/L) = Volume Titran (mL) * 2", language="markdown")
        st.caption("Petunjuk: Catat rumus ini untuk menghitung hasil lab nanti!")

    st.write("---")
    if st.button("🔄 Reset Aplikasi"):
        reset_game()
        st.rerun()

# ==========================================
# 4. IMPLEMENTASI NAVIGATION TABS
# ==========================================
st.markdown("<div class='app-brand'>EnvironForensic Lab v4.5</div>", unsafe_allow_html=True)
st.write("---")

if st.session_state.hp <= 0:
    st.error("🚨 **GAME OVER!** Kesalahan analisis beruntun membuat lisensi laboratorium forensik Anda dicabut.")
    if st.button("Ulangi Misi"):
        reset_game()
        st.rerun()
else:
    # Menggunakan container tab agar data antar halaman sinkron tanpa reload kosong
    menu_tabs = st.tabs(["🔎 1. Posko Lapangan", "🧪 2. Pengujian Mandiri", "⚖️ 3. Ruang Sidang"])

    # ------------------------------------------
    # TAB 1: POSKO LAPANGAN
    # ------------------------------------------
    with menu_tabs[0]:
        st.markdown("### 🗺️ Peta Sektor Sungai Citarum")
        
        st.markdown("""
        <div class='lab-card'>
        <strong>PETUNJUK INTELIJEN:</strong><br>
        Kami mendeteksi pembuangan ilegal pipa bawah air berada di zona koordinat yang berbau zat kimia menyengat. 
        Zona tersebut diberi kode nama: <strong>BETA</strong>.
        </div>
        """, unsafe_allow_html=True)
        
        lokasi_input = st.text_input("Ketik KODE ZONA LOKASI yang ingin Anda datangi untuk sampling (Gunakan HURUF KAPITAL):", key="input_lokasi")
        
        if st.button("Ambil Tindakan Amankan Lokasi 🧺", key="btn_sampling"):
            if lokasi_input.strip() == "BETA":
                st.session_state.collected_sample = "Sampel Limbah Tekstil"
                st.success("🎯 Sukses! Anda berhasil mengamankan 'Sampel Limbah Tekstil' ke dalam tas lab Anda. Silakan klik **Tab 2** di atas.")
            elif lokasi_input.strip() == "":
                st.warning("Input tidak boleh kosong! Ketik kode zona terlebih dahulu.")
            else:
                apply_penalty("ZONING SALAH! Anda mendatangi zona aman pemukiman warga.")

    # ------------------------------------------
    # TAB 2: PENGUJIAN MANDIRI
    # ------------------------------------------
    with menu_tabs[1]:
        st.markdown("### 🔬 Ruang Praktikum Mandiri")
        
        if st.session_state.collected_sample == "":
            st.warning("🔒 **Akses Terkunci:** Anda belum membawa botol sampel dari lapangan. Ambil sampel dulu di Tab 1!")
        else:
            # TAHAP 1: INPUT REAGEN
            if st.session_state.lab_step == "INPUT_REAGEN":
                st.markdown("""
                <div class='lab-card'>
                <h5>Langkah Fiksasi Oksigen:</h5>
                Berdasarkan jurnal, untuk mengikat oksigen mula-mula masukkan larutan Mangan(II) Sulfat. 
                <br><strong>Tugas Anda:</strong> Ketikkan <strong>RUMUS MOLEKUL KIMIA</strong> dari senyawa Mangan(II) Sulfat tersebut!
                </div>
                """, unsafe_allow_html=True)
                
                rumus_kimia = st.text_input("Ketik Rumus Molekul Reagen (Contoh: H2O, NaCl):", key="input_reagen")
                
                if st.button("Suntikkan Reagen Kimia 🧪", key="btn_reagen"):
                    if rumus_kimia.strip().upper() == "MNSO4":
                        st.success("🎯 Benar! Larutan membentuk endapan cokelat. Langkah berikutnya terbuka!")
                        st.session_state.lab_step = "HITUNG_DO"
                        st.rerun()
                    elif rumus_kimia.strip() == "":
                        st.warning("Masukkan rumus kimia terlebih dahulu!")
                    else:
                        apply_penalty("RUMUS SALAH! Reagen mencederai sampel.")
            
            # TAHAP 2: HITUNG DO
            elif st.session_state.lab_step == "HITUNG_DO":
                st.markdown("""
                <div class='lab-card'>
                <h5>Proses Titrasi Winkler Selesai:</h5>
                Indikator amilum biru tepat menghilang pada penambahan volume buret Natrium Tiosulfat sebesar <strong>1.5 mL</strong>.
                <br><br>
                <strong>Tugas Anda:</strong> Hitung nilai DO (Dissolved Oxygen) air tersebut menggunakan rumus yang ada di <strong>Buku Saku Sidebar Kiri</strong>!
                </div>
                """, unsafe_allow_html=True)
                
                input_angka = st.number_input("Masukkan hasil perhitungan nilai DO Anda (mg/L):", step=0.1, key="input_do")
                
                if st.button("Verifikasi & Cetak Sertifikat Hasil Analisis 📊", key="btn_hitung"):
                    if input_angka == 3.0:
                        st.success("🎯 Perhitungan Akurat! Sertifikat lab diterbitkan. Silakan lanjut ke **Tab 3**.")
                        st.session_state.do_calculated = 3.0
                        st.session_state.lab_step = "LAB_SUCCESS"
                        st.rerun()
                    else:
                        apply_penalty("PERHITUNGAN SALAH! Angka analisis tidak akurat.")
            
            # TAHAP 3: BERHASIL
            elif st.session_state.lab_step == "LAB_SUCCESS":
                st.markdown("<div class='lab-card'><h4>📊 DATA UTUSAN LABORATORIUM (SAH)</h4>"
                            "• Hasil Uji Dissolved Oxygen (DO): <strong>3.0 mg/L</strong><br>"
                            "• Hasil Uji COD: <strong>580 mg/L</strong></div>", unsafe_allow_html=True)
                st.info("Dokumen siap. Silakan bawa berkas ini menuju **Tab 3 (Ruang Sidang)**.")

    # ------------------------------------------
    # TAB 3: RUANG SIDANG
    # ------------------------------------------
    with menu_tabs[2]:
        st.markdown("### ⚖️ Otoritas Sidang Pengadilan Tindak Pidana Lingkungan")
        
        if st.session_state.do_calculated == 0.0:
            st.warning("🔒 **Sidang Terkunci:** Anda belum memiliki berkas laboratorium resmi dari Tab 2.")
        else:
            st.write("Bandingkan hasil pengujian Anda (DO = 3.0 mg/L) dengan kriteria **PP No.22/2021 (Baku mutu minimal DO > 4.0 mg/L)**.")
            
            pilihan_sidang = st.selectbox(
                "Pilih keputusan dakwaan berdasarkan status hukum final:",
                ["-- Pilih Dakwaan --",
                 "Pabrik bebas karena nilai DO 3.0 mg/L membuktikan air sungai sangat sehat.",
                 "Pabrik divonis bersalah karena hasil uji DO sebesar 3.0 mg/L berada DI BAWAH ambang batas baku mutu minimal (4.0 mg/L)."],
                key="select_sidang"
            )
            
            if st.button("🔨 KETOK PALU KEPUTUSAN HAKIM", key="btn_hakim"):
                if "divonis bersalah" in pilihan_sidang:
                    st.balloons()
                    st.success("🎉 **KASUS BERHASIL DIPECAHKAN! (CASE CLOSED)**")
                    st.markdown("Selamat! Bukti rumusan kimia dan angka hitunganmu mutlak memenangkan pengadilan lingkungan!")
                else:
                    apply_penalty("Hakim membatalkan gugatan karena argumen Anda keliru.")
