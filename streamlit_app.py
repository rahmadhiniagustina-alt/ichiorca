import streamlit as st
import pandas as pd
import time

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Chem Detective Indonesia",
    page_icon="🕵️‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS UNTUK MENU INTERAKTIF & ESTETIKA GAMING ---
st.markdown("""
    <style>
    /* Mengubah font global agar terasa seperti game investigasi */
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Special+Elite&display=swap');
    
    .main {
        background-color: #12161a;
        color: #ecf0f1;
    }
    .report-title {
        font-family: 'Special Elite', cursive;
        font-size: 42px;
        color: #e74c3c;
        text-align: center;
        margin-bottom: 5px;
        text-shadow: 2px 2px 4px #000000;
    }
    .sub-title {
        font-family: 'Share Tech Mono', monospace;
        color: #bdc3c7;
        text-align: center;
        font-size: 16px;
        letter-spacing: 2px;
        margin-bottom: 30px;
    }
    /* Style untuk Papan Kasus Interaktif */
    .case-board-title {
        font-family: 'Special Elite', cursive;
        color: #f39c12;
        border-bottom: 2px dashed #f39c12;
        padding-bottom: 10px;
        margin-top: 20px;
    }
    .interactive-card {
        background: linear-gradient(145deg, #1e252b, #171d22);
        border: 1px solid #34495e;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 25px;
        transition: all 0.3s ease-in-out;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.5);
    }
    .interactive-card:hover {
        transform: translateY(-5px);
        border-color: #e74c3c;
        box-shadow: 0px 0px 20px rgba(231, 76, 60, 0.4);
    }
    .case-badge {
        background-color: #e74c3c;
        color: white;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: bold;
        font-family: 'Share Tech Mono', monospace;
    }
    .clue-box {
        background-color: #1a252f;
        color: #ecf0f1;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #3498db;
        margin-bottom: 10px;
        font-family: 'Share Tech Mono', monospace;
    }
    /* Mengubah style tab Streamlit agar masuk ke tema gelap game */
    .stTabs [data-baseweb="tab"] {
        font-family: 'Share Tech Mono', monospace;
        font-size: 16px;
        color: #bdc3c7;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: #e74c3c;
    }
    .stTabs [aria-selected="true"] {
        color: #f39c12 !important;
        border-bottom-color: #f39c12 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- INITIALIZATION SESSION STATE ---
if 'current_case' not in st.session_state:
    st.session_state.current_case = None
if 'unlocked_clues' not in st.session_state:
    st.session_state.unlocked_clues = []
if 'lab_analyzed' not in st.session_state:
    st.session_state.lab_analyzed = False
if 'game_score' not in st.session_state:
    st.session_state.game_score = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'completed_cases' not in st.session_state:
    st.session_state.completed_cases = []

# --- DATABASE KASUS NYATA INDONESIA METADATA INTERAKTIF ---
CASES = {
    "Kasus 1: Misteri Penyakit Neurologis Teluk Buyat (2004)": {
        "id": "KB2004",
        "lokasi": "Teluk Buyat, Sulawesi Utara",
        "kesulitan": "⭐⭐",
        "durasi": "~10 Menit",
        "parameter_utama": "Hg, As, Bioakumulasi",
        "gambar": "http://googleusercontent.com/image_collection/image_retrieval/9183348929598449345_0",
        "deskripsi": "Masyarakat di sekitar pesisir Teluk Buyat melaporkan munculnya benjolan aneh pada kulit, sakit kepala hebat, dan gangguan fungsi saraf (neurologis). Nelayan juga melaporkan adanya kematian ikan secara mendadak di area teluk. Sebuah perusahaan pertambangan emas skala besar dituduh membuang limbah tailing-nya ke dasar laut.",
        "petunjuk_lapangan": [
            "🕵️‍♂️ Petunjuk 1: Limbah sisa pemisahan emas (tailing) dialirkan melalui pipa bawah laut pada kedalaman 82 meter.",
            "🕵️‍♂️ Petunjuk 2: Warga lokal memiliki kebiasaan mengonsumsi kerang dan ikan dasar laut (demersal) yang ditangkap langsung di teluk.",
            "🕵️‍♂️ Petunjuk 3: Hasil otopsi jaringan biologis ikan menunjukkan terjadinya kerusakan parah pada organ hati dan insang."
        ],
        "data_lab": {
            "pH Perairan": {"nilai": 8.1, "normal": "7.0 - 8.5", "status": "Normal"},
            "Merkuri (Hg) di Sedimen": {"nilai": 2.45, "normal": "< 0.4 mg/kg", "status": "Sangat Tinggi (Bahaya)"},
            "Arsen (As) di Sedimen": {"nilai": 18.2, "normal": "< 5.0 mg/kg", "status": "Melebihi Batas"},
            "DO (Dissolved Oxygen)": {"nilai": 5.2, "normal": "> 5.0 mg/L", "status": "Normal"}
        },
        "pertanyaan": "Berdasarkan tingginya kadar Merkuri (Hg) dan Arsen (As) pada sedimen, serta gejala klinis kerusakan saraf pada warga, proses bio-kimia lingkungan apa yang paling tepat menjelaskan fenomena ini?",
        "pilihan": [
            "Eutrofikasi masif akibat limpasan pupuk nitrogen pertanian warga.",
            "Metilasi merkuri oleh bakteri sedimen yang menyebabkan bioakumulasi dan biomagnifikasi logam berat melalui rantai makanan.",
            "Asidifikasi air laut akibat emisi gas karbon dioksida dari industri pariwisata."
        ],
        "jawaban_benar": "Metilasi merkuri oleh bakteri sedimen yang menyebabkan bioakumulasi dan biomagnifikasi logam berat melalui rantai makanan.",
        "edukasi": "Analisis Detektif: Logam berat merkuri (Hg) anorganik yang mengendap di sedimen Teluk Buyat diubah oleh bakteri anaerob menjadi senyawa organik metil merkuri yang sangat beracun. Senyawa ini terserap oleh plankton, dimakan ikan kecil, lalu ikan besar (bioakumulasi). Karena metil merkuri sulit diekskresikan, kadarnya berlipat ganda di top predator (biomagnifikasi), yaitu manusia yang memakannya, menyebabkan kerusakan sistem saraf pusat mirip Tragedi Minamata."
    },
    "Kasus 2: Krisis Oksigen Terlarut Sungai Citarum": {
        "id": "SC2018",
        "lokasi": "DAS Citarum, Jawa Barat",
        "kesulitan": "⭐⭐⭐",
        "durasi": "~15 Menit",
        "parameter_utama": "BOD, COD, DO, Cr6+",
        "gambar": "http://googleusercontent.com/image_collection/image_retrieval/13850938114624661230_0",
        "deskripsi": "Sungai Citarum sempat dinobatkan sebagai salah satu sungai paling tercemar di dunia. Di beberapa titik, air sungai berwarna hitam pekat, berbuih, dan mengeluarkan bau busuk hidrogen sulfida (H2S). Banyak industri tekstil, kertas, dan elektroplating beroperasi di sepanjang bantaran sungai.",
        "petunjuk_lapangan": [
            "🕵️‍♂️ Petunjuk 1: Banyak ditemukan 'pipa siluman' pembuangan limbah yang hanya aktif mengeluarkan air berwarna gelap di malam hari.",
            "🕵️‍♂️ Petunjuk 2: Struktur komunitas makrozoobentos (hewan dasar sungai) bergeser drastis, hanya menyisakan organisme indikator polusi berat seperti cacing Tubifex.",
            "🕵️‍♂️ Petunjuk 3: Air sungai berbau busuk tajam seperti telur busuk akibat kondisi anoksik (tanpa oksigen)."
        ],
        "data_lab": {
            "pH Air Sungai": {"nilai": 9.5, "normal": "6.0 - 9.0", "status": "Basa Kuat (Limbah Cuci)"},
            "BOD (Biochemical Oxygen Demand)": {"nilai": 180, "normal": "< 3 mg/L", "status": "Kritis (Sangat Tinggi)"},
            "COD (Chemical Oxygen Demand)": {"nilai": 450, "normal": "< 25 mg/L", "status": "Kritis (Sangat Tinggi)"},
            "Kromium Heksavalen (Cr6+)": {"nilai": 1.8, "normal": "< 0.05 mg/L", "status": "Karsinogenik Tinggi"},
            "DO (Dissolved Oxygen)": {"nilai": 0.5, "normal": "> 4.0 mg/L", "status": "Hampir Nol (Anoksia)"}
        },
        "pertanyaan": "Mengapa kadar DO di Sungai Citarum bisa anjlok hingga hampir nol, dan apa hubungannya dengan tingginya nilai BOD/COD serta keberadaan Kromium (Cr6+)?",
        "pilihan": [
            "Tingginya bahan organik dan kimia dari limbah tekstil memicu mikroorganisme menghabiskan oksigen terlarut untuk proses degradasi, diperparah racun Kromium yang mematikan biota penyumbang oksigen.",
            "Suhu air sungai yang terlalu dingin membuat kelarutan gas oksigen menurun drastis.",
            "Limbah domestik sabun mandi menyebabkan air menjadi terlalu jernih sehingga sinar matahari membakar oksigen."
        ],
        "jawaban_benar": "Tingginya bahan organik dan kimia dari limbah tekstil memicu mikroorganisme menghabiskan oksigen terlarut untuk proses degradasi, diperparah racun Kromium yang mematikan biota penyumbang oksigen.",
        "edukasi": "Analisis Detektif: Nilai BOD dan COD yang melonjak menunjukkan beban limbah organik dan anorganik yang sangat tinggi (dari proses pewarnaan dan pencucian tekstil). Bakteri aerob menggunakan seluruh oksigen terlarut (DO) untuk mengoksidasi polutan tersebut hingga habis. Akibatnya, kondisi menjadi anaerob dan menghasilkan gas H2S (bau busuk). Sementara itu, Kromium Heksavalen (Cr6+) berasal dari zat fiksasi warna tekstil yang bersifat toksik dan karsinogenik bagi lingkungan."
    },
    "Kasus 3: Semburan Sifat Kimia Lumpur Lapindo (2006)": {
        "id": "LL2006",
        "lokasi": "Porong, Sidoarjo, Jawa Timur",
        "kesulitan": "⭐⭐⭐⭐",
        "durasi": "~20 Menit",
        "parameter_utama": "TDS, Fenol, PAH, Salinitas",
        "gambar": "http://googleusercontent.com/image_collection/image_retrieval/6027939878467990540_0",
        "deskripsi": "Semburan lumpur panas yang keluar dari perut bumi menggenangi area pemukiman dan industri. Selain masalah fisik volume lumpur, air lindi dan uap yang keluar dari pusat semburan menimbulkan kekhawatiran karena mengandung material geologi dalam bumi yang pekat dan bersuhu tinggi.",
        "petunjuk_lapangan": [
            "🕵️‍♂️ Petunjuk 1: Suhu lumpur di pusat semburan mencapai 60°C - 100°C saat pertama kali keluar.",
            "🕵️‍♂️ Petunjuk 2: Terjadi penguapan gas-gas hidrokarbon dan sulfur ke udara yang menyebabkan sesak napas bagi warga radius 1 KM.",
            "🕵️‍♂️ Petunjuk 3: Air yang merembes dari tanggul lumpur masuk ke sumur galian milik warga sekitar dan mengubah rasa air menjadi asin."
        ],
        "data_lab": {
            "Suhu Air Rembesan": {"nilai": 42, "normal": "Suhu Kamar (~27°C)", "status": "Tinggi (Polusi Termal)"},
            "TDS (Total Dissolved Solids)": {"nilai": 24000, "normal": "< 1000 mg/L", "status": "Sangat Tinggi (Sifat Salin)"},
            "Kandungan Fenol": {"nilai": 3.2, "normal": "< 0.002 mg/L", "status": "Sangat Beracun"},
            "PAH (Polycyclic Aromatic Hydrocarbons)": {"nilai": 0.85, "normal": "Baku Mutu Nol", "status": "Berbahaya (Karsinogen)"}
        },
        "pertanyaan": "Karakteristik Kimia Lingkungan apa yang paling mendominasi cairan luapan Lumpur Lapindo sehingga berbahaya bagi air tanah warga jika terjadi kebocoran tanggul?",
        "pilihan": [
            "Tingginya kandungan senyawa organik buatan seperti pestisida DDT.",
            "Tingginya kadar salinitas (TDS) karena pengaruh formasi geologi air purba (connate water) serta adanya senyawa organik aromatik beracun seperti Fenol dan PAH.",
            "Tingginya kandungan bakteri E.coli akibat pencemaran tinja massal."
        ],
        "jawaban_benar": "Tingginya kadar salinitas (TDS) karena pengaruh formasi geologi air purba (connate water) serta adanya senyawa organik aromatik beracun seperti Fenol dan PAH.",
        "edukasi": "Analisis Detektif: Lumpur Lapindo membawa material dari formasi bawah tanah dalam yang kaya akan garam terlarut (membuat nilai TDS ekstrem tinggi mirip air laut). Selain itu, karena berasal dari formasi batuan induk hidrokarbon, lumpur ini membawa senyawa organik alami beracun seperti Fenol dan PAH (Polycyclic Aromatic Hydrocarbons) yang berbahaya karena dapat mencemari air tanah dangkal melalui proses pelindian (leaching) jika sistem tanggul bocor."
    }
}

# --- SIDEBAR (IDENTITAS, RADIO MUSIK & SKOR) ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #f39c12; font-family:\"Special Elite\"'>🕵️‍♂️ Markas Pusat</h2>", unsafe_allow_html=True)
    st.write("Gunakan analisis kimia terbaikmu untuk menyeret pelaku pencemaran ke pengadilan hijau!")
    st.write("---")
    
    player_name = st.text_input("Nama Agen Detektif:", "Detektif Anonim")
    
    # Fitur Interaktif Tambahan: Audio Suara Latar Simulasi (Radio Komunikasi)
    st.markdown("🎵 **Radio Komunikasi Agen:**")
    audio_type = st.radio("Aktifkan Efek Atmosfer Suara Lingkungan:", ["Mati", "Frekuensi Statis/Radio Polisi"], index=0)
    if audio_type == "Frekuensi Statis/Radio Polisi":
        # Menggunakan file audio statis ringan sebagai sound effect investigasi
        st.audio("https://www.soundjay.com/buttons/sounds/button-10.mp3", format="audio/mp3", autoplay=True)
        st.caption("🔊 *Efek radio aktif saat menu berinteraksi!*")
        
    st.write("---")
    st.metric(label="📊 Skor Penyelidikan Anda", value=f"{st.session_state.game_score} PTS")
    
    # Progress Penyelidikan Nasional
    progress_val = len(st.session_state.completed_cases) / len(CASES)
    st.write("🚀 **Progress Kasus Selesai:**")
    st.progress(progress_val)
    st.caption(f"{len(st.session_state.completed_cases)} dari {len(CASES)} berkas berhasil ditutup.")
    
    if st.button("🔄 Reset Semua Data"):
        st.session_state.current_case = None
        st.session_state.unlocked_clues = []
        st.session_state.lab_analyzed = False
        st.session_state.game_score = 0
        st.session_state.game_over = False
        st.session_state.completed_cases = []
        st.rerun()

# --- HALAMAN UTAMA (GAMEPLAY) ---
st.markdown("<div class='report-title'>🕵️‍♂️ CHEM DETECTIVE INDONESIA</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>CRIME SCENE INVESTIGATION: ENVIRONMENTAL CHEMISTRY EDITION</div>", unsafe_allow_html=True)

# FASE 1: PAPAN KASUS UTAMA INTERAKTIF
if st.session_state.current_case is None:
    st.markdown("<h3 class='case-board-title'>📌 PAPAN INVESTIGASI KASUS NASIONAL</h3>", unsafe_allow_html=True)
    st.write("Pilih salah satu berkas rahasia di bawah ini untuk memulai investigasi laboratorium:")
    
    # Menampilkan kasus dalam susunan kolom interaktif dengan indikator gaming
    for case_name, case_data in CASES.items():
        # Cek status kelulusan kasus
        is_completed = case_name in st.session_state.completed_cases
        status_badge = "✅ SELESAI" if is_completed else "⚠️ OPEN CASE"
        badge_color = "#28a745" if is_completed else "#d35400"
        
        # Grid layout untuk kartu kasus
        col_info, col_btn = st.columns([4, 1])
        
        with col_info:
            st.markdown(f"""
            <div class='interactive-card'>
                <span class='case-badge' style='background-color: {badge_color};'>{status_badge}</span>
                <span class='case-badge' style='background-color: #2980b9; margin-left: 5px;'>ID: {case_data['id']}</span>
                <h3 style='margin-top: 10px; color: #ecf0f1;'>{case_name}</h3>
                <p style='color: #bdc3c7; font-size: 14px; margin-bottom: 5px;'>📍 <strong>Lokasi Kejadian:</strong> {case_data['lokasi']}</p>
                <p style='color: #f1c40f; font-size: 14px; margin-bottom: 5px;'>📊 <strong>Tingkat Kesulitan:</strong> {case_data['kesulitan']} | ⏱️ <strong>Estimasi Uji:</strong> {case_data['durasi']}</p>
                <p style='color: #1abc9c; font-size: 14px;'>🔬 <strong>Fokus Parameter:</strong> <code>{case_data['parameter_utama']}</code></p>
            </div>
            """, unsafe_allow_html=True)
            
        with col_btn:
            st.write(" ")
            st.write(" ")
            st.write(" ")
            if is_completed:
                if st.button("🔎 Tinjau Ulang", key=f"btn_{case_data['id']}"):
                    st.session_state.current_case = case_name
                    st.session_state.unlocked_clues = case_data['petunjuk_lapangan'] # Buka semua jika sudah selesai
                    st.session_state.lab_analyzed = True
                    st.session_state.game_over = True
                    st.rerun()
            else:
                if st.button("🚀 Selidiki Kasus", key=f"btn_{case_data['id']}", type="primary"):
                    st.session_state.current_case = case_name
                    st.session_state.unlocked_clues = []
                    st.session_state.lab_analyzed = False
                    st.session_state.game_over = False
                    st.rerun()

# FASE 2: WORKSPACE DETEKTIF (KASUS BERJALAN)
else:
    case_title = st.session_state.current_case
    case_info = CASES[case_title]
    
    if st.button("⬅️ Kembali ke Papan Utama"):
        st.session_state.current_case = None
        st.rerun()
        
    st.markdown(f"### 📑 Berkas Aktif: {case_title}")
    
    # Layout Interaktif Dashboard
    col_text, col_img = st.columns([3, 2])
    with col_text:
        st.info(f"**Laporan TKP:** {case_info['deskripsi']}")
    with col_img:
        st.image(case_info['gambar'], use_container_width=True, caption=f"Bukti Foto Udara di {case_info['lokasi']}")
    
    # TAB INTERAKSI GAMEPLAY YANG DINAMIS
    tab1, tab2, tab3 = st.tabs(["🔍 1. Analisis Lapangan (TKP)", "🔬 2. Laboratorium Pengujian", "⚖️ 3. Pengadilan Hijau"])
    
    # --- TAB 1 ---
    with tab1:
        st.markdown("#### 🚨 Kumpulkan Sampel & Bukti Fisik")
        st.write("Cari petunjuk penting dengan memeriksa 3 area kritis di bawah ini:")
        
        col_b1, col_b2, col_b3 = st.columns(3)
        with col_b1:
            if st.button("📍 Periksa Titik Pembuangan (Hulu)", use_container_width=True):
                if case_info['petunjuk_lapangan'][0] not in st.session_state.unlocked_clues:
                    st.session_state.unlocked_clues.append(case_info['petunjuk_lapangan'][0])
                    st.toast("Petunjuk 1 Berhasil Ditemukan!", icon="🔍")
        with col_b2:
            if st.button("📍 Periksa Badan Air (Hilir)", use_container_width=True):
                if case_info['petunjuk_lapangan'][1] not in st.session_state.unlocked_clues:
                    st.session_state.unlocked_clues.append(case_info['petunjuk_lapangan'][1])
                    st.toast("Petunjuk 2 Berhasil Ditemukan!", icon="🔍")
        with col_b3:
            if st.button("📍 Wawancara Komunitas Lokal", use_container_width=True):
                if case_info['petunjuk_lapangan'][2] not in st.session_state.unlocked_clues:
                    st.session_state.unlocked_clues.append(case_info['petunjuk_lapangan'][2])
                    st.toast("Petunjuk 3 Berhasil Ditemukan!", icon="🔍")
        
        st.write("---")
        st.write("📦 **Koper Bukti Fisik Anda:**")
        if st.session_state.unlocked_clues:
            for clue in st.session_state.unlocked_clues:
                st.markdown(f"<div class='clue-box'>{clue}</div>", unsafe_allow_html=True)
        else:
            st.warning("Koper bukti kosong. Klik tombol area investigasi di atas!")

    # --- TAB 2 ---
    with tab2:
        st.markdown("#### 🧪 Hasil Analisis Instrumentasi Kimia")
        
        if not st.session_state.lab_analyzed:
            if st.button("⚡ Ekstraksi Sampel & Jalankan Kalibrasi Alat", type="primary"):
                progress_bar = st.progress(0)
                for percent_complete in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(percent_complete + 1)
                st.session_state.lab_analyzed = True
                st.rerun()
        else:
            st.success("💻 Monitor Laboratorium Mengonfirmasi Data Selesai Diekstrak!")
            
            # Tampilan Grid Metric Parameter Kimia
            lab_data = case_info['data_lab']
            cols = st.columns(len(lab_data))
            for i, (param, detail) in enumerate(lab_data.items()):
                with cols[i]:
                    is_danger = "Normal" not in detail['status']
                    st.metric(
                        label=param, 
                        value=detail['nilai'], 
                        delta=detail['status'], 
                        delta_color="inverse" if is_danger else "normal"
                    )
            
            # Tabel perbandingan baku mutu komprehensif
            st.write(" ")
            table_rows = [{"Parameter": p, "Hasil Sampel": d['nilai'], "Baku Mutu": d['normal'], "Status": d['status']} for p, d in lab_data.items()]
            st.table(pd.DataFrame(table_rows))

    # --- TAB 3 ---
    with tab3:
        st.markdown("#### ⚖️ Ajukan Tuntutan Hukum")
        
        # Validasi kecukupan data agar interaktif (Mahasiswa tidak bisa asal tebak)
        if not st.session_state.lab_analyzed or len(st.session_state.unlocked_clues) < 2:
            st.error("🔒 Akses Dikunci! Anda belum mengumpulkan bukti lapangan (minimal 2 petunjuk) dan belum melakukan uji instrumen laboratorium di Tab 2.")
        elif st.session_state.game_over:
            st.success("🔓 Berkas Kasus Ini Telah Selesai Disidangkan!")
            st.markdown(f"<div class='clue-box' style='border-left-color: #28a745;'><strong>💡 Edukasi Ilmiah Kasus:</strong><br>{case_info['edukasi']}</div>", unsafe_allow_html=True)
        else:
            st.write(case_info['pertanyaan'])
            with st.form(key="decision_form"):
                user_choice = st.radio("Pilih Kesimpulan Hukum Berdasarkan Logika Parameter Kimia:", case_info['pilihan'])
                submit_button = st.form_submit_button(label="⚖️ Ketok Palu Hakim (Kirim Bukti)")
                
                if submit_button:
                    if user_choice == case_info['jawaban_benar']:
                        st.balloons()
                        st.success("🎉 BERKAS BERHASIL DI-TUTUP! Analisis parameter kimia Anda 100% akurat dan diakui hukum!")
                        st.session_state.game_score += 100
                        if case_title not in st.session_state.completed_cases:
                            st.session_state.completed_cases.append(case_title)
                        st.session_state.game_over = True
                        st.rerun()
                    else:
                        st.error("❌ ARGUMEN LEMAH! Pengacara terdakwa berhasil mematahkan tuduhan Anda karena interpretasi zat kimia tidak sesuai data laboratorium. Skor berkurang 25 PTS.")
                        st.session_state.game_score -= 25
                        st.rerun()
