import streamlit as st
import pandas as pd

# ==========================================
# KONFIGURASI HALAMAN & THEME CUSTOMIZATION
# ==========================================
st.set_page_config(page_title="ModulDigital-Oxy", page_icon="🧪", layout="wide")

# CSS Custom untuk mengubah background menjadi terang, warna hijau-biru, font judul, dan style card
st.markdown("""
    <style>
    /* Mengubah font judul utama agar lebih menarik */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700;900&display=swap');
    
    .main-title {
        font-family: 'Poppins', sans-serif;
        font-weight: 900;
        background: -webkit-linear-gradient(45deg, #2E7D32, #1565C0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 45px;
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Style untuk Kartu Alat & Bahan (Menu 2) */
    .alat-card {
        background-color: #FFFFFF;
        border-left: 5px solid #2E7D32;
        border-right: 1px solid #E0E0E0;
        border-top: 1px solid #E0E0E0;
        border-bottom: 1px solid #E0E0E0;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        transition: transform 0.2s;
    }
    .alat-card:hover {
        transform: scale(1.02);
        border-left: 5px solid #1565C0;
    }
    
    /* Mengubah warna teks tombol bawaan streamlit agar lebih kontras */
    div.stButton > button:first-child {
        background-color: #2E7D32;
        color: white;
        border-radius: 8px;
        border: none;
    }
    div.stButton > button:first-child:hover {
        background-color: #1565C0;
        color: white;
    }
    </style>
""", unsafe_allowed_html=True)

# Inisialisasi Session State
if "sim_step_do" not in st.session_state: st.session_state.sim_step_do = 1
if "sim_step_bod" not in st.session_state: st.session_state.sim_step_bod = 1
if "sim_step_cod" not in st.session_state: st.session_state.sim_step_cod = 1

# ==========================================
# 1. NAVIGATION BAR DI BAGIAN ATAS (TOP BAR)
# ==========================================
# Menggunakan st.columns untuk membuat barisan menu horizontal di atas seperti di video
st.markdown("<h1 class='main-title'>🌿 ModulDigital-Oxy 💧</h1>", unsafe_allowed_html=True)

menu_cols = st.columns(7)
with menu_cols[0]: menu_home = st.button("🏠 Home", use_container_width=True)
with menu_cols[1]: menu_teori = st.button("📚 Teori", use_container_width=True)
with menu_cols[2]: menu_alat = st.button("🧪 Alat & Bahan", use_container_width=True)
with menu_cols[3]: menu_simulasi = st.button("🕹️ Simulasi", use_container_width=True)
with menu_cols[4]: menu_kalkulator = st.button("🧮 Kalkulator", use_container_width=True)
with menu_cols[5]: menu_interpretasi = st.button("📊 Interpretasi", use_container_width=True)
with menu_cols[6]: menu_kuis = st.button("🎮 Kuis & Evaluasi", use_container_width=True)

# Mengatur menu aktif berdasarkan tombol yang ditekan (default ke Home)
if "current_menu" not in st.session_state:
    st.session_state.current_menu = "Home"

if menu_home: st.session_state.current_menu = "Home"
elif menu_teori: st.session_state.current_menu = "Teori"
elif menu_alat: st.session_state.current_menu = "Alat"
elif menu_simulasi: st.session_state.current_menu = "Simulasi"
elif menu_kalkulator: st.session_state.current_menu = "Kalkulator"
elif menu_interpretasi: st.session_state.current_menu = "Interpretasi"
elif menu_kuis: st.session_state.current_menu = "Kuis"

st.markdown("---")

# ==========================================
# DISPLAY ISI MENU BERDASARKAN NAVIGASI ATAS
# ==========================================

