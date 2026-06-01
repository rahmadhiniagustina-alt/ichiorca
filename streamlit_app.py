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

# --- CUSTOM CSS UNTUK TAMPILAN MENARIK ---
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f9;
    }
    .report-title {
        font-size: 32px;
        font-weight: bold;
        color: #1e3d59;
        text-align: center;
        margin-bottom: 20px;
    }
    .case-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border-left: 5px solid #17a2b8;
    }
    .clue-box {
        background-color: #e8f4f8;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #007bff;
        margin-bottom: 10px;
    }
    .success-text {
        color: #28a745;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- INITIALIZATION SESSION STATE (Penyimpanan Data Game) ---
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

# --- DATA KASUS (DATABASE KASUS NYATA INDONESIA & GAMBAR) ---
CASES = {
    "Kasus 1: Misteri Penyakit Neurologis Teluk Buyat (2004)": {
        "lokasi": "Teluk Buyat, Sulawesi Utara",
        "gambar": "http://googleusercontent.com/image_collection/image_retrieval/9183348929598449345_0",
        "deskripsi": "Masyarakat di sekitar pesisir Teluk Buyat melaporkan munculnya benjolan aneh pada kulit, sakit kepala hebat, dan gangguan fungsi saraf (neurologis). Nelayan juga melaporkan adanya kematian ikan secara mendadak di area teluk. Sebuah perusahaan pertambangan emas skala besar dituduh membuang limbah tailing-nya ke dasar laut.",
        "petunjuk_lapangan": [
            "🕵️‍♂️ Petunjuk 1: Limbah sisa pemisahan emas (tailing) dialirkan melalui pipa bawah laut pada kedalaman 82 meter.",
            "🕵️‍♂️ Petunjuk 2: Warga lokal memiliki kebiasaan mengonsumsi kerang dan ikan dasar laut (demersal) yang ditangkap langsung di teluk.",
            "🕵️‍♂️ Petunjuk 3: Hasil otopsi jaringan biologis ikan menunjukkan terjadinya kerusakan parah pada organ hati dan insang."
        ],
        "data_lab": {
            "pH": {"nilai": 8.1, "normal": "7.0 - 8.5", "status": "Normal"},
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
        "lokasi": "Daerah Aliran Sungai (DAS) Citarum, Jawa Barat",
        "gambar": "http://googleusercontent.com/image_collection/image_retrieval/13850938114624661230_0",
        "deskripsi": "Sungai Citarum sempat dinobatkan sebagai salah satu sungai paling tercemar di dunia. Di beberapa titik, air sungai berwarna hitam pekat, berbuih, dan mengeluarkan bau busuk hidrogen sulfida (H2S). Banyak industri tekstil, kertas, dan elektroplating beroperasi di sepanjang bantaran sungai.",
        "petunjuk_lapangan": [
            "🕵️‍♂️ Petunjuk 1: Banyak ditemukan 'pipa siluman' pembuangan limbah yang hanya aktif mengeluarkan air berwarna gelap di malam hari.",
            "🕵️‍♂️ Petunjuk 2: Struktur komunitas makrozoobentos (hewan dasar sungai) bergeser drastis, hanya menyisakan organisme indikator polusi berat seperti cacing Tubifex.",
            "🕵️‍♂️ Petunjuk 3: Air sungai berbau busuk tajam seperti telur busuk akibat kondisi anoksik (tanpa oksigen)."
        ],
        "data_lab": {
            "pH": {"nilai": 9.5, "normal": "6.0 - 9.0", "status": "Basa Kuat (Limbah Cuci)"},
            "BOD (Biochemical Oxygen Demand)": {"nilai": 180, "normal": "< 3 mg/L", "status": "Kritis (Sangat Tinggi)"},
            "COD (Chemical Oxygen Demand)": {"nilai": 450, "normal": "< 25 mg/L", "status": "Kritis (Sangat Tinggi)"},
            "Kromium Heksavalen (Cr6+)": {"nilai": 1.8, "normal": "< 0.05 mg/L", "status": "Sifat Karsinogenik Tinggi"},
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
        "lokasi": "Porong, Sidoarjo, Jawa Timur",
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

# --- SIDEBAR (IDENTITAS & SKOR) ---
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #1e3d59;'>🕵️‍♂️ Markas Detektif</h2>", unsafe_allow_html=True)
    st.write("Selamat datang di **Chem Detective Indonesia**. Pecahkan kasus pencemaran lingkungan nyata berdasarkan data laboratorium kimia!")
    st.write("---")
    
    player_name = st.text_input("Masukkan Nama Detektif Anda:", "Detektif Anonim")
    st.success(f"Status: **Aktif**\n\nDetektif: {player_name}")
    st.metric(label="Total Skor Penyelidikan", value=f"{st.session_state.game_score} PTS")
    
    if st.button("🔄 Reset Semua Kasus"):
        st.session_state.current_case = None
        st.session_state.unlocked_clues = []
        st.session_state.lab_analyzed = False
        st.session_state.game_score = 0
        st.session_state.game_over = False
        st.rerun()

# --- HALAMAN UTAMA (GAMEPLAY) ---
st.markdown("<div class='report-title'>🕵️‍♂️ Chem Detective Indonesia 🔬</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><em>Media Pembelajaran Interaktif Analisis Kasus Kimia Lingkungan</em></p>", unsafe_allow_html=True)
st.write("---")

# FASE 1: PEMILIHAN KASUS
if st.session_state.current_case is None:
    st.subheader("📁 Pilih Berkas Kasus yang Ingin Anda Selidiki:")
    
    col1, col2 = st.columns(2)
    
    for idx, (case_name, case_data) in enumerate(CASES.items()):
        with col1 if idx % 2 == 0 else col2:
            st.markdown(f"""
            <div class='case-card'>
                <h4>{case_name}</h4>
                <p>📍 <strong>Lokasi:</strong> {case_data['lokasi']}</p>
                <p>📋 {case_data['deskripsi'][:120]}...</p>
            </div>
            """, unsafe_allow_html=True)
            # Menampilkan thumbnail gambar kecil di menu pilihan
            st.image(case_data['gambar'], use_container_width=True, caption=f"TKP {case_data['lokasi']}")
            if st.button(f"Ambil Kasus: {case_name.split(':')[0]}", key=case_name):
                st.session_state.current_case = case_name
                st.session_state.unlocked_clues = []
                st.session_state.lab_analyzed = False
                st.session_state.game_over = False
                st.rerun()

# FASE 2: INVESTIGASI KASUS YANG DIPILIH
else:
    case_title = st.session_state.current_case
    case_info = CASES[case_title]
    
    st.button("⬅️ Kembali ke Daftar Kasus", on_click=lambda: setattr(st.session_state, 'current_case', None))
    st.markdown(f"### 📑 Sedang Diselidiki: {case_title}")
    
    # Layout Kolom: Teks Deskripsi (Kiri) dan Gambar TKP Besar (Kanan)
    col_text, col_img = st.columns([2, 1])
    with col_text:
        st.info(f"**TKP:** {case_info['lokasi']}\n\n**Deskripsi Kasus:** {case_info['deskripsi']}")
    with col_img:
        st.image(case_info['gambar'], use_container_width=True, caption=f"Foto Kondisi Lapangan {case_title.split(':')[1]}")
    
    # PEMBAGIAN TABS UNTUK INTERAKSI GAME
    tab1, tab2, tab3 = st.tabs(["🔍 1. Investigasi Lapangan", "🔬 2. Analisis Laboratorium", "⚖️ 3. Penarikan Kesimpulan"])
    
    # --- TAB 1: INVESTIGASI LAPANGAN ---
    with tab1:
        st.subheader("Kumpulkan Petunjuk di Tempat Kejadian Perkara (TKP)")
        st.write("Klik tombol di bawah ini untuk mencari petunjuk fisik di lapangan:")
        
        col_btn1, col_btn2, col_btn3 = st.columns(3)
        
        with col_btn1:
            if st.button("🔍 Cari Petunjuk 1"):
                if case_info['petunjuk_lapangan'][0] not in st.session_state.unlocked_clues:
                    st.session_state.unlocked_clues.append(case_info['petunjuk_lapangan'][0])
        with col_btn2:
            if st.button("🔍 Cari Petunjuk 2"):
                if case_info['petunjuk_lapangan'][1] not in st.session_state.unlocked_clues:
                    st.session_state.unlocked_clues.append(case_info['petunjuk_lapangan'][1])
        with col_btn3:
            if st.button("🔍 Cari Petunjuk 3"):
                if case_info['petunjuk_lapangan'][2] not in st.session_state.unlocked_clues:
                    st.session_state.unlocked_clues.append(case_info['petunjuk_lapangan'][2])
        
        st.write("---")
        st.write("📋 **Kantong Petunjuk Anda:**")
        if st.session_state.unlocked_clues:
            for clue in st.session_state.unlocked_clues:
                st.markdown(f"<div class='clue-box'>{clue}</div>", unsafe_allow_html=True)
        else:
            st.warning("Belum ada petunjuk yang ditemukan. Klik tombol investigasi di atas!")
            
    # --- TAB 2: ANALISIS LABORATORIUM ---
    with tab2:
        st.subheader("Pengujian Sampel Air & Sedimen")
        st.write("Kirim sampel air/sedimen yang ditemukan di lapangan ke laboratorium analisis lingkungan untuk melihat kadar parameternya.")
        
        if not st.session_state.lab_analyzed:
            if st.button("🧪 Jalankan Uji Spektrofotometri & Titrasi"):
                with st.spinner("Mengukur kadar pH, COD, BOD, dan Logam Berat..."):
                    time.sleep(1.5)
                st.session_state.lab_analyzed = True
                st.rerun()
        else:
            st.success("🔬 Hasil Analisis Laboratorium Keluar!")
            
            lab_data = case_info['data_lab']
            
            cols = st.columns(len(lab_data))
            for i, (param, detail) in enumerate(lab_data.items()):
                with cols[i]:
                    st.metric(
                        label=param, 
                        value=detail['nilai'], 
                        delta=detail['status'], 
                        delta_color="inverse" if "Normal" not in detail['status'] else "normal"
                    )
            
            st.write("---")
            st.write("**Tabel Perbandingan Baku Mutu Lingkungan:**")
            
            table_rows = []
            for param, detail in lab_data.items():
                table_rows.append({
                    "Parameter Chemical": param,
                    "Hasil Analisis Sampel": detail['nilai'],
                    "Standar Baku Mutu (Normal)": detail['normal'],
                    "Keterangan Status": detail['status']
                })
            
            st.table(pd.DataFrame(table_rows))
            
    # --- TAB 3: PENARIKAN KESIMPULAN ---
    with tab3:
        st.subheader("Sidang Pengadilan Lingkungan Hidup")
        
        if not st.session_state.lab_analyzed or len(st.session_state.unlocked_clues) < 2:
            st.error("❌ Anda belum mengumpulkan cukup bukti! Selesaikan Fase 1 (minimal 2 petunjuk) yard dan Fase 2 (Analisis Lab) terlebih dahulu sebelum menuduh tersangka.")
        elif st.session_state.game_over:
            st.info("Kasus ini telah selesai disidangkan. Lihat hasil analisis edukasi di bawah.")
            st.markdown(f"<div class='clue-box'><strong>Edukasi Kasus:</strong><br>{case_info['edukasi']}</div>", unsafe_allow_html=True)
        else:
            st.warning("⚠️ **Tuduhan Anda menentukan nasib ekosistem!**")
            st.write(case_info['pertanyaan'])
            
            with st.form(key="decision_form"):
                user_choice = st.radio("Pilih Jawaban Pembuktian Anda:", case_info['pilihan'])
                submit_button = st.form_submit_button(label="⚖️ Ajukan Bukti ke Pengadilan")
                
                if submit_button:
                    if user_choice == case_info['jawaban_benar']:
                        st.balloons()
                        st.success("🎉 JAWABAN BENAR! Anda berhasil membuktikan sumber pencemaran berdasarkan data kimia lingkungan!")
                        st.session_state.game_score += 100
                        st.session_state.game_over = True
                    else:
                        st.error("❌ BUKTI DITOLAK! Argumen/kesimpulan Anda tidak sesuai dengan karakteristik parameter kimia yang diuji. Coba analisis lagi.")
                        st.session_state.game_score -= 25
                    
                    st.markdown(f"<div class='clue-box'><strong>Edukasi Kasus:</strong><br>{case_info['edukasi']}</div>", unsafe_allow_html=True)
