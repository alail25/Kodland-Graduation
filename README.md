# 🛡️ Bot Discord Pemeriksa Hoaks

Proyek final saya di **Kodland**: bot Discord yang membantu mengenali tanda-tanda hoaks. Pengguna mengirim **teks** atau **screenshot** berita, lalu AI menganalisis ciri-ciri yang mencurigakan dan memberi saran cara memverifikasinya.

> ⚠️ Bot ini **bukan pengecek fakta**. Hasilnya hanya perkiraan berdasarkan tanda-tanda umum hoaks. Selalu verifikasi ke sumber resmi seperti [turnbackhoax.id](https://turnbackhoax.id).

---

## ✨ Fitur

- **Cek teks**: analisis tanda hoaks dari teks berita atau pesan berantai
- **Cek screenshot**: AI membaca teks pada gambar lalu menganalisisnya
- **Cek pesan orang lain**: balas sebuah pesan dengan `$cek` untuk menganalisis isi (dan gambar) pesan itu
- **Tingkat kecurigaan** berlabel warna: 🟢 rendah, 🟡 sedang, 🔴 tinggi
- **Riwayat pengecekan** per pengguna, disimpan di SQLite
- **Statistik** jumlah pengecekan berdasarkan tingkat dan jenis input
- **Pengaman**: cooldown, batas ukuran input, batas waktu tunggu, dan perlindungan dasar dari *prompt injection*

## 💬 Perintah

| Perintah | Fungsi |
|---|---|
| `$cek <teks>` | Cek teks |
| `$cek` + lampiran gambar | Cek screenshot |
| `$cek` (membalas pesan lain) | Cek pesan yang dibalas |
| `$riwayat` | Tampilkan 5 pengecekan terakhirmu |
| `$hapusriwayat` | Hapus riwayat milikmu |
| `$statistik` | Statistik semua pengecekan |
| `$bantuan` | Tampilkan menu bantuan |

Contoh:

```
$cek BREAKING!!! SEBARKAN SEKARANG KE SEMUA GRUP!!!
```

Format jawaban bot:

```
Tingkat kecurigaan: tinggi
Tanda yang ditemukan:
- huruf kapital dan tanda seru berlebihan
- ajakan menyebarkan ke banyak grup
Saran verifikasi:
- cek turnbackhoax.id atau cari di media resmi
```

## 🧰 Teknologi

| Bagian | Teknologi |
|---|---|
| Bahasa | Python |
| Bot | [discord.py](https://discordpy.readthedocs.io) |
| AI | [Ollama](https://ollama.com) (model bisa diganti lewat `.env`, bisa membaca gambar) |
| Database | SQLite (`sqlite3` bawaan Python) |
| Konfigurasi | `python-dotenv` |

## 📁 Struktur Folder

```
Kodland-Graduation/
├── bot.py             # kode utama bot
├── requirements.txt   # daftar library
├── .env.example       # contoh isi file konfigurasi
├── .gitignore         # file yang tidak ikut diunggah
└── README.md
```

File `riwayat.db` dibuat otomatis saat bot pertama kali dijalankan.

## 🚀 Cara Menjalankan

### 1. Siapkan bot di Discord
1. Buka [Discord Developer Portal](https://discord.com/developers/applications) lalu buat aplikasi baru.
2. Di menu **Bot**, buat bot dan salin **token**-nya.
3. Di menu yang sama, aktifkan **Message Content Intent** (wajib, karena bot membaca isi pesan).
4. Undang bot ke servermu lewat menu **OAuth2 → URL Generator** (scope `bot`, izin untuk membaca dan mengirim pesan).

### 2. Siapkan Ollama
Pasang [Ollama](https://ollama.com) dan pastikan modelnya tersedia. Model bawaan di `.env.example` adalah `gemma4:31b-cloud`, tapi kamu bebas menggantinya, asalkan modelnya mendukung input gambar kalau ingin memakai fitur screenshot.

### 3. Unduh dan pasang
```bash
git clone https://github.com/alail25/Kodland-Graduation.git
cd Kodland-Graduation
pip install -r requirements.txt
```

### 4. Isi konfigurasi
Salin `.env.example` menjadi `.env`, lalu isi:

```env
DISCORD_TOKEN=token_bot_kamu
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=gemma4:31b-cloud
OLLAMA_API_KEY=
```

`OLLAMA_API_KEY` boleh dikosongkan kalau tidak dipakai.

### 5. Jalankan
```bash
python bot.py
```

Kalau berhasil, terminal menampilkan `Bot aktif sebagai ...`.

## ⚙️ Cara Kerja

1. Pengguna mengirim `$cek` dengan teks, gambar, atau membalas sebuah pesan.
2. Bot memeriksa input (batas karakter dan ukuran gambar), lalu mengirimnya ke model lewat Ollama bersama instruksi sistem khusus literasi digital.
3. Model membalas dengan format tetap: tingkat kecurigaan, tanda yang ditemukan, dan saran verifikasi.
4. Bot mengambil tingkat kecurigaan dari jawaban, menyimpannya ke SQLite, lalu menampilkan hasil dengan emoji warna.

### Batas dan keamanan
- Teks maksimal **4000 karakter**, gambar maksimal **5 MB**
- Cooldown **10 detik** per pengguna
- Batas waktu tunggu jawaban AI **120 detik**
- Teks pengguna dibungkus penanda `<<< >>>` dan diperlakukan hanya sebagai data, supaya perintah di dalam teks tidak diikuti AI
- Mention (`@everyone` dll.) dimatikan agar bot tidak bisa dipakai untuk spam
- Riwayat hanya menyimpan 200 karakter pertama dari teks, atau penanda `(screenshot)` untuk gambar
- Token disimpan di `.env` yang **tidak** ikut diunggah ke GitHub

## 📚 Yang Saya Pelajari

Selama belajar di Kodland, proyek ini menggabungkan banyak hal yang saya pelajari:

- Membuat **bot Discord** dengan `discord.py`: perintah, event, cooldown, dan penanganan error
- Menghubungkan aplikasi dengan **model AI lewat Ollama**, termasuk input gambar
- Merancang **prompt sistem** supaya jawaban AI konsisten dan aman dari prompt injection
- Menyimpan data dengan **SQLite**
- Mengelola rahasia dengan **`.env`** dan `.gitignore`
- Memakai **Git & GitHub** untuk mempublikasikan proyek

Sebelum proyek final, saya juga mengerjakan beberapa tugas lain di Kodland, misalnya bot Discord, aplikasi web dengan Flask, model Keras, Ollama, dan pengenalan suara. Kodenya tidak saya sertakan di repositori ini supaya fokus pada proyek final.

## 🔮 Rencana Pengembangan

- Antarmuka web dengan Flask
- Pencocokan otomatis dengan basis data hoaks yang sudah dibantah
- Dukungan pengecekan dari tautan berita

## 👤 Penulis

**alail25**, lulusan Kodland
GitHub: [@alail25](https://github.com/alail25)
