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

/* Card */
.card {
    background-color: white;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 5px 15px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.03);
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
    <h1 style='color:white;'>🧪 ModulDigital-Oxy</h1>
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
    <p>
    ModulDigital-Oxy adalah media pembelajaran interaktif untuk memahami:
    </p>

    <ul>
    <li>💧 Dissolved Oxygen (DO)</li>
    <li>🌱 Biochemical Oxygen Demand (BOD)</li>
    <li>🔥 Chemical Oxygen Demand (COD)</li>
    </ul>

    <p>
    Aplikasi ini dibuat lebih modern dan interaktif agar pembelajaran laboratorium menjadi lebih menyenangkan 🎉
    </p>
    </div>
    """, unsafe_allow_html=True)

    st.success("✨ Yuk mulai belajar dari menu di atas!")

# ==========================================
# TEORI (MATERI SUPER LENGKAP DIKEMBALIKAN UTUH)
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
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**Reaksi Preparasi:**")
        st.latex(r'''Mn^{2+}_{(aq)} + 2OH^{-}_{(aq)} \rightarrow Mn(OH)_{2(s)}''')
        
        st.markdown("**Reaksi Titrasi:**")
        st.latex(r'''I_2 + 2S_2O_3^{2-} \xrightarrow{H^+} S_4O_6^{2-} + 2I^-''')

        st.markdown("""
        <div class='card'>
        <p><b>Rumus Perhitungan Nilai DO:</b></p>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r'''DO\ (mg/L) = \frac{V \times N \times 8000 \times F}{50\ mL}''')

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
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**Reaksi Pengendapan (Pengikatan Oksigen):**")
        st.latex(r'''Mn^{2+} + 2OH^- + \frac{1}{2}O_2 \rightarrow MnO_2\cdot H_2O\ \text{(endapan coklat)}''')
        
        st.markdown("**Reaksi Pengasaman (Pelepasan Iodin):**")
        st.latex(r'''MnO_2\cdot H_2O + 2I^- + 4H^+ \rightarrow Mn^{2+} + I_2 + 3H_2O''')
        
        st.markdown("**Reaksi Titrasi:**")
        st.latex(r'''I_2 + 2S_2O_3^{2-} \rightarrow 2I^- + S_4O_6^{2-}''')

        st.markdown("""
        <div class='card'>
        <p><b>Rumus Perhitungan Nilai BOD:</b></p>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r'''BOD\ (mg/L) = 5 \times (DO_{awal} - DO_{akhir})''')

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
            <li><b>Tahap Pengujian:</b> Analis perlu menitar sampel hasil destruksi dengan larutan titran Ferro Ammonium Sulfat (FAS). Ion besi (II) (Fe²⁺) yang ada dalam larutan FAS akan mereduksi ion kromium heksavalen (Cr⁶⁺) menjadi ion krom (Cr³⁺) yang menghasilkan perubahan dari larutan <b>biru-kehijauan</b> menjadi warna <b>coklat-kemerahan</b> yang merupakan indikasi dari warna ion besi (III) (Fe³⁺).</li>
        </ul>
        
        <p><b>Persamaan Reaksi Tahap Destruksi:</b></p>
        </div>
        """, unsafe_allow_html=True)

        st.latex(r'''C_nH_aO_bN_c + cCr_2O_7^{2-} + 8cH^+ \rightarrow nCO_2 + \left(\frac{a+8c}{2}\right)H_2O + 2cCr^{3+}''')

        st.markdown("""
        <div class='card'>
        <p><b>Rumus Perhitungan Nilai COD:</b><br>
        Jumlah volume larutan FAS yang dibutuhkan sampai terjadinya perubahan warna dicatat dan dihitung dengan rumus:</p>
        </div>
        """, unsafe_allow_html=True)
        st.latex(r'''COD\ (mg/L) = \frac{(V_b - V_c) \times N_{FAS} \times 8000}{V_S}''')

