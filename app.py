import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("📚 Sistem Evaluasi Akademik Mahasiswa")

nama = st.text_input("Nama Mahasiswa")

tugas = st.number_input("Nilai Tugas", 0, 100, 80)
uts = st.number_input("Nilai UTS", 0, 100, 75)
uas = st.number_input("Nilai UAS", 0, 100, 85)

if st.button("Hitung"):

    nilai_akhir = 0.3*tugas + 0.3*uts + 0.4*uas

    status = "LULUS" if nilai_akhir >= 75 else "TIDAK LULUS"

    st.subheader("Hasil Evaluasi")

    st.write("Nama:", nama)
    st.write("Nilai Akhir:", round(nilai_akhir,2))
    st.write("Status:", status)

    st.subheader("Matriks Nilai")

    matriks = np.array([[tugas, uts, uas]])
    st.write(matriks)

    st.subheader("Cosine Similarity")

    ideal = np.array([100,100,100])

    similarity = np.dot(matriks[0], ideal) / (
        np.linalg.norm(matriks[0]) *
        np.linalg.norm(ideal)
    )

    st.write(round(similarity,3))

    fig, ax = plt.subplots()
    ax.bar(["Tugas","UTS","UAS"], [tugas, uts, uas])
    ax.set_title("Grafik Nilai")
    st.pyplot(fig)