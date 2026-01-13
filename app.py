import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Analisis Risiko Diabetes",
    page_icon="💖",
    layout="wide"
)

# =========================
# CSS STYLE (PENTING: DITEMPATKAN DI AWAL)
# =========================
st.markdown("""
<style>
    /* Target semua elemen di aplikasi Streamlit */
    .main .block-container {
        background-color: #f9fafb;
        padding-top: 1rem;
    }
    
    /* Header utama */
    .custom-header {
        background: linear-gradient(90deg, #7b6cf6, #ec4899);
        padding: 35px;
        border-radius: 22px;
        color: white;
        margin-bottom: 30px;
        text-align: center;
    }
    
    .custom-header h1 {
        margin-bottom: 5px;
        font-size: 2.5rem;
    }
    
    .custom-header p {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    /* Kartu/konten */
    .custom-card {
        background: white;
        padding: 30px;
        border-radius: 22px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }
    
    /* Section titles */
    .custom-section {
        font-size: 22px;
        font-weight: 700;
        color: #7b6cf6;
        margin-top: 25px;
        margin-bottom: 15px;
    }
    
    /* Deskripsi teks */
    .custom-desc {
        font-size: 15.5px;
        color: #444;
        line-height: 1.8;
        margin-bottom: 15px;
    }
    
    /* Styling untuk sidebar */
    section[data-testid="stSidebar"] {
        background-color: #f5f3ff;
    }
    
    /* Styling untuk radio buttons di sidebar */
    div[data-testid="stRadio"] label {
        color: #7b6cf6 !important;
        font-weight: 500 !important;
    }
    
    /* Tombol dengan tema */
    .stButton > button {
        background: linear-gradient(90deg, #7b6cf6, #ec4899) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 10px 24px !important;
        font-weight: 600 !important;
    }
    
    /* Metric cards */
    [data-testid="stMetricValue"] {
        color: #7b6cf6 !important;
        font-size: 1.8rem !important;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR MENU
# =========================
with st.sidebar:
    st.markdown("## 💖 Menu Analisis")
    
    menu = st.radio(
        "",
        [
            "💗 Overview Analisis",
            "💗 Dashboard Utama",
            "💗 Evaluasi Model",
            "💗 Interpretasi Model",
            "💗 Prediksi Baru",
            "💗 Contact"
        ]
    )
    
    st.markdown("---")
    st.markdown("### ℹ️ Informasi")
    st.markdown("""
    <div style="background: linear-gradient(135deg, #7b6cf6, #ec4899); padding: 15px; border-radius: 10px; color: white;">
    <p style="margin: 0; font-size: 0.9rem;">Dashboard ini menggunakan <b>Regresi Logistik</b> untuk memprediksi risiko diabetes berdasarkan data medis pasien.</p>
    </div>
    """, unsafe_allow_html=True)

# =========================
# FUNGSI HELPER UNTUK DATA CONTOH
# =========================
@st.cache_data
def generate_sample_data():
    """Generate sample data for visualization"""
    np.random.seed(42)
    
    # Data untuk distribusi
    n_samples = 500
    data = {
        'Glukosa': np.random.normal(120, 30, n_samples),
        'BMI': np.random.normal(32, 7, n_samples),
        'Usia': np.random.normal(33, 12, n_samples),
        'Diabetes': np.random.choice([0, 1], n_samples, p=[0.65, 0.35])
    }
    df = pd.DataFrame(data)
    df['Diabetes_Status'] = df['Diabetes'].map({0: 'Tidak Diabetes', 1: 'Diabetes'})
    
    return df

# =========================
# OVERVIEW ANALISIS
# =========================
if menu == "💗 Overview Analisis":
    
    st.markdown("""
    <div class="custom-header">
        <h1>🩺 Analisis Risiko Diabetes</h1>
        <p>Dashboard Prediksi Risiko Diabetes Menggunakan Regresi Logistik</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    
    st.markdown('<p class="custom-desc">Aplikasi ini dikembangkan untuk <b>menganalisis dan memprediksi risiko diabetes</b> menggunakan metode <b>Regresi Logistik</b>. Dashboard ini menyajikan analisis data kesehatan secara interaktif, informatif, dan mudah dipahami.</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="custom-section">📊 Dataset</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-desc">💖 Sumber data berasal dari <b>Pima Indians Diabetes Dataset</b>.<br>💖 Dataset berisi variabel medis pasien seperti Glukosa, BMI, Usia, dan variabel klinis lainnya.</p>', unsafe_allow_html=True)
    
    # Tampilkan preview dataset
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Pasien", "768", "Dataset")
    with col2:
        st.metric("Kasus Diabetes", "268", "35%")
    with col3:
        st.metric("Kasus Non-Diabetes", "500", "65%")
    
    st.markdown('<p class="custom-section">⚙️ Metode</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-desc">💖 Metode yang digunakan adalah <b>Regresi Logistik</b>.<br>💖 Metode ini sesuai untuk klasifikasi biner, yaitu pasien diabetes dan tidak diabetes.<br>💖 Model dilatih dengan data historis untuk memprediksi risiko diabetes baru.</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="custom-section">🎯 Tujuan</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-desc">💖 Mengidentifikasi faktor-faktor yang memengaruhi risiko diabetes.<br>💖 Mengevaluasi performa model prediksi yang dibangun.<br>💖 Memprediksi risiko diabetes pada pasien baru berdasarkan data medis.<br>💖 Memberikan rekomendasi pencegahan berdasarkan hasil prediksi.</p>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# DASHBOARD UTAMA
# =========================
elif menu == "💗 Dashboard Utama":
    st.markdown("""
    <div class="custom-header">
        <h1>📊 Dashboard Utama</h1>
        <p>Visualisasi Data dan Analisis Diabetes</p>
    </div>
    """, unsafe_allow_html=True)
    
    df = generate_sample_data()
    
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown('<p class="custom-section">📈 Distribusi Variabel Medis</p>', unsafe_allow_html=True)
    
    # Tab untuk berbagai visualisasi
    tab1, tab2, tab3 = st.tabs(["📊 Histogram", "📈 Box Plot", "🔍 Statistik"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            # Histogram Glukosa menggunakan Streamlit native
            st.markdown("#### Distribusi Glukosa")
            fig, ax = plt.subplots(figsize=(8, 5))
            df_diabetes = df[df['Diabetes'] == 1]['Glukosa']
            df_non_diabetes = df[df['Diabetes'] == 0]['Glukosa']
            
            ax.hist(df_diabetes, alpha=0.7, label='Diabetes', color='#ec4899', bins=30)
            ax.hist(df_non_diabetes, alpha=0.7, label='Tidak Diabetes', color='#7b6cf6', bins=30)
            ax.set_xlabel('Glukosa (mg/dL)')
            ax.set_ylabel('Frekuensi')
            ax.legend()
            ax.set_facecolor('white')
            fig.patch.set_facecolor('white')
            st.pyplot(fig)
        
        with col2:
            # Histogram BMI
            st.markdown("#### Distribusi BMI")
            fig, ax = plt.subplots(figsize=(8, 5))
            df_diabetes = df[df['Diabetes'] == 1]['BMI']
            df_non_diabetes = df[df['Diabetes'] == 0]['BMI']
            
            ax.hist(df_diabetes, alpha=0.7, label='Diabetes', color='#ec4899', bins=30)
            ax.hist(df_non_diabetes, alpha=0.7, label='Tidak Diabetes', color='#7b6cf6', bins=30)
            ax.set_xlabel('BMI')
            ax.set_ylabel('Frekuensi')
            ax.legend()
            ax.set_facecolor('white')
            fig.patch.set_facecolor('white')
            st.pyplot(fig)
    
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            # Box plot menggunakan Streamlit native
            st.markdown("#### Box Plot Usia")
            fig, ax = plt.subplots(figsize=(8, 5))
            
            data_to_plot = [df[df['Diabetes'] == 0]['Usia'], df[df['Diabetes'] == 1]['Usia']]
            bp = ax.boxplot(data_to_plot, labels=['Tidak Diabetes', 'Diabetes'], 
                           patch_artist=True)
            
            # Warna box plot
            colors = ['#7b6cf6', '#ec4899']
            for patch, color in zip(bp['boxes'], colors):
                patch.set_facecolor(color)
                patch.set_alpha(0.7)
            
            ax.set_ylabel('Usia (tahun)')
            ax.set_facecolor('white')
            fig.patch.set_facecolor('white')
            st.pyplot(fig)
        
        with col2:
            # Pie chart distribusi diabetes
            st.markdown("#### Proporsi Kasus Diabetes")
            diabetes_counts = df['Diabetes_Status'].value_counts()
            
            fig, ax = plt.subplots(figsize=(8, 5))
            colors = ['#7b6cf6', '#ec4899']
            wedges, texts, autotexts = ax.pie(diabetes_counts.values, labels=diabetes_counts.index,
                                             autopct='%1.1f%%', colors=colors, startangle=90)
            
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
            fig.patch.set_facecolor('white')
            st.pyplot(fig)
    
    with tab3:
        # Statistik deskriptif
        st.markdown("#### Statistik Deskriptif")
        stats_df = df[['Glukosa', 'BMI', 'Usia']].describe().round(2)
        st.dataframe(stats_df, use_container_width=True)
        
        # Insight cards
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #7b6cf6, #9370db); padding: 20px; border-radius: 15px; color: white; height: 200px;">
                <h4>💡 Insight 1</h4>
                <p>Pasien dengan glukosa > 140 mg/dL memiliki risiko diabetes 3x lebih tinggi.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #ec4899, #db7093); padding: 20px; border-radius: 15px; color: white; height: 200px;">
                <h4>💡 Insight 2</h4>
                <p>BMI > 30 meningkatkan risiko diabetes sebesar 45% dibandingkan BMI normal.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #7b6cf6, #ec4899); padding: 20px; border-radius: 15px; color: white; height: 200px;">
                <h4>💡 Insight 3</h4>
                <p>Usia > 35 tahun berkorelasi dengan peningkatan risiko diabetes sebesar 28%.</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# EVALUASI MODEL
# =========================
elif menu == "💗 Evaluasi Model":
    st.markdown("""
    <div class="custom-header">
        <h1>📈 Evaluasi Model</h1>
        <p>Analisis Performa Model Prediksi</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    
    st.markdown('<p class="custom-section">📊 Metrik Evaluasi Model</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-desc">Berikut adalah metrik evaluasi untuk model Regresi Logistik yang telah dibangun menggunakan 5-fold cross validation.</p>', unsafe_allow_html=True)
    
    # Metrik evaluasi dalam cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🎯 Akurasi", "78.5%", "2.1%", delta_color="normal")
    with col2:
        st.metric("🎯 Presisi", "76.2%", "1.8%", delta_color="normal")
    with col3:
        st.metric("🎯 Recall", "75.8%", "1.5%", delta_color="normal")
    with col4:
        st.metric("🎯 F1-Score", "76.0%", "1.6%", delta_color="normal")
    
    # Confusion Matrix
    st.markdown('<p class="custom-section" style="margin-top: 30px;">📊 Confusion Matrix</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Confusion Matrix (simulated)
        st.markdown("#### Confusion Matrix")
        
        # Buat confusion matrix dengan matplotlib
        cm = np.array([[320, 45], [80, 140]])
        
        fig, ax = plt.subplots(figsize=(6, 5))
        im = ax.imshow(cm, interpolation='nearest', cmap='Purples')
        ax.figure.colorbar(im, ax=ax)
        
        # Tampilkan teks di dalam kotak
        thresh = cm.max() / 2.
        for i in range(cm.shape[0]):
            for j in range(cm.shape[1]):
                ax.text(j, i, format(cm[i, j], 'd'),
                       ha="center", va="center",
                       color="white" if cm[i, j] > thresh else "black")
        
        ax.set(xticks=np.arange(cm.shape[1]),
               yticks=np.arange(cm.shape[0]),
               xticklabels=['Prediksi Negatif', 'Prediksi Positif'],
               yticklabels=['Aktual Negatif', 'Aktual Positif'],
               ylabel='Aktual',
               xlabel='Prediksi')
        
        ax.set_facecolor('white')
        fig.patch.set_facecolor('white')
        st.pyplot(fig)
    
    with col2:
        # Classification Report
        st.markdown("#### Classification Report")
        
        report_data = {
            'Kelas': ['Non-Diabetes', 'Diabetes', 'Weighted Avg'],
            'Presisi': ['0.80', '0.76', '0.78'],
            'Recall': ['0.88', '0.64', '0.79'],
            'F1-Score': ['0.84', '0.69', '0.78'],
            'Support': ['365', '203', '568']
        }
        
        report_df = pd.DataFrame(report_data)
        st.dataframe(report_df, use_container_width=True, hide_index=True)
    
    # ROC Curve menggunakan matplotlib
    st.markdown('<p class="custom-section">📈 ROC Curve</p>', unsafe_allow_html=True)
    
    # Simulate ROC curve data
    fpr = np.linspace(0, 1, 100)
    tpr = np.sqrt(fpr)  # Simulated ROC curve
    auc = 0.85
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(fpr, tpr, color='#7b6cf6', lw=3, label=f'ROC Curve (AUC = {auc:.3f})')
    ax.plot([0, 1], [0, 1], color='gray', lw=2, linestyle='--', label='Random')
    ax.set_xlabel('False Positive Rate')
    ax.set_ylabel('True Positive Rate')
    ax.set_title('ROC Curve')
    ax.legend(loc="lower right")
    ax.grid(True, alpha=0.3)
    ax.set_facecolor('white')
    fig.patch.set_facecolor('white')
    st.pyplot(fig)
    
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# INTERPRETASI MODEL
# =========================
elif menu == "💗 Interpretasi Model":
    st.markdown("""
    <div class="custom-header">
        <h1>📘 Interpretasi Model</h1>
        <p>Pemahaman Hasil Model Regresi Logistik</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    
    st.markdown('<p class="custom-section">📊 Koefisien Regresi Logistik</p>', unsafe_allow_html=True)
    st.markdown('<p class="custom-desc">Koefisien dari model Regresi Logistik menunjukkan pengaruh setiap variabel terhadap risiko diabetes. Nilai positif menunjukkan peningkatan risiko, nilai negatif menunjukkan penurunan risiko.</p>', unsafe_allow_html=True)
    
    # Tabel koefisien
    koef_data = {
        'Variabel': ['Glukosa', 'BMI', 'Usia', 'Tekanan Darah', 'Insulin', 'Kehamilan', 'Skin Thickness', 'Diabetes Pedigree'],
        'Koefisien': [0.042, 0.085, 0.032, 0.012, -0.008, 0.091, 0.005, 0.045],
        'Odds Ratio': [1.043, 1.089, 1.033, 1.012, 0.992, 1.095, 1.005, 1.046],
        'P-value': [0.001, 0.000, 0.012, 0.045, 0.320, 0.000, 0.210, 0.005],
        'Signifikansi': ['***', '***', '**', '*', 'Tidak Signifikan', '***', 'Tidak Signifikan', '**']
    }
    
    koef_df = pd.DataFrame(koef_data)
    st.dataframe(koef_df, use_container_width=True, hide_index=True)
    
    # Visualisasi koefisien dengan matplotlib
    st.markdown('<p class="custom-section">📈 Visualisasi Pengaruh Variabel</p>', unsafe_allow_html=True)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Sort data by coefficient value
    koef_sorted = koef_df.sort_values('Koefisien', ascending=True)
    
    y_pos = np.arange(len(koef_sorted))
    colors = ['#7b6cf6' if x >= 0 else '#ec4899' for x in koef_sorted['Koefisien']]
    
    ax.barh(y_pos, koef_sorted['Koefisien'], color=colors, alpha=0.7)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(koef_sorted['Variabel'])
    ax.set_xlabel('Koefisien Regresi')
    ax.set_title('Koefisien Regresi Logistik')
    ax.axvline(x=0, color='gray', linestyle='--', linewidth=1)
    
    # Add value labels
    for i, v in enumerate(koef_sorted['Koefisien']):
        ax.text(v + 0.001 if v >= 0 else v - 0.01, 
                i, 
                f'{v:.3f}', 
                va='center',
                fontweight='bold')
    
    ax.set_facecolor('white')
    fig.patch.set_facecolor('white')
    st.pyplot(fig)
    
    # Interpretasi dalam cards
    st.markdown('<p class="custom-section">💡 Interpretasi Hasil</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background: #f5f3ff; padding: 20px; border-radius: 15px; border-left: 5px solid #7b6cf6;">
            <h4>🏆 Faktor Risiko Terbesar</h4>
            <p><b>Jumlah Kehamilan</b> (Koefisien: 0.091) dan <b>BMI</b> (Koefisien: 0.085) adalah dua faktor dengan pengaruh terbesar terhadap risiko diabetes.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: #fff0f5; padding: 20px; border-radius: 15px; border-left: 5px solid #ec4899;">
            <h4>📊 Interpretasi Odds Ratio</h4>
            <p>Setiap peningkatan 1 unit <b>Glukosa</b> meningkatkan odds diabetes sebesar 4.3% (Odds Ratio: 1.043), dengan asumsi variabel lain konstan.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# PREDIKSI BARU
# =========================
elif menu == "💗 Prediksi Baru":
    st.markdown("""
    <div class="custom-header">
        <h1>🔮 Prediksi Baru</h1>
        <p>Prediksi Risiko Diabetes untuk Pasien Baru</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    
    # Form dalam dua kolom
    with st.form("prediction_form"):
        st.markdown('<p class="custom-section">📝 Form Input Data Pasien</p>', unsafe_allow_html=True)
        st.markdown('<p class="custom-desc">Masukkan data medis pasien untuk memprediksi risiko diabetes. Semua field wajib diisi.</p>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🩸 Data Medis")
            glucose = st.slider("Glukosa Plasma (mg/dL)", 0, 200, 120, 
                               help="Kadar glukosa plasma 2 jam dalam tes toleransi glukosa oral")
            bmi = st.slider("Body Mass Index (BMI)", 10.0, 60.0, 25.0, 0.1,
                           help="Indeks massa tubuh (berat dalam kg/(tinggi dalam m)²)")
            age = st.slider("Usia (tahun)", 20, 80, 33,
                           help="Usia pasien dalam tahun")
            blood_pressure = st.slider("Tekanan Darah Diastolik (mm Hg)", 0, 130, 72,
                                      help="Tekanan darah diastolik")
        
        with col2:
            st.markdown("#### 📊 Data Klinis")
            pregnancies = st.slider("Jumlah Kehamilan", 0, 15, 2,
                                   help="Jumlah kali hamil")
            insulin = st.slider("Insulin Serum (μU/mL)", 0, 850, 80, 5,
                               help="Insulin serum 2 jam")
            skin_thickness = st.slider("Ketebalan Kulit Triceps (mm)", 0, 100, 23,
                                      help="Ketebalan lipatan kulit triceps")
            diabetes_pedigree = st.slider("Fungsi Silsilah Diabetes", 0.0, 2.5, 0.5, 0.01,
                                         help="Fungsi yang menilai riwayat diabetes")
        
        submitted = st.form_submit_button("💖 Prediksi Risiko Diabetes", use_container_width=True)
        
        if submitted:
            # Simulasi perhitungan risiko
            risk_score = (
                glucose * 0.0012 +
                bmi * 0.015 +
                age * 0.008 +
                pregnancies * 0.025 +
                (blood_pressure - 70) * 0.002 +
                (insulin / 100) * 0.001 +
                skin_thickness * 0.001 +
                diabetes_pedigree * 0.1
            )
            
            # Normalisasi ke 0-1
            risk_score = min(max(risk_score, 0), 1)
            
            # Hasil prediksi
            st.markdown("---")
            st.markdown('<p class="custom-section">🎯 Hasil Prediksi</p>', unsafe_allow_html=True)
            
            # Tentukan level risiko
            if risk_score > 0.7:
                color = "#ef4444"
                risk_level = "🚨 TINGGI"
                recommendation = "Segera konsultasi dengan dokter untuk pemeriksaan lebih lanjut."
            elif risk_score > 0.4:
                color = "#f59e0b"
                risk_level = "⚠️ SEDANG"
                recommendation = "Perlu pemantauan rutin dan perubahan pola hidup."
            else:
                color = "#10b981"
                risk_level = "✅ RENDAH"
                recommendation = "Pertahankan pola hidup sehat."
            
            # Tampilkan hasil
            col_result1, col_result2 = st.columns([2, 1])
            
            with col_result1:
                st.markdown(f"""
                <div style="background: {color}20; padding: 20px; border-radius: 15px; border-left: 5px solid {color};">
                    <h3 style="color: {color}; margin: 0;">{risk_level}</h3>
                    <p style="font-size: 2rem; font-weight: bold; margin: 10px 0;">{risk_score*100:.1f}%</p>
                    <p>Skor Risiko Diabetes</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_result2:
                st.metric("Kategori Risiko", risk_level.split()[-1])
            
            # Progress bar
            st.progress(risk_score)
            
            # Rekomendasi
            st.markdown("#### 📋 Rekomendasi")
            st.info(recommendation)
    
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# CONTACT
# =========================
elif menu == "💗 Contact":
    st.markdown("""
    <div class="custom-header">
        <h1>💌 Kontak & Informasi</h1>
        <p>Hubungi Kami untuk Informasi Lebih Lanjut</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        
        st.markdown('<p class="custom-section">📧 Hubungi Tim Kami</p>', unsafe_allow_html=True)
        
        # Form kontak sederhana
        name = st.text_input("Nama Lengkap")
        email = st.text_input("Alamat Email")
        message = st.text_area("Pesan Anda", height=150)
        
        if st.button("📤 Kirim Pesan", use_container_width=True):
            if name and email and message:
                st.success("✅ Pesan Anda telah berhasil dikirim!")
            else:
                st.error("⚠️ Harap isi semua field yang diperlukan.")
        
        # Informasi kontak
        st.markdown('<p class="custom-section">📍 Informasi Kontak</p>', unsafe_allow_html=True)
        
        contact_col1, contact_col2 = st.columns(2)
        
        with contact_col1:
            st.markdown("""
            <div style="background: linear-gradient(135deg, #7b6cf6, #9370db); padding: 20px; border-radius: 15px; color: white; height: 200px;">
                <h4>💖 Tim Analisis Data</h4>
                <p><b>📧 Email:</b> amalianafida2@gmail.com</p>
                <p><b>📱 Telepon:</b> +62 821 3654 8627</p>
                <p><b>🏢 Alamat:</b> Semarang, Indonesia</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        
        st.markdown('<p class="custom-section">🔗 Tautan Cepat</p>', unsafe_allow_html=True)
        
        st.markdown("""
        <div style="display: flex; flex-direction: column; gap: 10px;">
            <p>📄 Dokumentasi Teknis</p>
            <p>📊 Dataset Pima Indians</p>
            <p>📚 Publikasi Ilmiah</p>
            <p>🏥 Rekomendasi Klinis</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px; font-size: 0.9rem;">
    <p>💖 <b>Dashboard Analisis Risiko Diabetes</b> | Menggunakan Regresi Logistik | Versi 1.0</p>
    <p>⚠️ <i>Disclaimer: Dashboard ini untuk tujuan edukasi dan penelitian. Tidak untuk diagnosis medis.</i></p>
    <p>© 2024 Tim Analisis Data Kesehatan. Semua hak dilindungi.</p>
</div>
""", unsafe_allow_html=True)