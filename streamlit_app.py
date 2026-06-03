import streamlit as st

# Config Halaman Utama
st.set_page_config(page_title="Modul Interaktif DO-BOD-COD", page_icon="📖", layout="wide")

# Inisialisasi status langkah agar berurutan
if 'langkah_belajar' not in st.session_state:
    st.session_state['langkah_belajar'] = 1

# Fungsi untuk navigasi tombol
def ke_langkah(nomor_langkah):
    st.session_state['langkah_belajar'] = nomor_langkah
    st.rerun()

# ==========================================
# SIDEBAR NAVIGATION (Panduan Menu Modul)
# ==========================================
st.sidebar.markdown("### 🗺️ Daftar Isi Modul")
pilihan = [
    "🏠 1. Pengantar & Kasus",
    "📚 2. Teori & Rumus Analisis",
    "✏️ 3. Latihan Hitung DO & BOD",
    "🔥 4. Latihan Hitung COD",
    "🏆 5. Evaluasi & Solusi IPAL"
]

# Mengunci menu radio agar user mengikuti alur langkah demi langkah
indeks_aktif = st.session_state['langkah_belajar'] - 1
menu = st.sidebar.radio("Pindah Ruang Belajar:", pilihan, index=indeks_aktif)

# ==========================================
# ALUR HALAMAN UTAMA
# ==========================================

# --- MENU 1: PENGANTAR ---
if "1." in menu:
    st.title("📖 Modul Interaktif: Analisis DO, BOD, dan COD 🌊")
    st.markdown("### *Studi Kasus Nyata: Dampak Limbah Domestik & Industri di Indonesia*")
    st.write("---")
    
    st.markdown("""
    💡 **CARA MENGGUNAKAN APLIKASI INI:**
    Modul ini dibuat untuk membantu kamu memahami parameter kimia lingkungan secara mandiri. 
    Kamu akan membaca teori, melihat data mentah laboratorium, lalu diminta **menghitung nilainya secara mandiri** sebelum dicocokkan oleh sistem.
    """)
    
    st.subheader("🕵️‍♂️ Latar Belakang Kasus: Pencemaran Sungai Citarum")
    st.write(
        "Sungai Citarum pernah dinobatkan sebagai salah satu sungai paling tercemar di dunia. "
        "Campuran antara limbah organik domestik (rumah tangga) dan limbah kimia dari industri tekstil "
        "membuat kadar oksigen terlarut anjlok drastis. Untuk membuktikannya secara hukum, seorang Analis Kimia "
        "harus melakukan pengujian parameter utama: DO, BOD, dan COD dengan metode konvensional (Titrasi)."
    )
    
    st.write("")
    if st.button("Mulai Belajar Teori ➡️", type="primary"):
        ke_langkah(2)


# --- MENU 2: TEORI & RUMUS ---
elif "2." in menu:
    st.title("📚 Ruang Teori & Penurunan Rumus")
    st.write("Pahami prinsip dasar dan rumus konvensional berikut sebelum melakukan perhitungan.")
    st.write("---")
    
    tab1, tab2, tab3 = st.tabs(["💧 Parameter DO", "🧫 Parameter BOD", "⚗️ Parameter COD"])
    
    with tab1:
        st.markdown("### Oksigen Terlarut (DO - Dissolved Oxygen)")
        st.write("Menggunakan **Metode Winkler (Titrasi Iodometri)**. Oksigen diikat oleh $MnSO_4$ dan alkali-iodida-azida menjadi endapan cokelat, dilarutkan dengan asam, lalu iodium bebas dititrasi dengan Natrium Tiosulfat ($Na_2S_2O_3$).")
        st.info(
            "📋 **Rumus Konvensional DO:**\n\n"
            "$$DO \\text{ (mg/L)} = \\frac{V \\times N \\times 8 \\times 1000}{V_{\\text{botol}} - 4}$$"
            "\n\n*Keterangan: $V$ = Vol Tiosulfat (mL), $N$ = Normalitas Tiosulfat, $8$ = BE Oksigen, $4$ = Vol pereaksi pengikat.*"
        )
        
    with tab2:
        st.markdown("### Kebutuhan Oksigen Biokimia (BOD - Biochemical Oxygen Demand)")
        st.write("BOD menunjukkan jumlah oksigen yang dihabiskan mikroorganisme selama 5 hari inkubasi ($20^\\circ\\text{C}$) untuk menguraikan zat organik.")
        st.info(
            "📋 **Rumus Konvensional BOD₅:**\n\n"
            "$$BOD_5 \\text{ (mg/L)} = DO_0 - DO_5$$"
            "\n\n*Keterangan: $DO_0$ = DO hari ke-0, $DO_5$ = DO setelah inkubasi 5 hari.*"
        )
        
    with tab3:
        st.markdown("### Kebutuhan Oksigen Kimia (COD - Chemical Oxygen Demand)")
        st.write("Zat organik dioksidasi paksa secara kimia oleh Kalium Bikromat ($K_2Cr_2O_7$) panas, lalu sisa bikromat yang tidak bereaksi dititrasi balik (*back titration*) dengan Ferro Ammonium Sulfat (FAS) indikator Ferroin.")
        st.info(
            "📋 **Rumus Konvensional COD:**\n\n"
            "$$COD \\text{ (mg/L)} = \\frac{(V_b - V_s) \\times N_{\\text{FAS}} \\times 8 \\times 1000}{V_{\\text{sampel}}}$$"
            "\n\n*Keterangan: $V_b$ = Vol FAS Blanko (mL), $V_s$ = Vol FAS Sampel (mL), $N$ = Normalitas FAS.*"
        )

    if st.button("Lanjut ke Latihan Hitung DO & BOD ➡️", type="primary"):
        ke_langkah(3)


