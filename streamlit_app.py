import streamlit as st
import pandas as pd

# ======================================================

# KONFIGURASI HALAMAN

# ======================================================

st.set_page_config(
page_title="ModulDigital-Oxy",
page_icon="🧪",
layout="wide"
)

# ======================================================

# CUSTOM CSS

# ======================================================

st.markdown("""

<style>

.stApp{
    background: linear-gradient(to bottom right, #dff6ff, #e8fff1);
}

h1,h2,h3{
    font-family: 'Trebuchet MS', sans-serif;
}

.main-title{
    text-align:center;
    font-size:50px;
    color:#0077b6;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:#009688;
    font-size:20px;
    margin-bottom:20px;
}

.card{
    background:white;
    padding:20px;
    border-radius:20px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

.footer{
    text-align:center;
    color:gray;
    padding:20px;
    font-size:14px;
}

</style>

""", unsafe_allow_html=True)

# ======================================================

# HEADER

# ======================================================

st.markdown("<div class='main-title'>🧪 ModulDigital-Oxy</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Media Pembelajaran Interaktif DO, BOD, dan COD 💧</div>", unsafe_allow_html=True)

# ======================================================

# NAVBAR

# ======================================================

menu = st.radio(
"",
[
"🏠 Home",
"📚 Teori",
"🧪 Alat & Bahan",
"🧐 Studi Kasus",
"🧮 Kalkulator",
"📊 Interpretasi",
"🎮 Kuis"
],
horizontal=True
)

# ======================================================

# HOME

# ======================================================

if menu == "🏠 Home":

    st.balloons()

st.markdown("""
<div class='card'>
<h2>👋 Selamat Datang di ModulDigital-Oxy</h2>

<p>
ModulDigital-Oxy merupakan media pembelajaran interaktif yang dirancang untuk membantu memahami parameter kualitas air:
</p>

<ul>
<li>💧 Dissolved Oxygen (DO)</li>
<li>🌱 Biochemical Oxygen Demand (BOD)</li>
<li>🔥 Chemical Oxygen Demand (COD)</li>
</ul>

<p>
Aplikasi ini dilengkapi dengan materi teori, alat dan bahan laboratorium, studi kasus, kalkulator otomatis, interpretasi hasil, dan kuis evaluasi.
</p>
</div>
""", unsafe_allow_html=True)

st.success("✨ Selamat belajar dan semoga sukses!")

# ======================================================

# MENU 1 TEORI

# ======================================================

    elif menu == "📚 Teori":

st.title("📚 Menu 1 — Teori")

tab1, tab2, tab3 = st.tabs([
    "💧 Uji DO",
    "🌱 Uji BOD",
    "🔥 Uji COD"
])