# ==========================================
# ALAT & BAHAN (1 GAMBAR INDIVIDU LENGKAP PER UJI)
# ==========================================
elif menu == "🧪 Alat & Bahan":

    st.markdown("<h2 style='color:#009688;'>🧪 Alat & Bahan Laboratorium</h2>", unsafe_allow_html=True)

    pilihan_materi = st.selectbox(
        "Pilih Parameter Pengujian:",
        ["Daftar Alat & Bahan Uji DO", "Daftar Alat & Bahan Uji BOD", "Daftar Alat & Bahan Uji COD"]
    )

    # ------------------------------------------
    # SUB-BAGIAN: ALAT & BAHAN UJI DO
    # ------------------------------------------
    if pilihan_materi == "Daftar Alat & Bahan Uji DO":
        st.markdown("### 💧 Komponen Analisis Uji DO (Dissolved Oxygen)")
        
        try:
            st.image("Gambar Alat DO.png", caption="Rangkaian Alat Analisis Parameter DO", use_container_width=True)
        except:
            st.warning("⚠️ File 'Gambar Alat DO.png' tidak ditemukan. Pastikan file gambar berada di folder yang sama dengan script python ini.")

        st.markdown("""
        <div class='card'>
        <h4>📋 Alat yang Digunakan beserta Fungsinya:</h4>
        <ul>
            <li><b>Botol Winkler (botol DO/BOD bottle):</b> Untuk pengambilan sampel air tanpa udara.</li>
            <li><b>Pipet volumetrik / pipet ukur:</b> Digunakan untuk menambahkan reagen secara tepat (MnSO₄, KI-NaOH-azida, H₂SO₄).</li>
            <li><b>Buret:</b> Digunakan untuk melakukan titrasi dengan larutan penitar Na₂S₂O₃ (natrium tiosulfat).</li>
            <li><b>Erlenmeyer (±150 mL):</b> Sebagai wadah penampung larutan selama proses titrasi berlangsung.</li>
            <li><b>Gelas ukur / labu ukur:</b> Digunakan untuk keperluan pengenceran serta preparasi larutan kerja.</li>
            <li><b>Statif dan klem:</b> Untuk menyangga dan menopang buret agar berdiri tegak lurus.</li>
            <li><b>Botol reagen gelap (dark bottle):</b> Tempat penyimpanan larutan pereaksi yang sensitif terhadap paparan cahaya.</li>
            <li><b>Pipet tetes:</b> Digunakan untuk menambahkan indikator amilum secara bertetes-tetes.</li>
            <li><b>Termometer (opsional):</b> Untuk melakukan pengukuran kondisi suhu awal pada sampel air uji.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='card' style='border-left: 5px solid #00b4db;'>
        <h3>📋 Bahan yang Digunakan:</h3>
        <ul>
            <li>Contoh air (air limbah / air sungai / air uji)</li>
            <li><b>MnSO₄ (Mangan(II) sulfat):</b> Berfungsi untuk membentuk endapan Mn(OH)₂ di dalam sampel.</li>
            <li><b>Alkali iodida azida (KI + NaOH + NaN₃):</b> Berfungsi membebaskan senyawa I₂ secara tidak langsung.</li>
            <li><b>H₂SO₄ pekat:</b> Memberikan suasana asam kuat serta melarutkan kembali flok endapan yang terbentuk.</li>
            <li><b>Na₂S₂O₃ (natrium tiosulfat):</b> Bertindak sebagai larutan titran standar.</li>
            <li><b>Indikator amilum (kanji/starch):</b> Penunjuk titik akhir titrasi (perubahan warna: dari biru tepat menjadi hilang/jernih).</li>
            <li><b>K₂Cr₂O₇ (kalium dikromat):</b> Digunakan sebagai larutan standar oksidator primer.</li>
            <li><b>KI (kalium iodida):</b> Digunakan untuk membantu reaksi pembentukan I₂.</li>
            <li><b>Air suling / aquadest:</b> Digunakan sebagai pelarut pereaksi dan pembilas alat gelas.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    # ------------------------------------------
    # SUB-BAGIAN: ALAT & BAHAN UJI BOD
    # ------------------------------------------
    elif pilihan_materi == "Daftar Alat & Bahan Uji BOD":
        st.markdown("### 🌱 Komponen Analisis Uji BOD (Biochemical Oxygen Demand)")
        
        try:
            st.image("Gambar Alat BOD.png", caption="Rangkaian Alat Analisis Parameter BOD", use_container_width=True)
        except:
            st.warning("⚠️ File 'Gambar Alat BOD.png' tidak ditemukan. Pastikan file gambar berada di folder yang sama dengan script python ini.")

        st.markdown("""
        <div class='card'>
        <h4>📋 Alat yang Digunakan beserta Fungsinya:</h4>
        <ul>
            <li><b>Botol Winkler (botol DO/BOD bottle):</b> Untuk wadah inkubasi dan pengambilan sampel air tanpa udara.</li>
            <li><b>Pipet volumetrik / pipet ukur:</b> Digunakan untuk mengambil volume larutan contoh air secara presisi dan tepat.</li>
            <li><b>Buret:</b> Untuk meneteskan larutan titran natrium tiosulfat secara teliti dan terkendali.</li>
            <li><b>Erlenmeyer (±150 mL):</b> Sebagai wadah titrasi campuran larutan uji sampel h-0 dan h-5.</li>
            <li><b>Inkubator (20°C):</b> Berfungsi untuk menginkubasi sampel air selama masa pengujian penguraian biologis (5 hari).</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='card' style='border-left: 5px solid #00c9a7;'>
        <h3>📋 Bahan yang Digunakan:</h3>
        <ul>
            <li><b>Mangan(II) sulfat (MnSO₄):</b> Berfungsi untuk mengikat molekul oksigen terlarut alami dalam sampel air.</li>
            <li><b>Larutan alkali-iodida-azida:</b> Membentuk kondisi lingkungan basa dan membantu pembentukan senyawa iodin.</li>
            <li><b>Asam sulfat pekat (H₂SO₄):</b> Untuk melarutkan kembali flok endapan coklat dan membebaskan molekul iodin bebas.</li>
            <li><b>Larutan natrium tiosulfat (Na₂S₂O₃):</b> Berperan sebagai larutan penitar (titran) utama pada penentuan nilai DO h-0 dan h-5.</li>
            <li><b>Indikator pati (amilum):</b> Digunakan untuk menunjukkan titik akhir penataran secara visual.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    # ------------------------------------------
    # SUB-BAGIAN: ALAT & BAHAN UJI COD
    # ------------------------------------------
    elif pilihan_materi == "Daftar Alat & Bahan Uji COD":
        st.markdown("### 🔥 Komponen Analisis Uji COD (Chemical Oxygen Demand)")
        
        try:
            st.image("Gambar Alat COD.jpg", caption="Rangkaian Alat Analisis Parameter COD", use_container_width=True)
        except:
            st.warning("⚠️ File 'Gambar Alat COD.jpg' tidak ditemukan. Pastikan file gambar berada di folder yang sama dengan script python ini.")

        st.markdown("""
        <div class='card'>
        <h4>📋 Alat yang Digunakan beserta Fungsinya:</h4>
        <ul>
            <li><b>Labu refluks (reflux flask):</b> Wadah utama tempat terjadinya reaksi destruksi dan oksidasi sampel air organik.</li>
            <li><b>Kondensor refluks (pendingin balik):</b> Berfungsi mengembunkan uap asam kembali ke labu agar tidak terbuang bebas.</li>
            <li><b>Pemanas listrik / heating mantle / hot plate:</b> Sumber panas eksternal untuk proses digesti campuran reagen pada ±150°C.</li>
            <li><b>Erlenmeyer (±250 mL):</b> Wadah penampung larutan dingin hasil refluks untuk melangsungkan titrasi.</li>
            <li><b>Buret:</b> Digunakan untuk meneteskan larutan penitar FAS (Ferrous Ammonium Sulfate) secara teliti.</li>
            <li><b>Pipet volumetrik / pipet ukur:</b> Digunakan untuk mengambil volume cuplikan sampel air serta larutan reagen utama.</li>
            <li><b>Gelas ukur:</b> Berfungsi untuk melakukan pengukuran volume reagen pelarut kasar.</li>
            <li><b>Corong kaca:</b> Alat bantu memindahkan cairan asam korosif agar tidak tumpah di luar mulut leher labu.</li>
            <li><b>Statif dan klem:</b> Untuk menopang serta menjaga kestabilan susunan buret beserta rangkaian alat gelas refluks.</li>
            <li><b>Termometer (opsional):</b> Digunakan untuk mengonfirmasi ketepatan suhu operasional proses digesti.</li>
            <li><b>Botol semprot aquadest:</b> Digunakan sebagai pembilas dinding sisa-sisa zat reagen pada alat gelas laboratorium.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='card' style='border-left: 5px solid #0077b6;'>
        <h3>📋 Bahan yang Digunakan:</h3>
        <ul>
            <li>Sampel air limbah / air uji</li>
            <li><b>Kalium dikromat (K₂Cr₂O₇):</b> Bertindak sebagai agen oksidator utama penyerang zat organik.</li>
            <li><b>Asam sulfat pekat (H₂SO₄):</b> Untuk menciptakan suasana lingkungan asam kuat yang ekstrem.</li>
            <li><b>Perak sulfat (Ag₂SO₄):</b> Digunakan sebagai bahan katalis untuk mempercepat jalannya laju oksidasi senyawa.</li>
            <li><b>Merkuri sulfat (HgSO₄):</b> Berfungsi khusus mengikat ion klorida agar tidak menimbulkan interferensi pembacaan Cl⁻.</li>
            <li><b>Larutan FAS (Ferrous Ammonium Sulfate):</b> Larutan standar sekunder yang berperan sebagai zat penitar (titran).</li>
            <li><b>Indikator ferroin:</b> Senyawa kompleks penunjuk titik akhir titrasi (perubahan warna: biru-kehijauan menjadi coklat-kemerahan).</li>
            <li><b>Aquadest / air bebas ion:</b> Digunakan sebagai larutan blanko pembanding sekaligus pelarut sistem.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.success("✨ Pembaruan Berhasil! Menu Alat & Bahan menggunakan 1 gambar ringkas per materi tanpa merusak bagian lainnya.")

# ==========================================
# SIMULASI
# ==========================================
elif menu == "🕹️ Simulasi":

    st.markdown("<h2 style='color:#009688;'>🕹️ Simulasi Interaktif</h2>", unsafe_allow_html=True)

    simulasi = st.selectbox(
        "Pilih Simulasi",
        ["💧 Simulasi DO", "🌱 Simulasi BOD", "🔥 Simulasi COD"]
    )

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

    parameter = st.selectbox(
        "Pilih Parameter",
        ["DO", "BOD", "COD"]
    )

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

    q1 = st.radio(
        "Apa kepanjangan DO?",
        [
            "Dissolved Oxygen",
            "Digital Oxygen",
            "Double Oxygen"
        ]
    )

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
