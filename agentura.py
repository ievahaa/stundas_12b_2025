import sqlite3

conn = sqlite3.connect("pasakumi.db")
conn.execute("PRAGMA foreign_keys = ON;")

# -------------------------
# Tabulu izveide (3 tabulas)
# -------------------------
conn.execute("""
CREATE TABLE IF NOT EXISTS vietas (
    vieta_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL,
    pilseta TEXT NOT NULL,
    adrese TEXT
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS grupas (
    grupa_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL UNIQUE,
    zanrs TEXT
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS pasakumi (
    pasakums_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nosaukums TEXT NOT NULL,
    datums TEXT NOT NULL,          -- 'YYYY-MM-DD'
    sakuma_laiks TEXT NOT NULL,    -- 'HH:MM'
    biletes_kopa INTEGER NOT NULL CHECK (biletes_kopa >= 0),
    vieta_id INTEGER NOT NULL,
    grupa_id INTEGER NOT NULL,
    FOREIGN KEY (vieta_id) REFERENCES vietas(vieta_id),
    FOREIGN KEY (grupa_id) REFERENCES grupas(grupa_id)
)
""")

conn.commit()