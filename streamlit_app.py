import streamlit as st
import random

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Praktik Kimia Organik", layout="wide", page_icon="🧪")

# --- DATA MATERI & PERCOBAAN (MENU 1 & 2) ---
MATERI = {
    "Ceric Ammonium Nitrat": {
        "prinsip": "Mengidentifikasi adanya gugus fungsi alkohol.",
        "reaksi": "$$R-OH + (NH_4)_2Ce(NO_3)_6 \\rightarrow [Ce(NO_3)_5(ROH)]^- + 2NH_4^+ + NO_3^-$$",
        "alat_bahan": "Tabung reaksi, pipet tetes, reagen Ceric Ammonium Nitrat, sampel.",
        "cara_kerja": "1. Masukkan 1 mL reagen ke tabung reaksi.\n2. Tambahkan 4-5 tetes sampel.\n3. Guncang dan amati perubahan warna.",
        "positif": "Perubahan warna dari kuning menjadi merah/merah muda menunjukkan adanya alkohol.",
        "kuis": [
            {"tanya": "Uji Ceric Ammonium Nitrat digunakan untuk mengidentifikasi gugus apa?", "opsi": ["Alkohol", "Karbonil", "Asam Karboksilat", "Ester"], "jawab": "Alkohol"},
            {"tanya": "Apa warna positif dari uji Ceric Nitrat?", "opsi": ["Merah/Merah Muda", "Cermin Perak", "Endapan Merah Bata", "Hijau/Biru"], "jawab": "Merah/Merah Muda"}
        ]
    },
    "Pereaksi Jones": {
        "prinsip": "Oksidasi alkohol primer dan sekunder menjadi asam karboksilat/keton, serta membedakannya dari alkohol tersier.",
        "reaksi": "$$3R-CH_2OH + 4CrO_3 + 12H^+ \\rightarrow 3R-COOH + 4Cr^{3+} + 9H_2O$$",
        "alat_bahan": "Tabung reaksi, pereaksi Jones ($CrO_3$ dalam $H_2SO_4$), aseton.",
        "cara_kerja": "1. Larutkan sampel dalam aseton.\n2. Tambahkan 1-2 tetes pereaksi Jones.\n3. Amati perubahan warna dalam 2 detik.",
        "positif": "Terbentuknya warna hijau atau biru-hijau (pembentukan $Cr^{3+}$). Alkohol tersier tetap jingga.",
        "kuis": [
            {"tanya": "Senyawa mana yang memberikan hasil NEGATIF (tetap jingga) pada uji Jones?", "opsi": ["t-butil alkohol", "1-butanol", "2-butanol", "Formaldehida"], "jawab": "t-butil alkohol"}
        ]
    },
    # Catatan: Sisa 7 pereaksi lainnya (Lucas, Iodoform, Na-Bisulfit, Schiff, Fehling, Hidroksilamin, Barit) 
    # dapat ditambahkan di sini dengan struktur dict yang sama.
}

# --- DATA GAME (MENU 3) ---
SENYAWA_LIST = ["Heksana", "1-butanol", "2-butanol", "t-butil alkohol", "Formaldehida", "Aseton", "Asam asetat", "Etil asetat"]

# Contoh Logika Alur Bagan Kerja Sederhana (Sesuaikan dengan foto baganmu nanti)
# Format: jika sampel X diuji dengan Y, hasilnya apa?
LOGIKA_BAGAN = {
    "Heksana": {"Ceric Ammonium Nitrat": "Negatif (Kuning)", "Pereaksi Jones": "Negatif (Jingga)"},
    "1-butanol": {"Ceric Ammonium Nitrat": "Positif (Merah)", "Pereaksi Jones": "Positif (Hijau)", "Pereaksi Lucas": "Negatif/Sangat Lambat"},
    "2-butanol": {"Ceric Ammonium Nitrat": "Positif (Merah)", "Pereaksi Jones": "Positif (Hijau)", "Pereaksi Lucas": "Positif (Keruh dalam 5-10 menit)"},
    "t-butil alkohol": {"Ceric Ammonium Nitrat": "Positif (Merah)", "Pereaksi Jones": "Negatif (Jingga)", "Pereaksi Lucas": "Positif Cepat (Keruh seketika)"},
    "Formaldehida": {"Pereaksi Schiff": "Positif (Ungu/Magenta)", "Pereaksi Fehling": "Positif (Endapan Merah Bata)"},
    "Aseton": {"Pereaksi Schiff": "Negatif", "Pereaksi Fehling": "Negatif", "Uji Iodoform": "Positif (Endapan Kuning)"},
    "Asam asetat": {"Uji barit": "Positif (Kekeruhan/Endapan)", "Ceric Ammonium Nitrat": "Negatif"},
    "Etil asetat": {"Hidroksilamin": "Positif (Warna Magenta/Merah Lembayung)", "Ceric Ammonium Nitrat": "Negatif"}
}

