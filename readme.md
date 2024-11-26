# **Image Background Remover with Transparency**

Developed by BBC Team

## **Deskripsi Proyek**

Proyek ini adalah sebuah aplikasi web sederhana untuk menghapus latar belakang gambar secara otomatis menggunakan algoritma **GrabCut**. Aplikasi ini menghasilkan gambar dengan latar belakang transparan yang disimpan dalam format `.png`. Proyek ini dirancang menggunakan framework **Flask** untuk server-side processing dan **Tailwind CSS** untuk tampilan antarmuka yang responsif.

## **Fitur Utama**

1. **Upload Gambar**: Mendukung format gambar `.jpg`, `.jpeg`, dan `.png`.
2. **Hapus Latar Belakang**: Menggunakan algoritma **GrabCut** untuk segmentasi gambar dan menghasilkan latar belakang transparan.
3. **Download Hasil**: Gambar hasil dapat diunduh dalam format `.png` dengan transparansi.
4. **Proses Otomatis**: Latar belakang diproses secara otomatis tanpa intervensi pengguna.
5. **Antarmuka Responsif**: Tampilan aplikasi modern dan responsif berkat **Tailwind CSS**.

---

## **Algoritma yang Digunakan**

Proyek ini menggunakan algoritma **GrabCut** untuk segmentasi gambar.

### **Apa itu GrabCut?**

**GrabCut** adalah algoritma berbasis **graph-cut optimization** yang digunakan untuk segmentasi gambar. Algoritma ini memisahkan objek foreground dari latar belakang menggunakan teknik berikut:

1. Membuat mask awal berdasarkan persegi panjang yang mengelilingi objek.
2. Menggunakan model Gaussian Mixture untuk mempelajari distribusi warna di latar depan (foreground) dan latar belakang (background).
3. Mengoptimalkan pemisahan menggunakan pemotongan graf (graph-cut) berdasarkan energi minimum.

### **Mekanisme Aplikasi**

1. **Pengunggahan Gambar**:
   - Pengguna mengunggah file gambar melalui antarmuka web.
   - Format yang didukung: `.jpg`, `.jpeg`, `.png`.
2. **Proses Segmentasi**:
   - Gambar dimuat menggunakan library OpenCV.
   - Mask awal dibuat menggunakan algoritma GrabCut dengan persegi panjang yang ditentukan secara otomatis.
   - Area objek dan latar belakang dipisahkan berdasarkan probabilitas warna.
3. **Hasil dengan Transparansi**:
   - Gambar hasil segmentasi diubah ke format **BGRA** (RGBA dengan saluran alpha).
   - Area latar belakang diatur sebagai transparan (alpha = 0).
4. **Penyimpanan dan Unduh**:
   - Gambar hasil disimpan dengan format `.png` untuk mempertahankan transparansi.
   - Pengguna dapat mengunduh gambar yang diproses melalui tombol unduh.

---

## **Struktur Folder**

```
/
├── app.py                  # File utama aplikasi Flask
├── static/
│   ├── uploads/            # Folder untuk menyimpan file gambar yang diunggah
│   ├── processed/          # Folder untuk menyimpan hasil gambar yang diproses
├── templates/
│   ├── index.html          # Template untuk halaman utama
│   ├── result.html         # Template untuk halaman hasil
├── README.md               # Dokumentasi proyek
└── requirements.txt        # Daftar library Python yang digunakan

```

---

## **Library yang Digunakan**

Proyek ini menggunakan beberapa library Python untuk memproses gambar dan mengelola server:

1. **Flask**: Framework web untuk mengelola server dan routing.
2. **OpenCV**: Digunakan untuk membaca, memproses, dan menyimpan gambar.
3. **NumPy**: Library untuk manipulasi array, digunakan dalam pengolahan gambar.
4. **Werkzeug**: Untuk keamanan nama file (secure filenames).

---

## **Instalasi dan Penggunaan**

Ikuti langkah-langkah berikut untuk menjalankan proyek ini di komputer lokal Anda.

### **1. Clone Repository**

```bash
git clone https://github.com/username/image-background-remover.git
cd image-background-remover

```

### **2. Buat Virtual Environment**

```bash
python -m venv env

```

### **3. Aktifkan Virtual Environment**

- **Windows**:

  ```bash
  env\Scripts\activate

  ```

- **Mac/Linux**:

  ```bash
  source env/bin/activate

  ```

### **4. Instal Dependensi**

```bash
pip install -r requirements.txt

```

### **5. Jalankan Aplikasi**

```bash
python app.py

```

Aplikasi akan berjalan di `http://127.0.0.1:5000`. Buka URL tersebut di browser Anda.

---

## **Cara Kerja**

1. Buka aplikasi di browser Anda.
2. Unggah gambar melalui formulir di halaman utama.
3. Klik **Process** untuk memulai segmentasi gambar.
4. Hasil gambar akan ditampilkan di halaman hasil dengan tombol untuk mengunduh file.

---

## **Contoh Penggunaan**

### **Input**:

Gambar dengan format `.jpg`, `.jpeg`, atau `.png`.

### **Output**:

Gambar hasil dengan objek foreground terpisah dari latar belakang, disimpan dalam format `.png` dengan transparansi.

---
