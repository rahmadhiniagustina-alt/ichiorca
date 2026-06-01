import streamlit as st
from pages.home import show_home
from pages.investigation import show_investigation
from pages.laboratory import show_laboratory
from pages.leaderboard import show_leaderboard
from pages.achievement import show_achievement
from pages.about import show_about
from utils.game_state import initialize_game

st.set_page_config(
    page_title="Chem Detective Indonesia",
    page_icon="🕵️",
    layout="wide"
)

initialize_game()

menu = st.sidebar.radio(
    "Menu",
    [
        "🏠 Beranda",
        "🎮 Investigasi",
        "🧪 Laboratorium",
        "🏆 Leaderboard",
        "🥇 Pencapaian",
        "👥 Tentang Kami"
    ]
)

st.sidebar.metric("🏆 Skor", st.session_state.score)
st.sidebar.metric("❤️ Nyawa", st.session_state.lives)

if st.sidebar.button("🔄 Reset Game"):
    st.session_state.score = 0
    st.session_state.lives = 3
    st.session_state.completed_cases = []
    st.rerun()

if menu == "🏠 Beranda":
    show_home()

elif menu == "🎮 Investigasi":
    show_investigation()

elif menu == "🧪 Laboratorium":
    show_laboratory()

elif menu == "🏆 Leaderboard":
    show_leaderboard()

elif menu == "🥇 Pencapaian":
    show_achievement()

elif menu == "👥 Tentang Kami":
    show_about()

import streamlit as st

def initialize_game():

    if "score" not in st.session_state:
        st.session_state.score = 0

    if "lives" not in st.session_state:
        st.session_state.lives = 3

    if "completed_cases" not in st.session_state:
        st.session_state.completed_cases = []

import streamlit as st

def initialize_game():

    if "score" not in st.session_state:
        st.session_state.score = 0

    if "lives" not in st.session_state:
        st.session_state.lives = 3

    if "completed_cases" not in st.session_state:
        st.session_state.completed_cases = []

import streamlit as st

def show_home():

    st.title("🕵️ Chem Detective Indonesia")

    try:
        st.image(
            "assets/indonesia_map.png",
            use_container_width=True
        )
    except:
        st.warning("Tambahkan peta Indonesia.")

    st.markdown("""
    ## Selamat Datang Detektif!

    Kamu akan menyelidiki berbagai kasus
    pencemaran lingkungan yang pernah terjadi
    di Indonesia.

    ### Misi:
    - Kumpulkan petunjuk
    - Analisis data laboratorium
    - Temukan penyebab pencemaran
    - Pecahkan seluruh kasus
    """)

    st.success("""
    🎯 Selesaikan 5 kasus untuk mendapatkan
    gelar Master Chem Detective Indonesia
    """)

import streamlit as st
from data.cases import cases

def show_investigation():

    st.title("🎮 Investigasi Kasus")

    case_name = st.selectbox(
        "Pilih Kasus",
        list(cases.keys())
    )

    case = cases[case_name]

    # Inisialisasi progress per kasus
    step_key = f"step_{case_name}"

    if step_key not in st.session_state:
        st.session_state[step_key] = 1

    step = st.session_state[step_key]

    try:
        st.image(
            case["image"],
            use_container_width=True
        )
    except:
        st.warning("Gambar belum tersedia.")

    progress = int((step / 4) * 100)

    st.progress(progress)

    # ======================
    # INVESTIGASI 1
    # ======================

    if step >= 1:

        st.subheader("🔍 Investigasi 1")

        for item in case["investigation1"]:
            st.write("•", item)

        if step == 1:

            if st.button("Lanjut Investigasi 2"):

                st.session_state[step_key] = 2
                st.rerun()

    # ======================
    # INVESTIGASI 2
    # ======================

    if step >= 2:

        st.subheader("🧪 Investigasi 2")

        for item in case["investigation2"]:
            st.write("•", item)

        if step == 2:

            if st.button("Lanjut Investigasi 3"):

                st.session_state[step_key] = 3
                st.rerun()

    # ======================
    # INVESTIGASI 3
    # ======================

    if step >= 3:

        st.subheader("📍 Investigasi 3")

        lokasi = st.radio(
            "Lokasi yang paling mencurigakan:",
            case["investigation3"]
        )

        if st.button("Periksa Lokasi"):

            if lokasi == case["location_answer"]:

                st.success("✅ Lokasi sesuai dengan bukti.")

                st.session_state[step_key] = 4
                st.rerun()

            else:

                st.session_state.lives -= 1

                st.error(
                    f"❌ Salah! Nyawa tersisa: {st.session_state.lives}"
                )

    # ======================
    # KESIMPULAN
    # ======================

    if step >= 4:

        st.subheader("📝 Kesimpulan")

        jawaban = st.radio(
            "Apa penyebab yang paling mungkin?",
            case["final_options"]
        )

        if st.button("Pecahkan Kasus"):

            if jawaban == case["correct"]:

                st.success("🎉 Kasus berhasil dipecahkan!")

                st.write(case["explanation"])

                if case_name not in st.session_state.completed_cases:

                    st.session_state.completed_cases.append(
                        case_name
                    )

                    st.session_state.score += 100

            else:

                st.session_state.lives -= 1

                st.error(
                    f"❌ Jawaban salah! Nyawa tersisa: {st.session_state.lives}"
                )

    # ======================
    # GAME OVER
    # ======================

    if st.session_state.lives <= 0:

        st.error("💀 GAME OVER")

        if st.button("Main Lagi"):

            st.session_state.lives = 3
            st.session_state.score = 0
            st.session_state.completed_cases = []

            st.rerun()

