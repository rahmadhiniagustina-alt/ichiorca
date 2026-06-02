import streamlit as st

# ==========================================
# 1. MANAGEMENT HALAMAN & THEME CYBERPUNK
# ==========================================
st.set_page_config(
    page_title="EnvironForensic Pro v5.0",
    page_icon="🧪",
    layout="wide"
)

# CSS Kustom ala OrganIQ
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=400;600;700&family=JetBrains+Mono:wght=400;700&display=swap');
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
    }
    .case-selection-card {
        background: linear-gradient(135deg, #1E293B 0%, #0F172A 100%);
        border: 2px solid #334155;
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        margin-bottom: 20px;
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
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. INISIALISASI STATE UTAMA GAME
# ==========================================
if "current_view" not in st.session_state: st.session_state.current_view = "MAIN_MENU"
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
# 3. SIDEBAR UTAMA & MUSIK BACKGROUND
# ==========================================
with st.sidebar:
    st.markdown("<div class='app-brand'>🕵️‍♂️ DETEKTIF HUD</div>", unsafe_allow_html=True)
    st.write("---")
    c_hp, c_sc = st.columns(2)
    c_hp.metric(label="❤️ Sisa HP", value=f"{st.session_state.hp} / 3")
    c_sc.metric(label="⭐ Skor Analisis", value=st.session_state.score)
    
    st.write("---")
    st.markdown("### 📖 Buku Rumus Kimia")
    with st.expander("Rumus DO (Titrasi Winkler) 🧪"):
        st.write("Mencari kadar DO Air:")
        st.code("DO (mg/L) = Volume Titran (mL) * 2", language="markdown")
        
    st.write("---")
    st.markdown("### 🎵 Atmosfer Investigasi")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3", format="audio/mp3", loop=True)
    
    st.write("---")
    if st.session_state.current_view != "MAIN_MENU":
        if st.button("🚪 Keluar ke Beranda"):
            back_to_menu()
            st.rerun()

# ==========================================
# 4. LOGIKA UTAMA JALUR HALAMAN
# ==========================================
st.markdown("<div class='app-brand'>EnvironForensic Lab v5.0</div>", unsafe_allow_html=True)
st.write("---")

# --- MENU UTAMA: PEMILIHAN KASUS ---
if st.session_state.current_view == "MAIN_MENU":
    st.markdown("### 📁 Pilih Berkas Kasus Kriminal Lingkungan:")
    
    col_k1, col_k2, col_k3 = st.columns(3)
    with col_k1:
        st.markdown("<div class='case-selection-card'><h3>🌊 Kasus 1</h3><p><strong>Polusi Organik Citarum</strong></p><p><span style='color: #10B981;'>🔓 Terbuka</span></p></div>", unsafe_allow_html=True)
        if st.button("Buka Kasus 1", key="open_c1"):
            st.session_state.current_view = "KASUS_1"
            st.rerun()
            
    with col_k2:
        status_k2 = "🔓 Terbuka" if st.session_state.case1_cleared else "🔒 Terkunci"
        color_k2 = "#10B981" if st.session_state.case1_cleared else "#EF4444"
        st.markdown(f"<div class='case-selection-card'><h3>🌋 Kasus 2</h3><p><strong>Tragedi Merkuri Buy
