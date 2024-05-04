import pickle
import streamlit as st

# Membaca model
try:
    diabetes_model = pickle.load(open('svm_model.sav', 'rb'))
    print("Model berhasil dimuat.")
except Exception as e:
    print("Gagal memuat model:", e)

# Judul web
st.title('Prediksi Penyakit Diabetes')

# Membagi kolom
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('Input nilai Pregnancies')

with col2:
    Glucose = st.text_input('Input nilai Glucose')

with col1:
    BloodPressure = st.text_input('Input nilai Blood Pressure')

with col2:
    SkinThickness = st.text_input('Input nilai Skin Thickness')

with col1:
    Insulin = st.text_input('Input nilai Insulin')

with col2:
    BMI = st.text_input('Input nilai BMI')

with col1:
    DiabetesPedigreeFunction = st.text_input('Input nilai Diabetes Pedigree Function')

with col2:
    Age = st.text_input('Input nilai Age')

# Code untuk prediksi
diab_diagnosis = ''

# Membuat tombol untuk prediksi
if st.button('Test Prediksi Diabetes'):
    # Konversi nilai input menjadi tipe data numerik
    Pregnancies = float(Pregnancies)
    Glucose = float(Glucose)
    BloodPressure = float(BloodPressure)
    SkinThickness = float(SkinThickness)
    Insulin = float(Insulin)
    BMI = float(BMI)
    DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
    Age = float(Age)

    # Prediksi menggunakan model
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    # Menampilkan hasil prediksi
    if diab_prediction[0] == 1:
        st.success('Pasien terkena Diabetes')
    else:
        st.success('Pasien tidak terkena Diabetes')
