import streamlit as st
import pandas as pd

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================
st.set_page_config(
    page_title="ModulDigital-Oxy",
    page_icon="🧪",
    layout="wide"
)

# ==========================================
# CUSTOM CSS MODERN
# ==========================================
st.markdown("""
<style>

/* Background utama */
.stApp {
    background: linear-gradient(to bottom right, #dff6ff, #e8fff1);
}

/* Navbar */
.navbar {
    background: linear-gradient(90deg, #00b4db, #00c9a7);
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 20px;
    text-align: center;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}

/* Subjudul */
.subtitle {
    text-align: center;
    color: #009688;
    font-size: 20px;
    margin-bottom: 30px;
}

/* Card Utama */
.card {
    background-color: white;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

/* Grid Grid Kecil untuk Alat & Bahan */
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 12px;
    margin-top: 10px;
    margin-bottom: 25px;
}

/* Item Kotak Alat (Biru) */
.tool-item {
    background-color: #f0f7ff;
    border-left: 5px solid #00b4db;
    padding: 12px;
    border-radius: 8px;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.04);
}

/* Item Kotak Bahan (Hijau/Teal) */
.chem-item {
    background-color: #f4fdfa;
    border-left: 5px solid #00c9a7;
    padding: 12px;
    border-radius: 8px;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.04);
}

.item-title {
    font-weight: bold;
    color: #333333;
    margin-bottom: 4px;
    font-size: 15px;
}

.item-desc {
    font-size: 13px;
    color: #666666;
    line-height: 1.4;
}

/* Footer */
.footer {
    text-align: center;
    padding: 20px;
    color: gray;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================
st.markdown("""
<div class='navbar'>
    <h1 style='color:white; margin:0;'>🧪 ModulDigital-Oxy</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Media Pembelajaran Interaktif DO, BOD, dan COD 💧</div>", unsafe_allow_html=True)

# ==========================================
# MENU ATAS
# ==========================================
menu = st.radio(
    "",
    [
        "🏠 Home",
        "📚 Teori",
        "🧪 Alat & Bahan",
        "🕹️ Simulasi",
        "🧮 Kalkulator",
        "📊 Interpretasi",
        "🎮 Kuis"
    ],
    horizontal=True
)

# ==========================================
# HOME
# ==========================================
if menu == "🏠 Home":
    st.balloons()
    st.markdown("""
    <div class='card'>
    <h2>👋 Selamat Datang!</h2>
    <p>ModulDigital-Oxy adalah media pembelajaran interaktif untuk memahami:</p>
    <ul>
        <li>💧 Dissolved Oxygen (DO)</li>
        <li>🌱 Biochemical Oxygen Demand (BOD)</li>
        <li>🔥 Chemical Oxygen Demand (COD)</li>
    </ul>
    <p>Aplikasi ini dibuat lebih modern dan interaktif agar pembelajaran laboratorium menjadi lebih menyenangkan 🎉</p>
    </div>
    """, unsafe_allow_html=True)
    st.success("✨ Yuk mulai belajar dari menu di atas!")

# ==========================================
# TEORI
# ==========================================
elif menu == "📚 Teori":
    st.markdown("<h2 style='color:#009688;'>📚 Materi Teori</h2>", unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["💧 DO", "🌱 BOD", "🔥 COD"])

    with tab1:
        st.markdown("""
        <div class='card'>
        <h3>💧 Dissolved Oxygen (DO)</h3>
        <p><b>Definisi:</b><br>Oksigen terlarut atau <i>dissolved oxygen</i> (DO) adalah elemen esensial yang dibutuhkan untuk mengoksidasi seluruh polutan yang terdapat dalam badan air baik secara kimiawi maupun secara biokimia.</p>
        <p><b>Metode Uji & Prinsip:</b><br>Nilai DO dapat diukur menggunakan metode titrimetri <b>iodometri</b> (SNI 6989:2004). Prinsipnya melibatkan proses reaksi reduksi dan oksidasi (redoks) menggunakan larutan natrium tiosulfat (Na₂S₂O₃) dengan indikator amilum.</p>
        <p><b>Persamaan Reaksi:</b><br>
        <code>Mn²⁺(aq) + 2OH⁻(aq) → Mn(OH)₂(s)</code><br>
        <code>I₂ + 2S₂O₃²⁻ —(H⁺)—> S₄O₆²⁻ + 2I⁻</code></p>
        </div>
        <div class='card'>
        <p><b>Rumus Perhitungan Nilai DO:</b></p>
        <div style='text-align: center; font-size: 18px; font-weight: bold;'>
            DO (mg/L) = (V × N × 8000 × F) / 50 mL
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown("""
        <div class='card'>
        <h3>🌱 Biochemical Oxygen Demand (BOD)</h3>
        <p><b>Definisi:</b><br>Biochemical oxygen demand (BOD) adalah salah satu parameter wajib ukur pada air limbah (SNI 6989.72:2009).</p>
        <p><b>Metode Uji & Prinsip:</b><br>Pengujian menggunakan metode Winkler melalui titrasi iodometri. Sampel diinkubasi di dalam botol winkler selama 5 hari pada suhu 20°C untuk menghitung selisih konsumsi oksigen oleh mikroorganisme.</p>
        <p><b>Persamaan Reaksi:</b><br>
        <code>Mn²⁺ + 2OH⁻ + ½ O₂ → MnO₂·H₂O (endapan coklat)</code><br>
        <code>I₂ + 2S₂O₃²⁻ → 2I⁻ + S₄O₆²⁻</code></p>
        </div>
        <div class='card'>
        <p><b>Rumus Perhitungan Nilai BOD:</b></p>
        <div style='text-align: center; font-size: 18px; font-weight: bold;'>
            BOD (mg/L) = 5 × (DO<sub>awal</sub> - DO<sub>akhir</sub>)
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown("""
        <div class='card'>
        <h3>🔥 Chemical Oxygen Demand (COD)</h3>
        <p><b>Definisi:</b><br>Chemical oxygen demand (COD) mengukur kebutuhan oksigen untuk mengoksidasi partikel organik secara kimiawi menggunakan oksidator kuat (SNI 6989:2019).</p>
        <p><b>Metode Uji & Prinsip:</b><br>Melalui teknik destruksi/refluks menggunakan Kalium Dikromat (K₂Cr₂O₇) dalam suasana asam tinggi, kemudian dititrasi kembali sisa dikromat menggunakan Ferro Ammonium Sulfate (FAS) dengan indikator ferroin.</p>
        </div>
        <div class='card'>
        <p><b>Rumus Perhitungan Nilai COD:</b></p>
        <div style='text-align: center; font-size: 18px; font-weight: bold;'>
            COD (mg/L) = [ (V<sub>blanko</sub> - V<sub>sampel</sub>) × N<sub>FAS</sub> × 8000 ] / V<sub>sampel</sub>
        </div>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# ALAT & BAHAN (FOTO DI ATAS DAFTARNYA)
# ==========================================
elif menu == "🧪 Alat & Bahan":

    st.markdown("<h2 style='color:#009688; margin-bottom:5px;'>🧪 Komponen Alat & Bahan Laboratorium</h2>", unsafe_allow_html=True)
    st.write("Silakan pilih parameter di bawah ini untuk melihat daftar alat dan bahan dengan tampilan kartu informatif.")

    pilihan_materi = st.selectbox(
        "Pilih Parameter Pengujian:",
        ["Daftar Alat & Bahan Uji DO", "Daftar Alat & Bahan Uji BOD", "Daftar Alat & Bahan Uji COD"]
    )

    # ------------------------------------------
    # SUB-BAGIAN: UJI DO
    # ------------------------------------------
    if pilihan_materi == "Daftar Alat & Bahan Uji DO":
        st.markdown("### 💧 Parameter Analisis DO (Dissolved Oxygen)")
        
        # Foto diletakkan di atas melebar penuh
        url_do = "https://github.com/user-attachments/assets/411a7412-1a3b-40e5-ab74-f1a394717e13"
        st.image(url_do, caption="Rangkaian Alat Analisis Parameter DO", use_container_width=True)

        # Konten list diletakkan di bawah foto
        st.markdown("#### 🛠️ Daftar Alat Kerja")
        st.markdown("""
        <div class='grid-container'>
            <div class='tool-item'><div class='item-title'>🔵 Botol Winkler</div><div class='item-desc'>Tempat pengambilan & fiksasi sampel air tanpa udara bebas.</div></div>
            <div class='tool-item'><div class='item-title'>🔵 Pipet Volumetrik</div><div class='item-desc'>Mengambil & menambah volume reagen (MnSO₄, alkali) secara presisi.</div></div>
            <div class='tool-item'><div class='item-title'>🔵 Buret & Statif</div><div class='item-desc'>Wadah penitar larutan standar Natrium Tiosulfat (Na₂S₂O₃).</div></div>
            <div class='tool-item'><div class='item-title'>🔵 Erlenmeyer 150mL</div><div class='item-desc'>Wadah menampung sampel air olahan selama proses titrasi berlangsung.</div></div>
            <div class='tool-item'><div class='item-title'>🔵 Gelas Ukur</div><div class='item-desc'>Mengukur volume pengenceran atau reagen kasar laboratorium.</div></div>
            <div class='tool-item'><div class='item-title'>🔵 Botol Gelap</div><div class='item-desc'>Tempat penyimpanan stok larutan yang sensitif terhadap paparan cahaya.</div></div>
            <div class='tool-item'><div class='item-title'>🔵 Pipet Tetes</div><div class='item-desc'>Membantu penambahan indikator larutan amilum secara bertahap.</div></div>
            <div class='tool-item'><div class='item-title'>🔵 Termometer</div><div class='item-desc'><i>(Opsional)</i> Digunakan untuk mendata suhu aktual awal sampel air.</div></div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### 🧪 Daftar Bahan Kimia")
        st.markdown("""
        <div class='grid-container'>
            <div class='chem-item'><div class='item-title'>🟢 Sampel Air</div><div class='item-desc'>Air limbah, sungai, atau air uji yang akan ditentukan kadar oksigennya.</div></div>
            <div class='chem-item'><div class='item-title'>🟢 Mangan Sulfat (MnSO₄)</div><div class='item-desc'>Zat kimia utama pengikat molekul oksigen terlarut alami.</div></div>
            <div class='chem-item'><div class='item-title'>🟢 Alkali Iodida Azida</div><div class='item-desc'>Pereaksi campuran (KI+NaOH+NaN₃) pembentuk senyawa kompleks iodin.</div></div>
            <div class='chem-item'><div class='item-title'>🟢 Asam Sulfat (H₂SO₄)</div><div class='item-desc'>Asam pekat untuk memberikan suasana asam & melarutkan flok endapan.</div></div>
            <div class='chem-item'><div class='item-title'>🟢 Natrium Tiosulfat</div><div class='item-desc'>Larutan standar (Na₂S₂O₃) yang bertindak selaku zat penitar (titran).</div></div>
            <div class='chem-item'><div class='item-title'>🟢 Indikator Amilum</div><div class='item-desc'>Larutan kanji penanda titik akhir titrasi (warna biru tepat hilang).</div></div>
            <div class='chem-item'><div class='item-title'>🟢 Kalium Dikromat</div><div class='item-desc'>Senyawa (K₂Cr₂O₇) standar primer untuk keperluan standardisasi titran.</div></div>
            <div class='chem-item'><div class='item-title'>🟢 Aquadest</div><div class='item-desc'>Air murni suling untuk pelarutan pereaksi dan pembersihan alat gelas.</div></div>
        </div>
        """, unsafe_allow_html=True)

    # ------------------------------------------
    # SUB-BAGIAN: UJI BOD
    # ------------------------------------------
    elif pilihan_materi == "Daftar Alat & Bahan Uji BOD":
        st.markdown("### 🌱 Parameter Analisis BOD (Biochemical Oxygen Demand)")
        
        # Foto diletakkan di atas melebar penuh
        url_bod = "https://github.com/user-attachments/assets/869acefd-cb84-49bc-81d7-9cd02cec5241"
        st.image(url_bod, caption="Rangkaian Alat Analisis Parameter BOD", use_container_width=True)

        # Konten list diletakkan di bawah foto
        st.markdown("#### 🛠️ Daftar Alat Kerja")
        st.markdown("""
        <div class='grid-container'>
            <div class='tool-item'><div class='item-title'>🔵 Botol BOD (Winkler)</div><div class='item-desc'>Wadah khusus kedap udara untuk proses inkubasi sampel h-0 dan h-5.</div></div>
            <div class='tool-item'><div class='item-title'>🔵 Inkubator 20°C</div><div class='item-desc'>Kondisi ruang stabil untuk pengeraman mikroorganisme selama 5 hari.</div></div>
            <div class='tool-item'><div class='item-title'>🔵 Buret & Statif</div><div class='item-desc'>Alat penetes larutan sekunder natrium tiosulfat dengan skala ketelitian tinggi.</div></div>
            <div class='tool-item'><div class='item-title'>🔵 Pipet Volumetrik</div><div class='item-desc'>Mengambil larutan air medium pengencer atau contoh limbah secara presisi.</div></div>
            <div class='tool-item'><div class='item-title'>🔵 Erlenmeyer 150mL</div><div class='item-desc'>Wadah penampungan titrat contoh uji guna mendeteksi titik akhir.</div></div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### 🧪 Daftar Bahan Kimia")
        st.markdown("""
        <div class='grid-container'>
            <div class='chem-item'><div class='item-title'>🟢 Air Sampel Uji</div><div class='item-desc'>Bahan uji air limbah terbagi dua fasa (Hari ke-0 dan inkubasi Hari ke-5).</div></div>
            <div class='chem-item'><div class='item-title'>🟢 Reagen Winkler</div><div class='item-desc'>Larutan MnSO₄ beserta larutan Alkali Iodida Azida pembentuk flok.</div></div>
            <div class='chem-item'><div class='item-title'>🟢 H₂SO₄ Pekat</div><div class='item-desc'>Zat pengkondisi asam ekstrem guna membebaskan molekul iodin bebas.</div></div>
            <div class='chem-item'><div class='item-title'>🟢 Larutan Na₂S₂O₃</div><div class='item-desc'>Larutan kimia penitar kuantitas kandungan oksigen terlarut sisa sediaan.</div></div>
            <div class='chem-item'><div class='item-title'>🟢 Indikator Pati</div><div class='item-desc'>Indikator kanji pemberi warna biru kompleks sebelum titik akhir dicapai.</div></div>
            <div class='chem-item'><div class='item-title'>🟢 Air Pengencer</div><div class='item-desc'>Air suling jenuh oksigen diperkaya nutrisi (bila sampel pekat).</div></div>
        </div>
        """, unsafe_allow_html=True)

    # ------------------------------------------
    # SUB-BAGIAN: UJI COD
    # ------------------------------------------
    elif pilihan_materi == "Daftar Alat & Bahan Uji COD":
        st.markdown("### 🔥 Parameter Analisis COD (Chemical Oxygen Demand)")
        
        # Foto diletakkan di atas melebar penuh
        url_cod = "https://github.com/user-attachments/assets/39987309-7194-4bd9-b1cc-8507f8fb8182"
        st.image(url_cod, caption="Rangkaian Alat Analisis Parameter COD", use_container_width=True)

        # Konten list diletakkan di bawah foto
        st.markdown("#### 🛠️ Daftar Alat Kerja")
        st.markdown("""
        <div class='grid-container'>
            <div class='tool-item'><div class='item-title'>🔵 Labu Refluks</div><div class='item-desc'>Labu alas bulat/datar tempat bertemunya reagen asam ekstrem & sampel.</div></div>
            <div class='tool-item'><div class='item-title'>🔵 Kondensor Balik</div><div class='item-desc'>Pendingin uap asam agar kembali mengembun ke bawah selama pemanasan.</div></div>
            <div class='tool-item'><div class='item-title'>🔵 Heating Mantle</div><div class='item-desc'>Alat pemanas elektrik bersuhu tinggi untuk proses digesti s/d ±150°C.</div></div>
            <div class='tool-item'><div class='item-title'>🔵 Buret Makro</div><div class='item-desc'>Tempat pengisian titran larutan FAS (Ferro Ammonium Sulfate).</div></div>
            <div class='tool-item'><div class='item-title'>🔵 Erlenmeyer 250mL</div><div class='item-desc'>Wadah titrasi sisa asam dikromat hasil destruksi yang telah dingin.</div></div>
            <div class='tool-item'><div class='item-title'>🔵 Corong & Pipet</div><div class='item-desc'>Alat pembantu pemindahan reagen kimia korosif demi keselamatan kerja.</div></div>
            <div class='tool-item'><div class='item-title'>🔵 Semprot Air</div><div class='item-desc'>Botol pembilas sisa reagen yang menempel di dinding dalam labu gelas.</div></div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("#### 🧪 Daftar Bahan Kimia")
        st.markdown("""
        <div class='grid-container'>
            <div class='chem-item'><div class='item-title'>🟢 Kalium Dikromat</div><div class='item-desc'>Senyawa (K₂Cr₂O₇) selaku oksidator utama penghancur polutan organik.</div></div>
            <div class='chem-item'><div class='item-title'>🟢 Asam Sulfat Reagen</div><div class='item-desc'>H₂SO₄ pekat pembangun suasana reaksi reduksi-oksidasi yang kuat.</div></div>
            <div class='chem-item'><div class='item-title'>🟢 Perak Sulfat (Ag₂SO₄)</div><div class='item-desc'>Zat katalisator yang mempercepat proses rusaknya rantai karbon organik.</div></div>
            <div class='chem-item'><div class='item-title'>🟢 Merkuri Sulfat</div><div class='item-desc'>HgSO₄ pengikat khusus ion klorida agar tidak menimbulkan interferensi pembacaan.</div></div>
            <div class='chem-item'><div class='item-title'>🟢 Larutan Titran FAS</div><div class='item-desc'>Ferrous Ammonium Sulfate penitar sisa dikromat yang tidak terpakai.</div></div>
            <div class='chem-item'><div class='item-title'>🟢 Indikator Ferroin</div><div class='item-desc'>Senyawa kompleks visual (perubahan warna: biru-hijau menjadi coklat-merah).</div></div>
            <div class='chem-item'><div class='item-title'>🟢 Larutan Blanko</div><div class='item-desc'>Menggunakan air bebas ion/aquadest sebagai kontrol pembanding analisis.</div></div>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# SIMULASI
# ==========================================
elif menu == "🕹️ Simulasi":
    st.markdown("<h2 style='color:#009688;'>🕹️ Simulasi Interaktif</h2>", unsafe_allow_html=True)
    simulasi = st.selectbox("Pilih Simulasi", ["💧 Simulasi DO", "🌱 Simulasi BOD", "🔥 Simulasi COD"])

    if simulasi == "💧 Simulasi DO":
        st.info("💡 Tambahkan reagen MnSO₄")
        if st.button("Tambahkan Reagen"):
            st.toast("✅ Reagen berhasil ditambahkan!")
            st.balloons()
        v = st.number_input("Masukkan Volume Titrasi", value=6.4)
        if st.button("Hitung DO"):
            hasil = (v * 0.025 * 8000) / 200
            st.success(f"🎉 Nilai DO = {hasil:.2f} mg/L")

    elif simulasi == "🌱 Simulasi BOD":
        do0 = st.number_input("DO Awal", value=8.5)
        do5 = st.number_input("DO Akhir", value=3.2)
        if st.button("Hitung BOD"):
            hasil = do0 - do5
            st.success(f"🌱 Nilai BOD = {hasil:.2f} mg/L")
            st.snow()

    elif simulasi == "🔥 Simulasi COD":
        blanko = st.number_input("Volume Blanko", value=20.0)
        sampel = st.number_input("Volume Sampel", value=12.0)
        if st.button("Hitung COD"):
            hasil = ((blanko - sampel) * 0.1 * 8000) / 50
            st.success(f"🔥 Nilai COD = {hasil:.2f} mg/L")
            st.balloons()

# ==========================================
# KALKULATOR
# ==========================================
elif menu == "🧮 Kalkulator":
    st.markdown("<h2 style='color:#009688;'>🧮 Kalkulator Otomatis</h2>", unsafe_allow_html=True)
    parameter = st.selectbox("Pilih Parameter", ["DO", "BOD", "COD"])

    if parameter == "DO":
        v = st.number_input("Volume Titran", value=7.0)
        n = st.number_input("Normalitas", value=0.025)
        vs = st.number_input("Volume Sampel", value=200.0)
        if st.button("Hitung"):
            hasil = (v * n * 8000) / vs
            st.metric("Hasil DO", f"{hasil:.2f} mg/L")

# ==========================================
# INTERPRETASI
# ==========================================
elif menu == "📊 Interpretasi":
    st.markdown("<h2 style='color:#009688;'>📊 Interpretasi Air</h2>", unsafe_allow_html=True)
    data = pd.DataFrame({
        "Kategori": ["Bersih", "Sedang", "Berat"],
        "DO": [">6", "2-6", "<2"]
    })
    st.table(data)
    st.success("🟢 Semakin tinggi DO maka kualitas air semakin baik")

# ==========================================
# KUIS
# ==========================================
elif menu == "🎮 Kuis":
    st.markdown("<h2 style='color:#009688;'>🎮 Kuis Interaktif</h2>", unsafe_allow_html=True)
    score = 0
    q1 = st.radio("Apa kepanjangan DO?", ["Dissolved Oxygen", "Digital Oxygen", "Double Oxygen"])
    if st.button("Submit Jawaban"):
        if q1 == "Dissolved Oxygen":
            score += 100
        st.success(f"🎉 Skor Kamu = {score}")
        if score == 100:
            st.balloons()

# ==========================================
# FOOTER
# ==========================================
st.markdown("""
<div class='footer'>
✨ Kelompok 8 kelas 1A ✨
</div>
""", unsafe_allow_html=True)
