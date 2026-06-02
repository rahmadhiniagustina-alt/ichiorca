import streamlit as st
import time

# ==========================================
# 1. KONFIGURASI HALAMAN & TEMA MODERN (OrganIQ Inspired)
# ==========================================
st.set_page_config(
    page_title="Environ Detective Pro",
    page_icon="🕵️‍♂️",
    layout="wide"
)

# Kustomisasi CSS untuk menciptakan UI Gelap, Premium, dan Berbasis Kartu
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;700&display=swap');
    
    /* Mengubah background aplikasi menjadi Dark Mode elegan */
    [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #0F172A !important;
        color: #E2E8F0 !important;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Menu Sidebar Gelap */
    [data-testid="stSidebar"] {
        background-color: #1E293B !important;
        border-right: 1px solid #334155;
    }
    
    /* Judul Utama */
    .main-title {
        font-size: 40px;
        font-weight: 800;
        background: linear-gradient(135deg, #38BDF8 0%, #06B6D4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
    }
    .main-subtitle {
        font-family: 'JetBrains Mono', monospace;
        font-size: 14px;
        color: #94A3B8;
        text-align: center;
        margin-bottom: 30px;
    }
    
    /* Gaya Kartu/Cards Informasi (Mirip OrganIQ) */
    .organ-card {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
    }
    
    /* Tombol Interaktif */
    .stButton>button {
        width: 100%;
        background-color: #0EA5E9;
        color: white !important;
        font-weight: 600;
        font-size: 15px;
        border-radius: 12px;
        padding: 12px;
        border: none;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #38BDF8;
        transform: translateY(-1px);
    }
    
    /* Elemen Pilihan Ganda (Radio Button) */
    div[data-testid="stRadio"] label {
        background-color: #1E293B !important;
        color: #E2E8F0 !important;
        border: 1px solid #334155 !important;
        padding: 12px 20px !important;
        border-radius: 10px !important;
        margin-bottom: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SISTEM STATE GAME (LOGIKA GAMEPLAY)
# ==========================================
def init_game_states():
    if "stage" not in st.session_state: st.session_state.stage = "BRIEFING"
    if "hp" not in st.session_state: st.session_state.hp = 3                   # Sistem Nyawa (Maksimal 3 salah)
    if "score" not in st.session_state: st.session_state.score = 100           # Sistem Skor Berkurang jika salah
    if "samples" not in st.session_state: st.session_state.samples = []         # Menyimpan list sampel terkumpul
    if "case2_unlocked" not in st.session_state: st.session_state.case2_unlocked = False
    if "test_executed" not in st.session_state: st.session_state.test_executed = False

init_game_states()

def apply_penalty(reason):
    st.session_state.hp -= 1
    st.session_state.score -= 25
    st.toast(f"❌ {reason}! Nyawa berkurang. Sisa HP: {st.session_state.hp}", icon="🚨")

def reset_current_case():
    st.session_state.stage = "BRIEFING"
    st.session_state.hp = 3
    st.session_state.score = 100
    st.session_state.samples = []
    st.session_state.test_executed = False

# ==========================================
# 3. INTERFASE NAVIGATION BAR & SIDEBAR Menu
# ==========================================
with st.sidebar:
    st.markdown("<h2 style='color: #38BDF8; text-align:center;'>🕵️‍♂️ DASHBOARD</h2>", unsafe_allow_html=True)
    st.write("---")
    
    # Indikator Status Nyawa & Skor Game (Membuat Game Lebih Menantang)
    st.markdown("### 📊 Status Detektif")
    col_hp, col_score = st.columns(2)
    col_hp.metric(label="❤️ Sisa HP", value=f"{st.session_state.hp} / 3")
    col_score.metric(label="⭐ Skor", value=st.session_state.score)
    
    st.write("---")
    st.markdown("### 🗂️ Berkas Kasus")
    status_k2 = "🔓 Ready" if st.session_state.case2_unlocked else "🔒 Locked"
    pilihan_kasus = st.selectbox(
        "Pilih Studi Kasus:",
        ["Kasus 1: Polusi Organik Citarum 🌊", f"Kasus 2: Logam Berat Teluk Buyat ({status_k2})"]
    )
    
    st.write("---")
    st.markdown("### 📖 Buku Panduan Praktikum")
    with st.expander("Metode Uji Kualitatif Air"):
        st.caption("**Uji DO/BOD/COD:** Mengukur tingkat deoksigenasi akibat pencemaran bahan organik (Limbah Tekstil, Domestik).")
        st.caption("**Uji AAS (Logam Berat):** Mengukur kadar raksa/merkuri dan arsenik dari limbah anorganik (Pertambangan).")

    st.write("---")
    st.markdown("### 🎵 Audio Atmosfer")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3", format="audio/mp3", loop=True)

# ==========================================
# 4. ALUR UTAMA GAMEPLAY
# ==========================================
st.markdown("<div class='main-title'>ENVIRON DETECTIVE LAB</div>", unsafe_allow_html=True)
st.markdown("<div class='main-subtitle'>[ INTEGRATED ENVIRONMENTAL CRIME INVESTIGATION ]</div>", unsafe_allow_html=True)

# GAME OVER CEK LOGIKA
if st.session_state.hp <= 0:
    st.error("🚨 GAME OVER! Anda kehilangan seluruh nyawa karena salah melakukan analisis. Reputasi analis Anda hancur di mata hukum.")
    if st.button("🔄 Ulangi Investigasi Kasus Ini"):
        reset_current_case()
        st.rerun()

# JIKA MEMILIH KASUS YANG MASIH TERKUNCI
elif "Kasus 2" in pilihan_kasus and not st.session_state.case2_unlocked:
    st.warning("🔒 **Akses Berkas Ditolak!** Selesaikan Kasus 1 dengan hasil akurat di pengadilan terlebih dahulu untuk membuka kunci Kasus Teluk Buyat.")

# ==========================================
# ALUR SKENARIO KASUS 1 (CITARUM)
# ==========================================
elif "Kasus 1" in pilihan_kasus:

    # --- TAHAP 1: BRIEFING ---
    if st.session_state.stage == "BRIEFING":
        st.markdown("### 📋 Laporan Kasus: Misteri Aliran Air Berwarna")
        
        col_img, col_txt = st.columns([1.2, 1])
        with col_img:
            st.image("https://upload.wikimedia.org/wikipedia/commons/e/ea/Citarum_River_pollution.jpg", 
                     caption="Lokasi Kejadian: Sungai Citarum, Sektor Industri Tekstil", use_container_width=True)
        with col_txt:
            st.markdown("""
            <div class='organ-card'>
            <strong>INFORMASI INTELIJEN:</strong><br>
            Warga mengeluhkan air sungai berubah warna secara dinamis (kadang merah, kadang hitam pekat) disertai bau amonia yang menyengat di malam hari. Ratusan ikan mati mendadak. 
            <br><br>
            Ada 3 titik potensial. Anda dibekali 3 unit HP. Setiap kesalahan teknis sampling atau metode laboratorium akan merusak akurasi data Anda!
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Mulai Investigasi Lapangan 🔍"):
                st.session_state.stage = "SAMPLING"
                st.rerun()

    # --- TAHAP 2: SAMPLING (EKSPLORASI NON-LINEAR) ---
    elif st.session_state.stage == "SAMPLING":
        st.markdown("### 📍 Fase Sampling Mandiri")
        st.write("Analisis karakteristik wilayah di bawah ini sebelum mengambil keputusan tindakan:")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("<div class='organ-card'><h4>🏡 Titik A: Hulu Pemukiman</h4><p>Kondisi air jernih dengan sedimentasi tanah biasa akibat aktivitas domestik masyarakat.</p></div>", unsafe_allow_html=True)
            if st.button("🧺 Ambil Sampel A"):
                if "Sampel A" not in st.session_state.samples:
                    st.session_state.samples.append("Sampel A")
                    apply_penalty("Membuang waktu pada sampel sekunder")
                else: st.warning("Sampel A sudah ada di inventori.")
                
        with c2:
            st.markdown("<div class='organ-card'><h4>🏭 Titik B: Area Outlet Industri</h4><p>Ditemukan pipa siluman tersembunyi di bawah permukaan air yang mengeluarkan busa pekat berbau asam tajam.</p></div>", unsafe_allow_html=True)
            if st.button("🧪 Ambil Sampel B (Target Utama)"):
                if "Sampel B" not in st.session_state.samples:
                    st.session_state.samples.append("Sampel B")
                    st.success("🎯 Bagus! Sampel utama limbah berbahaya berhasil diamankan.")
                else: st.warning("Sampel B sudah ada di inventori.")
                
        with c3:
            st.markdown("<div class='organ-card'><h4>🛶 Titik C: Hilir Aliran</h4><p>Air terlihat keruh kecokelatan bercampur sampah plastik makro terapung.</p></div>", unsafe_allow_html=True)
            if st.button("🧺 Ambil Sampel C"):
                if "Sampel C" not in st.session_state.samples:
                    st.session_state.samples.append("Sampel C")
                    apply_penalty("Membuang waktu pada sampel sekunder")
                else: st.warning("Sampel C sudah ada di inventori.")
                
        st.write("---")
        st.markdown(f"**Inventori Botol Sampel:** {', '.join(st.session_state.samples) if st.session_state.samples else 'Kosong'}")
        
        if "Sampel B" in st.session_state.samples:
            if st.button("Lanjutkan ke Laboratorium Analisis 🔬"):
                st.session_state.stage = "LAB"
                st.rerun()

    # --- TAHAP 3: LABORATORIUM (PILIHAN PARAMETER MENANTANG) ---
    elif st.session_state.stage == "LAB":
        st.markdown("### 🔬 Uji Kualitatif & Kuantitatif Digital")
        st.write("Pilih instrumen reagen pengujian yang sesuai dengan jenis kontaminan organik tekstil (pewarna/zat pengikat):")
        
        # Grid Card seperti menu utama OrganIQ
        col_param = st.selectbox(
            "Pilih Metode Analisis:",
            ["-- Klik untuk Memilih Instrumen --", "Spektrofotometri Serapan Atom (AAS)", "Kromatografi Gas Udara Ambien", "Titrasi Metode Winkler (DO / COD / BOD)"]
        )
        
        if col_param == "Spektrofotometri Serapan Atom (AAS)":
            if st.button("Jalankan Uji AAS"):
                apply_penalty("Instrumen AAS dipakai khusus mendeteksi logam berat (bukan polutan organik)")
        elif col_param == "Kromatografi Gas Udara Ambien":
            if st.button("Jalankan Uji Kromatografi"):
                apply_penalty("Salah media analisis! Ini alat ukur polusi udara")
        elif col_param == "Titrasi Metode Winkler (DO / COD / BOD)":
            st.success("🎯 Tepat! Parameter uji organik cair berhasil dipilih.")
            
            if st.button("⚙️ Mulai Proses Titrasi Instrumen"):
                progress = st.progress(0)
                for p in range(100):
                    time.sleep(0.005)
                    progress.progress(p + 1)
                st.session_state.test_executed = True
                
            if st.session_state.test_executed:
                st.markdown("<div class='organ-card'><h4>📊 Laporan Hasil Lab Terbit:</h4>"
                            "• Dissolved Oxygen (DO): <strong>1.2 mg/L</strong> (Baku Mutu > 4 mg/L)<br>"
                            "• Chemical Oxygen Demand (COD): <strong>620 mg/L</strong> (Baku Mutu < 25 mg/L)<br>"
                            "• Biochemical Oxygen Demand (BOD): <strong>380 mg/L</strong> (Baku Mutu < 3 mg/L)</div>", unsafe_allow_html=True)
                
                if st.button("Bawa Berkas ke Meja Hijau ⚖️"):
                    st.session_state.stage = "VERDICT"
                    st.rerun()

    # --- TAHAP 4: PERSIDANGAN ---
    elif st.session_state.stage == "VERDICT":
        st.markdown("### ⚖️ Sidang Putusan Pelanggaran Lingkungan")
        st.write("Hakim meminta kesimpulan ilmiah Anda berdasarkan data angka riil laboratorium tadi:")
        
        pilihan_sidang = st.radio(
            "Pilih pernyataan dakwaan yang valid menurut ilmu kimia lingkungan:",
            [
                "Limbah aman karena tingginya nilai COD mengindikasikan kelimpahan mineral organik menguntungkan.",
                "Terjadi pencemaran organik berat akibat pembuangan limbah tanpa diolah, ditandai lonjakan masif COD/BOD serta defisit oksigen terlarut (DO) kaku yang membunuh biota.",
                "Sungai hanya mengalami siklus eutrofikasi alami musiman akibat sedimentasi domestik hulu."
            ]
        )
        
        if st.button("🔨 Ketok Palu Sidang"):
            if "Pencemaran organik berat" in pilihan_sidang:
                st.balloons()
                st.success(f"🎉 KASUS CITARUM BERHASIL DIPECAHKAN! Skor Akhir: {st.session_state.score} Poin.")
                st.session_state.case2_unlocked = True
                st.info("🔓 Kasus 2 (Teluk Buyat) sekarang telah terbuka! Silakan ganti berkas di menu samping kiri untuk melanjutkan misi berikutnya.")
            else:
                apply_penalty("Dakwaan salah, pengacara pabrik memenangkan banding")
                
        st.write("---")
        if st.button("🔙 Reset Investigasi Ke Menu Utama"):
            reset_current_case()
            st.rerun()

# ==========================================
# RUNNING SKENARIO KASUS 2 (TELUK BUYAT)
# ==========================================
elif "Kasus 2" in pilihan_kasus and st.session_state.case2_unlocked:
    st.markdown("### 🌋 Kasus 2: Tragedi Merkuri Teluk Buyat, Sulawesi Utara")
    st.image("https://upload.wikimedia.org/wikipedia/commons/d/d4/Atomic_absorption_spectrometer.jpg", caption="Instrumen AAS Laboratorium Kualitatif", use_container_width=True)
    st.info("🎯 Anda berhasil masuk ke Kasus Baru! Di sini polutan utamanya berbeda, yaitu merkuri ($Hg$). Gunakan panduan buku saku untuk menentukan metode instrumen laboratorium yang tepat nanti.")
