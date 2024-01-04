# Analisis Sistem Informasi SIAKAD

Proyek ini adalah alat analisis yang dibuat oleh Muhamad Farhan (NIM: 22020057) sebagai bagian dari mata kuliah Analisis Sistem Informasi. Alat ini dirancang untuk melakukan scraping data dari situs web tertentu, dalam hal ini, situs web "edlink.id". Data yang dapat diambil meliputi URL, gambar, teks, judul, meta deskripsi, tautan tertentu, dan data tabel.

## Penggunaan

Berikut adalah langkah-langkah untuk menjalankan alat ini:

1. Pastikan Python telah terinstal di sistem Anda. Jika belum, Anda dapat mengunduhnya dari [python.org](https://www.python.org/).

2. Clone repositori ini ke komputer Anda:

   ```bash
   git clone https://github.com/username/repo.git
   ```

   Gantilah `username/repo` dengan URL repositori Anda sendiri.

3. Pindah ke direktori proyek:

   ```bash
   cd analisis-siakad
   ```

4. Instal dependensi yang diperlukan:

   ```bash
   pip install -r requirements.txt
   ```

5. Jalankan skrip utama:

   ```bash
   python main.py
   ```

   Ikuti petunjuk yang muncul untuk memilih jenis data yang ingin Anda ambil dari situs web.

## Struktur Proyek

    |--data/
    |--modules/
    ||--scraper.py
    ||--display.py
    ||--utility.py
    |--main.py


Folder `data` digunakan untuk menyimpan hasil scraping, dan folder `modules` berisi modul-modul terpisah yang digunakan dalam proyek ini.

## Kontribusi

Anda dipersilakan untuk berkontribusi pada proyek ini. Silakan buat _fork_ dari repositori ini, lakukan perubahan yang diperlukan, dan ajukan _pull request_.

## Lisensi

Proyek ini menggunakan lisensi MIT - lihat file [LICENSE](LICENSE) untuk detailnya.