# ======================================
# DO
# ======================================
with tab1:

    st.markdown("""
    <div class='card'>
    <h2>💧 Uji DO (Dissolved Oxygen) – Metode Winkler</h2>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Prinsip")
    st.write("""
    Jumlah iodin yang terbentuk sebanding dengan jumlah oksigen terlarut dalam sampel.
    Metode Winkler menentukan kadar oksigen terlarut melalui pembentukan iodin
    yang kemudian dititrasi dengan natrium tiosulfat.
    """)

    st.subheader("Tahapan Reaksi Kimia")

    st.write("a. Pembentukan endapan mangan(II) hidroksida")
    st.latex(r'''
    MnSO_4 + 2KOH \rightarrow Mn(OH)_2 + K_2SO_4
    ''')

    st.write("b. Oksidasi mangan oleh oksigen terlarut")
    st.latex(r'''
    2Mn(OH)_2 + O_2 \rightarrow 2MnO(OH)_2
    ''')

    st.write("c. Pembebasan iodin dalam suasana asam")
    st.latex(r'''
    MnO(OH)_2 + 2I^- + 4H^+ \rightarrow Mn^{2+} + I_2 + 3H_2O
    ''')

    st.write("d. Titrasi iodin dengan natrium tiosulfat")
    st.latex(r'''
    I_2 + 2Na_2S_2O_3 \rightarrow 2NaI + Na_2S_4O_6
    ''')

# ======================================
# BOD
# ======================================
with tab2:

    st.markdown("""
    <div class='card'>
    <h2>🌱 Uji BOD (Biochemical Oxygen Demand)</h2>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Prinsip")

    st.write("""
    Mikroorganisme menggunakan oksigen terlarut untuk menguraikan bahan organik.
    Penurunan DO selama inkubasi 5 hari digunakan untuk menghitung nilai BOD.
    """)

    st.subheader("Reaksi Umum")

    st.latex(r'''
    Bahan\ Organik + O_2 \xrightarrow{Mikroorganisme} CO_2 + H_2O + Energi
    ''')

    st.write("Contoh sederhana oksidasi glukosa")

    st.latex(r'''
    C_6H_{12}O_6 + 6O_2 \rightarrow 6CO_2 + 6H_2O
    ''')

# ======================================
# COD
# ======================================
with tab3:

    st.markdown("""
    <div class='card'>
    <h2>🔥 Uji COD (Chemical Oxygen Demand)</h2>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Prinsip")

    st.write("""
    Semakin banyak bahan organik dalam sampel,
    semakin banyak kalium dikromat yang bereaksi sehingga nilai COD semakin tinggi.
    """)

    st.subheader("Tahapan Reaksi Kimia")

    st.write("a. Oksidasi bahan organik")
    st.latex(r'''
    Bahan\ Organik + Cr_2O_7^{2-} + H^+ \rightarrow CO_2 + H_2O + Cr^{3+}
    ''')

    st.write("b. Reduksi ion dikromat")
    st.latex(r'''
    Cr_2O_7^{2-} + 14H^+ + 6e^- \rightarrow 2Cr^{3+} + 7H_2O
    ''')

    st.write("c. Titrasi sisa dikromat dengan FAS")
    st.latex(r'''
    Cr_2O_7^{2-} + 6Fe^{2+} + 14H^+ \rightarrow 2Cr^{3+} + 6Fe^{3+} + 7H_2O
    ''')

# ======================================================

# MENU 2 ALAT DAN BAHAN

# ======================================================

elif menu == "🧪 Alat & Bahan":

st.title("🧪 Menu 2 — Alat dan Bahan")

pilihan = st.selectbox(
    "Pilih Pengujian",
    ["💧 Uji DO", "🌱 Uji BOD", "🔥 Uji COD"]
)

# ======================================
# UJI DO
# ======================================
if pilihan == "💧 Uji DO":

    st.header("💧 Uji DO (Dissolved Oxygen)")
    st.subheader("Tujuan Pengujian")
    st.write("Menentukan kadar oksigen terlarut dalam sampel air menggunakan metode Winkler.")

    st.subheader("🛠️ Alat yang Digunakan")

    alat_do = {
        "Botol DO/BOD": "Menampung sampel air dan mencegah kontak udara.",
        "Buret": "Meneteskan larutan titran secara akurat.",
        "Erlenmeyer": "Wadah titrasi sampel.",
        "Pipet Volumetrik": "Mengambil volume reagen secara tepat.",
        "Gelas Ukur": "Mengukur volume larutan.",
        "Statif dan Klem": "Menopang buret saat titrasi."
    }

    for alat, fungsi in alat_do.items():
        with st.expander(f"🧪 {alat}"):
            st.write(f"Fungsi: {fungsi}")

    st.subheader("🧪 Bahan yang Digunakan")

    bahan_do = {
        "Sampel Air": "Objek yang dianalisis.",
        "MnSO₄": "Mengikat oksigen terlarut.",
        "Alkali Iodida-Azida": "Menyediakan suasana basa.",
        "H₂SO₄": "Membebaskan iodin.",
        "Na₂S₂O₃": "Larutan titrasi.",
        "Amilum": "Indikator titik akhir."
    }

    for bahan, fungsi in bahan_do.items():
        with st.expander(f"⚗️ {bahan}"):
            st.write(f"Fungsi: {fungsi}")

# ======================================
# UJI BOD
# ======================================
elif pilihan == "🌱 Uji BOD":

    st.header("🌱 Uji BOD")

    st.subheader("Tujuan Pengujian")
    st.write("Menentukan jumlah oksigen yang diperlukan mikroorganisme.")

    st.subheader("🛠️ Alat")

    alat_bod = [
        "Botol BOD 300 mL",
        "Inkubator BOD",
        "Buret",
        "Erlenmeyer",
        "Pipet Volumetrik",
        "Gelas Ukur"
    ]

    for alat in alat_bod:
        st.info(f"🧪 {alat}")

    st.subheader("🧪 Bahan")

    bahan_bod = [
        "Sampel Air",
        "Air Pengencer",
        "Larutan Buffer Fosfat",
        "MgSO₄",
        "CaCl₂",
        "FeCl₃",
        "Seed Mikroorganisme"
    ]

    for bahan in bahan_bod:
        st.success(f"⚗️ {bahan}")

# ======================================
# UJI COD
# ======================================
elif pilihan == "🔥 Uji COD":

    st.header("🔥 Uji COD")

    st.subheader("Tujuan Pengujian")
    st.write("Menentukan jumlah oksigen untuk oksidasi bahan pencemar.")

    st.subheader("🛠️ Alat")

    alat_cod = [
        "Labu Refluks",
        "Kondensor Refluks",
        "Hot Plate",
        "Buret",
        "Erlenmeyer",
        "Pipet Volumetrik",
        "Batu Didih"
    ]

    for alat in alat_cod:
        st.info(f"🧪 {alat}")

    st.subheader("🧪 Bahan")

    bahan_cod = [
        "K₂Cr₂O₇",
        "H₂SO₄",
        "Ag₂SO₄",
        "HgSO₄",
        "FAS",
        "Ferroin"
    ]

    for bahan in bahan_cod:
        st.success(f"⚗️ {bahan}")

# ======================================================

# MENU 3 STUDI KASUS

# ======================================================

elif menu == "🧐 Studi Kasus":

st.title("🧐 Studi Kasus Evaluasi Lapangan")

st.markdown("""
### Diberikan data pengujian air sungai:

- 💧 DO = 2.1 mg/L
- 🌱 BOD = 15 mg/L
- 🔥 COD = 180 mg/L
""")

q1 = st.text_input("1. Bagaimana kualitas air sampel tersebut?")
q2 = st.text_input("2. Apakah terjadi pencemaran organik?")

if st.button("Kirim Jawaban"):

    st.success("""
    ✅ Air tergolong tercemar berat.

    ✅ Terjadi pencemaran organik tinggi karena nilai BOD dan COD sangat tinggi
    sedangkan DO sangat rendah.
    """)

# ======================================================

# MENU 4 KALKULATOR

# ======================================================

elif menu == "🧮 Kalkulator":

st.title("🧮 Kalkulator Parameter")

tab1, tab2, tab3 = st.tabs([
    "💧 DO",
    "🌱 BOD",
    "🔥 COD"
])

with tab1:

    v = st.number_input("Volume Titran", value=7.0)
    n = st.number_input("Normalitas", value=0.025)
    vs = st.number_input("Volume Sampel", value=200.0)

    if st.button("Hitung DO"):
        hasil = (v*n*8000)/vs
        st.success(f"💧 DO = {hasil:.2f} mg/L")

with tab2:

    do0 = st.number_input("DO Awal", value=8.2)
    do5 = st.number_input("DO Akhir", value=4.0)

    if st.button("Hitung BOD"):
        hasil = do0-do5
        st.success(f"🌱 BOD = {hasil:.2f} mg/L")

with tab3:

    blanko = st.number_input("Volume Blanko", value=20.0)
    sampel = st.number_input("Volume Sampel", value=12.0)
    nfas = st.number_input("Normalitas FAS", value=0.1)
    vsampel = st.number_input("Volume Sampel COD", value=50.0)

    if st.button("Hitung COD"):
        hasil = ((blanko-sampel)*nfas*8000)/vsampel
        st.success(f"🔥 COD = {hasil:.2f} mg/L")

# ======================================================

# MENU 5 INTERPRETASI

# ======================================================

elif menu == "📊 Interpretasi":

st.title("📊 Interpretasi Kualitas Air")

st.subheader("💧 Parameter DO")

df_do = pd.DataFrame({
    "DO (mg/L)": [">6", "4-6", "2-4", "<2"],
    "Interpretasi": [
        "Sangat Baik",
        "Baik",
        "Tercemar Sedang",
        "Tercemar Berat"
    ]
})

st.table(df_do)

st.info("💡 DO tinggi menunjukkan kualitas air baik.")

st.subheader("🌱 Parameter BOD")

df_bod = pd.DataFrame({
    "BOD (mg/L)": ["<3", "3-6", "6-12", ">12"],
    "Interpretasi": [
        "Air Bersih",
        "Tercemar Ringan",
        "Tercemar Sedang",
        "Tercemar Berat"
    ]
})

st.table(df_bod)

st.subheader("🔥 Parameter COD")

df_cod = pd.DataFrame({
    "COD (mg/L)": ["<25", "25-50", "50-100", ">100"],
    "Interpretasi": [
        "Air Bersih",
        "Tercemar Ringan",
        "Tercemar Sedang",
        "Tercemar Berat"
    ]
})

st.table(df_cod)
```

# ======================================================

# MENU 6 KUIS

# ======================================================

elif menu == "🎮 Kuis":

st.title("🎮 Menu 6 — Kuis Evaluasi")

nama = st.text_input("Masukkan Nama Lengkap")

q1 = st.radio(
    "1. Apa fungsi utama pengukuran DO?",
    [
        "A. Mengukur jumlah mikroorganisme",
        "B. Mengukur kandungan logam berat",
        "C. Mengukur oksigen terlarut dalam air",
        "D. Mengukur pH air"
    ]
)

if st.button("Submit Jawaban"):

    skor = 0

    if q1 == "C. Mengukur oksigen terlarut dalam air":
        skor += 100

    st.success(f"🎉 Skor Anda = {skor}")

    if skor >= 80:
        st.balloons()

        st.markdown(f"""
        ## 📜 Sertifikat Kelulusan

        Diberikan kepada:

        ### {nama}

        Telah menyelesaikan pembelajaran ModulDigital-Oxy.
        """)

# ======================================================

# FOOTER

# ======================================================

st.markdown("""

<div class='footer'>
✨ Kelompok 8 kelas 1A ✨
</div>
""", unsafe_allow_html=True)
