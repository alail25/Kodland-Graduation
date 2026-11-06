# Bot Discord Pemeriksa Hoaks

Ini proyek final saya di Kodland. Bot Discord yang bisa mengecek apakah sebuah pesan atau berita punya ciri-ciri hoaks. Kita tinggal kirim teksnya atau screenshot-nya, nanti bot menjelaskan tanda yang mencurigakan dan menyarankan cara memverifikasinya.

Hasilnya cuma perkiraan, bukan pengecekan fakta. Tetap cek ke sumber resmi seperti [turnbackhoax.id](https://turnbackhoax.id).

## Yang bisa dilakukan bot

- Mengecek teks berita atau pesan berantai
- Mengecek screenshot (bot membaca teks di gambar)
- Mengecek pesan orang lain, tinggal balas pesannya dengan `$cek`
- Memberi tingkat kecurigaan: rendah, sedang, atau tinggi
- Menyimpan riwayat pengecekan tiap pengguna
- Menampilkan statistik pengecekan

## Perintah

| Perintah | Fungsi |
|---|---|
| `$cek <teks>` | cek teks |
| `$cek` + gambar | cek screenshot |
| `$cek` (balas pesan lain) | cek pesan yang dibalas |
| `$riwayat` | 5 pengecekan terakhirmu |
| `$hapusriwayat` | hapus riwayatmu |
| `$statistik` | statistik semua pengecekan |
| `$bantuan` | daftar perintah |

Contoh:

```
$cek BREAKING!!! SEBARKAN SEKARANG KE SEMUA GRUP!!!
```

## Yang dipakai

- Python
- discord.py
- Ollama untuk model AI-nya (bisa baca gambar)
- SQLite untuk menyimpan riwayat
- python-dotenv untuk menyimpan token di file `.env`

## Isi repo

```
bot.py             kode utama bot
requirements.txt   daftar library
.env.example       contoh isi file .env
.gitignore
README.md
```

File `riwayat.db` dibuat sendiri saat bot pertama kali jalan.

## Cara menjalankan

1. Buat bot di [Discord Developer Portal](https://discord.com/developers/applications), salin tokennya, dan aktifkan **Message Content Intent** di menu Bot. Setelah itu undang bot ke server.
2. Pasang [Ollama](https://ollama.com) dan siapkan modelnya. Kalau mau pakai fitur screenshot, modelnya harus bisa membaca gambar.
3. Unduh proyek dan pasang library:

```bash
git clone https://github.com/alail25/Kodland-Graduation.git
cd Kodland-Graduation
pip install -r requirements.txt
```

4. Salin `.env.example` jadi `.env`, lalu isi:

```env
DISCORD_TOKEN=token_bot_kamu
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=gemma4:31b-cloud
OLLAMA_API_KEY=
```

`OLLAMA_API_KEY` boleh dikosongkan kalau tidak dipakai, dan modelnya bisa diganti sesuka kamu.

5. Jalankan:

```bash
python bot.py
```

## Cara kerjanya

Kalau ada yang mengetik `$cek`, bot mengirim teks atau gambarnya ke model lewat Ollama, bersama instruksi supaya model menjawab dengan format tetap: tingkat kecurigaan, tanda yang ditemukan, dan saran verifikasi. Bot lalu mengambil tingkat kecurigaan dari jawaban itu, menyimpannya ke database, dan menampilkan hasilnya.

Beberapa batas yang saya pasang:

- teks maksimal 4000 karakter, gambar maksimal 5 MB
- cooldown 10 detik per pengguna
- kalau model tidak menjawab dalam 120 detik, bot berhenti menunggu
- teks pengguna dibungkus tanda `<<<` dan `>>>` dan diminta dianggap sebagai data saja, supaya perintah yang diselipkan di dalam teks tidak diikuti
- mention seperti `@everyone` dimatikan
- riwayat hanya menyimpan 200 karakter pertama dari teks

## Yang saya pelajari

Dari proyek ini dan tugas-tugas sebelumnya di Kodland, saya belajar membuat bot Discord dengan discord.py, memakai model AI lewat Ollama, menyimpan data dengan SQLite, menjaga token tetap aman dengan `.env` dan `.gitignore`, serta memakai Git dan GitHub. Sebelum proyek final saya juga mengerjakan bot Discord, aplikasi Flask, model Keras, Ollama, dan speech recognition. Kodenya tidak saya taruh di sini, supaya repo ini hanya berisi proyek final.

## Penulis

M. Rizqan Almaliky (@alail25)

Dibuat sebagai bagian dari kursus Kodland. Terima kasih kepada para mentor atas bimbingannya! 🙌
