import streamlit as st
import pickle
import pandas as pd

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Prediksi Harga Rumah",
    page_icon="🏠",
    layout="wide"
)

# =========================
# LOAD MODEL
# =========================
model = pickle.load(open("model/model.pkl", "rb"))

# =========================
# CSS CUSTOM
# =========================
st.markdown("""
<style>
.stApp{
    background-color:#F5F7FA;
}

.main-title{
    text-align:center;
    background: linear-gradient(90deg,#2563eb,#1d4ed8);
    color:white;
    padding:20px;
    border-radius:15px;
    margin-bottom:20px;
}

.info-box{
    background-color:#ffffff;
    padding:18px;
    border-radius:12px;
    border-left:6px solid #2563eb;
    margin-bottom:20px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
}

.footer{
    text-align:center;
    color:gray;
    font-size:14px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div class="main-title">
<h1>🏠 Prediksi Harga Rumah</h1>
<p>Implementasi Machine Learning menggunakan Random Forest Regressor</p>
</div>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/619/619153.png",
    width=120
)

st.sidebar.title("📌 Tentang Aplikasi")

st.sidebar.success("""
**Nama :** Najwa Kaila Nuraisyah 

**Mata Kuliah :**
Bengkel Koding Data Science

**Algoritma :**
Random Forest Regressor
""")

st.sidebar.info("""
Dataset menggunakan:

• Area (Square Feet)

• Rooms

Target:

• House Price
""")

# =========================
# DESKRIPSI
# =========================
st.markdown("""
<div class="info-box">

### Selamat Datang 👋

Aplikasi ini digunakan untuk memperkirakan harga rumah berdasarkan:

- 📐 Luas Rumah *(Square Feet / sq ft)*
- 🛏 Jumlah Ruangan

Silakan masukkan data rumah, kemudian klik **Prediksi Harga**.

</div>
""", unsafe_allow_html=True)

# =========================
# INPUT
# =========================
st.subheader("📋 Input Data Rumah")

st.info("📌 Masukkan luas rumah dalam satuan **Square Feet (sq ft / kaki persegi)**.")

col1, col2 = st.columns(2)

with col1:
    area = st.number_input(
        "📐 Luas Rumah (sq ft)",
        min_value=0.0,
        value=2000.0
    )

with col2:
    rooms = st.number_input(
        "🛏 Jumlah Ruangan",
        min_value=1,
        value=3,
        step=1
    )

# =========================
# BUTTON
# =========================
if st.button("🚀 Prediksi Harga Rumah", use_container_width=True):

    data = pd.DataFrame({
        "area": [area],
        "rooms": [rooms]
    })

    hasil = model.predict(data)

    harga_usd = hasil[0]

    kurs = 16500
    harga_idr = harga_usd * kurs

    st.markdown("---")

    st.subheader("📈 Hasil Prediksi")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="💲 Harga (USD)",
            value=f"${harga_usd:,.2f}"
        )

    with col2:
        st.metric(
            label="🇮🇩 Harga (IDR)",
            value=f"Rp {harga_idr:,.0f}"
        )

    st.success("✅ Prediksi berhasil dilakukan.")

    st.info("💡 Konversi ke Rupiah menggunakan asumsi kurs **1 USD = Rp16.500**.")

# =========================
# FOOTER
# =========================
st.markdown("---")

st.markdown("""
<div class="footer">

🏠 <b>House Price Prediction App</b><br><br>

Dikembangkan sebagai implementasi <b>Machine Learning</b>
menggunakan algoritma <b>Random Forest Regressor</b>
untuk memprediksi harga rumah berdasarkan luas rumah
dan jumlah ruangan.

<br><br>

⭐ Powered by <b>Python</b> • <b>Scikit-Learn</b> • <b>Streamlit</b>

</div>
""", unsafe_allow_html=True)