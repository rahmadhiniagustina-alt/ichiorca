import streamlit as st
import pandas as pd

# ==========================
# KONFIGURASI
# ==========================
st.set_page_config(
    page_title="Chem Detective Indonesia",
    page_icon="🕵️",
    layout="wide"
)

# ==========================
# SESSION STATE
# ==========================
if "score" not in st.session_state:
    st.session_state.score = 0

if "buyat_selesai" not in st.session_state:
    st.session_state.buyat_selesai = False

if "lapindo_selesai" not in st.session_state:
    st.session_state.lapindo_selesai = False

# ==========================
# SIDEBAR
# ==========================
st.sidebar.title("🕵️ Chem Detective")

st.sidebar.metric(
    "🏆 Skor",
    st.session_state.score
)

menu = st.sidebar.radio(
    "Menu",
    [
        "🏠 Beranda",
        "🎮 Investigasi",
        "🧪 Laboratorium",
        "📚 Basis Data Kasus",
        "🏆 Pencapaian",
        "👥 Tentang Kami"
    ]
)

# ==========================
# BERANDA
# ==========================
if menu == "🏠 Beranda":

    st.title("🕵️ Chem Detective Indonesia")

    st.write("""
    Game edukasi berbasis kasus pencemaran lingkungan di Indonesia.

    Pemain berperan sebagai analis kimia yang bertugas
    menginterpretasikan data laboratorium untuk menemukan
    penyebab suatu kasus pencemaran lingkungan.
    """)

    st.info("""
    Cocok digunakan sebagai media pembelajaran
    Kimia Lingkungan bagi mahasiswa Analisis Kimia.
    """)

# ==========================
# INVESTIGASI
# ==========================
elif menu == "🎮 Investigasi":

    kasus = st.selectbox(
        "Pilih Kasus",
        [
            "Teluk Buyat",
            "Lumpur Lapindo"
        ]
    )

    # ==================================
    # TELUK BUYAT
    # ==================================
    if kasus == "Teluk Buyat":

        st.header("🐟 Misteri Ikan yang Menghilang")

        progress = st.progress(0)

        st.write("""
        Nelayan mengeluhkan hasil tangkapan ikan
        yang semakin menurun.
        """)

        petunjuk = st.slider(
            "Jumlah Petunjuk",
            1,
            3,
            1
        )

        if petunjuk >= 1:
            progress.progress(33)
            st.info("pH air normal")

        if petunjuk >= 2:
            progress.progress(66)
            st.info("Kandungan Merkuri (Hg) tinggi")

        if petunjuk >= 3:
            progress.progress(100)
            st.info("Lokasi dekat kawasan pertambangan")

        jawaban = st.radio(
            "Sumber pencemaran yang paling mungkin:",
            [
                "Limbah rumah tangga",
                "Aktivitas pertambangan",
                "Limbah deterjen"
            ]
        )

        if st.button("Pecahkan Kasus Buyat"):

            if jawaban == "Aktivitas pertambangan":

                if not st.session_state.buyat_selesai:
                    st.session_state.score += 100
                    st.session_state.buyat_selesai = True

                st.success("🎉 Benar!")

                st.write("""
                Kandungan merkuri yang tinggi
                mengarah pada aktivitas pertambangan.
                """)

            else:
                st.error("Jawaban belum tepat.")

    # ==================================
    # LAPINDO
    # ==================================
    elif kasus == "Lumpur Lapindo":

        st.header("🌋 Desa yang Tenggelam")

        progress = st.progress(0)

        st.write("""
        Sebuah desa mengalami semburan lumpur
        dalam jumlah besar.
        """)

        petunjuk = st.slider(
            "Jumlah Petunjuk ",
            1,
            3,
            1,
            key="lapindo"
        )

        if petunjuk >= 1:
            progress.progress(33)
            st.info("COD tinggi")

        if petunjuk >= 2:
            progress.progress(66)
            st.info("Terdapat H₂S")

        if petunjuk >= 3:
            progress.progress(100)
            st.info("Dekat lokasi pengeboran")

        jawaban = st.radio(
            "Penyebab yang paling mungkin:",
            [
                "Limbah rumah tangga",
                "Aktivitas pengeboran",
                "Limbah deterjen"
            ],
            key="jawaban_lapindo"
        )

        if st.button("Pecahkan Kasus Lapindo"):

            if jawaban == "Aktivitas pengeboran":

                if not st.session_state.lapindo_selesai:
                    st.session_state.score += 100
                    st.session_state.lapindo_selesai = True

                st.success("🎉 Benar!")

                st.write("""
                Data menunjukkan hubungan dengan
                aktivitas pengeboran dan semburan lumpur.
                """)

            else:
                st.error("Jawaban belum tepat.")

# ==========================
# LABORATORIUM
# ==========================
elif menu == "🧪 Laboratorium":

    st.title("🧪 Laboratorium")

    df = pd.DataFrame(
        {
            "Parameter":[
                "pH",
                "COD",
                "BOD",
                "Nitrat",
                "Fosfat",
                "Merkuri"
            ],
            "Kegunaan":[
                "Menentukan keasaman",
                "Beban pencemar kimia",
                "Beban pencemar organik",
                "Indikator nutrien",
                "Indikator eutrofikasi",
                "Logam berat berbahaya"
            ]
        }
    )

    st.dataframe(
        df,
        use_container_width=True
    )

# ==========================
# BASIS DATA
# ==========================
elif menu == "📚 Basis Data Kasus":

    st.title("📚 Basis Data Kasus")

    with st.expander("Teluk Buyat"):

        st.write("""
        Kasus yang sering dikaitkan dengan
        pencemaran logam berat di lingkungan perairan.
        """)

    with st.expander("Lumpur Lapindo"):

        st.write("""
        Semburan lumpur panas yang memberikan
        dampak lingkungan dan sosial.
        """)

# ==========================
# PENCAPAIAN
# ==========================
elif menu == "🏆 Pencapaian":

    st.title("🏆 Pencapaian")

    if st.session_state.score >= 100:
        st.success("🥉 Rookie Detective")

    if st.session_state.score >= 200:
        st.success("🥈 Environmental Investigator")

    if (
        st.session_state.buyat_selesai
        and st.session_state.lapindo_selesai
    ):
        st.success("🥇 Master Chem Detective")
        st.balloons()

# ==========================
# TENTANG KAMI
# ==========================
elif menu == "👥 Tentang Kami":

    st.title("👥 Tentang Kami")

    st.write("""
    Chem Detective Indonesia merupakan media
    pembelajaran interaktif berbasis game
    untuk membantu mahasiswa memahami
    penerapan Kimia Lingkungan melalui
    studi kasus pencemaran lingkungan.
    """)

    st.write("Kelompok : 8")
    st.write("Program Studi : Analisis Kimia")