# --- MENU 3: LATIHAN DO & BOD ---
elif "3." in menu:
    st.title("✏️ Meja Hitung: Uji DO & BOD₅")
    st.write("Ambil kertas, pulpen, dan kalkulatormu. Hitunglah data laboratorium di bawah ini!")
    st.write("---")
    
    st.warning("📋 **Data Hasil Pengamatan Laboratorium:**\n"
               "- Volume Botol Winkler = **254 mL**\n"
               "- Normalitas Tiosulfat ($Na_2S_2O_3$) = **0.025 N**\n"
               "- Volume Tiosulfat untuk sampel Hari ke-0 ($DO_0$) = **7.2 mL**\n"
               "- Volume Tiosulfat untuk sampel Hari ke-5 ($DO_5$) = **2.1 mL**")
    
    st.markdown("#### 📝 Masukkan Hasil Hitunganmu:")
    
    # User menginputkan hasil hitungan mandirinya di sini
    user_do0 = st.number_input("1. Berapa nilai DO-0 hari? (mg/L)", min_value=0.0, step=0.01, format="%.2f")
    user_bod = st.number_input("2. Berapa nilai BOD-5 hari? (mg/L)", min_value=0.0, step=0.01, format="%.2f")
    
    # Kunci Jawaban Asli di Python (Sistem yang menghitung di latar belakang)
    kunci_do0 = (7.2 * 0.025 * 8 * 1000) / (254 - 4)  # Hasil: 5.76
    kunci_do5 = (2.1 * 0.025 * 8 * 1000) / (254 - 4)  # Hasil: 1.68
    kunci_bod = kunci_do0 - kunci_do5                 # Hasil: 4.08
    
    if st.button("🔍 Cek Jawaban DO & BOD Saya"):
        # Toleransi kesalahan desimal kecil (0.05)
        if abs(user_do0 - kunci_do0) < 0.05 and abs(user_bod - kunci_bod) < 0.05:
            st.balloons()
            st.success("🎉 **Luar Biasa! Perhitunganmu Tepat Sekali!**\n\n"
                       f"- DO_0 = {kunci_do0:.2f} mg/L\n"
                       f"- BOD_5 = {kunci_bod:.2f} mg/L")
            st.info("💡 **Pembahasan:** Air sungai memiliki DO awal yang lumayan (5.76 mg/L), tetapi dalam 5 hari bakteri menghabiskan 4.08 mg/L oksigen untuk makan polutan organik. Ini menandakan air mulai tercemar ringan-sedang.")
        else:
            st.error("❌ **Aduh, hitunganmu masih keliru.** Periksa kembali desimal atau penguranganmu, lalu coba cek lagi ya!")

    st.write("")
    if st.button("Lanjut ke Latihan COD ➡️", type="primary"):
        ke_langkah(4)


