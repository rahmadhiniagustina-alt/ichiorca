import streamlit as st
import time

# ==========================================
# 1. KONFIGURASI HALAMAN & TEMA (DARK STYLE)
# ==========================================
st.set_page_config(
    page_title="Environ Detective v2.0",
    page_icon="🕵️‍♂️",
    layout="wide"
)

# Kustomisasi CSS untuk Font Judul Menarik & Elemen UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Special+Elite&family=Ubuntu:wght@400;700&display=swap');
    
    /* Judul Utama ala Detektif */
    .detective-title {
        font-family: 'Special Elite', cursive;
        color: #FF4B4B;
        font-size: 42px;
        text-align: center;
        text-shadow: 2px 2px #1E1E1E;
        margin-bottom: 20px;
    }
    
    /* Box Laporan Kasus */
    .report-box { 
        padding: 20px; 
        background-color: #1E1E1E; 
        border-left: 6px solid #FF4B4B; 
        border-radius: 8px;
        font-family: 'Ubuntu', sans-serif;
        line-height: 1.6;
    }
    
    /* Tombol Utama */
    .stButton>button { 
        width: 100%; 
        background-color: #1E3A8A; 
        color: white; 
        font-weight: bold;
        border-radius: 10px; 
        padding: 10px;
        border: 1px solid #3B82F6;
    }
    .stButton>button:hover { 
        background-color: #3B82F6; 
        border-color: #60A5FA;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOGIKA RESET GAME (FUNGSI KEMBALI)
# ==========================================
def reset_game():
    st.session_state.stage = "BRIEFING"
    st.session_state.sample_collected = False
    st.session_state.test_done = False

# Inisialisasi State Awal jika belum ada
if "stage" not in st.session_state:
    reset_game()

# ==========================================
# 3. SIDEBAR MENU YANG MENARIK 🧭
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>📁 MENU UTAMA</h2>", unsafe_allow_html=True)
    st.write("---")
    
    # 📌 Sub-Menu 1: Profil Karakter
    st.markdown("### 👤 Profil Detektif")
    st.info("**Nama:** Inspektur Analis\n\n**Divisi:** Penegakan Hukum Lingkungan")
    
    # 📌 Sub-Menu 2: Daftar Kasus (Inspirasi untuk 5 kasus ke depan)
    st.markdown("### 🗂️ Pilih Berkas Kasus")
    pilihan_kasus = st.selectbox(
        "Pilih Kasus yang Ingin Diselidiki:",
        ["Kasus 1: Misteri Sungai Citarum 🌊", "Kasus 2: Teluk Buyat (Locked) 🔒", "Kasus 3: Karhutla Riau (Locked) 🔒"]
    )
    
    # 📌 Sub-Menu 3: Buku Panduan Analis (Cheat Sheet)
    st.markdown("### 📖 Buku Saku Baku Mutu")
    with st.expander("Lihat PP No. 22 Tahun 2021"):
        st.caption("Standar Air Sungai Kelas 2:")
        st.write("• **DO:** Harus > 4 mg/L")
        st.write("• **COD:** Harus < 25 mg/L")
        st.write("• **BOD:** Harus < 3 mg/L")

    # 📌 Sub-Menu 4: Kontrol Audio
    st.write("---")
    st.markdown("### 🎵 Atmosfer Detektif")
    audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"
    st.audio(audio_url, format="audio/mp3", loop=True)
    st.caption("💡 Putar musik di atas untuk menghidupkan suasana tegang!")

# ==========================================
# 4. GAMEPLAY ALUR UTAMA (KASUS 1)
# ==========================================

# Menampilkan Judul Keren di Setiap Halaman
st.markdown("<div class='detective-title'>🕵️‍♂️ ENVIRON DETECTIVE: INDONESIA</div>", unsafe_allow_html=True)
st.write("---")

if pilihan_kasus != "Kasus 1: Misteri Sungai Citarum 🌊":
    st.warning("⚠️ Kasus ini masih terkunci! Selesaikan Kasus 1 terlebih dahulu untuk membukanya.")

else:
    # ------------------------------------------
    # TAHAP 1: BRIEFING KASUS
    # ------------------------------------------
    if st.session_state.stage == "BRIEFING":
        st.subheader("🌊 Kasus 1: Misteri Air Berwarna di Sungai Citarum, Jawa Barat")
        
        col1, col2 = st.columns([1.2, 1])
        
        with col1:
            # Menggunakan URL gambar alternatif yang stabil dari Wikimedia
            st.image("https://upload.wikimedia.org/wikipedia/commons/9/9f/Citarum_River.jpg", 
                     caption="Kondisi tumpukan limbah domestik dan industri di salah satu titik aliran Citarum.", 
                     use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class='report-box'>
            🚨 <strong>LAPORAN MASUK:</strong><br>
            Warga di sekitar aliran sungai melaporkan adanya aktivitas mencurigakan. Air sungai kerap berubah warna secara drastis menjadi kehitaman dan mengeluarkan aroma menyengat yang memicu pusing kepala. 
            <br><br>
            Banyak habitat air mati mendadak dalam waktu berdekatan. Kecurigaan mengarah pada pipa pembuangan rahasia milik industri tekstil raksasa di area tersebut.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 📋 Agenda Investigasi Anda:")
            st.write("1. 📍 Pergi ke lapangan dan lakukan teknik sampling air.")
            st.write("2. 🔬 Uji parameter kimia air yang tepat menggunakan fasilitas lab.")
            st.write("3. ⚖️ Hadapi persidangan dengan bukti valid kesesuaian Baku Mutu.")
            
            st.write("")
            if st.button("Mulai Selidiki Lokasi ➡️"):
                st.session_state.stage = "SAMPLING"
                st.rerun()

    # ------------------------------------------
    # TAHAP 2: SAMPLING LAPANGAN
    # ------------------------------------------
    elif st.session_state.stage == "SAMPLING":
        st.subheader("📍 Peta Investigasi & Pengambilan Sampel Air")
        st.write("Analisis area sekitar dan kumpulkan sampel air dari titik-titik krusial di bawah ini:")
        st.write("")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 🏡 Titik A")
            st.info("**Hulu Sungai**\n\nDekat dengan wilayah pemukiman warga lokal.")
            if st.button("🧺 Ambil Sampel A"):
                st.toast("Sampel A diamankan! Fisik: Air agak keruh normal.")
                
        with col2:
            st.markdown("### 🏭 Titik B")
            st.warning("**Kawasan Industri**\n\nTepat di bawah pipa pembuangan tersembunyi Pabrik Tekstil.")
            if st.button("🧪 Ambil Sampel B (Target)"):
                st.toast("Sampel B berhasil diambil! Fisik: Berbau tajam, warna gelap kental.")
                st.session_state.sample_collected = True
                
        with col3:
            st.markdown("### 🛶 Titik C")
            st.info("**Hilir Sungai**\n\nAliran akhir sebelum menuju muara.")
            if st.button("🧺 Ambil Sampel C"):
                st.toast("Sampel C diamankan! Fisik: Air berwarna kecokelatan sedimen.")

        st.write("---")
        if st.session_state.sample_collected:
            st.success("✨ **Bagus!** Anda berhasil mengamankan Sampel B yang menjadi sumber kecurigaan utama.")
            if st.button("Bawa Sampel ke Laboratorium Analisis 🔬"):
                st.session_state.stage = "LAB"
                st.rerun()
        else:
            st.error("🛑 **Petunjuk:** Cari dan klik tombol ambil sampel pada titik yang paling berpotensi menghasilkan bukti pencemaran industri tertinggi.")

    # ------------------------------------------
    # TAHAP 3: PENGUJIAN LABORATORIUM
    # ------------------------------------------
    elif st.session_state.stage == "LAB":
        st.subheader("🔬 Laboratorium Analisis Instrumen & Kimia Lingkungan")
        st.write("Sebagai analis, pilih metode pengujian yang paling sensitif terhadap karakteristik polusi industri tekstil.")
        st.write("")
        
        parameter = st.selectbox(
            "Pilih Parameter & Alat Analisis:", 
            ["-- Silakan Pilih Alat --", "Metode AAS - Analisis Logam Berat Merkuri (Hg)", "Metode Titrasi & Winkler - Analisis DO, COD, & BOD", "Analisis Gas Ambien - Sulfur Dioksida (SO2)"]
        )
        
        if parameter == "Metode AAS - Analisis Logam Berat Merkuri (Hg)":
            st.error("❌ **Analisis Kurang Tepat!** Logam merkuri biasanya indikator limbah tambang emas, bukan limbah pewarna organik tekstil.")
        elif parameter == "Analisis Gas Ambien - Sulfur Dioksida (SO2)":
            st.error("❌ **Analisis Salah Tempat!** SO2 adalah parameter pencemaran udara, kita sedang menguji sampel air sungai.")
        elif parameter == "Metode Titrasi & Winkler - Analisis DO, COD, & BOD":
            st.success("🎯 **Pilihan Sempurna!** Parameter DO, COD, dan BOD adalah indikator mutlak untuk mengukur tingkat keparahan limbah organik cair.")
            
            if st.button("💥 Jalankan Pengujian Instrumen"):
                progress_bar = st.progress(0)
                for percent_complete in range(100):
                    time.sleep(0.008)
                    progress_bar.progress(percent_complete + 1)
                st.session_state.test_done = True
                
            if st.session_state.test_done:
                st.write("")
                st.markdown("### 📊 DATA HASIL ANALISIS DIGITAL KELUAR:")
                
                c1, c2, c3 = st.columns(3)
                c1.metric(label="🍂 Dissolved Oxygen (DO)", value="1.2 mg/L", delta="Sangat Rendah (Kritis)", delta_color="inverse")
                c2.metric(label="⚗️ Chemical Oxygen Demand (COD)", value="620 mg/L", delta="Sangat Tinggi (Bahaya)", delta_color="normal")
                c3.metric(label="🧫 Biochemical Oxygen Demand (BOD)", value="380 mg/L", delta="Sangat Tinggi (Bahaya)", delta_color="normal")
                
                st.write("---")
                if st.button("Siapkan Berkas & Menuju Ruang Sidang ⚖️"):
                    st.session_state.stage = "VERDICT"
                    st.rerun()

    # ------------------------------------------
    # TAHAP 4: PERSIDANGAN & TOMBOL RESET (KEMBALI KE AWAL)
    # ------------------------------------------
    elif st.session_state.stage == "VERDICT":
        st.subheader("⚖️ Sidang Pengadilan Tindak Pidana Lingkungan")
        st.write("Bandingkan hasil analisismu dengan regulasi pemerintah **PP No. 22 Tahun 2021 (Baku Mutu Air Sungai Kelas 2: DO > 4 mg/L dan COD < 25 mg/L)**.")
        st.write("")
        
        st.markdown("### 📋 Ajukan Tuntutan Hukum Anda Berdasarkan Bukti Kimia:")
        jawaban = st.radio(
            "Pilih kesimpulan akhir yang paling logis dan scientifically benar:", 
            [
                "Air dalam kondisi aman karena nilai COD tinggi memperkaya nutrien air.",
                "Air mengalami pencemaran berat akibat akumulasi limbah organik industri yang menghabiskan pasokan oksigen terlarut.",
                "Air tergolong tercemar ringan akibat aktivitas rumah tangga biasa."
            ]
        )
        
        st.write("")
        if st.button("🔨 Ketok Palu Keputusan Sidang"):
            if jawaban == "Air mengalami pencemaran berat akibat akumulasi limbah organik industri yang menghabiskan pasokan oksigen terlarut.":
                st.balloons()
                st.success("🎉 **KASUS BERHASIL DIPECAHKAN! (CASE CLOSED)**")
                st.markdown("""
                Aktivitas ilegal Pabrik Tekstil terbukti secara hukum telah mencemari Sungai Citarum. Dokumen hasil analisismu valid dan berhasil memaksa pabrik membayar denda restorasi lingkungan serta menutup pipa ilegal mereka! 
                <br><br>
                Selamat, kemampuan logika analisis kimia Anda berhasil menyelamatkan ekosistem sungai! 🤝
                """, unsafe_allow_html=True)
            else:
                st.error("❌ **Putusan Ditolak Hakim!** Argumen atau kesimpulan yang Anda ajukan kurang kuat secara ilmiah dan tidak sesuai dengan perbandingan angka baku mutu.")
        
        # 📌 JAWABAN POIN 3: Tombol Kembali ke Awal / Reset Game
        st.write("---")
        st.markdown("### 🔄 Opsi Navigasi Game")
        if st.button("🔙 Kembali ke Menu Awal & Reset Penyelidikan"):
            reset_game()
            st.rerun()
