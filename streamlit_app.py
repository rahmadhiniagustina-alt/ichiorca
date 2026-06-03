import streamlit as st

# Config Halaman Utama
st.set_page_config(page_title="Eco-Analyst Quest", page_icon="🌊", layout="wide")

# ==========================================
# 🛠️ SIDEBAR NAVIGATION (Menu Samping Yang Lucu)
# ==========================================
st.sidebar.image("https://fonts.gstatic.com/s/e/notoemoji/latest/1f9ea/512.webp", width=80) # Icon Tabung Reaksi Animasi
st.sidebar.markdown("## 🕵️‍♂️ Menu Detektif")
st.sidebar.write("Selesaikan semua misi untuk menyelamatkan lingkungan!")

# Fitur selectbox untuk memisahkan menu
menu = st.sidebar.radio(
    "Pilih Ruangan:",
    [
        "🏠 1. Pusat Komando (Beranda)", 
        "📚 2. Buku Saku Analis (Materi)", 
        "🧪 3. Lab Virtual (Uji DO & BOD)", 
        "🔥 4. Lab Virtual (Uji COD)",
        "⚙️ 5. Stasiun Pengolahan (Solusi)"
    ]
)

st.sidebar.write("---")
st.sidebar.caption("🎮 *Tugas Logida & Pemrograman Komputer - Analisis Kimia*")

# ==========================================
# JALUR LOGIKA MENU (IF-ELIF-ELSE)
# ==========================================

# --- MENU 1: BERANDA ---
if menu == "🏠 1. Pusat Komando (Beranda)":
    st.title("🧪 Eco-Analyst Quest: Detektif Air 🌊")
    st.markdown("### *Selamat Datang di Pusat Komando Analis Muda!* 🛡️")
    
    st.write("")
    st.info("👋 **Halo Analis Keren!** Sungai-sungai di Indonesia sedang dalam bahaya karena limbah tak berizin. Pilih lokasi misimu hari ini:")
    
    lokasi = st.selectbox("🗺️ Pilih Lokasi Kasus Nyata:", ["---", "📍 Sungai Citarum (Limbah Tekstil)", "📍 Teluk Jakarta (Limbah Domestik Kota)"])
    
    if lokasi != "---":
        st.success(f"🚀 **Misi Dipilih:** Anda akan diberangkatkan menuju **{lokasi}**. Siapkan buret dan erlenmeyermu!")

# --- MENU 2: MATERI ---
elif menu == "📚 2. Buku Saku Analis (Materi)":
    st.title("📚 Buku Saku Analis Lingkungan")
    st.write("Pelajari senjata analisamu di sini sebelum masuk ke laboratorium fisik:")
    
    # Menggunakan fitur tab agar materi terlihat rapi dan tidak penuh
    tab1, tab2, tab3 = st.tabs(["💧 Oksigen Terlarut (DO)", "🦠 Kebutuhan Oksigen Biologi (BOD)", "⚗️ Kebutuhan Oksigen Kimia (COD)"])
    
    with tab1:
        st.markdown("### 🐠 DO (Dissolved Oxygen)")
        st.write("DO adalah jumlah oksigen murni yang larut di dalam air. Semakin tinggi nilai DO, air semakin segar dan ikan-ikan semakin bahagia! 🐟")
        st.warning("⚠️ *Metode Analisis:* Titrasi Iodometri (Winkler) menggunakan amilum sebagai indikator.")
        
    with tab2:
        st.markdown("### 🧫 BOD (Biochemical Oxygen Demand)")
        st.write("BOD adalah banyaknya oksigen yang dibutuhkan oleh mikroorganisme untuk memakan zat organik. Jika BOD tinggi, berarti bakteri sedang pesta pora karena airnya penuh kotoran!")
        st.warning("⚠️ *Metode Analisis:* Selisih nilai DO hari ke-0 ($DO_0$) dengan DO setelah inkubasi 5 hari ($DO_5$).")

    with tab3:
        st.markdown("### 🔥 COD (Chemical Oxygen Demand)")
        st.write("COD adalah jumlah oksigen yang dibutuhkan untuk menghancurkan limbah secara kimiawi menggunakan oksidator kuat seperti Kalium Bikromat ($K_2Cr_2O_7$).")
        st.warning("⚠️ *Metode Analisis:* Refluks terbuka diikuti titrasi balik menggunakan larutan FAS dengan indikator Ferroin.")

# --- MENU 3: LAB DO & BOD ---
elif menu == "🧪 3. Lab Virtual (Uji DO & BOD)":
    st.title("🧪 Meja Analisis DO & BOD (Metode Winkler)")
    st.write("Mari lakukan titrasi manual untuk mengukur kadar oksigen terlarut.")
    
    st.caption("*(Gunakan slider di bawah untuk meniru volume tetesan tiosulfat dari buret)*")
    v_tiosulfat = st.slider("📐 Volume Na₂S₂O₃ terpakai (mL):", 0.0, 15.0, 6.2, step=0.1)
    
    # Rumus simulasi DO sederhana
    hasil_do = (v_tiosulfat * 0.1 * 8 * 1000) / 250 # Asumsi volume botol winkler 250 mL
    st.metric("Hasil DO Hari Ini", f"{hasil_do:.2f} mg/L")

# --- MENU 4: LAB COD ---
elif menu == "🔥 4. Lab Virtual (Uji COD)":
    st.title("🔥 Meja Analisis COD (Titrasi Balik)")
    st.write("Zat organik sudah direfluks panas bersama asam sulfat. Sekarang saatnya menitrasi sisa bikromat!")
    
    v_blanko = st.slider("📐 Volume FAS untuk Blanko (mL):", 15.0, 25.0, 20.0, step=0.1)
    v_sampel = st.slider("🧪 Volume FAS untuk Sampel Air (mL):", 5.0, 20.0, 11.2, step=0.1)
    
    # Hitung COD
    hasil_cod = ((v_blanko - v_sampel) * 0.1 * 8 * 1000) / 50
    st.metric("Kadar COD Hasil Analisis", f"{hasil_cod:.2f} mg/L")
    
    # Simpan angka COD secara otomatis agar bisa dipakai di menu 5
    st.session_state['hasil_cod'] = hasil_cod

# --- MENU 5: SOLUSI & PENGOLAHAN ---
elif menu == "⚙️ 5. Stasiun Pengolahan (Solusi)":
    st.title("⚙️ Stasiun Akhir: Rekayasa & Solusi")
    
    # Mengambil data dari Menu 4 (jika belum diisi, otomatis diset 150 mg/L)
    cod_tercatat = st.session_state.get('hasil_cod', 150.0)
    st.info(f"📋 Data Masuk dari Lab COD: **{cod_tercatat:.2f} mg/L**")
    
    debit = st.number_input("🚛 Masukkan Debit Air Limbah (m³/hari):", min_value=1, value=400)
    beban = (cod_tercatat * debit) / 1000
    st.write(f"⚖️ Beban pencemaran yang masuk ke sungai: **{beban:.2f} kg COD/hari**")
    
    st.write("---")
    metode = st.selectbox("🛠️ Pilih Metode IPAL Konvensional:", ["---", "Koagulasi-Flokulasi", "Lumpur Aktif"])
    
    if metode == "Lumpur Aktif":
        st.balloons() # Efek animasi lucu!
        st.success("🎉 **Bakteri Aerob Berhasil Bekerja!** Kadar COD turun 85% dan air sekarang AMAN dibuang ke lingkungan!")
