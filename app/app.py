import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open('model/model.pkl', 'rb'))

st.title("Prediksi Harga Rumah")

st.write("Masukkan data rumah")

area = st.number_input(
    "Luas Rumah",
    min_value=0.0
)

rooms = st.number_input(
    "Jumlah Ruangan",
    min_value=1,
    step=1
)

if st.button("Prediksi Harga"):

    data = pd.DataFrame({
        'area': [area],
        'rooms': [rooms]
    })

    hasil = model.predict(data)

    st.success(
        f"Prediksi Harga Rumah: ${hasil[0]:,.2f}"
    )