import streamlit as st
import pandas as pd
import time

# --- 1. KONFIGURASI HALAMAN UTAMA ---
st.set_page_config(
    page_title="Chem Detective Indonesia",
    page_icon="🕵️‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. MODIFIKASI UI/UX DENGAN CUSTOM CSS (TEMA GELAP GAME) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Special+Elite&display=swap');
    
    /* Mengubah latar belakang utama aplikasi */
    .main {
        background-color: #12161a;
        color: #ecf0f1;
    }
    
    /* Desain Judul Utama */
    .report-title {
        font-family: 'Special Elite', cursive;
        font-size: 40px;
        color: #e74c3c;
        text-align: center;
        margin-bottom: 5px;
        text-shadow: 2px 2px 4px #000000;
    }
    
    /* Desain Sub-Judul */
    .sub-title {
        font-family: 'Share Tech Mono', monospace;
        color: #bdc3c7;
        text-align: center;
        font-size: 15px;
        letter-spacing: 2px;
        margin-bottom: 30px;
    }
    
    /* Desain Judul Papan Kasus */
    .case-board-title {
        font-family: 'Special Elite', cursive;
        color: #f39c12;
        border-bottom: 2px dashed #f39c12;
        padding-bottom: 10px;
        margin-top: 20px;
    }
    
    /* Kartu Pilihan Kasus Interaktif (Bisa Hover) */
    .interactive-card {
        background: linear-gradient(145deg, #1e252b, #171d22);
        border: 1px solid #34495e;
        border-radius: 12px;
        padding: 22px;
        margin-bottom: 15px;
        transition: all 0.3s ease-in-out;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.5);
    }
    .interactive-card:hover {
        transform: translateY(-5px);
        border-color: #e74c3c;
        box-shadow: 0px 0px 20px rgba(231, 76, 60, 0.4);
    }
    
    /* Lencana Status Kasus */
    .case-badge {
        color: white;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: bold;
        font-family: 'Share Tech Mono', monospace;
    }
    
    /* Kotak Tampilan Petunjuk & Edukasi */
    .clue-box {
        background-color: #1a252f;
        color: #ecf0f1;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #3498db;
        margin-bottom: 10px;
        font-family: 'Share Tech Mono', monospace;
    }
    
    /* Kustomisasi Tab Menu Streamlit */
    .stTabs [data-baseweb="tab"] {
        font-family: 'Share Tech Mono', monospace;
        font-size: 16px;
        color: #bdc3c7;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: #e74c3c;
    }
    .stTabs [aria-selected="true"] {
        color: #f39c12 !important;
        border-bottom-color: #f39c12 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. LOGIKA INTERNAL DATA (DATABASE KIMIA LINGKUNGAN) ---
CASES = {
    "Kasus 1: Spesiasi Logam Berat & Biomagnifikasi Cairan Sedimen": {
        "id": "KL-TOKSIK-01",
        "lokasi": "Estuari Pesisir (Studi Kasus: Teluk Buyat)",
        "kesulitan": "⭐⭐",
        "durasi": "~10 Menit",
        "parameter_utama": "Hg2+ vs MeHg, Spesiasi Logam, Partisi Sedimen
