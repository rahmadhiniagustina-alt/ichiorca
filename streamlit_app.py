import streamlit as st
import random
import pandas as pd
import time

# =========================
# KONFIGURASI HALAMAN
# =========================

st.set_page_config(
    page_title="AquaLab",
    page_icon="💧",
    layout="wide"
)

# =========================
# SESSION STATE
# =========================

if "score" not in st.session_state:
    st.session_state.score = 0

if "level" not in st.session_state:
    st.session_state.level = 1

# =========================
# SIDEBAR
# =========================

st.sidebar.title("💧 AquaLab")

menu = st.sidebar.radio(
    "Pilih Menu",
    [
        "Home",
        "Story Mode",
        "Uji DO",
        "Uji BOD",
        "Uji COD",
        "Quiz",
        "Leaderboard"
    ]
)

st.sidebar.markdown("---")
st.sidebar.metric("🏆 Score", st.session_state.score)
st.sidebar.metric("🎮 Level", st.session_state.level)

# =========================
# HOME
# =========================

if menu == "Home":

    st.title("💧 AquaLab")
    st.subheader("Water Quality Investigator")

    st.image(
        "https://images.unsplash.com/photo-1521207418485-99c705420785?q=80&w=1200&auto=format&fit=crop",
        use_container_width=True
    )

    st.markdown("""
    ## Selamat Datang di AquaLab

    Anda adalah analis laboratorium lingkungan yang bertugas menyelidiki pencemaran air menggunakan:

    - DO (Dissolved Oxygen)
    - BOD (Biochemical Oxygen Demand)
    - COD (Chemical Oxygen Demand)

    Selesaikan setiap investigasi untuk menyelamatkan lingkungan!
    """)

    st.success("Gunakan menu di sidebar untuk memulai permainan.")

# =========================
# STORY MODE
# =========================

elif menu == "Story Mode":

    st.title("🕵️ Story Mode")

    kasus = random.choice([
        "Ikan mati ditemukan di sungai dekat pabrik tekstil.",
        "Air sumur warga berubah warna menjadi coklat.",
        "Danau kota dipenuhi lumut hijau.",
        "Bau menyengat muncul dari aliran sungai."
    ])

    st.warning(f"📌 Kasus Hari Ini:\n\n{kasus}")

    pilihan = st.selectbox(
        "Pilih pengujian yang ingin dilakukan:",
        [
            "DO",
            "BOD",
            "COD",
            "Semua Pengujian"
        ]
    )

    if st.button("Mulai Investigasi"):

        st.info(f"Anda memilih pengujian: {pilihan}")

        time.sleep(1)

        st.success("Investigasi dimulai!")

        st.session_state.score += 10

# =========================
# UJI DO
# =========================

elif menu == "Uji DO":

    st.title("🧪 Uji DO")

    st.write("Simulasi pengujian Dissolved Oxygen")

    langkah = st.multiselect(
        "Pilih langkah yang benar:",
        [
            "Tambahkan MnSO4",
            "Tambahkan Alkali Iodida Azida",
            "Tambahkan H2SO4",
            "Panaskan Sampel",
            "Titrasi dengan Na2S2O3"
        ]
    )

    jawaban = {
        "Tambahkan MnSO4",
        "Tambahkan Alkali Iodida Azida",
        "Tambahkan H2SO4",
        "Titrasi dengan Na2S2O3"
    }

    if st.button("Periksa Prosedur"):

        if set(langkah) == jawaban:

            st.success("✅ Prosedur benar!")

            st.session_state.score += 20

        else:

            st.error("❌ Masih ada langkah yang salah!")

    st.markdown("---")

    st.subheader("🎯 Mini Game Titrasi")

    tetes = st.slider(
        "Atur jumlah tetesan buret",
        0,
        100,
        50
    )

    if st.button("Mulai Titrasi"):

        if 45 <= tetes <= 55:

            st.success("Titik akhir titrasi tepat!")

            st.session_state.score += 15

        else:

            st.warning("Titrasi kurang akurat!")

    st.markdown("---")

    nilai_do = random.randint(2, 10)

    if st.button("Generate Hasil DO"):

        st.metric("Nilai DO", f"{nilai_do} mg/L")

        if nilai_do < 4:

            st.error("Air tercemar!")

        else:

            st.success("Kualitas air baik")

# =========================
# UJI BOD
# =========================

elif menu == "Uji BOD":

    st.title("🧫 Uji BOD")

    st.write("Hitung kebutuhan oksigen biologis")

    do_awal = st.number_input(
        "Masukkan DO awal",
        0.0,
        20.0,
        8.0
    )

    do_akhir = st.number_input(
        "Masukkan DO akhir",
        0.0,
        20.0,
        3.0
    )

    if st.button("Hitung BOD"):

        bod = do_awal - do_akhir

        st.metric("Nilai BOD", f"{bod:.2f} mg/L")

        if bod > 5:

            st.error("Pencemaran organik tinggi!")

        else:

            st.success("Pencemaran rendah")

        st.session_state.score += 20

# =========================
# UJI COD
# =========================

elif menu == "Uji COD":

    st.title("⚗️ Uji COD")

    st.write("Analisis kandungan bahan kimia organik")

    warna = st.selectbox(
        "Pilih perubahan warna:",
        [
            "Biru",
            "Hijau",
            "Oranye",
            "Tidak berubah"
        ]
    )

    if st.button("Analisis COD"):

        nilai = random.randint(20, 300)

        st.metric("Nilai COD", f"{nilai} mg/L")

        if nilai > 100:

            st.error("Limbah kimia tinggi!")

        else:

            st.success("Kondisi air cukup baik")

        st.session_state.score += 20

# =========================
# QUIZ
# =========================

elif menu == "Quiz":

    st.title("🎯 Quiz Challenge")

    soal1 = st.radio(
        "1. Jika nilai BOD tinggi maka...",
        [
            "Air sangat bersih",
            "Banyak bahan organik",
            "Oksigen meningkat",
            "Air steril"
        ]
    )

    soal2 = st.radio(
        "2. DO digunakan untuk mengukur...",
        [
            "Kadar logam",
            "Kadar oksigen terlarut",
            "Warna air",
            "pH air"
        ]
    )

    if st.button("Submit Quiz"):

        skor = 0

        if soal1 == "Banyak bahan organik":
            skor += 10

        if soal2 == "Kadar oksigen terlarut":
            skor += 10

        st.success(f"Skor Quiz: {skor}")

        st.session_state.score += skor

# =========================
# LEADERBOARD
# =========================

elif menu == "Leaderboard":

    st.title("🏆 Leaderboard")

    data = {
        "Nama": [
            "Andi",
            "Budi",
            "Siti",
            "Rina"
        ],
        "Score": [
            120,
            100,
            90,
            80
        ]
    }

    df = pd.DataFrame(data)

    st.table(df)

    st.subheader("🎖 Achievement")

    if st.session_state.score >= 50:
        st.success("🏅 Achievement Unlocked: Water Guardian")

    if st.session_state.score >= 100:
        st.success("🏅 Achievement Unlocked: Master Analyst")

# =========================
# FOOTER
# =========================

st.markdown("---")
st.caption("💧 AquaLab - Water Quality Investigator")
