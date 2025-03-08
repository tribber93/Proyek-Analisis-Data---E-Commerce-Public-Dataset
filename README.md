# Dashboard Analisis Data E-Commerce

Dashboard ini menampilkan hasil analisis data E-Commerce, termasuk tren penjualan bulanan, produk terlaris, dan distribusi metode pembayaran. Dibangun menggunakan **Streamlit** dan **Python**.

---

## Prasyarat

Sebelum menjalankan dashboard, pastikan Anda telah menginstal **Python 3.8 atau lebih baru**.

---

## Instalasi

1. Buat Virtual Environment:

   ```bash
   python -m venv venv
   ```

2. Aktifkan Virtual Environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. Install Prasyarat:
   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan Dashboard

1. Pastikan Dataset Tersedia:
   - Pastikan file dataset (merged_dataset.csv atau file lainnya) sudah tersedia di folder yang sesuai.
   - Jika dataset belum tersedia, jalankan notebook analisis data untuk menghasilkan file dataset yang diperlukan.
2. Jalankan Dashboard:
   ```bash
   streamlit run dashboard/dashboard.py
   ```
3. Akses Dashboard:
   - Buka browser dan akses alamat yang ditampilkan di terminal (biasanya http://localhost:8501).
   - Dashboard siap digunakan!

## Fitur Dashboard

1. Tren Penjualan Bulanan:

   - Menampilkan grafik line chart yang menunjukkan tren penjualan per bulan.
   - Dapat memfilter data berdasarkan tahun.

2. Top 10 Kategori Produk Terlaris:

   - Menampilkan grafik bar chart yang menunjukkan kategori produk terlaris.

3. Distribusi Metode Pembayaran:

   - Menampilkan grafik bar chart yang menunjukkan metode pembayaran paling populer.

4. Statistik Deskriptif:
   - Menampilkan statistik deskriptif untuk kolom numerik seperti harga, biaya pengiriman, dan total pembayaran.