# --- HOME ---
if st.session_state.current_menu == "Home":
    st.markdown("### 👋 Selamat Datang di ModulDigital-Oxy!")
    st.markdown("""
    Aplikasi ini dirancang sebagai platform edukasi digital interaktif untuk memahami analisis kualitas air berdasarkan tiga parameter utama laboratorium:
    * 💧 **DO** *(Dissolved Oxygen)*
    * 🌱 **BOD** *(Biochemical Oxygen Demand)*
    * 🔥 **COD** *(Chemical Oxygen Demand)*
    
    Silakan klik menu di bagian atas untuk mulai menjelajahi modul praktikum virtual ini! ✨
    """)
    st.success("🎉 **Yuk Mulai!** Pilih menu **📚 Teori** atau **🧪 Alat & Bahan** di atas untuk memulai pembelajaranmu!")

# --- MENU 1: TEORI ---
elif st.session_state.current_menu == "Teori":
    st.markdown("### 📚 Menu 1 — Teori Utama & Reaksi Kimia")
    tab_do, tab_bod, tab_cod = st.tabs(["💧 Uji DO (Winkler)", "🌱 Uji BOD", "🔥 Uji COD"])
    
    with tab_do:
        st.markdown("#### **Uji DO (Dissolved Oxygen) – Metode Winkler**")
        st.write("✨ **Prinsip:** Jumlah iodin yang terbentuk sebanding dengan jumlah oksigen terlarut dalam sampel.")
        st.markdown("""
        * **a. Pembentukan endapan mangan(II) hidroksida** $$\\text{MnSO}_4 + 2\\text{KOH} \\rightarrow \\text{Mn(OH)}_2\\downarrow + \\text{K}_2\\text{SO}_4$$
        * **b. Oksidasi mangan oleh oksigen terlarut** $$2\\text{Mn(OH)}_2 + \\text{O}_2 \\rightarrow 2\\text{MnO(OH)}_2\\downarrow \\text{ (Endapan Cokelat)}$$
        * **c. Pembebasan iodin dalam suasana asam** $$\\text{MnO(OH)}_2 + 2\\text{I}^- + 4\\text{H}^+ \\rightarrow \\text{Mn}^{2+} + \\text{I}_2 + 3\\text{H}_2\\text{O}$$
        * **d. Titrasi iodin dengan natrium tiosulfat** $$\\text{I}_2 + 2\\text{Na}_2\\text{S}_2\\text{O}_3 \\rightarrow 2\\text{NaI} + \\text{Na}_2\\text{S}_4\\text{O}_6$$
        """)

    with tab_bod:
        st.markdown("#### **Uji BOD (Biochemical Oxygen Demand)**")
        st.write("✨ **Prinsip:** Mikroorganisme menggunakan oksigen terlarut untuk menguraikan bahan organik selama inkubasi 5 hari.")
        st.markdown("""
        $$\\text{Bahan Organik} + \\text{O}_2 \\xrightarrow{\\text{Mikroorganisme}} \\text{CO}_2 + \\text{H}_2\\text{O} + \\text{Energi}$$
        *Contoh Sederhana:* $$\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\rightarrow 6\\text{CO}_2 + 6\\text{H}_2\\text{O}$$
        """)

    with tab_cod:
        st.markdown("#### **Uji COD (Chemical Oxygen Demand)**")
        st.write("✨ **Prinsip:** Senyawa organik dioksidasi oleh kalium dikromat ($\text{K}_2\text{Cr}_2\text{O}_7$) dalam suasana asam pekat.")
        st.markdown("""
        * **a. Oksidasi bahan organik oleh dikromat** $$\\text{Bahan Organik} + \\text{Cr}_2\\text{O}_7^{2-} + \\text{H}^+ \\rightarrow \\text{CO}_2 + \\text{H}_2\\text{O} + \\text{Cr}^{3+} \\text{ (Perubahan Jingga ke Hijau)}$$
        * **b. Titrasi sisa dikromat dengan FAS** $$\\text{Cr}_2\\text{O}_7^{2-} + 6\\text{Fe}^{2+} + 14\\text{H}^+ \\rightarrow 2\\text{Cr}^{3+} + 6\\text{Fe}^{3+} + 7\\text{H}_2\\text{O}$$
        """)

