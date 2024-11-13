import streamlit as st

from web_function import predict

def app(df, x, y):

    st.title("Halaman Prediksi")

    col1,col2,col3 = st.columns(3)

    with col1:
        pregnant = st.text_input ('Input Nilai pregnant')
    with col1:
        glucose = st.text_input ('Input Nilai glucose')
    with col1:
        bp = st.text_input ('Input Nilai bp')
    with col2:
        skin = st.text_input ('Input Nilai skin')
    with col2:
        insulin = st.text_input ('Input Nilai insulin')
    with col2:
        bmi = st.text_input ('Input Nilai bmi')
    with col3:
        pedigree = st.text_input ('Input Nilai pedigree')
    with col3:
        age = st.text_input ('Input Nilai age')

    features = [pregnant,glucose,bp,skin,insulin,bmi,pedigree,age]

    # Tombol prediksi
    if st.button("Prediksi"):
        prediction, score = predict(x,y,features)
        score = score
        st.info("Prediksi Sukses...")

        if (prediction == 1):
            st.warning("Orang tersebut rentan terkena diabetes")
        else:
            st.success("Orang tersebut relatif aman dari diabetes")

        st.write("Model yang digunakan memiliki tingkat akurasi ", (score*100),"%")