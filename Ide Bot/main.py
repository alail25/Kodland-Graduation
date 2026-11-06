import os
from dotenv import load_dotenv

load_dotenv()  # baca token dari file .env
import discord
from discord.ext import commands
import random

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

tips = [
    "Gunakan botol minum isi ulang daripada membeli air kemasan.",
    "Bawa tas belanja sendiri saat berbelanja.",
    "Pisahkan sampah organik dan anorganik di rumah.",
    "Manfaatkan kembali botol atau kardus bekas.",
    "Kurangi penggunaan sedotan sekali pakai.",
    "Gunakan wadah makan yang bisa dipakai berulang kali.",
    "Bawa alat makan sendiri saat membeli makanan.",
    "Gunakan sapu tangan daripada tisu sekali pakai.",
    "Perbaiki barang yang rusak jika masih bisa digunakan.",
]

facts = [
    "Plastik dapat membutuhkan ratusan tahun untuk terurai.",
    "Kertas dapat didaur ulang beberapa kali sebelum seratnya terlalu pendek.",
    "Sampah makanan dapat dijadikan kompos.",
    "Kaleng aluminium dapat didaur ulang dan digunakan kembali.",
    "Menggunakan tumbler membantu mengurangi botol plastik sekali pakai.",
    "Sampah elektronik sebaiknya tidak dicampur dengan sampah biasa."
]

challenges = [
    "Hari ini, gunakan botol minum isi ulang.",
    "Hari ini, jangan gunakan kantong plastik sekali pakai.",
    "Hari ini, pisahkan sampah organik dan anorganik.",
    "Hari ini, gunakan kedua sisi kertas sebelum membuangnya.",
    "Hari ini, cari satu barang bekas yang bisa digunakan kembali.",
    "Hari ini, bawa wadah makan sendiri jika membeli makanan."
]

jenis_sampah = {
    "botol plastik": "Botol plastik termasuk sampah anorganik dan dapat didaur ulang.",
    "kardus": "Kardus termasuk sampah anorganik dan dapat didaur ulang.",
    "kertas": "Kertas termasuk sampah anorganik dan dapat didaur ulang.",
    "kaleng": "Kaleng termasuk sampah anorganik dan dapat didaur ulang.",
    "kulit pisang": "Kulit pisang termasuk sampah organik dan dapat dijadikan kompos.",
    "sisa makanan": "Sisa makanan termasuk sampah organik dan dapat dijadikan kompos.",
    "baterai": "Baterai termasuk limbah berbahaya dan tidak boleh dibuang sembarangan.",
    "lampu": "Lampu bekas sebaiknya dipisahkan dari sampah biasa."
}

sampah_plastik = [
    "sampah plastik memakan waktu lama untuk di urai"
    "ketika plastik terurai ia menjadi mikroplastik yang dapat membahayakan lingkungan sekitar"
    "Lebih dari 150 juta ton plastik telah mengendap di lautan global."
    " Jika menumpuk di tanah, racun dari partikel plastik dapat membunuh organisme pengurai penting dan mengurangi kesuburan."
]

sampah_elektronik = [
    "Indonesia adalah penghasil limbah elektronik terbesar di Asia Tenggara, dengan total mencapai 1,9 juta ton."
    "zat beracun seperti timbal, kadmium, dan mekuri. zat ini dapat meresap ke dalam tanah dan mencemari sumber air."
    "Paparan zat dari limbah ini dapat memicu masalah kesehatan serius bagi manusia, mulai dari kerusakan organ (seperti hati dan ginjal) hingga risiko kanker."
    "hanya 22,3 persen yang berhasil dikumpulkan dan didaur ulang secara resmi secara global."
]

sampah_makanan = [
    "Sampah makanan yang tertimbun tanpa oksigen (kondisi anaerobik) menghasilkan gas metana (CH₄). menjadikannya salah satu pemicu utama pemanasan global."
    "Pembusukan makanan menghasilkan cairan pekat beracun bernama air lindi (leachate). Cairan ini merembes ke dalam tanah, meracuni cadangan air bersih warga, dan mematikan ekosistem sungai di sekitarnya"
    "sampah makanan di indonesia memiliki total timbunan mencapai 14,73 juta ton per tahun."
    "Gas hidrogen sulfida (H₂S) dan amonia yang dihasilkan dari pembusukan menimbulkan bau menyengat. Gas ini menyebabkan iritasi mata, gangguan pernapasan, dan masalah paru-paru"
]


@bot.event
async def on_ready():
    print(f"Bot aktif sebagai {bot.user}")

@bot.command()
async def tip(ctx):
    await ctx.send(f" **Eco Tip**\n{random.choice(tips)}")

@bot.command()
async def fact(ctx):
    await ctx.send(f" **Fakta Lingkungan**\n{random.choice(facts)}")

@bot.command()
async def challenge(ctx):
    await ctx.send(f" **Eco Challenge**\n{random.choice(challenges)}")

@bot.command()
async def fakta(ctx, kategori=None):
    if kategori is None:
        await ctx.send(
            "**Menu Fakta Sampah**\n\n"
            "Pilih kategori berikut:\n"
            "`/fakta plastik`\n"
            "`/fakta elektronik`\n"
            "`/fakta makanan`"
        )
        return

    kategori = kategori.lower()

    if kategori == "plastik":
        await ctx.send(
            f"**Fakta Sampah Plastik**\n\n"
            f"{random.choice(sampah_plastik)}"
        )

    elif kategori == "elektronik":
        await ctx.send(
            f"**Fakta Sampah Elektronik**\n\n"
            f"{random.choice(sampah_elektronik)}"
        )

    elif kategori == "makanan":
        await ctx.send(
            f"**Fakta Sampah Makanan**\n\n"
            f"{random.choice(sampah_makanan)}"
        )

    else:
        await ctx.send(
            "**Kategori tidak ditemukan.**\n\n"
            "Gunakan:\n"
            "`/fakta plastik`\n"
            "`/fakta elektronik`\n"
            "`/fakta makanan`"
        )

@bot.command()
async def sort(ctx, *, barang):
    barang = barang.lower()

    if barang in jenis_sampah:
        await ctx.send(f" **Hasil Pemilahan**\n{jenis_sampah[barang]}")
    else:
        await ctx.send(
            "Maaf, barang tersebut belum ada di data bot.\n"
            "Coba gunakan: botol plastik, kardus, kertas, kaleng, kulit pisang, sisa makanan, baterai, atau lampu."
        )

@bot.command()
async def helpeco(ctx):
    await ctx.send(
        """
 **Eco Tips Bot**

`/tip` - Menampilkan tips mengurangi sampah.
`/fact` - Menampilkan fakta lingkungan.
`/challenge` - Menampilkan tantangan ramah lingkungan.
`/sort <barang>` - Mengetahui jenis sampah.
`/fakta plastik` - Menampilkan fakta tentang sampah plastik
`/fakta elektronik` - Menampilkan fakta tentang sampah elektronik
`/fakta makanan` - Menampilkan fakta tentang sampah makanan
`/helpeco` - Menampilkan bantuan bot.

Contoh:
`/sort botol plastik`
        """
    )

bot.run(TOKEN)