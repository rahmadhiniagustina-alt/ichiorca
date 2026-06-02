import streamlit as st
import time

# ==========================================
# 1. MANAGEMENT HALAMAN & THEME CYBERPUNK
# ==========================================
st.set_page_config(
    page_title="EnvironForensic Pro v5.0",
    page_icon="🧪",
    layout="wide"
)

# CSS Kustom untuk Tampilan Premium Gelap ala OrganIQ dengan Efek Glow Kartu Kasus
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&family=JetBrains+Mono:wght@400;700&display=swap');
    
    [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #0A0E17 !important;
        color: #E2E8F0 !important;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    [data-testid="stSidebar"] {
        background-color: #111827 !important;
        border-right: 2px solid #1F2937;
    }
    
    .app-brand {
        font-size: 32px;
        font-weight: 800;
        background: linear-gradient(135deg, #10B981 0%, #06B6D4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .lab-card {
        background-color: #161E2E;
        border: 1px solid #1F2937;
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 15px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    }
    
    /* Grid Kartu Pemilihan Kasus Utama */
    .case-selection-card {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border: 2px solid #334155;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    .case-selection-card:hover {
        border-color: #06B6D4;
        box-shadow: 0 0 15px rgba(6, 182, 212, 0.3);
        transform: translateY(-3px);
    }
    
    .stTextInput input, .stNumberInput input {
        background-color: #1F2937 !important;
        color: #38BDF8 !important;
        border: 1px solid #374151 !important;
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #06B6D4 0%, #0891B2 100%);
        color: white !important;
        font-weight: 600;
        border-radius: 12px;
        padding: 12px;
        border: none;
        box-shadow: 0 4px 14px rgba(6, 182, 212, 0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #22D3EE 0%, #06B6D4 100%);
        box-shadow: 0 6px 20px rgba(6, 182, 212, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. INISIALISASI STATE UTAMA GAME
# ==========================================
if "current_view" not in st.session_state: st.session_state.current_view = "MAIN_MENU" # Panduan Halaman Depan
if "hp" not in st.session_state: st.session_state.hp = 3
if "score" not in st.session_state: st.session_state.score = 100
if "collected_sample" not in st.session_state: st.session_state.collected_sample = ""
if "lab_step" not in st.session_state: st.session_state.lab_step = "INPUT_REAGEN"
if "do_calculated" not in st.session_state: st.session_state.do_calculated = 0.0
if "case1_cleared" not in st.session_state: st.session_state.case1_cleared = False
if "show_edu_material" not in st.session_state: st.session_state.show_edu_material = False

def apply_penalty(reason):
    st.session_state.hp -= 1
    st.session_state.score -= 20
    st.toast(f"❌ Kesalahan: {reason}! HP berkurang.", icon="🚨")

def back_to_menu():
    st.session_state.current_view = "MAIN_MENU"
    st.session_state.hp = 3
    st.session_state.score = 100
    st.session_state.collected_sample = ""
    st.session_state.lab_step = "INPUT_REAGEN"
    st.session_state.do_calculated = 0.0
    st.session_state.show_edu_material = False

# ==========================================
# 3. SIDEBAR UTAMA & MUSIK (TIDAK DIHILANGKAN)
# ==========================================
with st.sidebar:
    st.markdown("<div class='app-brand'>🕵️‍♂️ DETEKTIF HUD</div>", unsafe_allow_html=True)
    st.write("---")
    c_hp, c_sc = st.columns(2)
    c_hp.metric(label="❤️ Sisa HP", value=f"{st.session_state.hp} / 3")
    c_sc.metric(label="⭐ Skor Analisis", value=st.session_state.score)
    
    st.write("---")
    st.markdown("### 📖 Buku Rumus Analisis Kimia")
    with st.expander("Rumus DO (Titrasi Winkler) 🧪"):
        st.write("Untuk mencari kadar DO Air, gunakan rumus penyederhanaan berikut:")
        st.code("DO (mg/L) = Volume Titran (mL) * 2", language="markdown")
        
    st.write("---")
    st.markdown("### 🎵 Atmosfer Investigasi")
    # Musik dimainkan otomatis secara melingkar (loop) di latar belakang
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3", format="audio/mp3", loop=True)
    
    st.write("---")
    if st.session_state.current_view != "MAIN_MENU":
        if st.button("🚪 Keluar ke Halaman Depan"):
            back_to_menu()
            st.rerun()

# ==========================================
# 4. LOGIKA UTAMA PERCABANGAN HALAMAN
# ==========================================
st.markdown("<div class='app-brand'>EnvironForensic Lab v5.0</div>", unsafe_allow_html=True)
st.write("---")

# ---------------------------------------------------------------------
# HALAMAN 1: HALAMAN DEPAN / PEMILIHAN 5 KASUS (MAIN MENU)
# ---------------------------------------------------------------------
if st.session_state.current_view == "MAIN_MENU":
    st.markdown("### 📁 Pilih Berkas Kasus Kriminal Lingkungan Anda:")
    st.write("Selamat datang Inspektur. Pilih salah satu berkas perkara aktif di bawah ini untuk memulai operasi forensik kimia:")
    
    # Grid Kasus 1, 2, 3
    col_k1, col_k2, col_k3 = st.columns(3)
    
    with col_k1:
        st.markdown("""
        <div class='case-selection-card'>
            <h3>🌊 Kasus 1</h3>
            <p><strong>Polusi Organik Sungai Citarum</strong></p>
            <p><span style='color: #10B981;'>🔓 Terbuka (Misi Aktif)</span></p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Buka Berkas Kasus 1", key="open_c1"):
            st.session_state.current_view = "KASUS_1"
            st.rerun()
            
    with col_k2:
        status_k2 = "🔓 Terbuka" if st.session_state.case1_cleared else "🔒 Terkunci"
        color_k2 = "#10B981" if st.session_state.case1_cleared else "#EF4444"
        st.markdown(f"""
        <div class='case-selection-card'>
            <h3>🌋 Kasus 2</h3>
            <p><strong>Tragedi Merkuri Teluk Buyat</strong></p>
            <p><span style='color: {color_k2};'>{status_k2}</span></p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Buka Berkas Kasus 2", key="open_c2"):
            if st.session_state.case1_cleared:
                st.session_state.current_view = "KASUS_2"
                st.rerun()
            else:
                st.error("Selesaikan Kasus 1 terlebih dahulu untuk membuka kunci Kasus 2!")
                
    with col_k3:
        st.markdown("""
        <div class='case-selection-card'>
            <h3>🛢️ Kasus 3</h3>
            <p><strong>Tumpahan Minyak Montara</strong></p>
            <p><span style='color: #EF4444;'>🔒 Terkunci (Sistem MA)</span></p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Berkas Disegel", key="lock_c3", disabled=True)

    # Grid Kasus 4 & 5
    st.write("")
    col_k4, col_k5, col_empty = st.columns(3)
    with col_k4:
        st.markdown("""
        <div class='case-selection-card'>
            <h3>🧪 Kasus 4</h3>
            <p><strong>Kebocoran Sianida Tambang Emas</strong></p>
            <p><span style='color: #EF4444;'>🔒 Terkunci (Sistem MA)</span></p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Berkas Disegel", key="lock_c4", disabled=True)
        
    with col_k5:
        st.markdown("""
        <div class='case-selection-card'>
            <h3>🌾 Kasus 5</h3>
            <p><strong>Eutrofikasi Massal Danau Toba</strong></p>
            <p><span style='color: #EF4444;'>🔒 Terkunci (Sistem MA)</span></p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Berkas Disegel", key="lock_c5", disabled=True)

# ---------------------------------------------------------------------
# HALAMAN 2: JALUR UTAMA GAMEPLAY KASUS 1 (CITARUM)
# ---------------------------------------------------------------------
elif st.session_state.current_view == "KASUS_1":
