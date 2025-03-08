# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("📊 Dashboard Analisis Data E-Commerce")

# Deskripsi
st.write("""
Dashboard ini menampilkan hasil analisis data E-Commerce, termasuk tren penjualan bulanan, produk terlaris, dan distribusi metode pembayaran.
""")

# Load Data
@st.cache_data  # Cache data untuk meningkatkan performa
def load_data():
    # Ganti dengan path dataset Anda
    df = pd.read_csv("dashboard/merged_dataset.csv")  # Pastikan dataset sudah di-merge dan di-cleaning
    return df

df = load_data()
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'], errors='coerce')

# Sidebar untuk Filter Data
st.sidebar.header("Filter Data")
selected_year = st.sidebar.selectbox("Pilih Tahun", df['order_purchase_timestamp'].dt.year.unique())

# Filter Data Berdasarkan Tahun
filtered_data = df[df['order_purchase_timestamp'].dt.year == selected_year]

# Tren Penjualan Bulanan
st.header("📈 Tren Penjualan Bulanan")
monthly_sales = filtered_data.groupby(filtered_data['order_purchase_timestamp'].dt.to_period('M')).agg({'price': 'sum'}).reset_index()
monthly_sales['order_purchase_timestamp'] = monthly_sales['order_purchase_timestamp'].astype(str)

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(data=monthly_sales, x='order_purchase_timestamp', y='price', marker='o', color='b', ax=ax)
# Hapus format scientific notation pada sumbu y
plt.ticklabel_format(style='plain', axis='y')
plt.title(f"Tren Penjualan Bulanan ({selected_year})", fontsize=16)
plt.xlabel("Bulan", fontsize=14)
plt.ylabel("Total Penjualan", fontsize=14)
plt.xticks(rotation=45)
plt.grid(linestyle='--', alpha=0.7)
st.pyplot(fig)

# Top 10 Kategori Produk Terlaris
st.header("🏆 Top 10 Kategori Produk Terlaris")
top_products = filtered_data['product_category_name_english'].value_counts().reset_index()
top_products.columns = ['Kategori Produk', 'Jumlah Penjualan']
top_10_products = top_products.head(10)

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=top_10_products, x='Jumlah Penjualan', y='Kategori Produk', hue='Kategori Produk', palette='viridis', ax=ax)
plt.title(f"Top 10 Kategori Produk Terlaris ({selected_year})", fontsize=16)
plt.xlabel("Jumlah Penjualan", fontsize=14)
plt.ylabel("Kategori Produk", fontsize=14)
plt.grid(axis='x', linestyle='--', alpha=0.7)
st.pyplot(fig)

# Distribusi Metode Pembayaran
st.header("💳 Distribusi Metode Pembayaran")
payment_methods = filtered_data['payment_type'].value_counts()

fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x=payment_methods.index, y=payment_methods.values, hue=payment_methods.values, palette='coolwarm', ax=ax)
plt.title(f"Distribusi Metode Pembayaran ({selected_year})", fontsize=16)
plt.xlabel("Metode Pembayaran", fontsize=14)
plt.ylabel("Jumlah Transaksi", fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig)

# Statistik Deskriptif
st.header("📊 Statistik Deskriptif")
st.write(filtered_data[['price', 'freight_value', 'payment_value']].describe())

# Catatan
st.write("""
**Catatan:**
- Data yang digunakan telah melalui proses cleaning dan preprocessing.
""")