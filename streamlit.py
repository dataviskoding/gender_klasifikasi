import streamlit as st
import numpy as np
import pickle

st.write("Klasifikasi Gender")


tinggi = st.number_input('Masukkan tinggi badan: ')

berat = st.number_input('Masukkan berat badan')

ukuran_sepatu = st.number_input('Masukkan ukuran sepatu')

# load the model from disk


if st.button('Prediksi: '):

    filename = 'klasifikasi_gender.sav'
    klasifikasi = pickle.load(open(filename, 'rb'))

    databaru = [tinggi,berat,ukuran_sepatu]
    prediksi = klasifikasi.predict([databaru])

    st.write("Hasil klasifikasi: ", prediksi)


else:

    st.write('') #displayed when the button is unclicked
