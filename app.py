import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Visualisasi Donasi Lingkungan", layout="wide")

# ==========================
# HEADER & DESKRIPSI
# ==========================
st.title("🌱 Dashboard Visualisasi Donasi Lingkungan")
st.write("Selamat datang! Aplikasi ini menampilkan data donasi dari sepuluh kampanye lingkungan. "
         "Gunakan menu dropdown untuk memilih jenis grafik dan jelajahi datanya secara visual.")

st.image("mangrove.jpg", caption="Kegiatan Pelestarian Mangrove")

# ==========================
# DATASET
# ==========================
data = pd.DataFrame({
    "Kampanye": [
        "Mangrove Balikpapan", "Pantai Samboja", "Delta Mahakam", "Hutan Kota Samarinda",
        "Terumbu Karang Derawan", "Sungai Karang Mumus", "Go Green Campus",
        "Taman Nasional Kutai", "Penanaman Pohon Bontang", "Ekosistem Pesisir Berau"
    ],
    "Donasi (juta)": [120, 85, 60, 90, 110, 75, 50, 130, 95, 70]
})

st.subheader("📊 Data Donasi Kampanye Lingkungan")
st.dataframe(data, use_container_width=True)

# ==========================
# DROPDOWN PILIH GRAFIK
# ==========================
tipe = st.selectbox(
    "Pilih jenis grafik:",
    ["Bar Chart", "Line Chart", "Area Chart", "Pie Chart", "Map"]
)

# ==========================
# BAR CHART
# ==========================
if tipe == "Bar Chart":
    st.subheader("📦 Bar Chart Donasi")
    st.bar_chart(data.set_index("Kampanye"))

# ==========================
# LINE CHART
# ==========================
elif tipe == "Line Chart":
    st.subheader("📈 Line Chart Donasi")
    st.line_chart(data.set_index("Kampanye"))

# ==========================
# AREA CHART
# ==========================
elif tipe == "Area Chart":
    st.subheader("🌊 Area Chart Donasi")
    st.area_chart(data.set_index("Kampanye"))

# ==========================
# PIE CHART
# ==========================
elif tipe == "Pie Chart":
    st.subheader("🥧 Pie Chart Donasi")
    fig, ax = plt.subplots()
    ax.pie(data["Donasi (juta)"], labels=data["Kampanye"], autopct="%1.1f%%")
    st.pyplot(fig)

# ==========================
# MAP
# ==========================
elif tipe == "Map":
    st.subheader("🗺️ Peta Persebaran Lokasi Kampanye")

    lokasi = pd.DataFrame({
        "lat": [-1.27, -1.10, -0.50, -0.52, 2.28, -0.43, -0.50, 0.55, 0.13, 2.15],
        "lon": [116.83, 117.00, 117.25, 117.13, 118.23, 117.15, 117.00, 117.48, 117.50, 118.00]
    })

    st.map(lokasi)

# ==========================
# SLIDER FILTER
# ==========================
st.subheader("🔎 Filter Donasi Minimum")
nilai = st.slider("Tampilkan kampanye dengan donasi minimal:", 0, 150, 80)

st.dataframe(data[data["Donasi (juta)"] >= nilai])






