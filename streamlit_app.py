import streamlit as st
import pandas as pd
import os

# =====================================
# KONFIGURASI
# =====================================

st.set_page_config(
    page_title="Chem Detective Indonesia",
    page_icon="🕵️",
    layout="wide"
)

# =====================================
# SESSION STATE
# =====================================

if "score" not in st.session_state:
    st.session_state.score = 0

if "lives" not in st.session_state:
    st.session_state.lives = 3

if "completed_cases" not in st.session_state:
    st.session_state.completed_cases = []

# =====================================
# LEADERBOARD
# =====================================

if not os.path.exists("leaderboard.csv"):
    pd.DataFrame(
        columns=["Nama", "Skor"]
    ).to_csv(
        "leaderboard.csv",
        index=False
    )

# =====================================
# DATA KASUS
# =====================================

cases = {

    "Teluk Buyat": {

        "image": "assets/buyat.jpg",

        "investigation1": [
            "Hasil tangkapan ikan menurun drastis",
            "Beberapa ikan ditemukan mati"
        ],

        "investigation2": [
            "Kandungan Merkuri tinggi",
            "pH normal"
        ],

        "investigation3": [
            "Kawasan pertambangan",
            "Kawasan pertanian",
            "Permukiman warga"
        ],

        "location_answer": "Kawasan pertambangan",

        "final_options": [
            "Limbah rumah tangga",
            "Aktivitas pertambangan",
            "Deterjen"
        ],

        "correct": "Aktivitas pertambangan",

        "explanation":
        "Merkuri yang tinggi mengarah pada pencemaran akibat aktivitas pertambangan."
    },

    "Lumpur Lapindo": {

        "image": "assets/lapindo.jpg",

        "investigation1": [
            "Muncul lumpur dalam jumlah besar",
            "Air sumur berbau menyengat"
        ],

        "investigation2": [
            "COD tinggi",
            "Terdapat H₂S"
        ],

        "investigation3": [
            "Kawasan pertanian",
            "Aktivitas pengeboran gas dan minyak",
            "Tempat pembuangan sampah"
        ],

        "location_answer":
        "Aktivitas pengeboran gas dan minyak",

        "final_options": [
            "Limbah rumah tangga",
            "Aktivitas pengeboran bawah tanah dan semburan lumpur",
            "Deterjen"
        ],

        "correct":
        "Aktivitas pengeboran bawah tanah dan semburan lumpur",

        "explanation":
        "Kasus mengarah pada semburan lumpur yang berkaitan dengan aktivitas pengeboran."
    },

    "Sungai Citarum": {

        "image": "assets/citarum.jpg",

        "investigation1": [
            "Air sungai berwarna hitam",
            "Bau kimia menyengat"
        ],

        "investigation2": [
            "COD tinggi",
            "pH basa"
        ],

        "investigation3": [
            "Pabrik tekstil",
            "Peternakan ayam",
            "Permukiman"
        ],

        "location_answer":
        "Pabrik tekstil",

        "final_options": [
            "Limbah pertanian",
            "Limbah tekstil",
            "Limbah rumah tangga"
        ],

        "correct":
        "Limbah tekstil",

        "explanation":
        "Limbah tekstil dapat mengubah warna air dan meningkatkan COD."
    },

    "Sungai Berbusa": {

        "image": "assets/detergent.jpg",

        "investigation1": [
            "Sungai dipenuhi busa",
            "Banyak ikan mati"
        ],

        "investigation2": [
            "Surfaktan tinggi",
            "Fosfat tinggi"
        ],

        "investigation3": [
            "Industri deterjen",
            "Pertambangan",
            "Perkebunan"
        ],

        "location_answer":
        "Industri deterjen",

        "final_options": [
            "Deterjen dan limbah rumah tangga",
            "Logam berat",
            "Aktivitas pengeboran"
        ],

        "correct":
        "Deterjen dan limbah rumah tangga",

        "explanation":
        "Surfaktan merupakan komponen utama deterjen."
    },

    "Danau Hijau": {

        "image": "assets/eutrofikasi.jpg",

        "investigation1": [
            "Air danau berwarna hijau",
            "Alga tumbuh sangat cepat"
        ],

        "investigation2": [
            "Nitrat tinggi",
            "Fosfat tinggi"
        ],

        "investigation3": [
            "Lahan pertanian",
            "Pabrik tekstil",
            "Pertambangan"
        ],

        "location_answer":
        "Lahan pertanian",

        "final_options": [
            "Eutrofikasi akibat pupuk pertanian",
            "Limbah tekstil",
            "Tumpahan minyak"
        ],

        "correct":
        "Eutrofikasi akibat pupuk pertanian",

        "explanation":
        "Nitrat dan fosfat tinggi menyebabkan eutrofikasi."
    }

}

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("🕵️ Chem Detective")