# --- MENU 2: ALAT DAN BAHAN (MODEL KARTU INTERAKTIF) ---
elif st.session_state.current_menu == "Alat":
    st.markdown("### 🧪 Menu 2 — Alat & Bahan Laboratorium (Interactive Cards)")
    st.write("✨ *Klik pada nama alat untuk melihat fungsi lengkap dan cara penggunaannya!*")
    
    pilihan_uji = st.selectbox("Pilih Parameter Uji:", ["Uji DO", "Uji BOD", "Uji COD"])
    
    # Data Alat dan Bahan
    data_alat = {
        "Uji DO": [
            {"nama": "Botol DO/BOD (300 mL)", "ikon": "🍾", "fungsi": "Menampung sampel air tanpa kontak udara luar.", "cara": "Isi sampel perlahan lewat dinding botol sampai meluap, lalu tutup rapat tanpa menyisakan gelembung."},
            {"nama": "Buret & Statif", "ikon": "🧪", "fungsi": "Meneteskan larutan standard Na₂S₂O₃ secara akurat.", "cara": "Isi buret dengan titran, sejajarkan meniskus bawah pada skala nol, lalu lakukan titrasi perlahan."},
            {"nama": "Pipet Volumetrik", "ikon": "🧪", "fungsi": "Mengambil volume reagen pengikat secara tepat.", "cara": "Gunakan pipet pump untuk menarik cairan reagen tepat pada garis tanda batas volume."}
        ],
        "Uji BOD": [
            {"nama": "Inkubator BOD (20°C)", "ikon": "📦", "fungsi": "Menjaga kondisi suhu optimum inkubasi mikroba.", "cara": "Masukkan botol BOD yang telah diukur DO awalnya, atur suhu alat pada 20°C, simpan selama 5 hari dalam kondisi gelap."},
            {"nama": "Botol BOD Terkalibrasi", "ikon": "🍾", "fungsi": "Wadah inkubasi sampel bebas kontaminasi luar.", "cara": "Tutup botol rapat-rapat dan tambahkan sedikit air pada bagian leher botol sebagai segel cairan hidrostatik."}
        ],
        "Uji COD": [
            {"nama": "Kondensor & Labu Refluks", "ikon": "⚗️", "fungsi": "Wadah destruksi sampel dan mengembunkan kembali uap asam.", "cara": "Pasang labu refluks di bawah kondensor aliran air dingin, pastikan sambungan erat agar uap tidak bocor."},
            {"nama": "Hot Plate Pemanas", "ikon": "♨️", "fungsi": "Memberikan energi panas konstan selama proses refluks.", "cara": "Nyalakan hot plate, atur suhu sesuai prosedur, dan panaskan campuran selama 2 jam kontinu."},
            {"nama": "Batu Didih", "ikon": "🪨", "fungsi": "Mencegah letupan mendadak (bumping) saat pemanasan.", "cara": "Masukkan 2-3 butir batu didih ke dalam labu sebelum pemanasan dimulai."}
        ]
    }
    
    # Menampilkan Alat dalam bentuk Card Kolom Komponen
    cols = st.columns(3)
    for index, item in enumerate(data_alat[pilihan_uji]):
        with cols[index % 3]:
            st.markdown(f"""
            <div class='alat-card'>
                <h3>{item['ikon']} {item['nama']}</h3>
                <p><b>Fungsi:</b> {item['fungsi']}</p>
            </div>
            """, unsafe_allowed_html=True)
            with st.expander(f"🔍 Lihat Cara Penggunaan {item['nama']}"):
                st.write(item['cara'])

