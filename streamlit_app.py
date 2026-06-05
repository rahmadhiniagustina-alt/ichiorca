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
# ALAT & BAHAN (DIPERBAIKIKAN SESUAI FILE DOCX DAN DATA REFERENSI)
# ==========================================
elif menu == "🧪 Alat & Bahan":

    st.markdown("<h2 style='color:#009688;'>🧪 Daftar Alat & Bahan Laboratorium</h2>", unsafe_allow_html=True)
    
    pilihan_materi = st.selectbox(
        "Pilih Parameter Pengujian:",
        ["Daftar Alat & Bahan Uji DO", "Daftar Alat & Bahan Uji BOD", "Daftar Alat & Bahan Uji COD"]
    )
    
    # ------------------------------------------
    # SUB-BAGIAN: ALAT & BAHAN UJI DO
    # ------------------------------------------
    if pilihan_materi == "Daftar Alat & Bahan Uji DO":
        st.markdown("### 💧 Komponen Analisis Uji DO (Dissolved Oxygen)")
        
        # Grid Tampilan Alat Uji DO (Menggunakan Layout Columns Sesuai Gambar Alat DO.png)
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("<div class='card'><h4>🧴 Botol Winkler</h4><p style='font-size:13px; color:#555;'>Untuk pengambilan sampel tanpa udara.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/BOD_bottle.jpg/220px-BOD_bottle.jpg", use_container_width=True)
            with st.expander("📖 Cara Penggunaan"):
                st.write("Isi botol dengan contoh air perlahan hingga meluap, pastikan tidak terbentuk gelembung udara, lalu segera tutup rapat.")
                
        with col2:
            st.markdown("<div class='card'><h4>🧪 Pipet Volumetrik</h4><p style='font-size:13px; color:#555;'>Menambahkan reagen secara presisi.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Pipettes_with_bulbs.jpg/220px-Pipettes_with_bulbs.jpg", use_container_width=True)
            with st.expander("📖 Cara Penggunaan"):
                st.write("Gunakan pro-pipet untuk memipet larutan reagen pembentuk endapan tepat pada tanda batas volume.")
                
        with col3:
            st.markdown("<div class='card'><h4>🧪 Buret</h4><p style='font-size:13px; color:#555;'>Untuk titrasi larutan Na₂S₂O₃.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Burette.png/220px-Burette.png", use_container_width=True)
            with st.expander("📖 Cara Penggunaan"):
                st.write("Bilas dan isi buret dengan larutan natrium tiosulfat standar, pastikan keran tidak bocor dan skala terbaca jelas.")
                
        with col4:
            st.markdown("<div class='card'><h4>⚗️ Erlenmeyer</h4><p style='font-size:13px; color:#555;'>Sebagai wadah proses titrasi.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Erlenmeyer_flask.jpg/220px-Erlenmeyer_flask.jpg", use_container_width=True)
            with st.expander("📖 Cara Penggunaan"):
                st.write("Pindahkan sebagian larutan contoh terasidifikasi dari botol winkler ke dalam erlenmeyer sebelum dititrasi.")

        col5, col6, col7, col8 = st.columns(4)
        
        with col5:
            st.markdown("<div class='card'><h4>🧪 Gelas Ukur</h4><p style='font-size:13px; color:#555;'>Pengenceran & preparasi larutan kasar.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Graduated_cylinder.jpg/180px-Graduated_cylinder.jpg", use_container_width=True)
            with st.expander("📖 Cara Penggunaan"):
                st.write("Tuangkan larutan penunjang atau aquadest sampai garis skala volume kasar yang diinginkan.")
                
        with col6:
            st.markdown("<div class='card'><h4>🗼 Statif & Klem</h4><p style='font-size:13px; color:#555;'>Menopang tegak buret titrasi.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Retort_stand.jpg/120px-Retort_stand.jpg", use_container_width=True)
            with st.expander("📖 Cara Penggunaan"):
                st.write("Jepit buret dengan kuat pada klem statif secara vertikal agar stabil saat proses penitaran berlangsung.")
                
        with col7:
            st.markdown("<div class='card'><h4>🟫 Botol Reagen Gelap</h4><p style='font-size:13px; color:#555;'>Penyimpanan larutan sensitif cahaya.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a2/Amber_glass_bottles.jpg/220px-Amber_glass_bottles.jpg", use_container_width=True)
            with st.expander("📖 Cara Penggunaan"):
                st.write("Gunakan untuk menaruh stok larutan peka cahaya seperti tiosulfat atau iodida azida.")
                
        with col8:
            st.markdown("<div class='card'><h4>🧪 Pipet Tetes</h4><p style='font-size:13px; color:#555;'>Penambahan indikator amilum.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Dropping_pipette_1.jpg/120px-Dropping_pipette_1.jpg", use_container_width=True)
            with st.expander("📖 Cara Penggunaan"):
                st.write("Ambil beberapa tetes larutan kanji/amilum untuk dimasukkan menjelang titik akhir titrasi tercapai.")

        st.markdown("<div class='card'><h4>🌡️ Alat Tambahan Lainnya (Opsional)</h4><p>• <b>Termometer:</b> Digunakan untuk mengukur kondisi suhu awal dari sampel air lapangan.</p></div>", unsafe_allow_html=True)

        # Bagian Daftar Bahan Kimia DO
        st.markdown("""
        <div class='card' style='border-left: 5px solid #00b4db;'>
        <h3>📋 Daftar Bahan Kimia yang Digunakan (Uji DO)</h3>
        <ul>
            <li><b>Contoh air:</b> Air limbah, air sungai, atau air uji lapangan.</li>
            <li><b>MnSO₄ (Mangan(II) sulfat):</b> Berfungsi membentuk endapan Mn(OH)₂ di dalam reaktor.</li>
            <li><b>Alkali iodida azida (KI + NaOH + NaN₃):</b> Berfungsi membebaskan I₂ secara tidak langsung.</li>
            <li><b>H₂SO₄ pekat:</b> Berfungsi memberikan suasana asam kuat dan melarutkan kembali endapan coklat.</li>
            <li><b>Na₂S₂O₃ (Natrium tiosulfat):</b> Bertindak sebagai larutan penitar standar (titran).</li>
            <li><b>Indikator amilum (kanji/starch):</b> Sebagai penentu titik akhir titrasi (perubahan warna: biru menjadi hilang jernih).</li>
            <li><b>K₂Cr₂O₇ (Kalium dikromat):</b> Digunakan sebagai larutan standar oksidator primer.</li>
            <li><b>KI (Kalium iodida):</b> Digunakan untuk membantu menghasilkan senyawa iodin bebas.</li>
            <li><b>Air suling / Aquadest:</b> Digunakan sebagai pembilas alat gelas dan pelarut pereaksi.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    # ------------------------------------------
    # SUB-BAGIAN: ALAT & BAHAN UJI BOD
    # ------------------------------------------
    elif pilihan_materi == "Daftar Alat & Bahan Uji BOD":
        st.markdown("### 🌱 Komponen Analisis Uji BOD (Biochemical Oxygen Demand)")
        
        # Grid Tampilan Alat Uji BOD (Menggunakan Layout Columns Sesuai Gambar Alat BOD.png)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("<div class='card'><h4>🧴 Botol Winkler (Botol DO/BOD)</h4><p style='font-size:13px; color:#555;'>Wadah sampel tanpa kontak udara.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/BOD_bottle.jpg/220px-BOD_bottle.jpg", use_container_width=True)
            with st.expander("📖 Cara Penggunaan"):
                st.write("Gunakan dua buah botol secara terpisah untuk penentuan kadar oksigen terlarut hari ke-0 (DO-0) dan hari ke-5 (DO-5).")
                
        with col2:
            st.markdown("<div class='card'><h4>🧪 Pipet Volumetrik / Pipet Ukur</h4><p style='font-size:13px; color:#555;'>Mengambil volume larutan dengan tepat.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Pipettes_with_bulbs.jpg/220px-Pipettes_with_bulbs.jpg", use_container_width=True)
            with st.expander("📖 Cara Penggunaan"):
                st.write("Gunakan untuk mengukur volume sampel air limbah secara presisi saat melakukan pengenceran.")
                
        with col3:
            st.markdown("<div class='card'><h4>🧪 Buret Titrasi</h4><p style='font-size:13px; color:#555;'>Meneteskan titran secara teliti.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Burette.png/220px-Burette.png", use_container_width=True)
            with st.expander("📖 Cara Penggunaan"):
                st.write("Gunakan untuk meneteskan larutan natrium tiosulfat secara konstan perlahan-lahan ke wadah titrat.")

        col4, col5, col6 = st.columns(3)
        
        with col4:
            st.markdown("<div class='card'><h4>⚗ ... Erlenmeyer</h4><p style='font-size:13px; color:#555;'>Wadah titrasi iodometri.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Erlenmeyer_flask.jpg/220px-Erlenmeyer_flask.jpg", use_container_width=True)
            with st.expander("📖 Cara Penggunaan"):
                st.write("Gunakan untuk menghomogenkan campuran zat uji selama tetesan tiosulfat ditambahkan.")
                
        with col5:
            st.markdown("<div class='card'><h4>🗼 Statif & Klem</h4><p style='font-size:13px; color:#555;'>Penyangga peralatan gelas.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Retort_stand.jpg/120px-Retort_stand.jpg", use_container_width=True)
            with st.expander("📖 Cara Penggunaan"):
                st.write("Pastikan tiang statif diletakkan pada permukaan meja kerja laboratorium yang rata.")
                
        with col6:
            st.markdown("<div class='card'><h4>📦 Inkubator BOD</h4><p style='font-size:13px; color:#555;'>Inkubasi sampel terkendali suhu 20°C.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Incubator_%28laboratory%29.jpg/220px-Incubator_%28laboratory%29.jpg", use_container_width=True)
            with st.expander("📖 Cara Penggunaan"):
                st.write("Masukkan botol BOD inkubasi 5 hari ke dalam ruang inkubator, kunci suhu di posisi stabil 20°C dan pertahankan kondisi gelap gulita.")

        # Bagian Daftar Bahan Kimia BOD
        st.markdown("""
        <div class='card' style='border-left: 5px solid #00c9a7;'>
        <h3>📋 Daftar Bahan Kimia yang Digunakan (Uji BOD)</h3>
        <ul>
            <li><b>Mangan(II) sulfat (MnSO₄):</b> Mengikat senyawa gas oksigen terlarut alami dalam sampel air.</li>
            <li><b>Larutan alkali-iodida-azida:</b> Membentuk kondisi lingkungan basa kuat dan membantu pelepasan iodin ekivalen.</li>
            <li><b>Asam sulfat pekat (H₂SO₄):</b> Membantu melarutkan kembali flok endapan suspensi dan membebaskan molekul iodin bebas.</li>
            <li><b>Larutan natrium tiosulfat (Na₂S₂O₃):</b> Berperan utama sebagai zat penitar/titran penentu kuantitas DO.</li>
            <li><b>Indikator pati (amilum):</b> Menunjukkan titik akhir jalannya titrasi secara visual melalui hilangnya kompleks warna biru.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    # ------------------------------------------
    # SUB-BAGIAN: ALAT & BAHAN UJI COD
    # ------------------------------------------
    elif pilihan_materi == "Daftar Alat & Bahan Uji COD":
        st.markdown("### 🔥 Komponen Analisis Uji COD (Chemical Oxygen Demand)")
        
        # Grid Tampilan Alat Uji COD (Menggunakan Layout Columns Sesuai Gambar Alat COD.jpg)
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.markdown("<div class='card'><h4>⚗️ Labu Refluks</h4><p style='font-size:12px;'>Wadah reaksi destruksi.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Florentine_flask.jpg/120px-Florentine_flask.jpg", use_container_width=True)
            with st.expander("📖 Fungsi & Pakai"):
                st.write("Tempat terjadinya proses pemutusan ikatan rantai senyawa karbon organik menggunakan campuran oksidator kuat.")
                
        with col2:
            st.markdown("<div class='card'><h4>🧪 Kondensor Refluks</h4><p style='font-size:12px;'>Pendingin balik uap asam.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Liebig_condenser_labeled.svg/220px-Liebig_condenser_labeled.svg.png", use_container_width=True)
            with st.expander("📖 Fungsi & Pakai"):
                st.write("Mengembunkan kembali uap asam sulfat pekat yang menguap agar tidak terbuang bebas ke udara luar.")
                
        with col3:
            st.markdown("<div class='card'><h4>♨️ Hot Plate / Pemanas</h4><p style='font-size:12px;'>Digesti sampel pada ±150°C.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Laboratory_hot_plate.jpg/220px-Laboratory_hot_plate.jpg", use_container_width=True)
            with st.expander("📖 Fungsi & Pakai"):
                st.write("Sumber panas konstan untuk mendidihkan campuran cairan destruksi selama durasi waktu 2 jam.")
                
        with col4:
            st.markdown("<div class='card'><h4>⚗️ Erlenmeyer (250 mL)</h4><p style='font-size:12px;'>Tempat titrasi sisa dikromat.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Erlenmeyer_flask.jpg/220px-Erlenmeyer_flask.jpg", use_container_width=True)
            with st.expander("📖 Fungsi & Pakai"):
                st.write("Tempat menampung filtrat hasil destruksi dingin yang siap direaksikan dengan larutan titran FAS.")
                
        with col5:
            st.markdown("<div class='card'><h4>🧪 Buret Hidro</h4><p style='font-size:12px;'>Titrasi dengan larutan FAS.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Burette.png/220px-Burette.png", use_container_width=True)
            with st.expander("📖 Fungsi & Pakai"):
                st.write("Mengukur secara teliti mililiter pemakaian larutan garam FAS sampai indikator berubah warna merah coklat.")

        col6, col7, col8, col9, col10 = st.columns(5)
        
        with col6:
            st.markdown("<div class='card'><h4>🧪 Pipet Volumetrik</h4><p style='font-size:12px;'>Mengambil volume reagen.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Pipettes_with_bulbs.jpg/220px-Pipettes_with_bulbs.jpg", use_container_width=True)
            with st.expander("📖 Fungsi & Pakai"):
                st.write("Mengambil porsi volume sampel air limbah dan kalium dikromat standar secara mengikat dan kuantitatif.")
                
        with col7:
            st.markdown("<div class='card'><h4>🧪 Gelas Ukur</h4><p style='font-size:12px;'>Ukur volume reagen kasar.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Graduated_cylinder.jpg/180px-Graduated_cylinder.jpg", use_container_width=True)
            with st.expander("📖 Fungsi & Pakai"):
                st.write("Mengukur asam sulfat pekat pembawa katalisator di lemari asam sebelum dicampurkan.")
                
        with col8:
            st.markdown("<div class='card'><h4>📐 Corong Kaca</h4><p style='font-size:12px;'>Membantu pindah larutan.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Glass_funnel.jpg/180px-Glass_funnel.jpg", use_container_width=True)
            with st.expander("📖 Fungsi & Pakai"):
                st.write("Mencegah terjadinya tumpahan cairan korosif berbahaya di luar bibir mulut wadah labu.")
                
        with col9:
            st.markdown("<div class='card'><h4>🗼 Statif & Klem</h4><p style='font-size:12px;'>Menopang buret & refluks.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Retort_stand.jpg/120px-Retort_stand.jpg", use_container_width=True)
            with st.expander("📖 Fungsi & Pakai"):
                st.write("Menjaga posisi leher labu dan pendingin balik agar tetap kokoh bertautan di atas hotplate.")
                
        with col10:
            st.markdown("<div class='card'><h4>🧴 Botol Semprot</h4><p style='font-size:12px;'>Pembilasan sisa alat gelas.</p></div>", unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Wash_bottle.jpg/150px-Wash_bottle.jpg", use_container_width=True)
            with st.expander("📖 Fungsi & Pakai"):
                st.write("Menyemprotkan air bebas ion untuk membilas sisa zat reagen yang menempel di dinding dalam alat.")

        st.markdown("<div class='card'><h4>🌡️ Komponen Tambahan (Opsional)</h4><p>• <b>Termometer:</b> Memastikan temperatur operasional destilasi berjalan di kisaran suhu yang tepat.</p></div>", unsafe_allow_html=True)

        # Bagian Daftar Bahan Kimia COD
        st.markdown("""
        <div class='card' style='border-left: 5px solid #0077b6;'>
        <h3>📋 Daftar Bahan Kimia yang Digunakan (Uji COD)</h3>
        <ul>
            <li><b>Sampel air limbah / air uji:</b> Sumber utama material organik yang hendak ditentukan nilai kebutuhan oksigen kimiawinya.</li>
            <li><b>Kalium dikromat (K₂Cr₂O₇):</b> Berperan vital sebagai agen oksidator utama penyerang senyawa organik.</li>
            <li><b>Asam sulfat pekat (H₂SO₄):</b> Memberikan kondisi keasaman ekstrem yang memicu daya kerja oksidasi dikromat.</li>
            <li><b>Perak sulfat (Ag₂SO₄):</b> Bertindak sebagai katalisator untuk mempercepat laju pembongkaran rantai karbon organik.</li>
            <li><b>Merkuri sulfat (HgSO₄):</b> Bahan spesifik yang mengikat gangguan ion klorida (menghindari interferensi pembacaan Cl⁻).</li>
            <li><b>Larutan FAS (Ferrous Ammonium Sulfate):</b> Bertindak sebagai agen pereduksi sisa dikromat sekaligus larutan titran resmi.</li>
            <li><b>Indikator ferroin:</b> Senyawa kompleks penentu titik akhir reaksi (perubahan warna: biru-kehijauan menjadi coklat-kemerahan).</li>
            <li><b>Aquadest / air bebas ion:</b> Digunakan sebagai cairan blanko pembanding dan pelarut utama.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.success("✨ Seluruh informasi gambar, fungsi alat, dan daftar reagen telah disesuaikan dengan instruksi kerja laboratorium!")

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