import streamlit as st
import pandas as pd

def show_laboratory():

    st.title("🧪 Laboratorium")

    data = pd.DataFrame({

        "Parameter":[
            "pH",
            "COD",
            "BOD",
            "Nitrat",
            "Fosfat",
            "Merkuri"
        ],

        "Fungsi":[
            "Menentukan tingkat keasaman",
            "Indikator pencemar kimia",
            "Indikator pencemar organik",
            "Penyebab eutrofikasi",
            "Penyebab eutrofikasi",
            "Logam berat berbahaya"
        ]
    })

    st.dataframe(
        data,
        use_container_width=True
    )

import streamlit as st
import pandas as pd
import os

def show_leaderboard():

    st.title("🏆 Leaderboard")

    if not os.path.exists("leaderboard.csv"):

        pd.DataFrame(
            columns=["Nama","Skor"]
        ).to_csv(
            "leaderboard.csv",
            index=False
        )

    nama = st.text_input(
        "Masukkan Nama"
    )

    if st.button("Simpan Skor"):

        data = pd.read_csv(
            "leaderboard.csv"
        )

        data.loc[len(data)] = [
            nama,
            st.session_state.score
        ]

        data.to_csv(
            "leaderboard.csv",
            index=False
        )

        st.success("Skor berhasil disimpan!")

    data = pd.read_csv(
        "leaderboard.csv"
    )

    data = data.sort_values(
        by="Skor",
        ascending=False
    )

    st.dataframe(
        data,
        use_container_width=True
    )

import streamlit as st
from utils.badges import get_badge

def show_achievement():

    st.title("🥇 Pencapaian")

    badge = get_badge(
        st.session_state.score
    )

    st.success(badge)

    if st.session_state.score >= 500:

        st.balloons()

        st.download_button(
            "📥 Unduh Sertifikat",
            data="""
MASTER CHEM DETECTIVE INDONESIA

Selamat!
Anda berhasil menyelesaikan
seluruh investigasi pencemaran lingkungan.
""",
            file_name="sertifikat.txt"
        )

import streamlit as st

def show_about():

    st.title("👥 Tentang Kami")

    st.write("""
    Chem Detective Indonesia adalah media
    pembelajaran interaktif yang membantu
    mahasiswa memahami kasus pencemaran
    lingkungan melalui pendekatan investigasi.
    """)

    st.subheader("Kelompok 8")

    st.write("""
    Program Studi Analisis Kimia
    """)

    st.write("""
    Dibuat untuk mata kuliah
    Kimia Lingkungan.
    """)

def get_badge(score):

    if score >= 500:
        return "🥇 Master Chem Detective"

    elif score >= 300:
        return "🥈 Environmental Investigator"

    elif score >= 100:
        return "🥉 Rookie Detective"

    return "Belum memiliki badge"

