import streamlit as st
import pandas as pd

# ==========================================
# 0. KONFIGURASI HALAMAN & STATE MANAGEMENT
# ==========================================
st.set_page_config(page_title="ModulDigital-Oxy", page_icon="🧪", layout="wide")

# Inisialisasi Session State untuk Simulasi & Kuis agar data tidak hilang saat refresh/pindah menu
if "sim_step_do" not in st.session_state: st.session_state.sim_step_do = 1
if "sim_step_bod" not in st.session_state: st.session_state.sim_step_bod = 1
if "sim_step_cod" not in st.session_state: st.session_state.sim_step_cod = 1
if "quiz_submitted" not in st.session_state: st.session_state.quiz_submitted = False

# ==========================================
# NAVIGATION BAR (SIDEBAR)
# ==========================================
st.sidebar.title("📌 ModulDigital-Oxy")
st.sidebar.write("Aplikasi Edukasi Analisis Kualitas Air")
menu = st.sidebar.radio(
    "Pilih Menu Pembelajaran:",
    ["Home & Pendahuluan", "Menu 1 — Teori", "Menu 2 — Alat & Bahan", "Menu 3 — Simulasi Praktikum", "Menu 4 — Kalkulator", "Menu 5 — Interpretasi Hasil", "Menu 6 — Kuis & Evaluasi"]
)

st.sidebar.markdown("---")
st.sidebar.caption("Sistem Penjaminan Mutu Industri - Politeknik AKA Bogor")

# ==========================================
# HOME / PENDAHULUAN
# ==========================================
if menu == "Home & Pendahuluan":
    st.title("🧪 Selamat Datang di ModulDigital-Oxy")
    st.markdown("""
    Kualitas air merupakan salah satu faktor penting yang menentukan kelayakan air untuk berbagai keperluan. 
    Aplikasi ini dirancang sebagai media pembelajaran interaktif virtual untuk menguasai tiga parameter utama kualitas air:
    * **DO** *(Dissolved Oxygen)*
    * **BOD** *(Biochemical Oxygen Demand)*
    * **COD** *(Chemical Oxygen Demand)*
    
    Silakan gunakan menu di sebelah kiri untuk mulai mengeksplorasi materi, melakukan simulasi laboratorium virtual, hingga menguji kemampuan Anda pada menu kuis!
    """)
    st.info("💡 **Tips:** Untuk pengalaman belajar terbaik, pelajari materi secara berurutan mulai dari Menu 1 hingga Menu 6.")

# ==========================================
# MENU 1 — TEORI
# ==========================================
elif menu == "Menu 1 — Teori":
    st.title("📚 Menu 1 — Teori Reaksi & Prinsip Analisis")
    
    tab_do, tab_bod, tab_cod = st.tabs(["💧 Uji DO (Metode Winkler)", "🌱 Uji BOD", "🔥 Uji COD"])
    
    with tab_do:
        st.header("Uji DO (Dissolved Oxygen) – Metode Winkler")
        st.markdown("**Prinsip:**")
        st.write("Jumlah iodin yang terbentuk sebanding dengan jumlah oksigen terlarut dalam sampel. Metode Winkler menentukan kadar oksigen terlarut melalui pembentukan iodin yang kemudian dititrasi dengan natrium tiosulfat.")
        
        st.markdown("**Tahapan Reaksi Kimia:**")
        st.markdown("""
        * **a. Pembentukan endapan mangan(II) hidroksida**
          $$\\text{MnSO}_4 + 2\\text{KOH} \\rightarrow \\text{Mn(OH)}_2 + \\text{K}_2\\text{SO}_4$$
        * **b. Oksidasi mangan oleh oksigen terlarut**
          $$2\\text{Mn(OH)}_2 + \\text{O}_2 \\rightarrow 2\\text{MnO(OH)}_2$$
        * **c. Pembebasan iodin dalam suasana asam**
          $$\\text{MnO(OH)}_2 + 2\\text{I}^- + 4\\text{H}^+ \\rightarrow \\text{Mn}^{2+} + \\text{I}_2 + 3\\text{H}_2\\text{O}$$
        * **d. Titrasi iodin dengan natrium tiosulfat**
          $$\\text{I}_2 + 2\\text{Na}_2\\text{S}_2\\text{O}_3 \\rightarrow 2\\text{NaI} + \\text{Na}_2\\text{S}_4\\text{O}_6$$
        """)

    with tab_bod:
        st.header("Uji BOD (Biochemical Oxygen Demand)")
        st.markdown("**Prinsip:**")
        st.write("Mikroorganisme menggunakan oksigen terlarut untuk menguraikan bahan organik. Penurunan DO selama inkubasi 5 hari digunakan untuk menghitung nilai BOD. BOD tidak melibatkan satu reaksi kimia tertentu, melainkan proses biologis oleh mikroorganisme aerob.")
        
        st.markdown("**Reaksi Umum:**")
        st.markdown("""
        $$\\text{Bahan Organik} + \\text{O}_2 \\xrightarrow{\\text{Mikroorganisme}} \\text{CO}_2 + \\text{H}_2\\text{O} + \\text{Energi}$$
        
        *Contoh Sederhana (Oksidasi Glukosa):*
        $$\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\rightarrow 6\\text{CO}_2 + 6\\text{H}_2\\text{O}$$
        """)

    with tab_cod:
        st.header("Uji COD (Chemical Oxygen Demand)")
        st.markdown("**Prinsip:**")
        st.write("Semakin banyak bahan organik dalam sampel, semakin banyak kalium dikromat yang bereaksi sehingga nilai COD semakin tinggi. Pada metode COD, senyawa organik dioksidasi oleh kalium dikromat dalam suasana asam.")
        
        st.markdown("**Tahapan Reaksi Kimia:**")
        st.markdown("""
        * **a. Oksidasi bahan organik oleh dikromat (Reaksi Umum)**
          $$\\text{Bahan Organik} + \\text{Cr}_2\\text{O}_7^{2-} + \\text{H}^+ \\rightarrow \\text{CO}_2 + \\text{H}_2\\text{O} + \\text{Cr}^{3+}$$
        * **b. Reduksi ion dikromat**
          $$\\text{Cr}_2\\text{O}_7^{2-} + 14\\text{H}^+ + 6\\text{e}^- \\rightarrow 2\\text{Cr}^{3+} + 7\\text{H}_2\\text{O}$$
          *(Catatan: Warna larutan berubah dari oranye $\\text{Cr}_2\\text{O}_7^{2-}$ menjadi hijau $\\text{Cr}^{3+}$)*
        * **c. Titrasi sisa dikromat dengan FAS**
          $$\\text{Cr}_2\\text{O}_7^{2-} + 6\\text{Fe}^{2+} + 14\\text{H}^+ \\rightarrow 2\\text{Cr}^{3+} + 6\\text{Fe}^{3+} + 7\\text{H}_2\\text{O}$$
        """)