# --- MENU 4: LATIHAN COD ---
elif "4." in menu:
    st.title("🔥 Meja Hitung: Uji COD (Titrasi Balik)")
    st.write("Sekarang, mari kita uji senyawa organik yang lebih kompleks (seperti limbah industri) melalui parameter COD.")
    st.write("---")
    
    st.warning("📋 **Data Hasil Pengamatan Laboratorium:**\n"
               "- Volume Sampel Air Sungai = **50.0 mL**\n"
               "- Normalitas Larutan FAS = **0.102 N**\n"
               "- Volume FAS untuk Blanko ($V_b$) = **20.4 mL**\n"
               "- Volume FAS untuk Sampel Sungai ($V_s$) = **11.2 mL**")
    
    st.markdown("#### 📝 Masukkan Hasil Hitunganmu:")
    user_cod = st.number_input("Berapakah nilai COD sampel air sungai tersebut? (mg/L)", min_value=0.0, step=0.1, format="%.2f")
    
    # Kunci Jawaban Asli COD
    kunci_cod = ((20.4 - 11.2) * 0.102 * 8 * 1000) / 50.0 # Hasil: 150.14
    
    if st.button("🔍 Cek Jawaban COD Saya"):
        if abs(user_cod - kunci_cod) < 0.1:
            st.balloons()
            st.success(f"🎉 **Benar! Nilai COD adalah {kunci_cod:.2f} mg/L.** Kamu sukses menaklukkan matematika kimia analisis!")
            st.info("💡 **Pembahasan Analis:** Ingat konsep titrasi balik! Volume sampel ($V_s = 11.2\\text{ mL}$) jauh lebih kecil daripada blanko ($V_b = 20.4\\text{ mL}$). Artinya, sisa kalium bikromat sedikit, karena sebagian besar bikromatnya habis dipakai merusak limbah kimia industri. Makanya nilai COD-nya melonjak tinggi!")
        else:
            st.error("❌ **Jawaban belum tepat.** Pengingat rumus: ((Vol Blanko - Vol Sampel) * N * 8000) / Vol Sampel Air. Ayo hitung ulang!")

    st.write("")
    if st.button("Lanjut ke Evaluasi Akhir & Solusi ➡️", type="primary"):
        ke_langkah(5)


# --- MENU 5: EVALUASI & SOLUSI ---
elif "5." in menu:
    st.title("🏆 Evaluasi Kelayakan & Stasiun Solusi")
    st.write("Mari kita bandingkan seluruh data yang sudah dihitung dengan regulasi hukum di Indonesia.")
    st.write("---")
    
    st.markdown("### 🏛️ Regulasi Pemerintah (PP No. 22 Tahun 2021 Kelas II)")
    st.write("- Baku Mutu BOD Maksimal: **3.0 mg/L**")
    st.write("- Baku Mutu COD Maksimal: **25.0 mg/L**")
    
    st.markdown("### 📊 Ringkasan Hasil Uji Laboratorium Kita")
    st.write("- Nilai BOD Anda: **4.08 mg/L** (⚠️ Melebihi baku mutu)")
    st.write("- Nilai COD Anda: **150.14 mg/L** (🚨 Melebihi baku mutu parah)")
    
    st.write("---")
    st.markdown("### 🛠️ Tantangan IPAL: Menghitung Beban & Solusi")
    st.write("Jika industri tekstil di dekat Citarum tersebut membuang limbah dengan debit **400 $m^3$/hari**, berapa beban pencemaran COD harian yang dilepas?")
    
    user_beban = st.number_input("Hitung Beban Pencemaran COD (kg COD/hari):", min_value=0.0, step=0.1)
    kunci_beban = (150.14 * 400) / 1000 # Hasil: 60.056 kg/hari
    
    if st.button("🔍 Cek Beban Pencemaran"):
        if abs(user_beban - kunci_beban) < 0.5:
            st.success(f"✅ **Benar! Bebannya adalah {kunci_beban:.2f} kg COD/hari.**")
            
            st.markdown("#### 🌿 Rekomendasi Teknologi Pengolahan Limbah:")
            st.write("Karena kadar COD didominasi polutan industri tinggi (150.14 mg/L), metode **Fisika Sedimentasi saja tidak cukup**. Kamu disarankan menggunakan kombinasi **Koagulasi-Flokulasi Kimia** untuk mengendapkan zat warna tekstil, dilanjutkan dengan sistem **Lumpur Aktif (Biologi Aerob)** agar saat air dibuang ke Sungai Citarum nilainya sudah berada di bawah 25 mg/L.")
        else:
            st.error("❌ Beban hitunganmu masih keliru. Rumus: (Kadar COD * Debit) / 1000")
