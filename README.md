# 🎓 Kodland Graduation

Kumpulan tugas dan latihan yang saya kerjakan selama belajar di **Kodland**, mulai dari dasar Python, HTML/CSS, Discord bot, web app dengan Flask dan database, sampai AI (klasifikasi gambar, LLM, dan speech recognition).

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-web%20framework-000000?logo=flask&logoColor=white)
![Discord.py](https://img.shields.io/badge/discord.py-bots-5865F2?logo=discord&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-database-003B57?logo=sqlite&logoColor=white)
![HTML/CSS](https://img.shields.io/badge/HTML%20%26%20CSS-frontend-E34F26?logo=html5&logoColor=white)

---

## 📚 Daftar Isi

- [Yang Saya Pelajari](#-yang-saya-pelajari)
- [Daftar Tugas](#-daftar-tugas)
- [Detail Tiap Tugas](#-detail-tiap-tugas)
- [Cara Menjalankan](#-cara-menjalankan)
- [Keamanan Token](#-keamanan-token)

---

## 🧠 Yang Saya Pelajari

| Bidang | Yang dipelajari |
|---|---|
| **Python dasar** | Variabel, input/output, perulangan `for`, modul `random`, list dan dictionary, fungsi |
| **HTML & CSS** | Struktur halaman, heading, list, gambar, tautan, `iframe` untuk widget cuaca, styling dengan CSS |
| **Discord bot** | Membuat bot dengan `discord.py`, event (`on_ready`, `on_message`), command dengan prefix, mengirim gambar, embed, dan file |
| **API** | Mengambil data dari API publik dengan `requests` dan membaca respons JSON |
| **Flask** | Routing, template Jinja2, mengirim data dari URL dan form ke template, file statis |
| **Database** | SQLite dengan Flask-SQLAlchemy: model, relasi (foreign key), operasi tambah, baca, ubah, hapus (CRUD) |
| **Autentikasi** | Registrasi dan login, session, hash password dengan `werkzeug.security`, setiap user hanya melihat data miliknya sendiri |
| **AI & Machine Learning** | Model klasifikasi gambar (Keras), menjalankan LLM lewat Ollama, speech recognition dan terjemahan otomatis |
| **Kebiasaan baik** | Menyimpan token di file `.env`, memakai `.gitignore`, membuat `requirements.txt` |

---

## 🗂️ Daftar Tugas

| # | Folder | Topik | Teknologi |
|---|---|---|---|
| 1 | `Codland Python 1` | Generator password acak | Python |
| 2 | `Kodland HTML` | Halaman web pertama | HTML, CSS |
| 3 | `Kodland Project bot` | Bot Discord pertama | discord.py |
| 4 | `Meme Bot kodland` | Bot pengirim meme | discord.py |
| 5 | `tugas tambahan ⭐` | Bot gambar rubah dari API | discord.py, requests |
| 6 | `Ide Bot` | Bot edukasi lingkungan dan sampah | discord.py |
| 7 | `flask1` | Website Flask pertama | Flask |
| 8 | `calculator-efisiensi` | Kalkulator efisiensi energi | Flask, Jinja2 |
| 9 | `meme-generator-ind-main` | Generator meme di web | Flask, HTML, CSS |
| 10 | `portfolio-ind-main` | Website portofolio dengan form feedback | Flask, SQLAlchemy |
| 11 | `diary-ind-login` / `diary-ind-main` | Latihan fitur login untuk diary | Flask, SQLAlchemy |
| 12 | `app` | Aplikasi diary lengkap dengan login dan CRUD | Flask, SQLAlchemy, Werkzeug |
| 13 | `Tugas pro` | Bot AI: LLM, deteksi objek, klasifikasi gambar, speech to text | discord.py, Ollama, Keras |
| 🏁 | `Project Final Kodland` | **Project final:** bot Discord pemeriksa hoaks | discord.py, Ollama, SQLite |

---

## 🔍 Detail Tiap Tugas

### 1. Generator Password (`Codland Python 1`)
Program Python yang membuat password acak sesuai panjang yang dimasukkan pengguna, memakai kombinasi huruf besar, huruf kecil, angka, dan simbol.
**Belajar:** `input()`, `for`, string, `random.choice()`.

### 2. Halaman Web Pertama (`Kodland HTML`)
Halaman HTML dengan heading, paragraf, list, gambar, dan widget prakiraan cuaca yang ditanam lewat `iframe`, dilengkapi file CSS.
**Belajar:** struktur dokumen HTML, tag dasar, menghubungkan CSS.

### 3. Bot Discord Pertama (`Kodland Project bot`)
Dua versi bot: `bot.py` memakai `discord.Client` dan `classclient.py` memakai `commands.Bot`. Perintah: `$hello` dan `$heh [jumlah]`.
**Belajar:** intents, event, command, argumen command.

### 4. Meme Bot (`Meme Bot kodland`)
Bot yang mengirim meme acak dari dua kategori: `$animals` dan `$programming`.
**Belajar:** membaca file gambar, `discord.File`, memilih data secara acak.

### 5. Tugas Tambahan ⭐ (`tugas tambahan ⭐`)
Bot yang mengambil gambar rubah acak dari API publik dengan perintah `$fox`.
**Belajar:** memanggil API dengan `requests`, membaca JSON, memakai embed Discord.

### 6. Ide Bot: Bot Edukasi Lingkungan (`Ide Bot`)
Bot bertema lingkungan dengan banyak perintah:

| Perintah | Fungsi |
|---|---|
| `/tip` | Tips hidup ramah lingkungan |
| `/fact` | Fakta tentang sampah dan daur ulang |
| `/challenge` | Tantangan harian |
| `/fakta <kategori>` | Fakta per kategori: sampah plastik, elektronik, makanan |
| `/sort <barang>` | Mengecek jenis sampah (organik, anorganik, berbahaya) |
| `/helpeco` | Daftar perintah |

**Belajar:** merancang bot dari ide sendiri, dictionary sebagai "database" kecil, mengelola banyak command.

### 7. Flask Pertama (`flask1`)
Website dengan beberapa halaman: fakta acak dari file `.txt`, fakta modern dari template, dan foto acak dari folder `static`.
**Belajar:** `@app.route`, `render_template`, `send_file`, membaca file dengan `os.listdir`.

### 8. Kalkulator Efisiensi Energi (`calculator-efisiensi`)
Website bertema hemat energi: pengguna memilih ukuran rumah, jumlah lampu, dan perangkat elektronik, lalu mendapat estimasi konsumsi energi (kWh). Ada juga halaman formulir yang menyimpan data ke file.
**Belajar:** route dinamis (`/<size>/<lights>/<device>`), template turunan (`dasar.html`), form `POST`, menulis file.

### 9. Meme Generator (`meme-generator-ind-main`)
Aplikasi web untuk membuat meme: pilih gambar, tulis teks atas dan bawah, atur posisi dan warna teks.
**Belajar:** menerima data form di Flask dan mengirimnya kembali ke template.

### 10. Portofolio Web (`portfolio-ind-main`)
Website portofolio pribadi dengan bagian About Me, My Skills, dan formulir Feedback yang menyimpan masukan ke database SQLite.
**Belajar:** Flask-SQLAlchemy, model database, redirect ke anchor (`#feedback`), desain halaman portofolio.

### 11. Latihan Login Diary (`diary-ind-login`, `diary-ind-main`)
Kerangka aplikasi diary dengan komentar tugas (membuat tabel `User`, menyimpan pengguna, verifikasi login). Bagian ini menjadi dasar untuk aplikasi `app`.

### 12. Aplikasi Diary Lengkap (`app`)
Aplikasi diary multi-pengguna:
- Registrasi dan login, password disimpan sebagai **hash**
- Setiap pengguna hanya melihat kartu (catatan) miliknya
- Buat, lihat, ubah, dan hapus catatan (CRUD)
- Logout dan header keamanan

**Belajar:** relasi tabel `User` dan `Card`, `session`, `generate_password_hash` / `check_password_hash`, otorisasi.

### 13. Tugas Pro: AI (`Tugas pro`)
Bot Discord yang menggabungkan beberapa teknologi AI:

| Perintah | Fungsi |
|---|---|
| `$ask_ollama <pertanyaan>` | Bertanya ke LLM lewat Ollama, jawaban panjang dikirim sebagai file `.txt` |
| `$detect_ollama` | Mendeteksi objek pada gambar yang dilampirkan |
| `$klasifikasi` | Klasifikasi gambar dengan model Keras (`merpati` atau `pipit`) |

Di dalam `Tugas pro/audio` ada skrip **speech to text**: merekam suara lewat mikrofon, mengubahnya jadi teks dengan Google Speech Recognition, lalu menerjemahkannya ke banyak bahasa dengan `googletrans`.

**Belajar:** memakai model ML yang sudah dilatih (`keras_model.h5`), pra-pemrosesan gambar (resize 224x224 dan normalisasi), streaming respons LLM, speech recognition, dan terjemahan otomatis.

### 🏁 Project Final: Bot Pemeriksa Hoaks (`Project Final Kodland`)
Bot Discord yang membantu memeriksa apakah sebuah informasi berpotensi hoaks. Teks atau gambar dianalisis oleh model AI lewat Ollama, lalu hasilnya diringkas beserta tingkat keyakinannya. Setiap pengecekan disimpan di database SQLite sehingga pengguna bisa melihat riwayatnya.

| Perintah | Fungsi |
|---|---|
| `$cek <teks>` | Memeriksa teks. Bisa juga dengan lampiran gambar, atau balas sebuah pesan dengan `$cek` |
| `$riwayat` | Menampilkan 5 pengecekan terakhir milik pengguna |
| `$hapusriwayat` | Menghapus riwayat pengguna |
| `$statistik` | Statistik semua pengecekan per tingkat hasil |
| `$bantuan` | Daftar perintah |

**Fitur penting:** batas panjang teks (4000 karakter) dan ukuran gambar (5 MB), batas waktu tunggu jawaban AI (120 detik), penanganan error command, dan token disimpan di `.env`.
**Belajar:** merancang project dari awal sampai selesai, memisahkan kode ke modul (`bot.py` dan `db.py`), query SQL dengan parameter, `asyncio`, menggabungkan LLM dengan database, dan mengelola konfigurasi lewat environment variable.

Cara menjalankan:

```bash
cd "Project Final Kodland"
pip install -r requirements.txt
cp .env.example .env        # lalu isi DISCORD_TOKEN dan pengaturan Ollama
python bot.py
```

---

## ▶️ Cara Menjalankan

Pastikan Python 3.11+ sudah terpasang.

```bash
# 1. Clone repo
git clone https://github.com/alail25/Kodland-Graduation.git
cd Kodland-Graduation

# 2. (Opsional) buat virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

**Project Flask** (`flask1`, `calculator-efisiensi`, `meme-generator-ind-main`, `portfolio-ind-main`, `app`):

```bash
pip install flask flask-sqlalchemy
cd app
python main2.py
# buka http://127.0.0.1:5000
```

*(Nama file utama: `main.py`, kecuali `app` dan `calculator-efisiensi` yang memakai `main2.py`.)*

**Project bot Discord:**

```bash
pip install discord.py requests python-dotenv
```

Buat bot di [Discord Developer Portal](https://discord.com/developers/applications), lalu simpan token di file `.env` (lihat bagian di bawah), jangan menulisnya langsung di kode.

**Tugas Pro (AI):**

```bash
pip install discord.py python-dotenv ollama tensorflow pillow numpy speechrecognition pyaudio googletrans==4.0.0-rc1
```

Untuk `$ask_ollama` dan `$detect_ollama`, jalankan [Ollama](https://ollama.com) lebih dulu.

---

## 🔐 Keamanan Token

Token bot dan API key **tidak boleh** ditulis di dalam kode atau di-upload ke GitHub. Cara yang benar:

1. Buat file `.env`:
   ```env
   DISCORD_TOKEN=isi_token_kamu
   OLLAMA_API_KEY=isi_api_key_kamu
   ```
2. Baca di kode:
   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()
   TOKEN = os.getenv("DISCORD_TOKEN")
   ```
3. Tambahkan `.env` ke `.gitignore`.

Semua bot di repo ini membaca token dari `.env`, dan file `.env` tidak ikut di-upload. Kalau kamu mencoba menjalankannya, isi token milikmu sendiri.

---

## 👤 Penulis

**M. Rizqan Almaliky** ([@alail25](https://github.com/alail25))

Dibuat sebagai bagian dari kursus Kodland. Terima kasih kepada para mentor atas bimbingannya! 🙌