# --- MENU 3: SIMULASI INTERAKTIF SAJA ---
elif st.session_state.current_menu == "Simulasi":
    st.markdown("### 🕹️ Menu 3 — Simulasi Laboratorium Virtual Interaktif")
    
    pilihan_sim = st.selectbox("Pilih Jenis Simulasi:", ["Simulasi 1: Pengujian DO", "Simulasi 2: Pengujian BOD5", "Simulasi 3: Pengujian COD"])
    
    if pilihan_sim == "Simulasi 1: Pengujian DO":
        st.subheader("💧 Virtual Lab: Uji DO Metode Winkler")
        
        if st.session_state.sim_step_do == 1:
            st.markdown("🪐 **Langkah 1: Pengambilan Sampel**")
            if st.button("Isi Botol DO dengan Sampel Air"):
                st.warning("⚠️ **Peringatan:** Pastikan tidak ada gelembung udara di dalam botol!")
                st.session_state.sim_step_do = 2
                st.slots = st.rerun()
                
        elif st.session_state.sim_step_do == 2:
            st.markdown("🪐 **Langkah 2: Ikat Oksigen**")
            if st.button("Tambahkan 2 mL MnSO₄ & Alkali Iodida-Azida"):
                st.success("💥 **Efek Visual:** Terbentuk endapan cokelat di dasar botol!")
                st.session_state.sim_step_do = 3
                st.rerun()
                
        elif st.session_state.sim_step_do == 3:
            st.markdown("🪐 **Langkah 3: Asidifikasi**")
            if st.button("Tambahkan 2 mL H₂SO₄ Pekat"):
                st.success("✨ **Efek Visual:** Endapan larut! Larutan berubah menjadi kuning kecokelatan.")
                st.session_state.sim_step_do = 4
                st.rerun()
                
        elif st.session_state.sim_step_do == 4:
            st.markdown("🪐 **Langkah 4: Titrasi**")
            v_titran = st.number_input("Masukkan Volume Hasil Titrasi Na₂S₂O₃ (mL):", min_value=0.0, value=7.0)
            if st.button("Selesaikan Titrasi"):
                st.balloons()
                st.success(f"🎉 **Sukses!** Proses titrasi selesai. Sila cek hasil perhitungan di Menu Kalkulator.")
                if st.button("Ulangi Simulasi 🔄"):
                    st.session_state.sim_step_do = 1
                    st.rerun()

    # (Simulasi BOD & COD diringkas agar hanya menyisakan alur tombol interaktif instan serupa)
    elif pilihan_sim == "Simulasi 2: Pengujian BOD5":
        st.subheader("🌱 Virtual Lab: Pengujian BOD₅")
        if st.button("Mulai Inkubasi Virtual 5 Hari Terkendali (20°C, Gelap) ⏳"):
            st.snow()
            st.success("✨ **Inkubasi Selesai!** DO akhir hari ke-5 siap diukur di Menu Kalkulator.")
            
    elif pilihan_sim == "Simulasi 3: Pengujian COD":
        st.subheader("🔥 Virtual Lab: Destruksi COD")
        if st.button("Jalankan Refluks Campuran K₂Cr₂O₇ + Ag₂SO₄ Selama 2 Jam ♨️"):
            st.toast("Proses pemanasan berlangsung...", icon="🔥")
            st.success("💥 **Efek Visual:** Warna larutan sukses berubah dari Oranye menjadi Hijau teroksidasi!")