st.sidebar.metric(
    "🏆 Skor",
    st.session_state.score
)

st.sidebar.metric(
    "❤️ Nyawa",
    st.session_state.lives
)

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

if st.sidebar.button("🔄 Reset Game"):

    st.session_state.score = 0
    st.session_state.lives = 3
    st.session_state.completed_cases = []

    st.rerun()

# =====================================
# BERANDA
# =====================================

if menu == "🏠 Beranda":

    st.title("🕵️ Chem Detective Indonesia")

    try:
        st.image(
            "assets/indonesia_map.png",
            width="stretch"
        )
    except:
        st.warning("Tambahkan gambar peta Indonesia.")

    st.markdown("""
    ## Selamat Datang Detektif!

    Pecahkan berbagai kasus pencemaran lingkungan di Indonesia.
    """)

# =====================================
# INVESTIGASI
# =====================================

elif menu == "🎮 Investigasi":

    kasus = st.selectbox(
        "Pilih Kasus",
        list(cases.keys())
    )

    c = cases[kasus]

    try:
        st.image(
            c["image"],
            width="stretch"
        )
    except:
        pass

    st.subheader("🔍 Investigasi 1")

    for i in c["investigation1"]:
        st.write("•", i)

    st.subheader("🧪 Investigasi 2")

    for i in c["investigation2"]:
        st.write("•", i)

    st.subheader("📍 Investigasi 3")

    lokasi = st.radio(
        "Lokasi yang paling mencurigakan",
        c["investigation3"]
    )

    st.subheader("📝 Kesimpulan")

    jawaban = st.radio(
        "Apa penyebab yang paling mungkin?",
        c["final_options"]
    )

    if st.button("Pecahkan Kasus"):

        if (
            lokasi == c["location_answer"]
            and
            jawaban == c["correct"]
        ):

            st.success("🎉 Kasus berhasil dipecahkan!")

            st.write(c["explanation"])

            if kasus not in st.session_state.completed_cases:

                st.session_state.completed_cases.append(
                    kasus
                )

                st.session_state.score += 100

        else:

            st.session_state.lives -= 1

            st.error(
                f"❌ Salah! Nyawa tersisa {st.session_state.lives}"
            )

# =====================================
# LABORATORIUM
# =====================================

elif menu == "🧪 Laboratorium":

    st.title("🧪 Laboratorium")

    df = pd.DataFrame({

        "Parameter":
        ["pH","COD","BOD","Nitrat","Fosfat","Merkuri"],

        "Fungsi":[
            "Keasaman",
            "Pencemar kimia",
            "Pencemar organik",
            "Nutrien",
            "Nutrien",
            "Logam berat"
        ]
    })

    st.dataframe(df)

# =====================================
# LEADERBOARD
# =====================================

elif menu == "🏆 Leaderboard":

    st.title("🏆 Leaderboard")

    nama = st.text_input("Nama")

    if st.button("Simpan Skor"):

        data = pd.read_csv("leaderboard.csv")

        data.loc[len(data)] = [
            nama,
            st.session_state.score
        ]

        data.to_csv(
            "leaderboard.csv",
            index=False
        )

        st.success("Skor berhasil disimpan!")

    data = pd.read_csv("leaderboard.csv")

    data = data.sort_values(
        by="Skor",
        ascending=False
    )

    st.dataframe(data)

# =====================================
# PENCAPAIAN
# =====================================

elif menu == "🥇 Pencapaian":

    st.title("🥇 Pencapaian")

    score = st.session_state.score

    if score >= 100:
        st.success("🥉 Rookie Detective")

    if score >= 300:
        st.success("🥈 Environmental Investigator")

    if score >= 500:

        st.success(
            "🥇 Master Chem Detective"
        )

        st.balloons()

# =====================================
# ABOUT
# =====================================

elif menu == "👥 Tentang Kami":

    st.title("👥 Tentang Kami")

    st.write("""
    Chem Detective Indonesia adalah media pembelajaran
    berbasis game investigasi pencemaran lingkungan.

    Kelompok 8
    Program Studi Analisis Kimia
    """)
