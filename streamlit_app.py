import streamlit as st
import time

# ==========================================
# 1. KONFIGURASI HALAMAN & DESIGN THEME PREMIUM
# ==========================================
st.set_page_config(
    page_title="Environ Detective v2.5",
    page_icon="🕵️‍♂️",
    layout="wide"
)

# Kustomisasi CSS Total: Font, Background Kasus, Warna Teks Jelas
st.markdown("""
    <style>
    /* Mengimpor Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Courier+Prime:wght@400;700&family=Special+Elite&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    
    /* Global Font Aplikasi */
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Judul Utama Bergaya Detektif / Retro Noir */
    .detective-title {
        font-family: 'Special Elite', cursive;
        color: #C2185B;
        font-size: 46px;
        text-align: center;
        margin-bottom: 5px;
        letter-spacing: 2px;
    }
    .detective-subtitle {
        font-family: 'Courier Prime', monospace;
        color: #4A5568;
        font-size: 16px;
        text-align: center;
        margin-bottom: 25px;
        font-weight: bold;
    }
    
    /* Perbaikan Box Laporan Kasus (Kontras Tinggi & Menarik) */
    .report-box { 
        padding: 25px; 
        background-color: #F8FAFC; 
        color: #1E293B;
        border-left: 8px solid #C2185B; 
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        font-size: 16px;
        line-height: 1.7;
        margin-bottom: 20px;
    }
    
    /* Judul Sub Bab Kasus */
    .case-header {
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #0F172A;
        font-weight: 700;
        font-size: 24px;
        margin-top: 10px;
        margin-bottom: 15px;
    }
    
    /* Mengubah Gaya Tombol Utama */
    .stButton>button { 
        width: 100%; 
        background: linear-gradient(135deg, #C2185B 0%, #880E4F 100%);
        color: white !important; 
        font-weight: bold;
        font-size: 16px;
        border-radius: 12px; 
        padding: 12px;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(194, 24, 91, 0.2);
    }
    .stButton>button:hover { 
        background: linear-gradient(135deg, #E91E63 0%, #C2185B 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(194, 24, 91, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. LOGIKA UTAMA & RESET GAME
# ==========================================
def reset_game():
    st.session_state.stage = "BRIEFING"
    st.session_state.sample_collected = False
    st.session_state.test_done = False

if "stage" not in st.session_state:
    reset_game()

# ==========================================
# 3. SIDEBAR NAVIGASI DESIGN PREMIUM
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #C2185B;'>📁 BERKAS DETEKTIF</h2>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("### 👤 Identitas Analis")
    st.success("🕵️‍♂️ **Nama:** Inspektur Analis\n\n💼 **Divisi:** Penegakan Hukum Lingkungan")
    
    st.markdown("### 🗂️ Pilih Berkas Kasus")
    pilihan_kasus = st.selectbox(
        "Daftar Kasus Aktif:",
        ["Kasus 1: Misteri Sungai Citarum 🌊", "Kasus 2: Teluk Buyat (Locked) 🔒", "Kasus 3: Karhutla Riau (Locked) 🔒"]
    )
    
    st.markdown("### 📖 Buku Saku Regulasi")
    with st.expander("Lihat PP No. 22 Tahun 2021 📑"):
        st.caption("Standar Air Sungai Kelas 2:")
        st.write("• **DO:** Harus > 4 mg/L")
        st.write("• **COD:** Harus < 25 mg/L")
        st.write("• **BOD:** Harus < 3 mg/L")

    st.write("---")
    st.markdown("### 🎵 Atmosfer Investigasi")
    # Menggunakan URL musik instrumental yang stabil
    audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"
    st.audio(audio_url, format="audio/mp3", loop=True)
    st.caption("💡 Putar musik di atas untuk menghidupkan suasana tegang!")

# ==========================================
# 4. HALAMAN GAMEPLAY UTAMA
# ==========================================

# Judul Utama Aplikasi dengan Font Menarik
st.markdown("<div class='detective-title'>🚨 ENVIRON DETECTIVE 🚨</div>", unsafe_allow_html=True)
st.markdown("<div class='detective-subtitle'>[ LOGIKA & PEMROGRAMAN KOMPUTER - ANALISIS KIMIA ]</div>", unsafe_allow_html=True)
st.write("---")

if pilihan_kasus != "Kasus 1: Misteri Sungai Citarum 🌊":
    st.warning("⚠️ Berkas kasus ini masih disegel/terkunci! Selesaikan Kasus 1 terlebih dahulu.")

else:
    # ------------------------------------------
    # TAHAP 1: BRIEFING KASUS (HALAMAN PERTAMA)
    # ------------------------------------------
    if st.session_state.stage == "BRIEFING":
        st.markdown("<div class='case-header'>🌊 Kasus 1: Misteri Air Berwarna di Sungai Citarum, Jawa Barat</div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns([1.1, 1])
        
        with col1:
            # Menggunakan link gambar baru dari Wikimedia Commons yang terjamin aman & muncul tanpa diblokir
            st.image("https://upload.wikimedia.org/wikipedia/commons/e/ea/Citarum_River_pollution.jpg", 
                     caption="Bukti Foto: Kondisi tumpukan limbah domestik dan industri di salah satu titik aliran Citarum.", 
                     use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class='report-box'>
            🚨 <strong>LAPORAN TIM INTELIJEN LINGKUNGAN:</strong><br><br>
            Warga di sekitar bantaran aliran sungai melaporkan adanya aktivitas pembuangan mencurigakan. 
            Setiap malam hari, air sungai kerap berubah warna secara drastis menjadi kehitaman dan mengeluarkan aroma zat kimia menyengat yang memicu pusing kepala. 
            <br><br>
            Dalam minggu ini, ratusan biota air ditemukan mati mendadak. Kecurigaan utama mengarah pada pipa pembuangan rahasia milik salah satu Industri Tekstil raksasa di kawasan tersebut.
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 📋 Agenda Investigasi Analisis Kimia:")
            st.markdown("🔹 **1.** pergi ke lokasi peta untuk melakukan teknik sampling air sungai.")
            st.markdown("🔹 **2.** Uji parameter kimia air yang tepat menggunakan instrumen laboratorium.")
            st.markdown("🔹 **3.** Tuntut pelaku di pengadilan berdasarkan regulasi baku mutu hukum.")
            
            st.write("")
            if st.button("Mulai Selidiki Lokasi Lapangan ➡️"):
                st.session_state.stage = "SAMPLING"
                st.rerun()

    # ------------------------------------------
    # TAHAP 2: SAMPLING LAPANGAN
    # ------------------------------------------
    elif st.session_state.stage == "SAMPLING":
        st.markdown("<div class='case-header'>📍 Peta Investigasi & Pengambilan Sampel Air</div>", unsafe_allow_html=True)
        st.write("Gunakan instrumen botol sampling Anda pada titik-titik koordinat berikut:")
        st.write("")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 🏡 Titik A")
            st.info("**Hulu Sungai**\n\nDekat dengan wilayah pemukiman warga lokal.")
            if st.button("🧺 Ambil Sampel A"):
                st.toast("Sampel A berhasil diambil. Karakteristik fisik: Air agak keruh normal.")
                
        with col2:
            st.markdown("### 🏭 Titik B")
            st.warning("**Kawasan Industri**\n\nTepat di bawah pipa pembuangan tersembunyi Pabrik Tekstil.")
            if st.button("🧪 Ambil Sampel B (Target utama)"):
                st.toast("Sampel B berhasil diambil! Karakteristik fisik: Berbau tajam, warna gelap pekat.")
                st.session_state.sample_collected = True
                
        with col3:
            st.markdown("### 🛶 Titik C")
            st.info("**Hilir Sungai**\n\nAliran akhir sebelum menuju muara.")
            if st.button("🧺 Ambil Sampel C"):
                st.toast("Sampel C berhasil diambil. Karakteristik fisik: Air berwarna kecokelatan sedimen.")

        st.write("---")
        if st.session_state.sample_collected:
            st.success("✨ **Bagus, Detektif!** Anda berhasil mengamankan Sampel B yang paling mencurigakan.")
            if st.button("Bawa Sampel ke Laboratorium Analisis 🔬"):
                st.session_state.stage = "LAB"
                st.rerun()
        else:
            st.error("🛑 **Petunjuk:** Anda belum mengambil sampel di titik yang berpotensi menjadi sumber utama kejahatan lingkungan!")

    # ------------------------------------------
    # TAHAP 3: PENGUJIAN LABORATORIUM
    # ------------------------------------------
    elif st.session_state.stage == "LAB":
        st.markdown("<div class='case-header'>🔬 Laboratorium Analisis Instrumen Kimia</div>", unsafe_allow_html=True)
        st.write("Pilih metode analisis laboratorium yang paling tepat untuk menguji karakteristik limbah cair industri pewarna tekstil.")
        st.write("")
        
        parameter = st.selectbox(
            "Pilih Metode & Alat Uji Kimia:", 
            ["-- Silakan Pilih Alat --", "Metode AAS - Analisis Logam Berat Merkuri (Hg)", "Metode Titrasi & Winkler - Analisis DO, COD, & BOD", "Analisis Gas Ambien - Sulfur Dioksida (SO2)"]
        )
        
        if parameter == "Metode AAS - Analisis Logam Berat Merkuri (Hg)":
            st.error("❌ **Kurang Tepat!** Merkuri digunakan untuk kasus pencemaran tambang emas ilegal, bukan pabrik pewarna tekstil cair.")
        elif parameter == "Analisis Gas Ambien - Sulfur Dioksida (SO2)":
            st.error("❌ **Salah Media!** Gas SO2 dipakai untuk analisis pencemaran kualitas udara, sampel kita berupa air.")
        elif parameter == "Metode Titrasi & Winkler - Analisis DO, COD, & BOD":
            st.success("🎯 **Pilihan Sempurna!** Uji DO, COD, dan BOD adalah indikator mutlak untuk mengetahui tingkat pencemaran limbah organik.")
            
            if st.button("💥 Jalankan Analisis Digital"):
                progress_bar = st.progress(0)
                for percent_complete in range(100):
                    time.sleep(0.006)
                    progress_bar.progress(percent_complete + 1)
                st.session_state.test_done = True
                
            if st.session_state.test_done:
                st.write("")
                st.markdown("### 📊 DATA HASIL LABORATORIUM KELUAR:")
                
                c1, c2, c3 = st.columns(3)
                c1.metric(label="🍂 Dissolved Oxygen (DO)", value="1.2 mg/L", delta="Sangat Rendah (Buruk)", delta_color="inverse")
                c2.metric(label="⚗️ Chemical Oxygen Demand (COD)", value="620 mg/L", delta="Sangat Tinggi (Bahaya)", delta_color="normal")
                c3.metric(label="🧫 Biochemical Oxygen Demand (BOD)", value="380 mg/L", delta="Sangat Tinggi (Bahaya)", delta_color="normal")
                
                st.write("---")
                if st.button("Ajukan Berkas Hasil Lab ke Ruang Sidang ⚖️"):
                    st.session_state.stage = "VERDICT"
                    st.rerun()

    # ------------------------------------------
    # TAHAP 4: PERSIDANGAN & RESET TOTAL (UNTUK KEMBALI KE MENU AWAL)
    # ------------------------------------------
    elif st.session_state.stage == "VERDICT":
        st.markdown("<div class='case-header'>⚖️ Sidang Pengadilan Tindak Pidana Lingkungan</div>", unsafe_allow_html=True)
        st.write("Bandingkan hasil analisismu dengan Peraturan Pemerintah **PP No. 22 Tahun 2021 (Baku Mutu Air Sungai Kelas 2: DO > 4 mg/L dan COD < 25 mg/L)**.")
        st.write("")
        
        st.markdown("### 📋 Berikan Kesimpulan Hukum Anda di Depan Hakim:")
        jawaban = st.radio(
            "Berdasarkan bukti ilmiah di atas, bagaimana kesimpulan Anda?", 
            [
                "Air dalam kondisi aman karena nilai COD tinggi meningkatkan mineral air.",
                "Sungai Citarum mengalami Pencemaran Berat akibat pembuangan limbah organik industri tekstil tanpa diolah, terbukti dari nilai COD/BOD melonjak tajam dan DO drop kritis.",
                "Sungai mengalami pencemaran ringan yang disebabkan oleh sampah plastik pemukiman warga biasa."
            ]
        )
        
        st.write("")
        if st.button("🔨 Ketok Palu Keputusan Hakim"):
            if jawaban == "Sungai Citarum mengalami Pencemaran Berat akibat pembuangan limbah organik industri tekstil tanpa diolah, terbukti dari nilai COD/BOD melonjak tajam dan DO drop kritis.":
                st.balloons()
                st.success("🎉 **KASUS BERHASIL DIPECAHKAN! (CASE CLOSED)**")
                st.markdown("""
                Selamat! Hasil analisis laboratorium kimia Anda sah demi hukum. Pabrik tekstil nakal terbukti bersalah membuang limbah ilegal tanpa IPAL, dikenai denda miliaran rupiah, dan diperintahkan melakukan restorasi ekosistem sungai. 
                <br><br>
                Logika analisis Anda berhasil menyelamatkan lingkungan! 🤝
                """, unsafe_allow_html=True)
            else:
                st.error("❌ **Tuntutan Ditolak!** Hakim menganggap analisis kesimpulan Anda tidak sinkron dengan data baku mutu PP No. 22 Tahun 2021.")
        
        # 📌 JAWABAN POIN 3: Tombol Navigasi Reset Sempurna Kembali ke Menu Awal
        st.write("---")
        st.markdown("### 🔄 Opsi Navigasi Berkas")
        if st.button("🔙 Tutup Berkas Kasus & Kembali ke Menu Awal"):
            reset_game()
            st.rerun()
