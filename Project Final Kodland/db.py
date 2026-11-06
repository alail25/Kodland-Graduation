import sqlite3
from contextlib import closing
from pathlib import Path

DB_PATH = Path(__file__).parent / "riwayat.db"


def _koneksi() -> sqlite3.Connection:
    return sqlite3.connect(DB_PATH)


def init_db() -> None:
    with closing(_koneksi()) as konek:
        konek.execute(
            """
            CREATE TABLE IF NOT EXISTS pengecekan (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                jenis TEXT NOT NULL,
                ringkasan TEXT NOT NULL,
                tingkat TEXT NOT NULL,
                waktu TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
            )
            """
        )
        konek.commit()


def simpan_cek(user_id: int, jenis: str, ringkasan: str, tingkat: str) -> None:
    with closing(_koneksi()) as konek:
        konek.execute(
            "INSERT INTO pengecekan (user_id, jenis, ringkasan, tingkat) VALUES (?, ?, ?, ?)",
            (str(user_id), jenis, ringkasan, tingkat),
        )
        konek.commit()


def riwayat_pengguna(user_id: int, batas: int = 5) -> list[tuple]:
    with closing(_koneksi()) as konek:
        baris = konek.execute(
            """
            SELECT jenis, ringkasan, tingkat, waktu
            FROM pengecekan
            WHERE user_id = ?
            ORDER BY id DESC
            LIMIT ?
            """,
            (str(user_id), batas),
        ).fetchall()
    return baris


def statistik() -> tuple[int, dict, dict]:
    with closing(_koneksi()) as konek:
        total = konek.execute("SELECT COUNT(*) FROM pengecekan").fetchone()[0]
        per_tingkat = dict(
            konek.execute(
                "SELECT tingkat, COUNT(*) FROM pengecekan GROUP BY tingkat ORDER BY COUNT(*) DESC"
            ).fetchall()
        )
        per_jenis = dict(
            konek.execute(
                "SELECT jenis, COUNT(*) FROM pengecekan GROUP BY jenis ORDER BY COUNT(*) DESC"
            ).fetchall()
        )
    return total, per_tingkat, per_jenis
