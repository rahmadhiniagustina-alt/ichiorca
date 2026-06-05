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

/* Judul utama */
.main-title {
    font-size: 45px;
    font-weight: bold;
    text-align: center;
    color: #0077b6;
    margin-top: 10px;
    margin-bottom: 10px;
    font-family: 'Trebuchet MS', sans-serif;
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
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.01);
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
        "📋 Cara Kerja",
        "🧮 Kalkulator",
        "📊 Analisis",
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
    <p>
    ModulDigital-Oxy adalah media pembelajaran interaktif untuk memahami:
    </p>
    <ul>
        <li>💧 Dissolved Oxygen (DO)</li>
        <li>🌱 Biochemical Oxygen Demand (BOD)</li>
        <li>🔥 Chemical Oxygen Demand (COD)</li>
    </ul>
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
        <p><b>Definisi:</b><br>
        Oksigen terlarut atau <i>dissolved oxygen</i> (DO) adalah elemen esensial yang dibutuhkan untuk mengoksidasi seluruh polutan yang terdapat dalam badan air baik secara kimiawi maupun secara biokimia. Secara tidak langsung, DO juga berpengaruh pada kadar padatan tersuspensi total (<i>total suspended solids</i> / TSS) yang terkandung pada badan air.</p>
        
        <p><b>Metode Uji & Prinsip:</b><br>
        Nilai DO dapat diukur menggunakan cara konvensional melalui metode titrimetri, yakni <b>iodometri</b> seperti yang disarankan pada <b>Standar Nasional Indonesia Nomor 6989 Tahun 2004</b>. Secara prinsip, metode iodometri dilakukan dengan teknik titrasi yang melibatkan proses reaksi reduksi dan oksidasi (redoks).</p>
        
        <p>Dalam metode ini, oksigen yang terlarut dalam sampel akan bereaksi dengan ion mangan (II) dalam suasana basa sehingga menghasilkan mangan hidroksida [Mn(OH)₂] di mana zat ini akan direduksi kembali menjadi mangan (II) dengan adanya penambahan larutan iodida (I⁻) dalam suasana asam. Pertukaran elektron terjadi sehingga reaksi ini membebaskan iodin (I₂) yang akan diukur kadarnya melalui titrasi dengan natrium tiosulfat (Na₂S₂O₃) menggunakan indikator amilum.</p>
        
        <p><b>Persamaan Reaksi:</b></p>
        <p><b>Reaksi Preparasi:</b><br>
        <code style='font-size: 16px;'>Mn²⁺(aq) + 2OH⁻(aq) → Mn(OH)₂(s)</code></p>
        <br>
        <p><b>Reaksi Titrasi:</b><br>
        <code style='font-size: 16px;'>I₂ + 2S₂O₃²⁻ —(H⁺)—> S₄O₆²⁻ + 2I⁻</code></p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='card'>
        <p><b>Rumus Perhitungan Nilai DO:</b></p>
        <div style='text-align: center; font-size: 18px; font-weight: bold; padding: 10px;'>
            DO (mg/L) = <span style='border-bottom: 2px solid black; padding-bottom: 2px;'>V × N × 8000 × F</span><br>
            <span style='display: block; margin-top: 5px;'>50 mL</span>
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab2:
        st.markdown("""
        <div class='card'>
        <h3>🌱 Biochemical Oxygen Demand (BOD)</h3>
        <p><b>Definisi:</b><br>
        Biochemical oxygen demand (BOD) atau kebutuhan oksigen biologis (KOB) adalah salah satu parameter wajib ukur pada air limbah.</p>
        
        <p><b>Metode Uji & Prinsip:</b><br>
        Cara ujinya tertera pada <b>Standar Nasional Indonesia Nomor 6989 Bagian 72 Tahun 2009</b> yang diadaptasi dari <i>American Public Health Association</i> (APHA) 5210. Pengujian BOD dapat dilakukan dengan menggunakan metode Winkler yakni melalui titrasi iodometri yang merupakan metode referensi <i>United States Environmental Protection Agency</i> (USEPA).</p>
        
        <p>Secara prinsip, titrasi iodometri merupakan titrasi reduksi-oksidasi (redoks) yang menggunakan Mangan klorida (MnCl₂), Larutan kalium iodida dalam natrium hidroksida (NaOH-KI), asam sulfat (H₂SO₄), dan natrium tiosulfat (Na₂S₂O₃). Prinsipnya adalah dengan menambahkan sampel dengan mangan klorida dan larutan kalium iodida dalam natrium hidroksida yang kemudian dikondisikan pada keadaan asam dengan penambahan asam sulfat sehingga ion iodida pada vessel titrat berubah menjadi iodin yang ekivalen dengan kadar oksigen terlarut. Vessel titrat kemudian dititrasi dengan larutan natrium tiosulfat dengan menggunakan indikator kanji.</p>
        
        <p><b>Persamaan Reaksi:</b></p>
        <p><b>Reaksi Pengendapan (Pengikatan Oksigen):</b><br>
        <code style='font-size: 16px;'>Mn²⁺ + 2OH⁻ + ½ O₂ → MnO₂·H₂O (endapan coklat)</code></p>
        <br>
        <p><b>Reaksi Pengasaman (Pelepasan Iodin):</b><br>
        <code style='font-size: 16px;'>MnO₂·H₂O + 2I⁻ + 4H⁺ → Mn²⁺ + I₂ + 3H₂O</code></p>
        <br>
        <p><b>Reaksi Titrasi:</b><br>
        <code style='font-size: 16px;'>I₂ + 2S₂O₃²⁻ → 2I⁻ + S₄O₆²⁻</code></p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='card'>
        <p><b>Rumus Perhitungan Nilai BOD:</b></p>
        <div style='text-align: center; font-size: 18px; font-weight: bold; padding: 10px;'>
            BOD (mg/L) = 5 × (DO<sub>awal</sub> - DO<sub>akhir</sub>)
        </div>
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown("""
        <div class='card'>
        <h3>🔥 Chemical Oxygen Demand (COD)</h3>
        <p><b>Definisi:</b><br>
        Chemical oxygen demand (COD) adalah suatu parameter yang mengukur kebutuhan oksigen untuk mengoksidasi partikel-partikel yang terdapat dalam sampel air limbah melalui jalur kimia, yakni reaksi oksidasi dan reduksi.</p>
        
        <p><b>Metode Uji & Prinsip:</b><br>
        Berdasarkan <b>Standar Nasional Indonesia Nomor 6989 Tahun 2019</b>, COD dapat diukur dengan cara teknik titrasi (titrimetri). Prinsip pengujian dilakukan dengan dua tahapan, yakni tahap destruksi dan tahap pengujian.</p>
        
        <ul>
            <li><b>Tahap Destruksi:</b> Dilakukan dengan cara refluks (terbuka ataupun tertutup) yang berfungsi untuk mereaksikan kalium dikromat (K₂Cr₂O₇) dalam suasana asam dan mengubahnya menjadi ion kromat (Cr³⁺). Yang membedakan kedua cara ini adalah alat destruksi serta kuantitas reagen yang digunakan.</li>
            <li><b>Tahap Pengujian:</b> Analis perlu menitar sampel hasil destruksi dengan larutan titran Ferro Ammonium Sulfate (FAS). Ion besi (II) (Fe²⁺) yang ada dalam larutan FAS akan mereduksi ion kromium heksavalen (Cr⁶⁺) menjadi ion krom (Cr³⁺) yang menghasilkan perubahan dari larutan <b>biru-kehijauan</b> menjadi warna <b>coklat-kemerahan</b> yang merupakan indikasi dari warna ion besi (III) (Fe³⁺).</li>
        </ul>
        
        <p><b>Persamaan Reaksi Tahap Destruksi:</b></p>
        <div style='text-align: center; background-color: #f8f9fa; padding: 15px; border-radius: 10px; font-family: monospace; font-size: 16px; font-weight: bold;'>
            C<sub>n</sub>H<sub>a</sub>O<sub>b</sub>N<sub>c</sub> + c Cr<sub>2</sub>O<sub>7</sub><sup>2-</sup> + 8cH<sup>+</sup> → n CO<sub>2</sub> + [ (a + 8c) / 2 ] H<sub>2</sub>O + 2c Cr<sup>3+</sup>
        </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='card'>
        <p><b>Rumus Perhitungan Nilai COD:</b><br>
        Jumlah volume larutan FAS yang dibutuhkan sampai terjadinya perubahan warna dicatat dan dihitung dengan rumus:</p>
        <div style='text-align: center; font-size: 18px; font-weight: bold; padding: 10px;'>
            COD (mg/L) = <span style='border-bottom: 2px solid black; padding-bottom: 2px;'>(V<sub>b</sub> - V<sub>c</sub>) × N<sub>FAS</sub> × 8000</span><br>
            <span style='display: block; margin-top: 5px;'>V<sub>s</sub></span>
        </div>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# ALAT & BAHAN
# ==========================================
elif menu == "🧪 Alat & Bahan":

    st.markdown("<h2 style='color:#009688; margin-bottom:5px;'>🧪 Komponen Alat & Bahan Laboratorium</h2>", unsafe_allow_html=True)
    st.write("Silakan pilih parameter di bawah ini untuk melihat daftar alat dan bahan dengan tampilan kartu informatif.")

    pilihan_materi = st.selectbox(
        "Pilih Parameter Pengujian:",
        ["Daftar Alat & Bahan Uji DO", "Daftar Alat & Bahan Uji BOD", "Daftar Alat & Bahan Uji COD"]
    )

    if pilihan_materi == "Daftar Alat & Bahan Uji DO":
        st.markdown("### 💧 Parameter Analisis DO (Dissolved Oxygen)")
        url_do = "https://github.com/user-attachments/assets/411a7412-1a3b-40e5-ab74-f1a394717e13"
        st.image(url_do, caption="Rangkaian Alat Analisis Parameter DO", use_container_width=True)

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

    elif pilihan_materi == "Daftar Alat & Bahan Uji BOD":
        st.markdown("### 🌱 Parameter Analisis BOD (Biochemical Oxygen Demand)")
        url_bod = "https://github.com/user-attachments/assets/869acefd-cb84-49bc-81d7-9cd02cec5241"
        st.image(url_bod, caption="Rangkaian Alat Analisis Parameter BOD", use_container_width=True)

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

    elif pilihan_materi == "Daftar Alat & Bahan Uji COD":
        st.markdown("### 🔥 Parameter Analisis COD (Chemical Oxygen Demand)")
        url_cod = "https://github.com/user-attachments/assets/39987309-7194-4bd9-b1cc-8507f8fb8182"
        st.image(url_cod, caption="Rangkaian Alat Analisis Parameter COD", use_container_width=True)

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
# CARA KERJA
# ==========================================
elif menu == "📋 Cara Kerja":
    st.markdown("<h2 style='color:#009688;'>📋 Prosedur & Cara Kerja Laboratorium</h2>", unsafe_allow_html=True)
    
    pilihan_kerja = st.selectbox(
        "Pilih Cara Kerja Parameter:",
        ["Cara Kerja Uji DO", "Cara Kerja Uji BOD", "Cara Kerja Uji COD"]
    )
    
    if pilihan_kerja == "Cara Kerja Uji DO":
        st.markdown("""
        <div class='card'>
        <h3>💧 Prosedur Analisis Uji DO</h3>
        <ol>
            <li><b>Pengambilan Sampel:</b>
                <ul>
                    <li>Siapkan botol Winkler.</li>
                    <li>Isi sampel air sampai meluap penuh.</li>
                    <li>Pastikan tidak ada gelembung udara.</li>
                    <li>Tutup rapat segera agar tidak ada oksigen tambahan dari udara.</li>
                    <li>Lakukan pengujian secepat mungkin setelah sampling.</li>
                </ul>
            </li>
            <br>
            <li><b>Penambahan reagen pertama (fiksasi oksigen):</b>
                <ul>
                    <li>Tambahkan: Larutan 1 mL MnSO₄ & 1 mL alkali iodida azida (KI + NaOH + NaN₃).</li>
                    <li>Masukkan ujung pipet tepat di permukaan larutan (hindari udara masuk).</li>
                    <li>Tutup botol lalu homogenkan.</li>
                    <li>Akan terbentuk endapan coklat (MnO₂ / senyawa mangan teroksidasi).</li>
                </ul>
            </li>
            <br>
            <li><b>Pengendapan:</b>
                <ul>
                    <li>Diamkan selama 5–10 menit.</li>
                    <li>Endapan dibiarkan terbentuk sempurna.</li>
                </ul>
            </li>
            <br>
            <li><b>Penambahan asam:</b>
                <ul>
                    <li>Tambahkan 1 mL H₂SO₄ pekat.</li>
                    <li>Tutup kembali botol.</li>
                    <li>Kocok hingga endapan larut sempurna.</li>
                    <li>Reaksi ini akan membebaskan iodin (I₂) sesuai kadar oksigen terlarut.</li>
                </ul>
            </li>
            <br>
            <li><b>Persiapan Titrasi:</b>
                <ul>
                    <li>Ambil 50 mL larutan hasil reaksi.</li>
                    <li>Masukkan ke dalam Erlenmeyer 150 mL.</li>
                </ul>
            </li>
            <br>
            <li><b>Titrasi:</b>
                <ul>
                    <li>Titrasi menggunakan Na₂S₂O₃ (natrium tiosulfat).</li>
                    <li>Tambahkan indikator amilum (kanji) saat warna mulai kuning... kuning pucat.</li>
                    <li>Lanjutkan titrasi sampai: warna biru tepat hilang → ini adalah titik akhir titrasi.</li>
                </ul>
            </li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
        
    elif pilihan_kerja == "Cara Kerja Uji BOD":
        st.markdown("""
        <div class='card'>
        <h3>🌱 Prosedur Analisis Uji BOD</h3>
        <ol>
            <li><b>Persiapan Sampel:</b>
                <ul>
                    <li>Isi botol Winkler dengan sampel air hingga penuh untuk menghindari masuknya udara.</li>
                    <li>Tambahkan mangan(II) sulfat dan larutan alkali-iodida-</li>
                    <li>Endapan mangan oksida akan terbentuk.</li>
                </ul>
            </li>
            <br>
            <li><b>Inkubasi:</b>
                <ul>
                    <li>Sampel diinkubasi selama 5 days pada suhu 20°C tanpa gangguan.</li>
                    <li>Setelah inkubasi, tambahkan asam sulfat pekat untuk melarutkan endapan. Reaksi ini menghasilkan iodin bebas.</li>
                </ul>
            </li>
            <br>
            <li><b>Titrasi:</b>
                <ul>
                    <li>Titrasi larutan dengan natrium tiosulfat hingga warna kuning pucat.</li>
                    <li>Tambahkan indikator pati; larutan akan berubah biru.</li>
                    <li>Lanjutkan titrasi hingga larutan tidak berwarna.</li>
                </ul>
            </li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
        
    elif pilihan_kerja == "Cara Kerja Uji COD":
        st.markdown("""
        <div class='card'>
        <h3>🔥 Prosedur Analisis Uji COD</h3>
        <ol>
            <li><b>Persiapan sampel:</b>
                <ul>
                    <li>Ambil volume sampel sesuai metode (umumnya 10–50 mL).</li>
                    <li>Jika perlu, lakukan pengenceran.</li>
                    <li>Tambahkan HgSO₄ (jika ada gangguan klorida).</li>
                </ul>
            </li>
            <br>
            <li><b>Penambahan reagen oksidator:</b>
                <ul>
                    <li>Tambahkan: Larutan K₂Cr₂O₇ (kalium dikromat) berlebih & Larutan H₂SO₄ pekat + Ag₂SO₄ (katalis).</li>
                    <li>Campuran akan menjadi sangat asam (media oksidasi kuat).</li>
                </ul>
            </li>
            <br>
            <li><b>Proses refluks (digestion):</b>
                <ul>
                    <li>Sampel dipanaskan pada ±150°C selama 2 jam (120 menit).</li>
                    <li>Tujuan: mengoksidasi senyawa organik menjadi CO₂ dan H₂O.</li>
                </ul>
            </li>
            <br>
            <li><b>Pendinginan:</b>
                <ul>
                    <li>Setelah refluks selesai, dinginkan sampel hingga suhu ruang.</li>
                </ul>
            </li>
            <br>
            <li><b>Titrasi:</b>
                <ul>
                    <li>Tambahkan indikator ferroin.</li>
                    <li>Titrasi sisa K₂Cr₂O₇ dengan larutan FAS (Fe(NH₄)₂(SO₄)₂).</li>
                    <li>Titik akhir: perubahan warna dari hijau kebiruan → merah bata/coklat kemerahan.</li>
                </ul>
            </li>
        </ol>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 🧮 KALKULATOR
# ==========================================
elif menu == "🧮 Kalkulator":
    st.markdown("<h2 style='color:#009688;'>🧮 Kalkulator Laboratorium</h2>", unsafe_allow_html=True)
    st.write("Silakan pilih parameter uji untuk menghitung konsentrasi analit berdasarkan rumus standardisasi laboratorium.")
    
    pilihan_kalkulator = st.selectbox(
        "Pilih Parameter Kalkulator:",
        ["Kalkulator Parameter DO", "Kalkulator Parameter BOD", "Kalkulator Parameter COD"]
    )

    # ------------------------------------------
    # KALKULATOR DO 
    # ------------------------------------------
    if pilihan_kalkulator == "Kalkulator Parameter DO":
        st.markdown("""
        <div class='card'>
        <h3>💧 Perhitungan Kadar DO (Dissolved Oxygen)</h3>
        <p>Formula: <b>DO (mg/L) = (V × N × 8000 × F) / 50 mL</b></p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            v_do = st.number_input("Volume Penitar / Titran Na₂S₂O₃ (V) [mL]", min_value=0.000, value=7.000, step=0.001, format="%.3f")
            n_do = st.number_input("Normalitas Penitar / Na₂S₂O₃ (N)", min_value=0.0000, value=0.0250, step=0.0001, format="%.4f")
        with col2:
            f_do = st.number_input("Faktor Koreksi Volume Penitar (F)", min_value=0.0, value=1.0, step=0.01, format="%.2f")
            v_sampel_do = st.number_input("Volume Sampel Terpilih (V_s) [mL]", min_value=0.001, value=50.000, step=0.001, format="%.3f")
            
        if st.button("Hitung Nilai DO", key="btn_do"):
            if v_sampel_do > 0:
                hasil_do = (v_do * n_do * 8000 * f_do) / v_sampel_do
                st.markdown(f"""
                <div style='background-color: #e8fff1; padding: 15px; border-radius: 10px; border-left: 5px solid #00c9a7; margin-top: 15px;'>
                    <span style='font-size: 16px; color: #333;'>Hasil Analisis Pembacaan:</span><br>
                    <b style='font-size: 24px; color: #009688;'>Kadar DO = {hasil_do:.2f} mg/L</b>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()

    # ------------------------------------------
    # KALKULATOR BOD
    # ------------------------------------------
    elif pilihan_kalkulator == "Kalkulator Parameter BOD":
        st.markdown("""
        <div class='card'>
        <h3>🌱 Perhitungan Kadar BOD (Biochemical Oxygen Demand)</h3>
        <p>Formula: <b>BOD (mg/L) = 5 × (DO<sub>awal</sub> - DO<sub>akhir</sub>)</b></p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            do_awal = st.number_input("Konsentrasi Oksigen Terlarut Hari ke-0 (DO awal) [mg/L]", min_value=0.0, value=8.5, step=0.1, format="%.2f")
        with col2:
            do_akhir = st.number_input("Konsentrasi Oksigen Terlarut Hari ke-5 (DO akhir) [mg/L]", min_value=0.0, value=3.2, step=0.1, format="%.2f")
            
        if st.button("Hitung Nilai BOD", key="btn_bod"):
            if do_awal >= do_akhir:
                hasil_bod = 5 * (do_awal - do_akhir)
                st.markdown(f"""
                <div style='background-color: #e8fff1; padding: 15px; border-radius: 10px; border-left: 5px solid #00c9a7; margin-top: 15px;'>
                    <span style='font-size: 16px; color: #333;'>Hasil Analisis Pembacaan:</span><br>
                    <b style='font-size: 24px; color: #009688;'>Kadar BOD = {hasil_bod:.2f} mg/L</b>
                </div>
                """, unsafe_allow_html=True)
                st.snow()
            else:
                st.error("Nilai DO awal harus lebih besar atau sama dengan nilai DO akhir!")

    # ------------------------------------------
    # KALKULATOR COD
    # ------------------------------------------
    elif pilihan_kalkulator == "Kalkulator Parameter COD":
        st.markdown("""
        <div class='card'>
        <h3>🔥 Perhitungan Kadar COD (Chemical Oxygen Demand)</h3>
        <p>Formula: <b>COD (mg/L) = [ (V<sub>b</sub> - V<sub>c</sub>) × N<sub>FAS</sub> × 8000 ] / V<sub>s</sub></b></p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            v_blanko = st.number_input("Volume Penitaran Blanko (V_b) [mL]", min_value=0.000, value=20.000, step=0.001, format="%.3f")
            v_contoh = st.number_input("Volume Penitaran Contoh/Sampel (V_c) [mL]", min_value=0.000, value=12.000, step=0.001, format="%.3f")
        with col2:
            n_fas = st.number_input("Normalitas Larutan Titran FAS (N_FAS)", min_value=0.0000, value=0.1000, step=0.0001, format="%.4f")
            v_s_cod = st.number_input("Volume Sampel Air yang Diuji (V_s) [mL]", min_value=0.001, value=50.000, step=0.001, format="%.3f")
            
        if st.button("Hitung Nilai COD", key="btn_cod"):
            if v_s_cod > 0:
                hasil_cod = ((v_blanko - v_contoh) * n_fas * 8000) / v_s_cod
                st.markdown(f"""
                <div style='background-color: #e8fff1; padding: 15px; border-radius: 10px; border-left: 5px solid #00c9a7; margin-top: 15px;'>
                    <span style='font-size: 16px; color: #333;'>Hasil Analisis Pembacaan:</span><br>
                    <b style='font-size: 24px; color: #009688;'>Kadar COD = {hasil_cod:.2f} mg/L</b>
                </div>
                """, unsafe_allow_html=True)
                st.balloons()

# ==========================================
# ANALISIS
# ==========================================
elif menu == "📊 Analisis":
    st.markdown("<h2 style='color:#009688;'>📊 Analisis Kualitas Air</h2>", unsafe_allow_html=True)
    st.write("Gunakan menu ini untuk mengecek status pencemaran air secara otomatis berdasarkan acuan baku mutu resmi nasional.")

    # Bagian 1: Alat Cek Kualitas Air Otomatis
    st.markdown("""
    <div class='card'>
        <h3>🔍 Alat Cek Status Air Otomatis</h3>
        <p>Masukkan hasil kadar pengujian laboratorium Anda di bawah ini untuk mengetahui status kualitas sampel air.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        input_do = st.number_input("Masukkan Nilai DO Anda (mg/L):", min_value=0.0, value=5.0, step=0.1)
    with col2:
        input_bod = st.number_input("Masukkan Nilai BOD Anda (mg/L):", min_value=0.0, value=3.0, step=0.1)
    with col3:
        input_cod = st.number_input("Masukkan Nilai COD Anda (mg/L):", min_value=0.0, value=20.0, step=0.1)

    if st.button("Analisis Kualitas Air", key="btn_interpretasi"):
        st.markdown("#### 📢 Hasil Analisis Sistem:")
        
        # Logika Evaluasi Sederhana
        if input_do >= 6.0 and input_bod <= 2.0 and input_cod <= 10.0:
            st.success("🟢 KATEGORI: AIR BERSIH (Memenuhi Baku Mutu Kelas 1)\n\nAir dalam kondisi sangat baik, kaya oksigen, rendah cemaran organik, aman untuk ekosistem dan bahan baku air minum.")
        elif input_do >= 3.0 and input_bod <= 6.0 and input_cod <= 40.0:
            st.warning("🟡 KATEGORI: TERCEMAR SEDANG (Memenuhi Baku Mutu Kelas 2/3)\n\nAir mengalami penurunan kualitas karena cemaran organik sedang. Masih dapat digunakan untuk sarana rekreasi air, pembudidayaan ikan air tawar, atau peternakan.")
        else:
            st.error("🔴 KATEGORI: TERCEMAR BERAT (Melebihi Batas Aman / Kelas 4)\n\nAir dalam kondisi kritis! Oksigen terlarut (DO) terlalu rendah atau beban limbah kimia (BOD/COD) terlalu tinggi. Hanya dapat digunakan untuk mengairi pertamanan atau membutuhkan pengolahan intensif.")

    # Bagian 2: Tabel Acuan Resmi Baku Mutu Air Nasional
    st.markdown("""
    <div class='card' style='margin-top:25px;'>
        <h3>📋 Tabel Acuan Baku Mutu Air Nasional (PP No. 22 Tahun 2021)</h3>
        <p>Klasifikasi peruntukan kelas air berdasarkan standar baku mutu lingkungan hidup:</p>
    </div>
    """, unsafe_allow_html=True)

    data_mutu = pd.DataFrame({
        "Parameter": ["DO (Oksigen Terlarut)", "BOD (Kebutuhan Oksigen Biologis)", "COD (Kebutuhan Oksigen Kimia)"],
        "Kelas 1 (Air Minum)": ["≥ 6 mg/L", "≤ 2 mg/L", "≤ 10 mg/L"],
        "Kelas 2 (Rekreasi Air)": ["≥ 4 mg/L", "≤ 3 mg/L", "≤ 25 mg/L"],
        "Kelas 3 (Perikanan & Ternak)": ["≥ 3 mg/L", "≤ 6 mg/L", "≤ 40 mg/L"],
        "Kelas 4 (Irigasi/Taman)": ["≥ 0 mg/L", "≤ 12 mg/L", "≤ 80 mg/L"]
    })
    
    st.table(data_mutu)
    
    st.markdown("""
    <div class='tool-item' style='margin-top:10px;'>
        <div class='item-title'>💡 Tips Membaca Parameter Hubungan DO, BOD, & COD:</div>
        <div class='item-desc'>
            • Hubungan parameter ini berbanding terbalik. Semakin tinggi jumlah polutan organik di dalam air, maka angka <b>BOD dan COD akan melesat naik</b>.<br>
            • Kenaikan beban organik tersebut memicu mikroorganisme bekerja keras dan mengonsumsi oksigen secara besar-besaran, yang berakibat pada <b>turunnya drastis nilai DO (oksigen terlarut)</b> hingga menyebabkan biota air mati.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# KUIS
# ==========================================
elif menu == "🎮 Kuis":
    st.markdown("<h2 style='color:#009688;'>🎮 Kuis Interaktif Parameter Air</h2>", unsafe_allow_html=True)
    st.write("Silakan jawab pertanyaan di bawah ini secara teliti untuk menguji pemahaman materi laboratorium Anda.")

    # Inisialisasi Session State untuk melacak status pengiriman kuis
    if "kuis_disubmit" not in st.session_state:
        st.session_state.kuis_disubmit = False
    if "skor_akhir" not in st.session_state:
        st.session_state.skor_akhir = 0

    # Data Soal Kuis 
    soal_list = [
        {
            "id": "q1",
            "tanya": "1. BOD merupakan singkatan dari ...",
            "opsi": ["A. Biological Oxygen Data", "B. Biochemical Oxygen Demand", "C. Biochemical Oxidation Data", "D. Biological Oxidation Demand"],
            "kunci": "B. Biochemical Oxygen Demand",
            "alasan": "BOD adalah Biochemical Oxygen Demand, yaitu jumlah oksigen yang dibutuhkan mikroorganisme untuk menguraikan bahan organik dalam air."
        },
        {
            "id": "q2",
            "tanya": "2. Parameter DO digunakan untuk mengetahui ...",
            "opsi": ["A. Jumlah logam berat dalam air", "B. Kadar oksigen terlarut dalam air", "C. Tingkat keasaman air", "D. Kekeruhan air"],
            "kunci": "B. Kadar oksigen terlarut dalam air",
            "alasan": "DO (Dissolved Oxygen) digunakan untuk mengukur jumlah oksigen yang terlarut dalam air."
        },
        {
            "id": "q3",
            "tanya": "3. Pada metode Winkler, larutan Na₂S₂O₃ digunakan sebagai ...",
            "opsi": ["A. Indikator", "B. Oksidator", "C. Titran", "D. Katalis"],
            "kunci": "C. Titran",
            "alasan": "Natrium tiosulfat digunakan sebagai larutan penitar untuk menentukan jumlah iodin yang terbentuk pada titrasi DO."
        },
        {
            "id": "q4",
            "tanya": "4. COD digunakan untuk mengukur ...",
            "opsi": ["A. Jumlah mikroorganisme dalam air", "B. Kebutuhan oksigen secara kimia", "C. Kandungan garam dalam air", "D. Tingkat warna air"],
            "kunci": "B. Kebutuhan oksigen secara kimia",
            "alasan": "COD (Chemical Oxygen Demand) menunjukkan jumlah oksigen yang dibutuhkan untuk mengoksidasi bahan organik secara kimia."
        },
        {
            "id": "q5",
            "tanya": "5. Alat yang digunakan untuk menyimpan sampel DO agar tidak terkena udara adalah ...",
            "opsi": ["A. Gelas ukur", "B. Labu ukur", "C. Botol Winkler", "D. Erlenmeyer"],
            "kunci": "C. Botol Winkler",
            "alasan": "Botol Winkler dirancang khusus agar sampel tidak kontak dengan udara sehingga kadar oksigen tidak berubah."
        },
        {
            "id": "q6",
            "tanya": "6. Inkubator pada pengujian BOD biasanya diatur pada suhu ...",
            "opsi": ["A. 0°C", "B. 10°C", "C. 20°C", "D. 50°C"],
            "kunci": "C. 20°C",
            "alasan": "Pengujian BOD standar dilakukan pada suhu 20°C selama 5 hari agar aktivitas mikroorganisme optimal."
        },
        {
            "id": "q7",
            "tanya": "7. Indikator yang digunakan pada titrasi DO metode Winkler adalah ...",
            "opsi": ["A. Fenolftalein", "B. Metil jingga", "C. Ferroin", "D. Amilum (pati)"],
            "kunci": "D. Amilum (pati)",
            "alasan": "Indikator amilum membentuk warna biru dengan iodin dan digunakan untuk menunjukkan titik akhir titrasi."
        },
        {
            "id": "q8",
            "tanya": "8. Semakin tinggi nilai BOD suatu air, maka ...",
            "opsi": ["A. Air semakin bersih", "B. Kandungan bahan organik semakin tinggi", "C. Oksigen terlarut semakin tinggi", "D. Air semakin jernih"],
            "kunci": "B. Kandungan bahan organik semakin tinggi",
            "alasan": "Nilai BOD tinggi menunjukkan banyak bahan organik yang harus diuraikan mikroorganisme sehingga kebutuhan oksigen meningkat."
        },
        {
            "id": "q9",
            "tanya": "9. Pada pengujian COD, senyawa yang digunakan sebagai oksidator adalah ...",
            "opsi": ["A. NaOH", "B. KMnO₄", "C. K₂Cr₂O₇", "D. NaCl"],
            "kunci": "C. K₂Cr₂O₇",
            "alasan": "Kalium dikromat (K₂Cr₂O₇) merupakan oksidator kuat yang digunakan untuk mengoksidasi bahan organik pada uji COD."
        },
        {
            "id": "q10",
            "tanya": "10. Tujuan utama pengukuran DO adalah ...",
            "opsi": ["A. Mengetahui kadar bahan organik", "B. Menentukan tingkat salinitas", "C. Mengetahui jumlah oksigen terlarut dalam air", "D. Mengukur kadar logam berat"],
            "kunci": "C. Mengetahui jumlah oksigen terlarut dalam air",
            "alasan": "DO digunakan untuk mengetahui kadar oksigen terlarut yang penting bagi kehidupan organisme air dan kualitas perairan."
        }
    ]

    # Render Pertanyaan Kuis dan Evaluasi Langsung Di Bawah Soal
    jawaban_user = {}
    for item in soal_list:
        st.markdown(f"<div class='card'><b>{item['tanya']}</b></div>", unsafe_allow_html=True)
        
        jawaban_user[item["id"]] = st.radio(
            "Pilih Jawaban Anda:",
            item["opsi"],
            index=None,
            key=f"radio_{item['id']}"
        )
        
        # JIKA kuis sudah disubmit, langsung munculkan hasilnya di bawah soal bersangkutan
        if st.session_state.kuis_disubmit:
            pilihan = jawaban_user[item["id"]]
            if pilihan == item["kunci"]:
                st.success(f"🔹 JAWABAN ANDA BENAR ({pilihan})")
            else:
                st.error(f"🔸 JAWABAN ANDA SALAH. Anda memilih ({pilihan if pilihan is not None else 'Belum Diisi'})")
            
            st.info(f"💡 *Alasan/Pembahasan:* {item['alasan']}")
            
        st.write("")

    # Tombol Evaluasi Nilai Kuis
    if st.button("Kirim Seluruh Jawaban Kuis", key="btn_submit_kuis"):
        # Validasi jika ada soal yang belum dikerjakan/diisi sama sekali
        belum_diisi = [item["tanya"][:4] for item in soal_list if jawaban_user[item["id"]] is None]
        
        if belum_diisi:
            st.warning(f"⚠️ Tolong isi semua pertanyaan terlebih dahulu! Nomor yang belum diisi: {', '.join(belum_diisi)}")
            st.session_state.kuis_disubmit = False
        else:
            # Hitung skor akhir
            total_skor = 0
            for item in soal_list:
                if jawaban_user[item["id"]] == item["kunci"]:
                    total_skor += 10
            
            # Simpan status ke session state dan picu jalannya penampilan interpretasi bawah soal
            st.session_state.kuis_disubmit = True
            st.session_state.skor_akhir = total_skor
            st.rerun()

    # Tampilkan Total Skor Akhir di bagian paling bawah setelah disubmit
    if st.session_state.kuis_disubmit:
        st.markdown("---")
        st.markdown(f"""
        <div style='background-color: #f0f7ff; padding: 20px; border-radius: 15px; border-left: 5px solid #00b4db; text-align: center; margin-top:20px; margin-bottom:20px;'>
            <h3 style='margin:0; color:#0077b6;'>📊 Total Skor Anda</h3>
            <b style='font-size: 40px; color:#00b4db;'>{st.session_state.skor_akhir} / 100</b>
        </div>
        """, unsafe_allow_html=True)
        
        if st.session_state.skor_akhir == 100:
            st.balloons()
        elif st.session_state.skor_akhir >= 70:
            st.snow()

# ==========================================
# FOOTER
# ==========================================
st.markdown("""
<div class='footer'>
✨ Kelompok 8 kelas 1A ✨
</div>
""", unsafe_allow_html=True)