# ==========================================
# MENU 2 — ALAT & BAHAN
# ==========================================
elif menu == "Menu 2 — Alat & Bahan":
    st.title("🧪 Menu 2 — Daftar Alat & Bahan Laboratorium")
    st.write("Pengujian kualitas air memerlukan alat laboratorium yang presisi dan reagen kimia yang spesifik.")
    
    pilihan_uji = st.selectbox("Pilih Parameter Uji:", ["Uji DO (Dissolved Oxygen)", "Uji BOD (Biochemical Oxygen Demand)", "Uji COD (Chemical Oxygen Demand)"])
    
    if pilihan_uji == "Uji DO (Dissolved Oxygen)":
        st.subheader("📋 Alat & Bahan untuk Analisis DO Winkler")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**🛠️ Alat & Fungsi:**")
            st.markdown("""
            1. **Botol DO/BOD (300 mL):** Menampung sampel air dan mencegah kontak dengan udara luar.
            2. **Buret:** Meneteskan larutan natrium tiosulfat secara akurat saat titrasi.
            3. **Erlenmeyer:** Wadah menampung larutan saat proses titrasi sampel.
            4. **Pipet Volumetrik:** Mengambil volume reagen kimia secara tepat.
            5. **Gelas Ukur:** Mengukur volume larutan/sampel secara umum.
            6. **Statif dan Klem:** Menopang buret agar berdiri kokoh selama titrasi.
            """)
        with col2:
            st.markdown("**🧪 Bahan & Fungsi:**")
            st.markdown("""
            1. **Sampel Air:** Objek analisis kandungan oksigen terlarutnya.
            2. **Larutan Mangan(II) Sulfat ($\text{MnSO}_4$):** Mengikat oksigen terlarut menjadi endapan mangan teroksidasi.
            3. **Larutan Alkali Iodida-Azida:** Menyediakan suasana basa, menyumbang ion iodida, dan menghilangkan gangguan ion nitrit.
            4. **Asam Sulfat Pekat ($\text{H}_2\text{SO}_4$):** Melarutkan kembali endapan dan membebaskan iodin bebas.
            5. **Natrium Tiosulfat ($\text{Na}_2\text{S}_2\text{O}_3$):** Sebagai larutan standar/titran untuk menetapkan iodin.
            6. **Indikator Amilum:** Penanda titik akhir titrasi (perubahan warna biru menjadi jernih/tidak berwarna).
            """)

    elif pilihan_uji == "Uji BOD (Biochemical Oxygen Demand)":
        st.subheader("📋 Alat & Bahan untuk Analisis BOD")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**🛠️ Alat & Fungsi:**")
            st.markdown("""
            1. **Botol BOD 300 mL:** Menampung sampel selama masa inkubasi.
            2. **Inkubator BOD ($20^\circ\text{C}$):** Menjaga suhu lingkungan pengerjaan konstan selama 5 hari.
            3. **Buret, Erlenmeyer, Pipet, Gelas Ukur:** Digunakan untuk rangkaian pengukuran kadar DO awal dan DO akhir.
            """)
        with col2:
            st.markdown("**🧪 Bahan & Fungsi:**")
            st.markdown("""
            1. **Sampel Air:** Sampel uji organik yang akan dianalisis.
            2. **Air Pengencer:** Mengencerkan sampel yang memiliki konsentrasi pencemar organik tinggi.
            3. **Larutan Buffer Fosfat:** Menjaga stabilitas derajat keasaman (pH) selama inkubasi.
            4. **Larutan $\text{MgSO}_4$, $\text{CaCl}_2$, $\text{FeCl}_3$:** Menyediakan nutrisi unsur makro esensial (Magnesium, Kalsium, Besi) bagi mikroorganisme.
            5. **Seed Mikroorganisme:** Menambah populasi bakteri pengurai jika sampel minim mikroba asli.
            6. **Reagen Uji DO Lengkap:** Untuk mengukur kadar DO Hari ke-0 ($\text{DO}_0$) dan Hari ke-5 ($\text{DO}_5$).
            """)

    elif pilihan_uji == "Uji COD (Chemical Oxygen Demand)":
        st.subheader("📋 Alat & Bahan untuk Analisis COD")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**🛠️ Alat & Fungsi:**")
            st.markdown("""
            1. **Labu & Kondensor Refluks:** Wadah destruksi sampel dan mengembunkan uap asam agar kembali ke sistem reaksi tanpa habis menguap.
            2. **Hot Plate / Heating Mantle:** Sumber panas pemanas campuran destruksi selama refluks.
            3. **Batu Didih:** Mencegah letupan mendadak *(bumping)* akibat pemanasan lokal yang ekstrem.
            4. **Buret & Erlenmeyer:** Untuk proses titrasi kelebihan dikromat menggunakan larutan FAS.
            """)
        with col2:
            st.markdown("**🧪 Bahan & Fungsi:**")
            st.markdown("""
            1. **Kalium Dikromat ($\text{K}_2\text{Cr}_2\text{O}_7$):** Reagen oksidator kuat untuk menghancurkan bahan organik.
            2. **Asam Sulfat Pekat ($\text{H}_2\text{SO}_4$):** Menciptakan suasana asam ekstrem yang kuat untuk reaksi oksidasi.
            3. **Perak Sulfat ($\text{Ag}_2\text{SO}_4$):** Katalisator utama untuk mempercepat laju oksidasi senyawa organik rantai lurus.
            4. **Merkuri Sulfat ($\text{HgSO}_4$):** Zat penopeng *(masking agent)* untuk membebaskan gangguan interferensi dari ion klorida ($\text{Cl}^-$).
            5. **Ferrous Ammonium Sulfate (FAS):** Larutan standar penitrasi sisa kalium dikromat.
            6. **Indikator Ferroin:** Menunjukkan titik akhir titrasi secara visual.
            """)