# --- MENU 4: KALKULATOR ---
elif st.session_state.current_menu == "Kalkulator":
    st.markdown("### 🧮 Menu 4 — Kalkulator Parameter Otomatis")
    tab1, tab2, tab3 = st.tabs(["Kalkulator DO", "Kalkulator BOD₅", "Kalkulator COD"])
    
    with tab1:
        v_do = st.number_input("Volume Titran Na₂S₂O₃ (mL):", min_value=0.0, value=7.0, key="c_vdo")
        n_do = st.number_input("Normalitas Na₂S₂O₃ (N):", min_value=0.000, value=0.025, format="%.4f", key="c_ndo")
        vs_do = st.number_input("Volume Sampel Air (mL):", min_value=1.0, value=200.0, key="c_vsdo")
        if st.button("Hitung DO ✨"):
            res = (v_do * n_do * 8000) / vs_do
            st.metric("Hasil Konsentrasi DO", f"{res:.2f} mg/L")
            
    with tab2:
        do0 = st.number_input("DO Awal Hari ke-0 (mg/L):", min_value=0.0, value=8.2)
        do5 = st.number_input("DO Akhir Hari ke-5 (mg/L):", min_value=0.0, value=4.0)
        fp = st.number_input("Faktor Pengenceran (Isi 1 jika murni):", min_value=1, value=1)
        if st.button("Hitung BOD₅ ✨"):
            res = (do0 - do5) * fp
            st.metric("Hasil Konsentrasi BOD₅", f"{res:.2f} mg/L")
            
    with tab3:
        v_a = st.number_input("Volume FAS Blanko (mL):", min_value=0.0, value=20.0)
        v_b = st.number_input("Volume FAS Sampel (mL):", min_value=0.0, value=12.0)
        n_fas = st.number_input("Normalitas FAS (N):", min_value=0.000, value=0.100, format="%.4f")
        vs_cod = st.number_input("Volume Sampel yang Direfluks (mL):", min_value=1.0, value=50.0)
        if st.button("Hitung COD ✨"):
            res = ((v_a - v_b) * n_fas * 8000) / vs_cod
            st.metric("Hasil Konsentrasi COD", f"{res:.2f} mg/L")

# --- MENU 5: INTERPRETASI HASIL ---
elif st.session_state.current_menu == "Interpretasi":
    st.markdown("### 📊 Menu 5 — Interpretasi Hasil & Kategori Baku Mutu")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("💧 **Baku Mutu DO**\n* > 6: Sangat Baik 😊\n* 4 - 6: Baik 👍\n* 2 - 4: Tercemar Sedang ⚠️\n* < 2: Tercemar Berat 🚨")
    with col2:
        st.warning("🌱 **Baku Mutu BOD**\n* < 3: Bersih 😊\n* 3 - 6: Tercemar Ringan 🟡\n* 6 - 12: Tercemar Sedang 🟠\n* > 12: Tercemar Berat 🚨")
    with col3:
        st.error("🔥 **Baku Mutu COD**\n* < 25: Air Bersih 😊\n* 25 - 50: Tercemar Ringan 🟡\n* 50 - 100: Tercemar Sedang 🟠\n* > 100: Tercemar Berat 🚨")

# --- MENU 6: KUIS & EVALUASI ---
elif st.session_state.current_menu == "Kuis":
    st.markdown("### 🎮 Menu 6 — Kuis Evaluasi Interaktif")
    nama = st.text_input("Nama Praktikan:", placeholder="Ketik nama di sini...")
    
    st.markdown("---")
    q1 = st.radio("1. Apa fungsi utama dari pengujian analisis parameter DO?", ["Mengukur jumlah mikroba", "Mengukur kadar oksigen terlarut dalam air", "Mengukur konsentrasi asam sulfat"])
    
    if st.button("Kirim Jawaban & Evaluasi Nilai 🚀"):
        st.balloons()
        if "oksigen terlarut" in q1:
            st.success(f"🎉 Selamat {nama}! Jawaban kamu betul dan mendapatkan nilai sempurna! ✨")
        else:
            st.error("❌ Jawabanmu kurang tepat, ayo coba pelajari lagi bab Teori!")

# ==========================================
# FOOTER IDENTITAS (KEMENPERIN / KELOMPOK)
# ==========================================
st.markdown("---")
st.markdown("<p style='text-align: center; color: #777;'>Built with 💚 by <b>Kelompok 8 kelas 1A</b></p>", unsafe_allowed_html=True)
