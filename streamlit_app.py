import streamlit as st

# ==========================================
# 1. MANAGEMENT HALAMAN & THEME CYBERPUNK
# ==========================================
st.set_page_config(
    page_title="EnvironForensic Pro v5.0",
    page_icon="🧪",
    layout="wide"
)

# CSS Kustom - Estetika visual lab forensik secara utuh
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=400;600;700;800&family=JetBrains+Mono:wght=400;700&display=swap');
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
    }
    .case-selection-card {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border: 2px solid #334155;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        margin-bottom: 20px;
        min-height: 180px;
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
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. INISIALISASI STATE UTAMA GAME
# ==========================================
if "current_view" not in st.session_state: st.session_state.current_view = "MAIN_MENU"
if "hp" not in st.session_state: st.session_state.hp = 3
if "score" not in st.session_state: st.session_state.score = 100
if "case1_cleared" not in st.session_state: st.session_state.case1_cleared = False
if "case2_cleared" not in st.session_state: st.session_state.case2_cleared = False
if "show_edu_material" not in st.session_state: st.session_state.show_edu_material = False

# State spesifik Kasus 1
if "collected_sample" not in st.session_state: st.session_state.collected_sample = ""
if "lab_step" not in st.session_state: st.session_state.lab_step = "INPUT_REAGEN"
if "do_calculated" not in st.session_state: st.session_state.do_calculated = 0.0

# State spesifik Kasus 2
if "c2_sample" not in st.session_state: st.session_state.c2_sample = ""
if "c2_lab_step" not in st.session_state: st.session_state.c2_lab_step = "SET_LAMP_AAS"
if "c2_hg_calculated" not in st.session_state: st.session_state.c2_hg_calculated = 0.0

def apply_penalty(reason):
    st.session_state.hp -= 1
    st.session_state.score -= 20
    st.toast(f"❌ Kesalahan: {reason}! HP berkurang.", icon="🚨")

def back_to_menu():
    st.session_state.current_view = "MAIN_MENU"
    st.session_state.hp = 3
    st.session_state.score = 100
    st.session_state.collected_sample = ""
    st.session_state.lab_step = "INPUT_REAGEN"
    st.session_state.do_calculated = 0.0
    st.session_state.c2_sample = ""
    st.session_state.c2_lab_step = "SET_LAMP_AAS"
    st.session_state.c2_hg_calculated = 0.0
    st.session_state.show_edu_material = False

# ==========================================
# 3. SIDEBAR UTAMA & MUSIK BACKGROUND
# ==========================================
with st.sidebar:
    st.markdown("<div class='app-brand'>🕵️‍♂️ DETEKTIF HUD</div>", unsafe_allow_html=True)
    st.write("---")
    c_hp, c_sc = st.columns(2)
    c_hp.metric(label="❤️ Sisa HP", value=f"{st.session_state.hp} / 3")
    c_sc.metric(label="⭐ Skor Analisis", value=st.session_state.score)
    
    st.write("---")
    st.markdown("### 📖 Buku Rumus Kimia")
    if st.session_state.current_view == "KASUS_1":
        with st.expander("Rumus DO (Titrasi Winkler) 🧪"):
            st.write("Mencari kadar DO Air:")
            st.code("DO (mg/L) = Volume Titran (mL) * 2", language="markdown")
    elif st.session_state.current_view == "KASUS_2":
        with st.expander("Panduan Spektroskopi AAS 🔬"):
            st.write("• Lampu Katoda Merkuri (Hg) beroperasi pada panjang gelombang **253.7 nm**.")
            st.write("• Rumus Kadar Konsetrasi:")
            st.code("Kadar Hg (ppm) = Absorbansi / 0.1", language="markdown")
    else:
        st.write("Silakan pilih kasus untuk memuat data rumus forensik.")
        
    st.write("---")
    st.markdown("### 🎵 Atmosfer Investigasi")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3", format="audio/mp3", loop=True)
    
    st.write("---")
    if st.session_state.current_view != "MAIN_MENU":
        if st.button("🚪 Keluar ke Beranda"):
            back_to_menu()
            st.rerun()

# ==========================================
# 4. LOGIKA UTAMA JALUR HALAMAN
# ==========================================
st.markdown("<div class='app-brand'>EnvironForensic Lab v5.0</div>", unsafe_allow_html=True)
st.write("---")

# --- MENU UTAMA: PEMILIHAN 5 KASUS (KASUS 1 & 2 DIBUKA SEJAK AWAL) ---
if st.session_state.current_view == "MAIN_MENU":
    st.markdown("### 📁 Pilih Berkas Kasus Kriminal Lingkungan:")
    
    col_k1, col_k2, col_k3 = st.columns(3)
    with col_k1:
        st.markdown("<div class='case-selection-card'><h3>🌊 Kasus 1</h3><p><strong>Polusi Organik Citarum</strong></p><p><span style='color: #10B981;'>🔓 Terbuka</span></p></div>", unsafe_allow_html=True)
        if st.button("Buka Kasus 1", key="open_c1"):
            st.session_state.current_view = "KASUS_1"
            st.rerun()
            
    with col_k2:
        # PENGUNCIAN DIHAPUS: Kasus 2 sekarang langsung berstatus Terbuka secara bebas
        st.markdown("<div class='case-selection-card'><h3>🌋 Kasus 2</h3><p><strong>Tragedi Merkuri Buyat</strong></p><p><span style='color: #10B981;'>🔓 Terbuka</span></p></div>", unsafe_allow_html=True)
        if st.button("Buka Kasus 2", key="open_c2"):
            st.session_state.current_view = "KASUS_2"
            st.rerun()
                
    with col_k3:
        st.markdown("<div class='case-selection-card'><h3>🛢️ Kasus 3</h3><p><strong>Tumpahan Minyak Montara</strong></p><p><span style='color: #EF4444;'>🔒 Terkunci</span></p></div>", unsafe_allow_html=True)
        st.button("Disegel", key="lock_c3", disabled=True)

    col_k4, col_k5, col_empty = st.columns(3)
    with col_k4:
        st.markdown("<div class='case-selection-card'><h3>🧪 Kasus 4</h3><p><strong>Kebocoran Sianida Tambang</strong></p><p><span style='color: #EF4444;'>🔒 Terkunci</span></p></div>", unsafe_allow_html=True)
        st.button("Disegel Kasus 4", key="lock_c4", disabled=True)
        
    with col_k5:
        st.markdown("<div class='case-selection-card'><h3>🌾 Kasus 5</h3><p><strong>Eutrofikasi Danau Toba</strong></p><p><span style='color: #EF4444;'>🔒 Terkunci</span></p></div>", unsafe_allow_html=True)
        st.button("Disegel Kasus 5", key="lock_c5", disabled=True)

# --- HALAMAN GAMEPLAY: KASUS 1 (CITARUM) ---
elif st.session_state.current_view == "KASUS_1":
    if st.session_state.hp <= 0:
        st.error("🚨 **GAME OVER!** Analisis Anda ditolak Mahkamah Agung karena kelalaian data.")
        if st.button("Ulangi Kasus 1"):
            back_to_menu()
            st.session_state.current_view = "KASUS_1"
            st.rerun()
    else:
        menu_tabs = st.tabs(["🔎 1. Investigasi Lapangan", "🧪 2. Uji Laboratorium", "⚖️ 3. Putusan Sidang"])

        # TAB 1: AREA SAMPLING
        with menu_tabs[0]:
            st.markdown("### 🗺️ Pengambilan Sampel Sektor Sungai Citarum")
            st.markdown("<div class='lab-card'><strong>PETUNJUK:</strong> Pipa rahasia berada di zona: <strong>BETA</strong>.</div>", unsafe_allow_html=True)
            lokasi_input = st.text_input("Ketik KODE ZONA LOKASI target (Gunakan HURUF KAPITAL):", key="c1_loc")
            if st.button("Amankan Area & Ambil Sampel 🧺", key="btn_c1_sam"):
                if lokasi_input.strip() == "BETA":
                    st.session_state.collected_sample = "Sampel Limbah Cair"
                    st.success("🎯 Berhasil! Sampel disimpan. Silakan klik **Tab 2 (Uji Laboratorium)** di atas.")
                elif lokasi_input.strip() == "":
                    st.warning("Kolom tidak boleh kosong!")
                else:
                    apply_penalty("ZONING SALAH! Anda mendatangi pemukiman warga.")

        # TAB 2: RUANG LABORATORIUM
        with menu_tabs[1]:
            st.markdown("### 🔬 Uji Titrasi Winkler Mandiri")
            if st.session_state.collected_sample == "":
                st.warning("🔒 Mengunci Analisis: Ambil botol sampel Anda terlebih dahulu di Tab 1!")
            else:
                if st.session_state.lab_step == "INPUT_REAGEN":
                    st.markdown("<div class='lab-card'><strong>TUGAS:</strong> Masukkan rumus molekul kimia untuk senyawa <strong>Mangan(II) Sulfat</strong> sebagai reagen pengikat oksigen utama!</div>", unsafe_allow_html=True)
                    rumus_kimia = st.text_input("Ketik Rumus Molekul Reagen:", key="c1_reag")
                    if st.button("Suntikkan Senyawa Reagen 🧪", key="btn_c1_reag"):
                        if rumus_kimia.strip().upper() == "MNSO4":
                            st.success("🎯 Benar! Endapan cokelat sukses terbentuk. Langkah hitungan terbuka!")
                            st.session_state.lab_step = "HITUNG_DO"
                            st.rerun()
                        else:
                            apply_penalty("RUMUS SALAH! Larutan rusak akibat kontaminasi silang.")
                            
                elif st.session_state.lab_step == "HITUNG_DO":
                    st.markdown("<div class='lab-card'><strong>DATA:</strong> Indikator amilum menghilang tepat pada volume buret <strong>1.5 mL</strong>. Hitung kadar DO menggunakan rumus panduan di sidebar kiri!</div>", unsafe_allow_html=True)
                    input_angka = st.number_input("Masukkan angka hasil perhitungan DO Anda (mg/L):", step=0.1, key="c1_num")
                    if st.button("Sertifikasi Keakuratan Angka 📊", key="btn_c1_calc"):
                        if input_angka == 3.0:
                            st.success("🎯 Sempurna! Data sinkron. Berkas forensik siap dibawa ke **Tab 3 (Putusan Sidang)**.")
                            st.session_state.do_calculated = 3.0
                            st.session_state.lab_step = "LAB_SUCCESS"
                            st.rerun()
                        else:
                            apply_penalty("PERHITUNGAN CACAT! Hasil tidak sesuai dengan prinsip stoikiometri.")
                            
                elif st.session_state.lab_step == "LAB_SUCCESS":
                    st.markdown("<div class='lab-card'><h4>📊 DATA UTUSAN LABORATORIUM (SAH)</h4>• Kadar DO: <strong>3.0 mg/L</strong><br>• Kadar COD: <strong>580 mg/L</strong></div>", unsafe_allow_html=True)
                    st.info("Sertifikat analisis siap dibawa ke sidang meja hijau di Tab 3.")

        # TAB 3: RUANG SIDANG & EVALUASI PEMBAHASAN AKADEMIK
        with menu_tabs[2]:
            st.markdown("### ⚖️ Pengadilan Tinggi Pidana Kejahatan Lingkungan")
            if st.session_state.do_calculated == 0.0:
                st.warning("🔒 Sidang Ditunda: Dokumen pembuktian angka lab di Tab 2 belum lengkap!")
            else:
                st.write("Bandingkan hasil pengujian Anda (DO = 3.0 mg/L) dengan kriteria **PP No.22/2021 (Baku mutu minimal DO > 4.0 mg/L)**.")
                pilihan_sidang = st.selectbox(
                    "Pilih kalimat kesimpulan dakwaan akhir Anda di hadapan Majelis Hakim:",
                    ["-- Pilih Dakwaan --",
                     "Pabrik bebas karena angka DO 3.0 mg/L membuktikan pasokan oksigen sungai cukup.",
                     "Pabrik divonis bersalah karena hasil uji DO sebesar 3.0 mg/L berada di bawah ambang batas baku mutu."],
                    key="c1_sidang"
                )
                
                if st.button("🔨 KETOK PALU KEPUTUSAN HAKIM", key="btn_c1_judge"):
                    if "divonis bersalah" in pilihan_sidang:
                        st.balloons()
                        st.session_state.case1_cleared = True
                        st.session_state.show_edu_material = True
                        st.success("🎉 KASUS 1 BERHASIL DIPECAHKAN! (CASE CLOSED)")
                    else:
                        apply_penalty("Tuntutan Anda mentah karena salah memberikan kesimpulan argumentasi hukum.")
                
                if st.session_state.show_edu_material:
                    st.write("---")
                    st.markdown("### 📖 EVALUASI PASCA-OPERASI (PEMBAHASAN AKADEMIK)")
                    tab_materi, tab_berita = st.tabs(["📚 1. Pembahasan Teori Kimia", "📰 2. Bukti Nyata Dunia Nyata"])
                    
                    with tab_materi:
                        st.markdown("""
                        <div class='lab-card' style='border-color: #10B981;'>
                        <h4> Mengapa Kadar DO Bisa Drop dan COD Melonjak?</h4>
                        Limbah cair industri tekstil kaya akan senyawa organik kompleks (seperti pewarna gugus azo). Mikroorganisme air bekerja ekstra keras memutus ikatan kimia polutan tersebut melalui proses oksidasi.
                        <br><br>
                        <ul>
                            <li><strong>DO (Dissolved Oxygen):</strong> Adalah jumlah gas oksigen terlarut di air. Karena dipakai terus-menerus oleh mikroba untuk mengoksidasi limbah organik, jumlah oksigen di air drop drastis (menyentuh 3.0 mg/L). Biota sungai mati lemas akibat hipoksia.</li>
                            <li><strong>COD (Chemical Oxygen Demand):</strong> Jumlah total oksigen yang dibutuhkan untuk mengoksidasi polutan secara kimiawi menggunakan oksidator kuat. Nilai COD yang tinggi (580 mg/L) mencerminkan beban polutan kimia beracun.</li>
                        </ul>
                        </div>
                        """, unsafe_allow_html=True)
                        
                    with tab_berita:
                        st.markdown("""
                        <div class='lab-card' style='border-color: #06B6D4;'>
                        <h4> 📰 Fakta Riil Kasus Hukum Sungai Citarum</h4>
                        Kasus yang Anda selesaikan di game ini diangkat dari kejahatan lingkungan nyata di aliran Sungai Citarum, Jawa Barat. 
                        <br><br>
                        <strong>Kutipan Berita Resmi Ringkas:</strong><br>
                        <em>"Satgas Citarum Harum melakukan pengecoran dan penutupan paksa pada puluhan lubang pipa pembuangan limbah rahasia milik pabrik tekstil besar di Cimahi dan Bandung Barat. Pabrik terbukti membuang air sisa produksi berwarna hitam pekat bersuhu panas tanpa melalui proses IPAL, melanggar UU No 32 Tahun 2009."</em>
                        </div>
                        """, unsafe_allow_html=True)

# --- HALAMAN GAMEPLAY: KASUS 2 (TELUK BUYAT) ---
elif st.session_state.current_view == "KASUS_2":
    if st.session_state.hp <= 0:
        st.error("🚨 **GAME OVER!** Reputasi laboratorium Anda hancur akibat salah kalibrasi instrumen.")
        if st.button("Ulangi Kasus 2"):
            back_to_menu()
            st.session_state.current_view = "KASUS_2"
            st.rerun()
    else:
        c2_tabs = st.tabs(["🔎 1. Investigasi Pantai", "🔬 2. Spektroskopi AAS", "⚖️ 3. Putusan Sidang Teluk"])

        # TAB 1: AREA INVESTIGASI
        with c2_tabs[0]:
            st.markdown("### 🏖️ Pencarian Titik Pembuangan Tailing Tambang")
            st.markdown("<div class='lab-card'><strong>MISI INVESTIGASI:</strong> Berdasarkan laporan nelayan lokal, sedimen yang terkontaminasi raksa berat berada di area muara teluk bagian <strong>SELATAN</strong>.</div>", unsafe_allow_html=True)
            lokasi_c2 = st.text_input("Ketik KODE AREA target (Gunakan HURUF KAPITAL):", key="c2_loc")
            if st.button("Ekstraksi Sedimen Teluk 🧺", key="btn_c2_sam"):
                if lokasi_c2.strip() == "SELATAN":
                    st.session_state.c2_sample = "Sedimen Pantai Raksa"
                    st.success("🎯 Sukses! Sampel matriks sedimen seberat 10 gram berhasil diamankan. Silakan lanjut ke **Tab 2**.")
                elif lokasi_c2.strip() == "":
                    st.warning("Area tidak boleh kosong!")
                else:
                    apply_penalty("AREA BERSIH! Anda membuang waktu di titik wisata karang.")

        # TAB 2: LABORATORIUM INSTRUMEN AAS
        with c2_tabs[1]:
            st.markdown("### 🔬 Destruksi & Analisis Logam Berat dengan AAS")
            if st.session_state.c2_sample == "":
                st.warning("🔒 Mengunci Analisis: Ambil sampel sedimen luar teluk dulu di Tab 1!")
            else:
                if st.session_state.c2_lab_step == "SET_LAMP_AAS":
                    st.markdown("<div class='lab-card'><strong>TUGAS KALIBRASI:</strong> Nyalakan Hollow Cathode Lamp (HCL) khusus Merkuri. Berapa angka panjang gelombang (wavelength) emisi utama atom Hg dalam satuan nanometer (nm)? (Petunjuk ada di Buku Rumus kiri)</div>", unsafe_allow_html=True)
                    wave_input = st.number_input("Masukkan Jarak Panjang Gelombang (nm):", step=0.1, key="c2_wave")
                    if st.button("Tembakkan Laser Katoda 💥", key="btn_c2_wave"):
                        if wave_input == 253.7:
                            st.success("🎯 Kalibrasi Sempurna! Detektor menangkap garis spektrum emisi atom gas raksa. Modul hitungan terbuka.")
                            st.session_state.c2_lab_step = "HITUNG_AAS"
                            st.rerun()
                        else:
                            apply_penalty("SALAH PANJANG GELOMBANG! Alat AAS menangkap spektrum palsu dari logam lain.")
                            
                elif st.session_state.c2_lab_step == "HITUNG_AAS":
                    st.markdown("<div class='lab-card'><strong>DATA DETEKTOR:</strong> Hasil pembacaan nilai Absorbansi (A) sampel sedimen menunjukkan angka <strong>0.25</strong>. Hitung kadar konsentrasi Merkuri (Hg) menggunakan rumus pembagian di sidebar buku rumus!</div>", unsafe_allow_html=True)
                    hg_input = st.number_input("Masukkan konsentrasi Merkuri hasil hitungan (ppm):", step=0.01, key="c2_hg_val")
                    if st.button("Verifikasi Kadar Logam 📊", key="btn_c2_hg"):
                        if hg_input == 2.5:
                            st.success("🎯 Data Valid & Akurat! Berkas forensik pencemaran Teluk Buyat terkunci dan siap diajukan ke Pengadilan Internasional di **Tab 3**.")
                            st.session_state.c2_hg_calculated = 2.5
                            st.session_state.c2_lab_step = "AAS_SUCCESS"
                            st.rerun()
                        else:
                            apply_penalty("SALAH PERHITUNGAN! Data ini bisa digugurkan oleh pengacara perusahaan.")
                            
                elif st.session_state.c2_lab_step == "AAS_SUCCESS":
                    st.markdown("<div class='lab-card'><h4>📊 SERTIFIKAT HASIL AAS (RESMI)</h4>• Analit: <strong>Merkuri (Hg) / Raksa</strong><br>• Konsentrasi: <span style='color: #EF4444;'><strong>2.5 ppm (mg/kg)</strong></span></div>", unsafe_allow_html=True)
                    st.info("Kadar aman sedimen menurut standar internasional (EPA) maksimal adalah 0.15 ppm. Hasil Anda 15x lipat lebih tinggi!")

        # TAB 3: PUTUSAN SIDANG
        with c2_tabs[2]:
            st.markdown("### ⚖️ Mahkamah Konstitusi & Tuntutan Ganti Rugi Korban")
            if st.session_state.c2_hg_calculated == 0.0:
                st.warning("🔒 Pintu Sidang Terkunci: Bukti ilmiah instrumen AAS di Tab 2 belum diterbitkan!")
            else:
                st.write("Data Anda membuktikan kadar Hg sebesar **2.5 ppm**, sedangkan warga sekitar mulai menderita penyakit neurologis aneh (penyakit Minamata).")
                dakwaan_c2 = st.selectbox(
                    "Pilih kalimat kesimpulan bukti forensik Anda di depan Hakim Agung:",
                    ["-- Pilih Argumen --",
                     "Perusahaan penambang dibebaskan karena kadar raksa 2.5 ppm masih di bawah batas aman air minum.",
                     "Perusahaan tambang wajib membayar ganti rugi dan melakukan restorasi karena pencemaran merkuri 2.5 ppm merusak rantai makanan laut."],
                    key="c2_sidang_box"
                )
                if st.button("🔨 KETOK PALU KEPUTUSAN AKHIR", key="btn_c2_judge"):
                    if "wajib membayar ganti rugi" in dakwaan_c2:
                        st.balloons()
                        st.session_state.case2_cleared = True
                        st.success("🎉 LUAR BIASA! KASUS 2 BERHASIL DIPECAHKAN. ANDA ADALAH DETEKTIF LINGKUNGAN ELITE!")
                    else:
                        apply_penalty("Tuntutan Anda kalah di persidangan akibat argumen yang lemah.")