# --- INISIALISASI SESSION STATE ---
if 'menu' not in st.session_state:
    st.session_state.menu = "Beranda"
if 'game_started' not in st.session_state:
    st.session_state.game_started = False

# --- SIDEBAR NAVIGASI ---
with st.sidebar:
    st.title("🧪 Lab Organik")
    st.write("Aplikasi Identifikasi Senyawa")
    st.write("---")
    if st.button("🏠 Beranda", use_container_width=True): st.session_state.menu = "Beranda"
    if st.button("📚 Menu 1: Materi Pembelajaran", use_container_width=True): st.session_state.menu = "Materi"
    if st.button("🎯 Menu 2: Menentukan Senyawa", use_container_width=True): st.session_state.menu = "Kuis Percobaan"
    if st.button("🕵️‍♂️ Menu 3: Sampel Misterius", use_container_width=True): st.session_state.menu = "Game Misteri"

# ==============================================================================
# 🏠 HALAMAN: BERANDA
# ==============================================================================
if st.session_state.menu == "Beranda":
    st.title("Selamat Datang di Web Aplikasi Praktik Kimia Organik!")
    st.markdown("""
    Aplikasi ini dirancang khusus untuk membantumu menguasai analisis kualitatif identifikasi **8 Gugus Fungsi Senyawa Organik**:
    * *Heksana, 1-butanol, 2-butanol, t-butil alkohol, Formaldehida, Aseton, Asam asetat, dan Etil asetat.*
    
    ### Fitur Utama:
    1. **Materi Pembelajaran:** Pelajari prinsip, reaksi kimia, cara kerja, dan hasil pengamatan dari 9 jenis uji identifikasi.
    2. **Menentukan Senyawa Organik:** Uji pemahaman materi dan praktikmu per metode uji lewat kuis interaktif.
    3. **Mengidentifikasi Senyawa Organik Misterius:** Rasakan sensasi menjadi detektif kimia! Selesaikan teka-teki sampel misterius berdasarkan alur bagan kerja laboratorium. Hati-hati, kamu hanya punya 3 nyawa!
    """)

# ==============================================================================
# 📚 HALAMAN: MENU 1 (MATERI)
# ==============================================================================
elif st.session_state.menu == "Materi":
    st.title("📚 Materi Pembelajaran (9 Percobaan)")
    
    pilihan_uji = st.selectbox("Pilih Jenis Percobaan:", list(MATERI.keys()) + ["Pereaksi Lucas", "Uji Iodoform", "Pereaksi Na-Bisulfit", "Pereaksi Schiff", "Pereaksi Fehling", "Hidroksilamin", "Uji barit"])
    
    if pilihan_uji in MATERI:
        data = MATERI[pilihan_uji]
        
        tab1, tab2, tab3, tab4 = st.tabs(["💡 Prinsip & Reaksi", "🛠️ Alat & Bahan", "📝 Cara Kerja", "🔍 Hasil Pengamatan"])
        
        with tab1:
            st.subheader("Prinsip Analisis")
            st.write(data["prinsip"])
            st.subheader("Persamaan Reaksi")
            st.markdown(data["reaksi"])
            
        with tab2:
            st.subheader("Alat & Bahan")
            st.write(data["alat_bahan"])
            
        with tab3:
            st.subheader("Cara Kerja / Prosedur")
            st.info(data["cara_kerja"])
            
        with tab4:
            st.subheader("Uji Positif")
            st.success(data["positif"])
    else:
        st.warning("Data untuk uji ini belum diinput penuh di kode. Silakan lengkapi dictionary `MATERI`.")

# ==============================================================================
# 🎯 HALAMAN: MENU 2 (KUIS PERCOBAAN)
# ==============================================================================
elif st.session_state.menu == "Kuis Percobaan":
    st.title("🎯 Uji Pemahaman Percobaan")
    
    percobaan_terpilih = st.selectbox("Pilih Percobaan yang Ingin Diuji:", list(MATERI.keys()))
    tipe_kuis = st.radio("Pilih Tipe Evaluasi:", ["Uji Pemahaman Materi (Prinsip & Reaksi)", "Uji Pemahaman Praktik (Cara Kerja)"])
    
    st.write("---")
    st.subheader(f"Pertanyaan untuk {percobaan_terpilih} ({tipe_kuis})")
    
    if percobaan_terpilih in MATERI:
        kuis_list = MATERI[percobaan_terpilih]["kuis"]
        
        for i, kuis in enumerate(kuis_list):
            st.write(f"**Soal {i+1}:** {kuis['tanya']}")
            jawaban_user = st.radio(f"Pilih jawaban untuk soal {i+1}:", kuis["opsi"], key=f"kuis_{percobaan_terpilih}_{i}")
            
            if st.button(f"Cek Jawaban Soal {i+1}", key=f"btn_{percobaan_terpilih}_{i}"):
                if jawaban_user == kuis["jawab"]:
                    st.success("🎉 Benar sekali!")
                else:
                    st.error(f"❌ Salah. Jawaban yang benar adalah: {kuis['jawab']}")
            st.write("")