# ==========================================
# MENU 3 — SIMULASI PRAKTIKUM
# ==========================================
elif menu == "Menu 3 — Simulasi Praktikum":
    st.title("🕹️ Menu 3 — Simulasi Laboratorium Virtual")
    
    pilihan_sim = st.selectbox("Pilih Simulasi Praktikum:", ["Simulasi 1: Pengujian DO", "Simulasi 2: Pengujian BOD5", "Simulasi 3: Pengujian COD", "Studi Kasus Interaktif"])
    
    # --- SIMULASI DO ---
    if pilihan_sim == "Simulasi 1: Pengujian DO":
        st.subheader("💧 Virtual Lab: Penetapan DO Metode Winkler")
        
        if st.session_state.sim_step_do == 1:
            st.info("💡 **Langkah 1: Pengambilan Sampel**")
            if st.button("Ambil Botol DO & Isi dengan Sampel Air hingga Penuh"):
                st.toast("Sampel berhasil dimasukkan!", icon="✅")
                st.warning("⚠️ **Pesan Sistem:** Pastikan tidak terdapat gelembung udara dalam botol karena dapat memengaruhi hasil pengukuran DO.")
                st.session_state.sim_step_do = 2
                st.rerun()
                
        elif st.session_state.sim_step_do == 2:
            st.info("💡 **Langkah 2: Penambahan Reagen Pengikat**")
            if st.button("Klik & Tambahkan 2 mL reagen MnSO₄"):
                st.success("Hasil: Larutan tetap jernih.")
                st.session_state.sim_step_do = 3
                st.rerun()
                
        elif st.session_state.sim_step_do == 3:
            st.info("💡 **Langkah 3: Pembentukan Endapan Mangan**")
            if st.button("Klik & Tambahkan 2 mL reagen Alkali Iodida-Azida"):
                st.warning("💥 Hasil: Terbentuk endapan putih yang kemudian dengan cepat berubah menjadi cokelat!")
                st.session_state.sim_step_do = 4
                st.rerun()
                
        elif st.session_state.sim_step_do == 4:
            st.info("💡 **Langkah 4: Homogenisasi**")
            if st.button("Balik botol DO beberapa kali"):
                st.success("Hasil: Endapan sekarang tersebar merata di dalam seluruh volume sampel.")
                st.session_state.sim_step_do = 5
                st.rerun()
                
        elif st.session_state.sim_step_do == 5:
            st.info("💡 **Langkah 5: Asidifikasi (Pelarutan Endapan)**")
            if st.button("Klik & Tambahkan 2 mL H₂SO Peat"):
                st.warning("💥 Hasil: Endapan larut kembali dengan sempurna dan larutan berubah menjadi kuning kecokelatan (Iodin bebas lepas).")
                st.session_state.sim_step_do = 6
                st.rerun()
                
        elif st.session_state.sim_step_do == 6:
            st.info("💡 **Langkah 6: Titrasi Kadar Oksigen**")
            st.write("Prosedur: Isi buret dengan larutan standard $\\text{Na}_2\\text{S}_2\\text{O}_3$, titrasi hingga larutan kuning pucat, tambahkan amilum (warna jadi biru), lalu teruskan titrasi sampai warna biru tepat hilang.")
            v_titran_sim = st.number_input("Masukkan Volume Hasil Titrasi Na₂S₂O₃ (mL):", min_value=0.0, value=6.4, step=0.1)
            if st.button("Konfirmasi & Hitung Hasil"):
                # Hitung otomatis simulasi dengan N=0.025 dan Vs=200mL standar
                do_sim_res = (v_titran_sim * 0.025 * 8000) / 200
                st.success(f"🎉 Simulasi Selesai! Nilai DO Terhitung = {do_sim_res:.1f} mg/L (Kualitas Air: Baik)")
                if st.button("Ulangi Simulasi DO"):
                    st.session_state.sim_step_do = 1
                    st.rerun()

    # --- SIMULASI BOD ---
    elif pilihan_sim == "Simulasi 2: Pengujian BOD5":
        st.subheader("🌱 Virtual Lab: Pengujian BOD₅")
        
        if st.session_state.sim_step_bod == 1:
            st.info("💡 **Langkah 1: Persiapan Sampel & Opsi Pengenceran**")
            opsi_penc = st.checkbox("Apakah sampel memerlukan pengenceran? (Untuk air limbah padat organik)")
            fp_val = st.number_input("Tentukan Faktor Pengenceran (FP):", min_value=1, value=1 if not opsi_penc else 10)
            if st.button("Lanjutkan ke Pengukuran DO Awal"):
                st.session_state.fp_val = fp_val
                st.session_state.sim_step_bod = 2
                st.rerun()
                
        elif st.session_state.sim_step_bod == 2:
            st.info("💡 **Langkah 2: Pengukuran DO Awal (Hari Ke-0)**")
            st.write("Pengguna menjalankan rangkaian uji Winkler seperti simulasi sebelumnya.")
            do0_sim = st.number_input("Masukkan nilai DO₀ hasil pembacaan (mg/L):", min_value=0.0, value=8.5)
            if st.button("Simpan Data DO₀ & Lanjutkan Inkubasi"):
                st.session_state.do0_sim = do0_sim
                st.session_state.sim_step_bod = 3
                st.rerun()
                
        elif st.session_state.sim_step_bod == 3:
            st.info("💡 **Langkah 3: Proses Inkubasi Virtual**")
            st.markdown("""
            Mengatur Inkubator BOD:
            * **Suhu:** $20^\circ\text{C}$
            * **Waktu:** 5 Hari
            * **Kondisi Lingkungan:** Gelap total (mencegah fotosintesis alga)
            """)
            if st.button("Mulai Inkubasi 5 Hari (Simulasi Cepat)"):
                st.toast("Inkubasi selesai!", icon="⏳")
                st.session_state.sim_step_bod = 4
                st.rerun()
                
        elif st.session_state.sim_step_bod == 4:
            st.info("💡 **Langkah 4: Pengukuran DO Akhir (Hari Ke-5)**")
            do5_sim = st.number_input("Masukkan nilai DO₅ hasil pengujian kembali (mg/L):", min_value=0.0, value=3.2)
            if st.button("Hitung Nilai Akhir BOD₅"):
                bod_calc = (st.session_state.do0_sim - do5_sim) * st.session_state.fp_val
                st.success(f"📊 Hasil Analisis: DO₀ = {st.session_state.do0_sim} mg/L, DO₅ = {do5_sim} mg/L")
                st.metric(label="Nilai BOD₅ Akhir", value=f"{bod_calc:.1f} mg/L")
                
                # Interpretasi
                if bod_calc < 3: status = "🟢 Bersih"
                elif 3 <= bod_calc <= 6: status = "🟡 Tercemar Ringan"
                elif 6 < bod_calc <= 12: status = "🟠 Tercemar Sedang"
                else: status = "🔴 Tercemar Berat"
                st.write(f"Kondisi Air Sampel: **{status}**")
                
                if st.button("Ulangi Simulasi BOD"):
                    st.session_state.sim_step_bod = 1
                    st.rerun()

    # --- SIMULASI COD ---
    elif pilihan_sim == "Simulasi 3: Pengujian COD":
        st.subheader("🔥 Virtual Lab: Destruksi & Analisis COD")
        
        if st.session_state.sim_step_cod == 1:
            st.info("💡 **Langkah 1 & 2: Pengambilan Sampel & Masking Klorida**")
            st.write("Pipet 50 mL sampel air ke dalam labu refluks, kemudian tambahkan reagen serbuk $\\text{HgSO}_4$.")
            st.caption("Pesan Sistem: $\\text{HgSO}_4$ digunakan untuk menghilangkan gangguan interferensi ion klorida.")
            if st.button("Tambahkan Sampel & HgSO₄"):
                st.session_state.sim_step_cod = 2
                st.rerun()
                
        elif st.session_state.sim_step_cod == 2:
            st.info("💡 **Langkah 3 & 4: Penambahan Oksidator & Katalis Asam**")
            st.write("Tambahkan larutan standar $\\text{K}_2\\text{Cr}_2\\text{O}_7$ (larutan langsung berubah warna menjadi **Oranye**). Tambahkan campuran asam sulfat-perak sulfat secara perlahan melalui dinding labu.")
            if st.button("Tambahkan K₂Cr₂O₇ & Campuran Katalis"):
                st.session_state.sim_step_cod = 3
                st.rerun()
                
        elif st.session_state.sim_step_cod == 3:
            st.info("💡 **Langkah 5 & 6: Proses Refluks & Pendinginan**")
            st.write("Hubungkan kondensor pendingin, masukkan batu didih, nyalakan pemanas hot plate pada suhu destruksi selama 2 jam.")
            if st.button("Nyalakan Pemanas (Mulai Refluks 2 Jam)"):
                st.warning("💥 Hasil: Proses oksidasi selesai! Warna larutan berubah dari Oranye menjadi **Hijau** (menandakan terbentuknya ion $\\text{Cr}^{3+}$).")
                st.success("Larutan didinginkan hingga mencapai suhu ruang.")
                st.session_state.sim_step_cod = 4
                st.rerun()
                
        elif st.session_state.sim_step_cod == 4:
            st.info("💡 **Langkah 7 & 8: Titrasi Balik Sisa Oksidator**")
            st.write("Tambahkan 2-3 tetes indikator ferroin ke dalam larutan hasil destruksi. Titrasi sisa dikromat menggunakan larutan standar FAS.")
            v_blanko_sim = st.number_input("Masukkan Volume FAS Blanko (A) dalam mL:", min_value=0.0, value=20.0)
            v_sampel_sim = st.number_input("Masukkan Volume FAS Sampel (B) dalam mL:", min_value=0.0, value=12.0)
            
            if st.button("Hitung Kadar COD"):
                cod_sim_res = ((v_blanko_sim - v_sampel_sim) * 0.1 * 8000) / 50
                st.metric(label="Hasil COD", value=f"{cod_sim_res:.1f} mg/L")
                
                if cod_sim_res < 25: status = "🟢 Air Bersih"
                elif 25 <= cod_sim_res <= 50: status = "🟡 Tercemar Ringan"
                elif 50 < cod_sim_res <= 100: status = "🟠 Tercemar Sedang"
                else: status = "🔴 Tercemar Berat"
                st.write(f"Kategori Kualitas Air: **{status}**")
                
                if st.button("Ulangi Simulasi COD"):
                    st.session_state.sim_step_cod = 1
                    st.rerun()

    # --- STUDI KASUS INTERAKTIF ---
    elif pilihan_sim == "Studi Kasus Interaktif":
        st.subheader("🧐 Studi Kasus Evaluasi Lapangan")
        st.markdown("""
        Diberikan sebuah data pengujian air sungai tak dikenal sebagai berikut:
        * **DO:** $2.1 \\text{ mg/L}$
        * **BOD:** $15 \\text{ mg/L}$
        * **COD:** $180 \\text{ mg/L}$
        """)
        
        q1 = st.text_input("1. Bagaimana kualitas air sampel tersebut?")
        q2 = st.text_input("2. Apakah terjadi pencemaran organik?")
        
        if st.button("Kirim Jawaban"):
            st.markdown("**🔍 Jawaban Analisis Sistem:**")
            st.success("""
            * Sampel air sungai tersebut tergolong ke dalam perairan **Tercemar Berat**.
            * **Ya**, telah terjadi pencemaran polutan organik yang sangat masif. Hal ini ditunjukkan dan dikonfirmasi langsung oleh tingginya nilai parameter BOD dan COD, yang berakibat pada drop ekstremnya kadar DO karena habis dikonsumsi mikroba pengurai.
            """)

