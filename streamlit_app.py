import streamlit as st

# ==========================================
# 1. MANAGEMENT HALAMAN & THEME LIGHT MODE
# ==========================================
st.set_page_config(
    page_title="EnvironForensic Pro v5.0 (Mode Pemula)",
    page_icon="🧪",
    layout="wide"
)

# CSS Kustom Tema Terang yang Bersih dan Nyaman
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=400;600;700;800&family=JetBrains+Mono:wght=400;700&display=swap');
    
    [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #F8FAFC !important;
        color: #1E293B !important;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    [data-testid="stSidebar"] {
        background-color: #F1F5F9 !important;
        border-right: 2px solid #E2E8F0;
    }
    .app-brand {
        font-size: 32px;
        font-weight: 800;
        background: linear-gradient(135deg, #059669 0%, #0891B2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .lab-card {
        background-color: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        color: #334155;
    }
    .hint-box {
        background-color: #EFF6FF;
        border-left: 5px solid #3B82F6;
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 15px;
        font-size: 14px;
        color: #1E40AF;
    }
    .case-selection-card {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFC 100%);
        border: 2px solid #CBD5E1;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        margin-bottom: 20px;
        min-height: 160px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        color: #1E293B;
    }
    .stTextInput input, .stNumberInput input {
        background-color: #FFFFFF !important;
        color: #0F172A !important;
        border: 1px solid #CBD5E1 !important;
        font-family: 'JetBrains Mono', monospace !important;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #059669 0%, #0D9488 100%);
        color: white !important;
        font-weight: 600;
        border-radius: 12px;
        padding: 12px;
        border: none;
        box-shadow: 0 4px 6px rgba(5, 150, 105, 0.2);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #047857 0%, #0F766E 100%);
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. INISIALISASI STATE UTAMA GAME
# ==========================================
if "current_view" not in st.session_state: st.session_state.current_view = "MAIN_MENU"
if "hp" not in st.session_state: st.session_state.hp = 3
if "score" not in st.session_state: st.session_state.score = 100
if "show_edu_material" not in st.session_state: st.session_state.show_edu_material = False

# Reset State untuk masing-masing kasus
for prefix in ["c1", "c2", "c3", "c4", "c5"]:
    if f"{prefix}_sample" not in st.session_state: st.session_state[f"{prefix}_sample"] = ""
if "lab_step" not in st.session_state: st.session_state.lab_step = "INPUT_REAGEN"
if "c2_lab_step" not in st.session_state: st.session_state.c2_lab_step = "SET_LAMP_AAS"
if "c3_lab_step" not in st.session_state: st.session_state.c3_lab_step = "SET_CARRIER_GAS"
if "c4_lab_step" not in st.session_state: st.session_state.c4_lab_step = "SET_WAVELENGTH_UV"
if "c5_lab_step" not in st.session_state: st.session_state.c5_lab_step = "SET_WAVELENGTH_PO4"

if "do_calculated" not in st.session_state: st.session_state.do_calculated = 0.0
if "c2_hg_calculated" not in st.session_state: st.session_state.c2_hg_calculated = 0.0
if "c3_area_calculated" not in st.session_state: st.session_state.c3_area_calculated = 0.0
if "c4_cn_calculated" not in st.session_state: st.session_state.c4_cn_calculated = 0.0
if "c5_po4_calculated" not in st.session_state: st.session_state.c5_po4_calculated = 0.0

def apply_penalty(reason):
    st.session_state.hp -= 1
    st.session_state.score -= 20
    st.toast(f"❌ Keliru: {reason}! Nyawa berkurang.", icon="🚨")

def back_to_menu():
    st.session_state.current_view = "MAIN_MENU"
    st.session_state.hp = 3
    st.session_state.score = 100
    st.session_state.show_edu_material = False
    st.session_state.c1_sample = ""
    st.session_state.lab_step = "INPUT_REAGEN"
    st.session_state.do_calculated = 0.0
    st.session_state.c2_sample = ""
    st.session_state.c2_lab_step = "SET_LAMP_AAS"
    st.session_state.c2_hg_calculated = 0.0
    st.session_state.c3_sample = ""
    st.session_state.c3_lab_step = "SET_CARRIER_GAS"
    st.session_state.c3_area_calculated = 0.0
    st.session_state.c4_sample = ""
    st.session_state.c4_lab_step = "SET_WAVELENGTH_UV"
    st.session_state.c4_cn_calculated = 0.0
    st.session_state.c5_sample = ""
    st.session_state.c5_lab_step = "SET_WAVELENGTH_PO4"
    st.session_state.c5_po4_calculated = 0.0

# ==========================================
# 3. SIDEBAR DETEKTIF HUD
# ==========================================
with st.sidebar:
    st.markdown("<div class='app-brand'>🕵️‍♂️ ASISTEN LAB</div>", unsafe_allow_html=True)
    st.info("💡 **Mode Pemula Aktif:** Panduan instrumen kimia disediakan langsung di setiap kotak instruksi!")
    st.write("---")
    c_hp, c_sc = st.columns(2)
    c_hp.metric(label="❤️ Sisa Nyawa", value=f"{st.session_state.hp} / 3")
    c_sc.metric(label="⭐ Skor Analisis", value=st.session_state.score)
    st.write("---")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3", format="audio/mp3", loop=True)
    if st.session_state.current_view != "MAIN_MENU":
        if st.button("🚪 Kembali ke Menu Utama"):
            back_to_menu()
            st.rerun()

# ==========================================
# 4. LOGIKA UTAMA JALUR HALAMAN
# ==========================================
st.markdown("<div class='app-brand'>🎓 Laboratorium Forensik Lingkungan Interaktif</div>", unsafe_allow_html=True)
st.write("---")

if st.session_state.hp <= 0:
    st.error("🚨 **KESEHATAN HABIS!** Tenang, mari kita ulangi dan belajar lagi bersama-sama.")
    if st.button("Mulai Ulang Game"):
        back_to_menu()
        st.rerun()

# --- BERANDA UTAMA (SEMUA BISA DIMAINKAN) ---
elif st.session_state.current_view == "MAIN_MENU":
    st.markdown("### 📁 Selamat datang! Pilih kasus kriminal lingkungan yang ingin Anda selidiki:")
    
    col_k1, col_k2, col_k3 = st.columns(3)
    with col_k1:
        st.markdown("<div class='case-selection-card'><h3>🌊 Kasus 1</h3><p>Polusi Organik Sungai Citarum</p><p style='color: #059669; font-weight: bold;'>🔓 Siap Dimainkan</p></div>", unsafe_allow_html=True)
        if st.button("Masuk Kasus 1", key="open_c1"):
            st.session_state.current_view = "KASUS_1"
            st.rerun()
    with col_k2:
        st.markdown("<div class='case-selection-card'><h3>🌋 Kasus 2</h3><p>Tragedi Merkuri Teluk Buyat</p><p style='color: #059669; font-weight: bold;'>🔓 Siap Dimainkan</p></div>", unsafe_allow_html=True)
        if st.button("Masuk Kasus 2", key="open_c2"):
            st.session_state.current_view = "KASUS_2"
            st.rerun()
    with col_k3:
        st.markdown("<div class='case-selection-card'><h3>🛢️ Kasus 3</h3><p>Tumpahan Minyak Montara Laut Laut</p><p style='color: #059669; font-weight: bold;'>🔓 Siap Dimainkan</p></div>", unsafe_allow_html=True)
        if st.button("Masuk Kasus 3", key="open_c3"):
            st.session_state.current_view = "KASUS_3"
            st.rerun()

    col_k4, col_k5, _ = st.columns(3)
    with col_k4:
        st.markdown("<div class='case-selection-card'><h3>🧪 Kasus 4</h3><p>Kebocoran Sianida Tambang Emas</p><p style='color: #059669; font-weight: bold;'>🔓 Siap Dimainkan</p></div>", unsafe_allow_html=True)
        if st.button("Masuk Kasus 4", key="open_c4"):
            st.session_state.current_view = "KASUS_4"
            st.rerun()
    with col_k5:
        st.markdown("<div class='case-selection-card'><h3>🌾 Kasus 5</h3><p>Ledakan Alga Danau Toba</p><p style='color: #059669; font-weight: bold;'>🔓 Siap Dimainkan</p></div>", unsafe_allow_html=True)
        if st.button("Masuk Kasus 5", key="open_c5"):
            st.session_state.current_view = "KASUS_5"
            st.rerun()

# --- KASUS 1: CITARUM ---
elif st.session_state.current_view == "KASUS_1":
    tabs = st.tabs(["🔎 1. Ambil Sampel", "🧪 2. Uji Kimia Lab", "⚖️ 3. Putusan Sidang"])
    with tabs[0]:
        st.markdown("### 🗺️ Lokasi Pembuangan Limbah Tekstil")
        st.markdown("<div class='lab-card'>Ada pabrik nakal membuang limbah cair rahasia tanpa diolah. Intelijen memberi tahu lokasinya ada di zona <strong>BETA</strong>.</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='hint-box'>💡 <strong>Petunjuk Mudah:</strong> Ketik kata <strong>BETA</strong> di kolom bawah untuk mengambil sampelnya.</div>", unsafe_allow_html=True)
        lokasi = st.text_input("Masukkan Kode Lokasi:", key="c1_loc")
        if st.button("Ambil Sampel Air 🧺", key="btn_c1_sam"):
            if lokasi.strip().upper() == "BETA":
                st.session_state.c1_sample = "Limbah Citarum"
                st.success("🎯 Sukses! Botol sampel berhasil diambil. Sekarang, silakan klik **Tab 2 (Uji Kimia Lab)** di bagian atas!")
            else: apply_penalty("Kata sandi lokasi salah, coba ketik BETA.")
            
    with tabs[1]:
        st.markdown("### 🔬 Menghitung Kadar Oksigen Air (Titrasi Winkler)")
        if st.session_state.c1_sample == "": st.warning("Ambil botol sampelmu di Tab 1 dulu ya!")
        else:
            if st.session_state.lab_step == "INPUT_REAGEN":
                st.markdown("<div class='lab-card'><strong>Penjelasan:</strong> Kita perlu memasukkan zat kimia pengikat oksigen bernama Mangan(II) Sulfat agar air berubah warna menjadi cokelat.</div>", unsafe_allow_html=True)
                st.markdown("<div class='hint-box'>💡 <strong>Petunjuk Mudah:</strong> Rumus kimia molekulnya adalah <strong>MnSO4</strong> (Perhatikan huruf besar kecilnya). Ketik di bawah!</div>", unsafe_allow_html=True)
                reagen = st.text_input("Ketik rumus molekul reagen:", key="c1_reag")
                if st.button("Suntikkan Reagen Ke Botol 🧪"):
                    if reagen.strip() == "MnSO4":
                        st.success("🎯 Bagus! Cairannya berubah warna. Langkah hitungan otomatis terbuka!")
                        st.session_state.lab_step = "HITUNG_DO"
                        st.rerun()
                    else: apply_penalty("Rumus kimia kurang tepat, pastikan mengetik MnSO4.")
            elif st.session_state.lab_step == "HITUNG_DO":
                st.markdown("<div class='lab-card'><strong>Cara Menghitung:</strong> Di lab, volume cairan buret yang terpakai adalah 1.5 mL. Rumus mencari kadar oksigen (DO) adalah: <code>Volume Terpakai x 2</code></div>", unsafe_allow_html=True)
                st.markdown("<div class='hint-box'>💡 <strong>Petunjuk Mudah:</strong> Hitung 1.5 dikali 2, hasilnya adalah <strong>3.0</strong>. Masukkan angka 3.0 di bawah!</div>", unsafe_allow_html=True)
                angka = st.number_input("Hasil kadar DO (mg/L):", step=0.1, key="c1_num")
                if st.button("Kunci Angka Laboratorium"):
                    if angka == 3.0:
                        st.success("🎯 Hebat! Perhitunganmu 100% akurat. Lanjut ke **Tab 3 (Putusan Sidang)**!")
                        st.session_state.do_calculated = 3.0
                        st.session_state.lab_step = "LAB_SUCCESS"
                        st.rerun()
                    else: apply_penalty("Hitunganmu keliru, coba isi dengan angka 3.0.")
            elif st.session_state.lab_step == "LAB_SUCCESS":
                st.markdown("<div class='lab-card'><h4>📊 SERTIFIKAT LAB SUDAH TERBIT</h4>• Kadar Oksigen Air Anda: <strong>3.0 mg/L</strong><br>• Ambang batas aman minimal pemerintah: <strong>4.0 mg/L</strong><br><br><em>Artinya, oksigen di sungai ini terlalu tipis sehingga ikan-ikan mati lemas!</em></div>", unsafe_allow_html=True)
                
    with tabs[2]:
        st.markdown("### ⚖️ Ruang Sidang Meja Hijau")
        if st.session_state.do_calculated == 0.0: st.warning("Selesaikan analisis uji lab di Tab 2 dulu!")
        else:
            st.markdown("<div class='lab-card'>Berdasarkan bukti ilmiah buatanmu di lab, kadar oksigen sungai (3.0 mg/L) terbukti merusak lingkungan. Apa tuntutanmu sebagai detektif?</div>", unsafe_allow_html=True)
            pilihan = st.selectbox("Pilih Kesimpulan Dakwaan:", ["-- Pilih Kalimat --", "Bebaskan Pabrik", "Pabrik divonis bersalah karena kadar oksigen 3.0 mg/L melanggar aturan baku mutu."], key="c1_sd")
            if st.button("🔨 KETOK PALU KEPUTUSAN HAKIM"):
                if "divonis bersalah" in pilihan:
                    st.balloons()
                    st.session_state.show_edu_material = True
                    st.success("🎉 KASUS 1 SELESAI DENGAN INDAH! Kamu berhasil menyelamatkan Sungai Citarum!")
                else: apply_penalty("Tuntutanmu keliru, pabrik merusak alam harus dihukum!")

# --- KASUS 2: TELUK BUYAT (AAS) ---
elif st.session_state.current_view == "KASUS_2":
    tabs = st.tabs(["🔎 1. Ambil Sampel Pantai", "🔬 2. Alat AAS (Merkuri)", "⚖️ 3. Putusan Sidang"])
    with tabs[0]:
        st.markdown("### 🏖️ Investigasi Logam Berat")
        st.markdown("<div class='lab-card'>Limbah raksa dari penambangan mencemari muara laut. Warga melapor titik pembuangannya ada di wilayah <strong>SELATAN</strong>.</div>", unsafe_allow_html=True)
        st.markdown("<div class='hint-box'>💡 <strong>Petunjuk Mudah:</strong> Ketik kata <strong>SELATAN</strong> untuk menyendok pasir/sedimen laut.</div>", unsafe_allow_html=True)
        lokasi = st.text_input("Ketik Lokasi:", key="c2_loc")
        if st.button("Amankan Sedimen Pantai 🧺"):
            if lokasi.strip().upper() == "SELATAN":
                st.session_state.c2_sample = "Sedimen Buyat"
                st.success("🎯 Berhasil mengambil sampel sedimen! Mari lanjut ke **Tab 2**.")
            else: apply_penalty("Lokasi salah, ketik SELATAN.")
    with tabs[1]:
        st.markdown("### 🔬 Mengenal Alat AAS (Spektroskopi Serapan Atom)")
        if st.session_state.c2_sample == "": st.warning("Ambil sampel di Tab 1 dulu!")
        else:
            if st.session_state.c2_lab_step == "SET_LAMP_AAS":
                st.markdown("<div class='lab-card'><strong>Cara Kerja Alat:</strong> Alat AAS mendeteksi raksa (Merkuri) menggunakan tembakan lampu laser khusus. Agar laser mendeteksi raksa dengan pas, alat harus diatur ke angka panjang gelombang atomnya.</div>", unsafe_allow_html=True)
                st.markdown("<div class='hint-box'>💡 <strong>Petunjuk Mudah:</strong> Panjang gelombang standar untuk Merkuri (Hg) adalah <strong>253.7</strong> nm. Masukkan angka itu di bawah!</div>", unsafe_allow_html=True)
                wave = st.number_input("Atur Panjang Gelombang (nm):", step=0.1, key="c2_w")
                if st.button("Tembakkan Laser Kalibrasi 💥"):
                    if wave == 253.7:
                        st.success("🎯 Luar biasa! Alat AAS berhasil menangkap sinyal raksa. Menu hitungan terbuka!")
                        st.session_state.c2_lab_step = "HITUNG_AAS"
                        st.rerun()
                    else: apply_penalty("Sinyal buram! Masukkan angka panjang gelombang raksa yang benar: 253.7")
            elif st.session_state.c2_lab_step == "HITUNG_AAS":
                st.markdown("<div class='lab-card'><strong>Membaca Hasil Alat:</strong> Detektor AAS memunculkan nilai serapan warna (Absorbansi) sebesar 0.25. Rumus mencari kadarnya: <code>Nilai Absorbansi / 0.1</code></div>", unsafe_allow_html=True)
                st.markdown("<div class='hint-box'>💡 <strong>Petunjuk Mudah:</strong> 0.25 dibagi 0.1 hasilnya adalah <strong>2.5</strong>. Ketik angka 2.5 di bawah!</div>", unsafe_allow_html=True)
                hg = st.number_input("Kadar Merkuri (ppm):", step=0.1, key="c2_hg")
                if st.button("Kunci Sertifikat Logam"):
                    if hg == 2.5:
                        st.success("🎯 Sempurna! Data valid. Berkas hukum siap dibawa ke **Tab 3**.")
                        st.session_state.c2_hg_calculated = 2.5
                        st.session_state.c2_lab_step = "AAS_SUCCESS"
                        st.rerun()
                    else: apply_penalty("Hitungan salah, jawabannya adalah 2.5")
            elif st.session_state.c2_lab_step == "AAS_SUCCESS":
                st.markdown("<div class='lab-card'><h4>📊 HASIL UJI SPEKTROSKOPI AAS</h4>• Kadar Merkuri: <strong>2.5 ppm</strong><br>• Batas Maksimal Aman Internasional: <strong>0.15 ppm</strong><br><br><span style='color:red;'><strong>Kesimpulan:</strong> Pasir pantai mengandung raksa 15 kali lipat di atas batas normal! Berbahaya bagi nelayan!</span></div>", unsafe_allow_html=True)
    with tabs[2]:
        st.markdown("### ⚖️ Putusan Mahkamah")
        if st.session_state.c2_hg_calculated == 0.0: st.warning("Selesaikan uji lab di Tab 2 dulu!")
        else:
            pilihan = st.selectbox("Tuntutan Hukum:", ["-- Pilih --", "Bebaskan Perusahaan", "Perusahaan wajib membayar ganti rugi karena merkuri 2.5 ppm meracuni ikan dan nelayan."], key="c2_sd")
            if st.button("🔨 KETOK PALU SIDANG"):
                if "wajib membayar ganti rugi" in pilihan:
                    st.balloons()
                    st.success("🎉 KASUS 2 CLOSED! Keadilan bagi masyarakat Teluk Buyat berhasil ditegakkan!")
                else: apply_penalty("Pilih dakwaan yang membela lingkungan warga.")

# --- KASUS 3: MONTARA (GC-FID) ---
elif st.session_state.current_view == "KASUS_3":
    tabs = st.tabs(["🔎 1. Ambil Sampel Laut", "⛽ 2. Alat GC (Minyak)", "⚖️ 3. Putusan Sidang"])
    with tabs[0]:
        st.markdown("### 🛢️ Investigasi Tumpahan Minyak Lepas Pantai")
        st.markdown("<div class='lab-card'>Minyak mentah bocor di tengah laut. Satelit mendeteksi area pencemaran paling tebal ada di blok <strong>TIMUR</strong>.</div>", unsafe_allow_html=True)
        st.markdown("<div class='hint-box'>💡 <strong>Petunjuk Mudah:</strong> Ketik kata <strong>TIMUR</strong> di kolom input untuk mengambil sampel air laut berminyak.</div>", unsafe_allow_html=True)
        lokasi = st.text_input("Ketik Blok Koordinat:", key="c3_loc")
        if st.button("Ambil Sampel Minyak 🌊"):
            if lokasi.strip().upper() == "TIMUR":
                st.session_state.c3_sample = "Minyak Bumi"
                st.success("🎯 Berhasil mengisolasi sampel minyak mentah! Silakan buka **Tab 2**.")
            else: apply_penalty("Salah koordinat, ketik TIMUR.")
    with tabs[1]:
        st.markdown("### 🔬 Mengenal Kromatografi Gas (GC)")
        if st.session_state.c3_sample == "": st.warning("Ambil sampel di Tab 1 dulu!")
        else:
            if st.session_state.c3_lab_step == "SET_CARRIER_GAS":
                st.markdown("<div class='lab-card'><strong>Cara Kerja Alat:</strong> Alat Kromatografi Gas (GC) memisahkan komponen minyak bumi dengan cara mendorong sampel menggunakan hembusan 'Gas Pembawa' yang tidak bereaksi (inert).</div>", unsafe_allow_html=True)
                st.markdown("<div class='hint-box'>💡 <strong>Petunjuk Mudah:</strong> Gas mulia pembawa yang paling sering dipakai di laboratorium bernama gas <strong>Helium</strong>. Ketik Helium di bawah!</div>", unsafe_allow_html=True)
                gas = st.text_input("Nama Gas Pembawa:", key="c3_gas")
                if st.button("Injeksi & Alirkan Gas"):
                    if gas.strip().upper() in ["HELIUM", "HE"]:
                        st.success("🎯 Gas menyembur stabil! Mesin GC berhasil memisahkan komponen hidrokarbon.")
                        st.session_state.c3_lab_step = "HITUNG_GC"
                        st.rerun()
                    else: apply_penalty("Alat tersumbat! Ketik kata Helium.")
            elif st.session_state.c3_lab_step == "HITUNG_GC":
                st.markdown("<div class='lab-card'><strong>Membaca Grafik Alat:</strong> Mesin GC memunculkan grafik puncak dengan luas area 10.000 unit. Rumus persentase kandungan minyak di air adalah: <code>Luas Area / 5000</code></div>", unsafe_allow_html=True)
                st.markdown("<div class='hint-box'>💡 <strong>Petunjuk Mudah:</strong> 10.000 dibagi 5.000 hasilnya adalah <strong>2.0</strong>. Masukkan angka 2.0 di bawah!</div>", unsafe_allow_html=True)
                persen = st.number_input("Total Hidrokarbon Minyak (%):", step=0.1, key="c3_pct")
                if st.button("Sahkan Grafik Kromatogram"):
                    if persen == 2.0:
                        st.success("🎯 Tepat sekali! Kadar tumpahan terdata resmi. Lanjut ke **Tab 3**!")
                        st.session_state.c3_area_calculated = 2.0
                        st.session_state.c3_lab_step = "GC_SUCCESS"
                        st.rerun()
                    else: apply_penalty("Jawaban salah, ketik angka 2.0.")
            elif st.session_state.c3_lab_step == "GC_SUCCESS":
                st.markdown("<div class='lab-card'><h4>📊 SERTIFIKAT FORENSIK GC-FID</h4>• Kadar TPH Minyak Bumi: <strong>2.0%</strong><br>• Status: <span style='color:red;'>Sangat Beracun (Mampu merusak terumbu karang dan mematikan rumput laut)</span></div>", unsafe_allow_html=True)
    with tabs[2]:
        st.markdown("### ⚖️ Putusan Sidang Hukum Maritim")
        if st.session_state.c3_area_calculated == 0.0: st.warning("Selesaikan uji GC di Tab 2 dulu!")
        else:
            pilihan = st.selectbox("Keputusan Sidang:", ["-- Pilih --", "Gugatan Gugur", "Operator kilang lepas pantai dinyatakan bersalah dan wajib mendanai pembersihan laut."], key="c3_sd")
            if st.button("🔨 KETOK PALU MARITIM"):
                if "dinyatakan bersalah" in pilihan:
                    st.balloons()
                    st.success("🎉 KASUS 3 CLOSED! Laut Indonesia berhasil dilindungi dari pencemaran korporasi!")
                else: apply_penalty("Pilih keputusan hukum yang adil untuk kelestarian laut.")

# --- KASUS 4: SIANIDA TAMBANG (UV-VIS) ---
elif st.session_state.current_view == "KASUS_4":
    tabs = st.tabs(["🔎 1. Ambil Sampel Sungai", "🧪 2. Alat Spektrofotometer", "⚖️ 3. Putusan Sidang"])
    with tabs[0]:
        st.markdown("### 🧪 Kebocoran Racun Sianida Tambang Emas")
        st.markdown("<div class='lab-card'>Limbah cair pengolahan emas bocor ke sungai desa. Laporan warga menyatakan titik pencemaran berasal dari aliran sungai sektor <strong>UTARA</strong>.</div>", unsafe_allow_html=True)
        st.markdown("<div class='hint-box'>💡 <strong>Petunjuk Mudah:</strong> Ketik kata <strong>UTARA</strong> untuk mengambil sampel air sungai beracun tersebut.</div>", unsafe_allow_html=True)
        lokasi = st.text_input("Ketik Sektor Sungai:", key="c4_loc")
        if st.button("Ambil Sampel Air Racun 🧺"):
            if lokasi.strip().upper() == "UTARA":
                st.session_state.c4_sample = "Sianida Cair"
                st.success("🎯 Botol sampel racun sianida berhasil diamankan! Lanjut ke **Tab 2**.")
            else: apply_penalty("Salah rute, ketik UTARA.")
    with tabs[1]:
        st.markdown("### 🔬 Mengenal Spektrofotometer UV-Vis")
        if st.session_state.c4_sample == "": st.warning("Ambil sampel di Tab 1 dulu!")
        else:
            if st.session_state.c4_lab_step == "SET_WAVELENGTH_UV":
                st.markdown("<div class='lab-card'><strong>Cara Kerja Alat:</strong> Alat ini menembakkan cahaya dengan warna khusus untuk mendeteksi kepekatan warna cairan kimia. Larutan uji sianida yang sudah diberi zat pembentuk warna biru dibaca pada panjang gelombang khusus agar hasilnya akurat.</div>", unsafe_allow_html=True)
                st.markdown("<div class='hint-box'>💡 <strong>Petunjuk Mudah:</strong> Sesuai standar baku mutu lab, ketik angka panjang gelombang optimalnya yaitu <strong>578</strong> nm di bawah!</div>", unsafe_allow_html=True)
                wave = st.number_input("Atur Panjang Gelombang Alat (nm):", step=1, key="c4_w")
                if st.button("Set Warna Cahaya Monokromator"):
                    if wave == 578:
                        st.success("🎯 Akurat! Alat Spektro berhasil mendeteksi warna kompleks sianida.")
                        st.session_state.c4_lab_step = "HITUNG_UV"
                        st.rerun()
                    else: apply_penalty("Warna cahaya tidak pas, masukkan angka panjang gelombang: 578")
            elif st.session_state.c4_lab_step == "HITUNG_COLO":
                pass # Digantikan alur state yang sinkron
            elif st.session_state.c4_lab_step == "HITUNG_UV":
                st.markdown("<div class='lab-card'><strong>Membaca Layar Alat:</strong> Nilai serapan cahaya (Absorbansi) yang muncul adalah 0.30. Rumus mencari kadar racunnya adalah: <code>Nilai Absorbansi x 2</code></div>", unsafe_allow_html=True)
                st.markdown("<div class='hint-box'>💡 <strong>Petunjuk Mudah:</strong> 0.30 dikali 2 hasilnya adalah <strong>0.6</strong>. Masukkan angka 0.6 di bawah!</div>", unsafe_allow_html=True)
                cn = st.number_input("Kadar Racun Sianida (mg/L):", step=0.01, key="c4_cn")
                if st.button("Validasi Hasil Detektor"):
                    if cn == 0.6:
                        st.success("🎯 Sempurna! Data forensik sah diterbitkan. Silakan ke **Tab 3**!")
                        st.session_state.c4_cn_calculated = 0.6
                        st.session_state.c4_lab_step = "UV_SUCCESS"
                        st.rerun()
                    else: apply_penalty("Hitungan kurang tepat, masukkan angka 0.6.")
            elif st.session_state.c4_lab_step == "UV_SUCCESS":
                st.markdown("<div class='lab-card'><h4>📊 LAPORAN SAH SPEKTROFOTOMETRI UV-VIS</h4>• Sianida Bebas (CN⁻): <strong>0.6 mg/L</strong><br>• Batas Maksimal Aman dari Pemerintah: <strong>0.05 mg/L</strong><br><br><span style='color:red;'><strong>Bahaya:</strong> Kadar sianida sungai 12 kali lipat melewati batas maut! Sangat beracun bagi hewan ternak warga!</span></div>", unsafe_allow_html=True)
    with tabs[2]:
        st.markdown("### ⚖️ Sidang Pidana Korporasi")
        if st.session_state.c4_cn_calculated == 0.0: st.warning("Selesaikan uji lab di Tab 2 dulu!")
        else:
            pilihan = st.selectbox("Dakwaan Jaksa:", ["-- Pilih --", "Bebaskan Direktur", "Manajemen perusahaan dijatuhi hukuman pidana akibat kelalaian kebocoran pipa sianida tambang."], key="c4_sd")
            if st.button("🔨 EKSEKUSI TUNTUTAN PIDANA"):
                if "dijatuhi hukuman pidana" in pilihan:
                    st.balloons()
                    st.success("🎉 KASUS 4 CLOSED! Kelompok tambang liar berhasil ditindak secara hukum!")
                else: apply_penalty("Pilih dakwaan hukuman pidana bagi perusak sungai warga.")

# --- KASUS 5: EUTROFIKASI TOBA (MOLIBDAT BIRU) ---
elif st.session_state.current_view == "KASUS_5":
    tabs = st.tabs(["🔎 1. Ambil Sampel Air", "🧪 2. Alat Spektrofotometer (Fosfat)", "⚖️ 3. Sanksi Administrasi"])
    with tabs[0]:
        st.markdown("### 🌾 Kasus Ledakan Alga Hijau pekat ( Blooming Algae )")
        st.markdown("<div class='lab-card'>Sisa pakan ikan dari keramba raksasa komersial memicu penumpukan fosfat. Kematian ikan massal paling parah terjadi di sektor keramba wilayah <strong>BARAT</strong>.</div>", unsafe_allow_html=True)
        st.markdown("<div class='hint-box'>💡 <strong>Petunjuk Mudah:</strong> Ketik kata <strong>BARAT</strong> untuk mengambil sampel air danau yang berwarna hijau keruh.</div>", unsafe_allow_html=True)
        lokasi = st.text_input("Ketik Wilayah Danau:", key="c5_loc")
        if st.button("Ambil Sampel Air Danau 🧺"):
            if lokasi.strip().upper() == "BARAT":
                st.session_state.c5_sample = "Fosfat Air"
                st.success("🎯 Sampel air kaya nutrisi fosfat berhasil dikumpulkan! Ayo buka **Tab 2**.")
            else: apply_penalty("Salah area sampling, ketik BARAT.")
    with tabs[1]:
        st.markdown("### 🔬 Analisis Kadar Nutrien Pupuk Fosfat")
        if st.session_state.c5_sample == "": st.warning("Ambil sampel di Tab 1 dulu!")
        else:
            if st.session_state.c5_lab_step == "SET_WAVELENGTH_PO4":
                st.markdown("<div class='lab-card'><strong>Cara Kerja Metode:</strong> Air danau dicampur reagen amonium molibdat hingga berubah menjadi warna biru kompleks yang indah. Warna biru tua ini dibaca menggunakan sinar inframerah dekat agar kadarnya ketahuan.</div>", unsafe_allow_html=True)
                st.markdown("<div class='hint-box'>💡 <strong>Petunjuk Mudah:</strong> Panjang gelombang standar emas untuk mengukur kompleks molibdat biru ini adalah <strong>880</strong> nm. Ketik angka 880 di bawah!</div>", unsafe_allow_html=True)
                wave = st.number_input("Atur Panjang Gelombang Inframerah (nm):", step=1, key="c5_w")
                if st.button("Nyalakan Sinar Monokromator 🔎"):
                    if wave == 880:
                        st.success("🎯 Sinar terkalibrasi pas! Detektor siap membaca kepekatan biru cairan.")
                        st.session_state.c5_lab_step = "HITUNG_PO4"
                        st.rerun()
                    else: apply_penalty("Salah gelombang cahaya, ketik angka: 880")
            elif st.session_state.c5_lab_step == "HITUNG_PO4":
                st.markdown("<div class='lab-card'><strong>Membaca Nilai Layar:</strong> Hasil ukur nilai Absorbansi larutan adalah 0.15. Rumus konversi kadar fosfatnya: <code>Nilai Absorbansi / 0.5</code></div>", unsafe_allow_html=True)
                st.markdown("<div class='hint-box'>💡 <strong>Petunjuk Mudah:</strong> 0.15 dibagi 0.5 hasilnya adalah <strong>0.3</strong>. Masukkan angka 0.3 di kolom bawah!</div>", unsafe_allow_html=True)
                po4 = st.number_input("Kadar Fosfat Danau (ppm):", step=0.01, key="c5_po4")
                if st.button("Sertifikasi Kadar Nutrien"):
                    if po4 == 0.3:
                        st.success("🎯 Luar biasa tepat! Hasil laboratorium terkunci dengan sah. Silakan menuju **Tab 3**!")
                        st.session_state.c5_po4_calculated = 0.3
                        st.session_state.c5_lab_step = "PO4_SUCCESS"
                        st.rerun()
                    else: apply_penalty("Hitungan salah, jawabannya adalah 0.3")
            elif st.session_state.c5_lab_step == "PO4_SUCCESS":
                st.markdown("<div class='lab-card'><h4>📊 HASIL SAH SPEKTROFOTOMETRI DANAU</h4>• Kadar Ortofosfat (PO₄³⁻): <strong>0.3 ppm</strong><br>• Ambang Batas Aman Alami Danau Toba: <strong>0.02 ppm</strong><br><br><em>Artinya kadar pupuk fosfat penumbuh alga sudah 15 kali melampaui batas wajar, menyebabkan air danau kekurangan oksigen akibat pembusukan tumbuhan air!</em></div>", unsafe_allow_html=True)
    with tabs[2]:
        st.markdown("### ⚖️ Ruang Sanksi Dinas Lingkungan Hidup")
        if st.session_state.c5_po4_calculated == 0.0: st.warning("Selesaikan uji lab di Tab 2 dulu!")
        else:
            pilihan = st.selectbox("Tindakan Tegas Pemerintah:", ["-- Pilih --", "Biarkan Saja Operasionalnya", "Pemerintah mencabut izin usaha keramba raksasa komersial karena terbukti memicu pencemaran fosfat 0.3 ppm."], key="c5_sd")
            if st.button("🔨 KETOK PALU SANKSI ADMINISTRASI"):
                if "mencabut izin" in pilihan:
                    st.balloons()
                    st.success("🎉 KASUS 5 CLOSED! SELAMAT! Kamu telah menuntaskan seluruh kasus dan sah menjadi Detektif Lingkungan Juara!")
                else: apply_penalty("Pilih tindakan tegas pencabutan izin demi menyelamatkan ekosistem pariwisata Danau Toba!")