# ==============================================================================
# 🕵️‍♂️ HALAMAN: MENU 3 (GAME MISTERI)
# ==============================================================================
elif st.session_state.menu == "Game Misteri":
    st.title("🕵️‍♂️ Mengidentifikasi Senyawa Organik Misterius")
    
    # Tombol Mulai / Reset Game
    if not st.session_state.game_started:
        if st.button("Mulai Game Baru 🚀"):
            st.session_state.sampel_rahasia = random.choice(SENYAWA_LIST)
            st.session_state.nyawa = 3
            st.session_state.log_uji = []
            st.session_state.game_over = False
            st.session_state.game_won = False
            st.session_state.game_started = True
            st.rerun()
            
    if st.session_state.game_started:
        # Tampilkan Status Game
        col1, col2 = st.columns([2, 1])
        
        with col2:
            st.metric(label="Sisa Nyawa (Kesempatan Salah)", value=st.session_state.nyawa)
            st.write("**Riwayat Pengujianmu:**")
            if not st.session_state.log_uji:
                st.caption("Belum ada pengujian.")
            for log in st.session_state.log_uji:
                st.text(log)
        
        with col1:
            st.subheader("Uji Sampel Kamu")
            st.info("Petunjuk: Amati foto bagan kerja yang kamu miliki, lalu pilih uji yang valid untuk mengerucutkan dugaan senyawa!")
            
            # --- BAGIAN UNTUK BAGAN KERJA (UPLOAD FOTO/GAMBAR) ---
            # Kamu bisa meletakkan file foto bagan kerja di folder yang sama lalu panggil pakai:
            # st.image("bagan_kerja.png", caption="Panduan Alur Bagan Kerja")
            st.caption("[Tempat Gambar/Foto Bagan Kerja Anda]") 
            
            if not st.session_state.game_over and not st.session_state.game_won:
                # 1. Pilih Langkah Uji
                pilihan_uji_game = st.selectbox(
                    "Pilih Pereaksi / Uji Kimia sesuai Bagan:", 
                    ["Ceric Ammonium Nitrat", "Pereaksi Jones", "Pereaksi Lucas", "Uji Iodoform", "Pereaksi Na-Bisulfit", "Pereaksi Schiff", "Pereaksi Fehling", "Hidroksilamin", "Uji barit"]
                )
                
                if st.button("Lakukan Pengujian 🧪"):
                    senyawa_aktif = st.session_state.sampel_rahasia
                    
                    # Cek apakah uji ini ada di logika bagan untuk senyawa rahasia tersebut
                    if senyawa_aktif in LOGIKA_BAGAN and pilihan_uji_game in LOGIKA_BAGAN[senyawa_aktif]:
                        hasil_reaksi = LOGIKA_BAGAN[senyawa_aktif][pilihan_uji_game]
                        st.session_state.log_uji.append(f"✔️ {pilihan_uji_game}: {hasil_reaksi}")
                        st.success(f"Hasil Pengujian: **{hasil_reaksi}**")
                    else:
                        # Jika uji tidak sesuai alur bagan kerja/tidak memberikan hasil konklusif untuk senyawa tersebut (salah jalur bagan)
                        st.session_state.nyawa -= 1
                        st.session_state.log_uji.append(f"❌ {pilihan_uji_game}: Salah Jalur/Uji Tidak Sesuai Bagan!")
                        st.error("Uji yang kamu pilih salah atau tidak sesuai rute alur bagan kerja!")
                        
                        if st.session_state.nyawa <= 0:
                            st.session_state.game_over = True
                        st.rerun()
                
                st.write("---")
                # 2. Tebak Senyawa Akhir
                st.subheader("Kesimpulan Akhir")
                tebakan = st.selectbox("Jika sudah yakin, tebak nama senyawanya:", ["-- Pilih Senyawa --"] + SENYAWA_LIST)
                
                if st.button("Kirim Jawaban Akhir 🏁"):
                    if tebakan == st.session_state.sampel_rahasia:
                        st.session_state.game_won = True
                        st.rerun()
                    else:
                        st.session_state.nyawa -= 1
                        st.error("Tebakanmu salah!")
                        if st.session_state.nyawa <= 0:
                            st.session_state.game_over = True
                        st.rerun()

            # --- KONDISI AKHIR GAME ---
            if st.session_state.game_won:
                st.balloons()
                st.success(f"🎉 Selamat! Kamu berhasil mengidentifikasi bahwa sampel misterius tersebut adalah **{st.session_state.sampel_rahasia}**!")
                if st.button("Main Lagi"): st.session_state.game_started = False; st.rerun()
                
            elif st.session_state.game_over:
                st.error(f"💀 Game Over! Kamu kehabisan nyawa. Sampel misterius yang asli adalah **{st.session_state.sampel_rahasia}**.")
                if st.button("Coba Lagi"): st.session_state.game_started = False; st.rerun()