# ==========================================
# MENU 4 — KALKULATOR
# ==========================================
elif menu == "Menu 4 — Kalkulator":
    st.title("🧮 Menu 4 — Kalkulator Parameter Otomatis")
    st.write("Gunakan menu kalkulator ini untuk memproses data mentah praktikum Anda menjadi nilai konsentrasi numerik secara instan.")
    
    tab1, tab2, tab3 = st.tabs(["Kalkulator DO", "Kalkulator BOD₅", "Kalkulator COD"])
    
    with tab1:
        st.subheader("Perhitungan Oksigen Terlarut (DO)")
        v_do = st.number_input("Volume Titran Na₂S₂O₃ (V) dalam mL:", min_value=0.0, step=0.1, value=7.0)
        n_do = st.number_input("Normalitas Reagen Na₂S₂O₃ (N):", min_value=0.0, format="%.4f", step=0.001, value=0.025)
        vs_do = st.number_input("Volume Sampel Air Teranalisis (Vs) dalam mL:", min_value=1.0, value=200.0)
        
        if st.button("Hitung Kadar DO", key="btn_do"):
            res_do = (v_do * n_do * 8000) / vs_do
            st.metric(label="Kadar DO Hasil Perhitungan", value=f"{res_do:.2f} mg/L")
            # Tautan interpretasi otomatis
            if res_do > 6: st.success("🟢 Kualitas air sangat baik.")
            elif 4 <= res_do <= 6: st.info("🟢 Kualitas air baik.")
            elif 2 <= res_do < 4: st.warning("🟡 Kualitas air tercemar sedang.")
            else: st.error("🔴 Kualitas air tercemar berat.")
            
    with tab2:
        st.subheader("Perhitungan Biochemical Oxygen Demand (BOD₅)")
        do0 = st.number_input("Kadar DO Awal Hari ke-0 (DO₀) dalam mg/L:", min_value=0.0, value=8.2)
        do5 = st.number_input("Kadar DO Akhir Hari ke-5 (DO₅) dalam mg/L:", min_value=0.0, value=4.0)
        pake_fp = st.checkbox("Gunakan Faktor Pengenceran (FP)")
        fp = st.number_input("Faktor Pengenceran (Isi 1 jika murni tanpa pengenceran):", min_value=1, value=1) if pake_fp else 1
        
        if st.button("Hitung Kadar BOD₅", key="btn_bod"):
            res_bod = (do0 - do5) * fp
            st.metric(label="Kadar BOD₅ Hasil Perhitungan", value=f"{res_bod:.2f} mg/L")
            if res_bod < 3: st.success("🟢 Tingkat pencemaran: Air bersih")
            elif 3 <= res_bod <= 6: st.info("🟡 Tingkat pencemaran: Tercemar ringan")
            elif 6 < res_bod <= 12: st.warning("🟠 Tingkat pencemaran: Tercemar sedang")
            else: st.error("🔴 Tingkat pencemaran: Tercemar berat")
            
    with tab3:
        st.subheader("Perhitungan Chemical Oxygen Demand (COD)")
        v_a = st.number_input("Volume FAS untuk Blanko (A) dalam mL:", min_value=0.0, value=20.0)
        v_b = st.number_input("Volume FAS untuk Sampel (B) dalam mL:", min_value=0.0, value=12.0)
        n_fas = st.number_input("Normalitas Larutan Standar FAS (N):", min_value=0.0, format="%.4f", value=0.1)
        vs_cod = st.number_input("Volume Sampel Air yang Direfluks (Vs) dalam mL:", min_value=1.0, value=50.0)
        
        if st.button("Hitung Kadar COD", key="btn_cod"):
            res_cod = ((v_a - v_b) * n_fas * 8000) / vs_cod
            st.metric(label="Kadar COD Hasil Perhitungan", value=f"{res_cod:.2f} mg/L")
            if res_cod < 25: st.success("🟢 Kategori: Air bersih")
            elif 25 <= res_cod <= 50: st.info("🟡 Kategori: Tercemar ringan")
            elif 50 < res_cod <= 100: st.warning("🟠 Kategori: Tercemar sedang")
            else: st.error("🔴 Kategori: Tercemar berat")

