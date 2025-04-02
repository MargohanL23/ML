import streamlit as st
import pandas as pd
import nbformat
from nbconvert import PythonExporter
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
csv_file = "/Users/suryayehezki/Desktop/dashboard/bank_transactions_data_2.csv"
df = pd.read_csv(csv_file)

# Load and execute notebook
notebook_file = "/Users/suryayehezki/Desktop/dashboard/CLUSTERING.ipynb"
with open(notebook_file, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

exporter = PythonExporter()
script, _ = exporter.from_notebook_node(nb)
exec(script, globals())  # Execute the notebook script

# Streamlit UI
st.title("Dashboard Transaksi Bank")

st.sidebar.header("Navigasi")
page = st.sidebar.radio("Pilih Halaman", ["Data Overview", "Clustering Results", "Visualisasi Data"])

if page == "Data Overview":
    st.header("Data Overview")
    st.write(df.head())
    st.write("Total Data:", df.shape)
    st.write("Statistik Deskriptif:")
    st.write(df.describe())

elif page == "Clustering Results":
    st.header("Clustering Results")
    st.write("Menampilkan hasil clustering dari notebook...")
    # Tambahkan visualisasi atau hasil clustering dari CLUSTERING.ipynb jika memungkinkan

elif page == "Visualisasi Data":
    st.header("Visualisasi Data")
    
    # Plot distribusi transaksi
    st.subheader("Distribusi Jumlah Transaksi")
    fig, ax = plt.subplots()
    sns.histplot(df['amount'], bins=30, kde=True, ax=ax)
    st.pyplot(fig)
    
    # Plot jumlah transaksi berdasarkan kategori
    st.subheader("Jumlah Transaksi per Kategori")
    fig, ax = plt.subplots()
    sns.countplot(y=df['category'], order=df['category'].value_counts().index, ax=ax)
    st.pyplot(fig)
    
    # Scatter plot transaksi berdasarkan waktu jika ada kolom timestamp
    if 'timestamp' in df.columns:
        st.subheader("Tren Transaksi dari Waktu ke Waktu")
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df = df.sort_values('timestamp')
        fig, ax = plt.subplots()
        ax.plot(df['timestamp'], df['amount'], marker='o', linestyle='-', alpha=0.5)
        plt.xticks(rotation=45)
        st.pyplot(fig)
