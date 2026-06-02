import streamlit as st

# ==========================================
# 1. KONFIGURASI HALAMAN & TEMA
# ==========================================
st.set_page_config(
    page_title="Environ Detective",
    page_icon="🕵️‍♂️",
    layout="wide"
)

# Menambahkan CSS custom agar tampilan lebih menarik dan bertema gelap (Dark Detective)
st.markdown("""
    <style>
    .main { background-color: #121212; color: #FFFFFF; }
    .stButton>button { width: 100%; background-color: #1E3A8A; color: white; border-radius: 8px; }
    .stButton>button:hover { background-color: #3B82F6; }
    .report-box { padding: 15px; background-color: #1E1E1E; border-left: 5px solid #3B82F6; border-radius: 4px; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. INISIALISASI STATE GAME (LOGIKA PROG)
# ==========================================
if "stage" not in st.session_state:
    st.session_state.stage = "BRIEFING"
if "sample_collected" not in st.session_state:
    st.session_state.sample_collected = False
if "test_done" not in st.session_state:
    st.session_state.test_done = False

# ==========================================
# 3. AUDIO BACKLOG (MUSIK DETEKTIF)
# ==========================================
st.sidebar.markdown("### 🎵 Audio Kontrol")
audio_file = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" 
st.sidebar.audio(audio_file, format="audio/mp3", loop=True)
st.sidebar.info("Aktifkan audio di atas untuk merasakan atmosfer detektif!")

# ==========================================
# 4. ALUR GAME (GAMEPLAY LOOP)
# ==========================================

# ------------------------------------------
# TAHAP 1: BRIEFING KASUS
# ------------------------------------------
if st.session_state.stage == "BRIEFING":
    st.title("🕵️‍♂️ ENVIRON DETECTIVE: KASUS INDONESIA")
    st.subheader("Kasus 1: Misteri Air Berwarna di Sungai Citarum, Jawa Barat")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/e/ea/Citarum_River_pollution.jpg", 
                 caption="Kondisi visual salah satu sudut titik Sungai Citarum", use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class='report-box'>
        <strong>LAPORAN AWAL INVESTIGASI:</strong><br>
        Warga di sekitar bantaran sungai melaporkan bahwa air sungai kerap berubah warna menjadi hitam pekat dan mengeluarkan bau menyengat pada malam hari. 
        Banyak ikan yang ditemukan mati mengambang. Diduga ada aktivitas pembuangan limbah tanpa diolah dari sektor industri tekstil sekitar.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📋 Tugas Anda sebagai Analis Kimia:")
        st.write("1. Lakukan sampling di area yang mencurigakan.")
        st.write("2. Uji parameter kimia lingkungan yang tepat di laboratorium.")
        st.write("3. Tentukan apakah air melanggar Baku Mutu PP No. 22 Tahun 2021.")
        
        if st.button("Mulai Investigasi Lapangan ➡️"):
            st.session_state.stage = "SAMPLING"
            st.rerun()

# ------------------------------------------
# TAHAP 2: SAMPLING LAPANGAN
# ------------------------------------------
elif st.session_state.stage == "SAMPLING":
    st.title("📍 Peta Investigasi & Sampling Lapangan")
    st.write("Klik titik lokasi di bawah ini untuk mengambil sampel air sungai.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("📌 Titik A: Hulu Sungai (Dekat Pemukiman)")
        if st.button("Ambil Sampel A"):
            st.toast("Sampel A berhasil diambil! Air terlihat agak keruh.")
            
    with col2:
        st.warning("📌 Titik B: Area Industri (Dekat Pipa Pabrik Tekstil)")
        if st.button("Ambil Sampel B 🧪"):
            st.toast("Sampel B berhasil diambil! Air berwarna gelap dan berbau kimia tajam.")
            st.session_state.sample_collected = True
            
    with col3:
        st.info("📌 Titik C: Hilir Sungai")
        if st.button("Ambil Sampel C"):
            st.toast("Sampel C berhasil diambil! Air berwarna kecokelatan.")

    st.write("---")
    if st.session_state.sample_collected:
        st.success("✅ Anda telah mengambil sampel krusial (Sampel B) dari area industri!")
        if st.button("Bawa Sampel ke Laboratorium 🔬"):
            st.session_state.stage = "LAB"
            st.rerun()
    else:
        st.error("❌ Anda harus mencari dan mengambil sampel di area yang paling berpotensi menjadi sumber pencemaran utama dahulu.")

# ------------------------------------------
# TAHAP 3: PENGUJIAN LABORATORIUM DIGITAL
# ------------------------------------------
elif st.session_state.stage == "LAB":
    st.title("🔬 Laboratorium Analisis Kimia Lingkungan")
    st.write("Pilih parameter uji yang tepat untuk menganalisis limbah organik industri tekstil pada Sampel B.")
    
    parameter = st.selectbox("Pilih Alat & Parameter Uji:", 
                             ["-- Pilih Parameter --", "Uji Logam Merkuri (Hg)", "Uji Parameter DO, COD, & BOD", "Uji Gas Sulfur Dioksida (SO2)"])
    
    if parameter == "Uji Logam Merkuri (Hg)":
        st.error("💡 Detektif Note: Kurang tepat. Kasus ini berfokus pada limbah warna organik industri tekstil, bukan pertambangan emas.")
    elif parameter == "Uji Gas Sulfur Dioksida (SO2)":
        st.error("💡 Detektif Note: Kurang tepat. SO2 digunakan untuk analisis pencemaran kualitas udara, bukan air.")
    elif parameter == "Uji Parameter DO, COD, & BOD":
        st.success("🎯 Pilihan Tepat! Ini adalah parameter utama untuk mengukur beban pencemaran limbah organik industri air.")
        
        # Simulasi progress bar pengujian
        if st.button("Jalankan Analisis Instrumen"):
            import time
            progress_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)
                progress_bar.progress(percent_complete + 1)
            
            st.session_state.test_done = True
            
        if st.session_state.test_done:
            st.markdown("### 📊 HASIL ANALISIS LABORATORIUM DIGITAL:")
            st.metric(label="Dissolved Oxygen (DO)", value="1.2 mg/L", delta="- Rendah (Buruk)")
            st.metric(label="Chemical Oxygen Demand (COD)", value="620 mg/L", delta="+ Tinggi (Bahaya)")
            st.metric(label="Biochemical Oxygen Demand (BOD)", value="380 mg/L", delta="+ Tinggi (Bahaya)")
            
            if st.button("Tarik Kesimpulan Kasus (Persidangan) ⚖️"):
                st.session_state.stage = "VERDICT"
                st.rerun()

# ------------------------------------------
# TAHAP 4: PERSIDANGAN / PENARIKAN KESIMPULAN
# ------------------------------------------
elif st.session_state.stage == "VERDICT":
    st.title("⚖️ Sidang Putusan Lingkungan")
    st.write("Berdasarkan PP No. 22 Tahun 2021, standar baku mutu air sungai Kelas 2 adalah **DO > 4 mg/L dan COD < 25 mg/L**.")
    st.write("Dari hasil laboratorium Anda: **DO = 1.2 mg/L dan COD = 620 mg/L**.")
    
    st.markdown("### ❓ Berikan Kesimpulan Analisis Anda:")
    jawaban = st.radio("Apa status mutu air Sungai Citarum pada titik industri tersebut?", 
                       ["Memenuhi baku mutu (Aman)", "Tercemar Ringan", "Tercemar Berat akibat Aktivitas Pembuangan Limbah Organik"])
    
    if st.button("Kirim Putusan Kasus"):
        if jawaban == "Tercemar Berat akibat Aktivitas Pembuangan Limbah Organik":
            st.balloons()
            st.success("🎉 CASE CLOSED! Analisis Anda 100% Benar. Pabrik Tekstil terbukti membuang limbah tanpa melalui IPAL (Instalasi Pengolahan Air Limbah) sehingga menghabiskan oksigen terlarut (DO) di air. Anda naik pangkat menjadi Detektif Lingkungan Senior!")
            
            if st.button("Mainkan Kasus Selanjutnya 🔄"):
                st.session_state.stage = "BRIEFING"
                st.session_state.sample_collected = False
                st.session_state.test_done = False
                st.rerun()
        else:
            st.error("❌ Jawaban salah atau kurang tepat! Periksa kembali perbandingan hasil lab Anda dengan standar regulasi baku mutu.")