# ==========================================
# MENU 5 — INTERPRETASI HASIL
# ==========================================
elif menu == "Menu 5 — Interpretasi Hasil":
    st.title("📊 Menu 5 — Interpretasi Kualitas & Klasifikasi Air")
    st.write("Halaman ini menyajikan tabel acuan resmi penilaian baku mutu air berdasarkan nilai ketiga parameter laboratorium.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 💧 Parameter DO")
        df_do = pd.DataFrame({
            "DO (mg/L)": ["> 6", "4 – 6", "2 – 4", "< 2"],
            "Interpretasi Status": ["Sangat Baik", "Baik", "Tercemar Sedang", "Tercemar Berat"]
        })
        st.table(df_do)
        st.info("💡 **Contoh:** Jika DO = 7.2 mg/L → Air memiliki kandungan oksigen terlarut tinggi, mendukung biota air dengan sangat baik.")
        
    with col2:
        st.markdown("### 🌱 Parameter BOD")
        df_bod = pd.DataFrame({
            "BOD (mg/L)": ["< 3", "3 – 6", "6 – 12", "> 12"],
            "Interpretasi Status": ["Air Bersih", "Tercemar Ringan", "Tercemar Sedang", "Tercemar Berat"]
        })
        st.table(df_bod)
        st.warning("💡 **Contoh:** Jika BOD = 10 mg/L → Kandungan zat organik cukup tinggi, mikroba butuh banyak oksigen untuk dekomposisi.")
        
    with col3:
        st.markdown("### 🔥 Parameter COD")
        df_cod = pd.DataFrame({
            "COD (mg/L)": ["< 25", "25 – 50", "50 – 100", "> 100"],
            "Interpretasi Status": ["Air Bersih", "Tercemar Ringan", "Tercemar Sedang", "Tercemar Berat"]
        })
        st.table(df_cod)
        st.error("💡 **Contoh:** Jika COD = 150 mg/L → Polutan kimiawi tinggi, daya dukung lingkungan menurun drastis.")

    st.markdown("---")
    st.subheader("🧠 Logika Analisis Gabungan (Simultan)")
    st.write("Sistem pakar aplikasi akan membaca korelasi ketiga parameter untuk menyimpulkan kondisi ekosistem secara utuh:")
    
    cas1, cas2 = st.columns(2)
    with cas1:
        st.markdown("""
        **Kasus 1: Perairan Sehat**
        * DO: $7.0 \\text{ mg/L}$ | BOD: $2.5 \\text{ mg/L}$ | COD: $20 \\text{ mg/L}$
        * **Kesimpulan:** Kesetimbangan mantap, air bersih, biota akuatik berkembang optimal.
        """)
    with cas2:
        st.markdown("""
        **Kasus 2: Pencemaran Organik Masif**
        * DO: $2.0 \\text{ mg/L}$ | BOD: $15 \\text{ mg/L}$ | COD: $180 \\text{ mg/L}$
        * **Kesimpulan:** Air tercemar berat. Rendahnya DO akibat habis dipakai mikroorganisme mendegradasi beban polutan organik yang ekstrem.
        """)

# ==========================================
# MENU 6 — KUIS & EVALUASI
# ==========================================
elif menu == "Menu 6 — Kuis & Evaluasi":
    st.title("🎮 Menu 6 — Kuis Evaluasi Mandiri & Sertifikat")
    st.write("Uji pemahaman teoretis dan kalkulasi Anda setelah menyelesaikan seluruh rangkaian modul digital di atas.")
    
    # Input Data Pengguna untuk Sertifikat
    st.subheader("📝 Data Peserta")
    nama_user = st.text_input("Masukkan Nama Lengkap Anda (Untuk Pencetakan Sertifikat Kelulusan):", placeholder="Contoh: Budi Santoso, A.Md.Si.")
    
    st.markdown("---")
    st.subheader("📋 Bagian 1: Pilihan Ganda")
    
    q1 = st.radio("1. Apa fungsi utama pengukuran DO?", ["A. Mengukur jumlah mikroorganisme", "B. Mengukur kandungan logam berat", "C. Mengukur oksigen terlarut dalam air", "D. Mengukur pH air"])
    q2 = st.radio("2. Parameter yang menunjukkan kebutuhan oksigen oleh mikroorganisme adalah...", ["A. DO", "B. COD", "C. BOD", "D. TSS"])
    q3 = st.radio("3. Pada uji COD, reagen utama oksidator yang digunakan adalah...", ["A. KMnO₄", "B. K₂Cr₂O₇", "C. NaOH", "D. HCl"])
    q4 = st.radio("4. Parameter BOD standard umumnya diukur setelah inkubasi terkendali selama...", ["A. 1 hari", "B. 3 hari", "C. 5 hari", "D. 7 hari"])
    q5 = st.radio("5. Indikator spesifik yang digunakan pada titrasi DO metode Winkler adalah...", ["A. Metil jingga", "B. Fenolftalein", "C. Ferroin", "D. Amilum"])
    
    st.markdown("---")
    st.subheader("🧮 Bagian 2: Perhitungan & Studi Kasus")
    
    st.markdown("**Soal Hitungan DO:** Volume titran=7.0 mL, N=0.025 N, Volume sampel=200 mL. Berapa nilai DO?")
    ans_do = st.number_input("Jawaban Hitungan DO (mg/L):", min_value=0.0, step=0.1, value=0.0)
    
    st.markdown("**Soal Hitungan BOD:** Data lapangan menunjukkan nilai DO₀ = 8.2 mg/L dan DO₅ = 4.0 mg/L. Berapa nilai BOD₅?")
    ans_bod = st.number_input("Jawaban Hitungan BOD₅ (mg/L):", min_value=0.0, step=0.1, value=0.0)
    
    st.markdown("**Soal Hitungan COD:** Volume Blanko = 20 mL, Volume Sampel = 12 mL, N FAS = 0.1 N, Volume sampel air destruksi = 50 mL. Berapa COD-nya?")
    ans_cod = st.number_input("Jawaban Hitungan COD (mg/L):", min_value=0.0, step=1.0, value=0.0)
    
    st.markdown("**Studi Kasus Kontekstual:** Hasil uji air sungai: DO=1.8 mg/L, BOD=18 mg/L, COD=220 mg/L.")
    ans_kasus = st.selectbox("Bagaimana status kesimpulan akhir Anda terhadap air sungai tersebut?", ["Pilih Jawaban", "Air bersih bebas cemaran", "Air mengalami pencemaran organik tinggi & status tercemar berat", "Air mengalami pencemaran logam berat"])

    st.markdown("---")
    
    if st.button("Kirim Lembar Jawaban & Hitung Skor Akhir"):
        skor = 0
        # Cek Pilihan Ganda
        if "C. Mengukur oksigen terlarut dalam air" in q1: skor += 10
        if "C. BOD" in q2: skor += 10
        if "B. K₂Cr₂O₇" in q3: skor += 10
        if "C. 5 hari" in q4: skor += 10
        if "D. Amilum" in q5: skor += 10
        
        # Cek Perhitungan & Kasus
        if abs(ans_do - 7.0) < 0.1: skor += 15
        if abs(ans_bod - 4.2) < 0.1: skor += 15
        if abs(ans_cod - 128.0) < 0.1: skor += 15
        if ans_kasus == "Air mengalami pencemaran organik tinggi & status tercemar berat": skor += 15
        
        st.session_state.skor_akhir = skor
        st.session_state.quiz_submitted = True
        
        st.subheader("📊 Hasil Evaluasi")
        st.write(f"Skor Anda: **{skor} / 100**")
        
        if skor >= 90: st.success("🌟 Kategori: Sangat Baik! Pertahankan prestasi Anda.")
        elif 80 <= skor < 90: st.info("👍 Kategori: Baik! Anda memahami materi dengan mantap.")
        elif 70 <= skor < 80: st.warning("🗂️ Kategori: Cukup. Silakan tinjau kembali beberapa bagian formula.")
        else: st.error("📚 Kategori: Perlu Belajar Lagi. Jangan berkecil hati, silakan baca ulang Menu Teori & Jalankan ulang simulasi lab.")
        
        # FITUR BONUS: Sertifikat Virtual Sederhana
        if skor >= 80:
            st.markdown("---")
            st.balloons()
            if not nama_user:
                nama_user = "Peserta ModulDigital-Oxy"
                
            st.markdown(f"""
            <div style="border: 5px solid #4CAF50; padding: 25px; text-align: center; background-color: #f9f9f9; border-radius: 10px;">
                <h1 style="color: #4CAF50; margin: 0;">📜 SERTIFIKAT KELULUSAN</h1>
                <p style="font-size: 18px; margin: 10px 0;">Diberikan dengan hormat kepada:</p>
                <h2 style="text-decoration: underline; color: #333; margin: 5px 0;">{nama_user}</h2>
                <p style="font-size: 16px; margin: 10px 0;">Telah MENYELESAIKAN dengan hasil baik seluruh materi pembelajaran pada:</p>
                <h3 style="color: #2196F3; margin: 5px 0;">Modul Digital-Oxy: Analisis Kualitas Air (DO, BOD, dan COD)</h3>
                <p style="font-size: 14px; margin: 15px 0; font-weight: bold;">Skor Kelulusan Akhir: {skor}/100</p>
                <p style="font-size: 12px; color: #777; margin-top: 20px;">Dibuat secara otomatis oleh Sistem ModulDigital-Oxy via Streamlit</p>
            </div>
            """, unsafe_allowed_html=True)
