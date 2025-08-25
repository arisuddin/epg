import os
import requests

# Dua URL EPG public
EPG_URLS = [
    "https://raw.githubusercontent.com/AqFad2811/epg/refs/heads/main/astro.xml",      # URL pertama
    "https://raw.githubusercontent.com/AqFad2811/epg/refs/heads/main/indonesia.xml",    # URL kedua
]

local_file = os.path.join(os.getcwd(), "epg.xml")  # simpan di root repo
combined_content = ""

for url in EPG_URLS:
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        combined_content += r.text + "\n"  # gabungkan konten
        print(f"EPG berhasil diambil dari {url}")
    except Exception as e:
        print(f"Gagal mengambil EPG dari {url}: {e}")

# tulis gabungan ke file
try:
    with open(local_file, "w", encoding="utf-8") as f:
        f.write(combined_content)
    print(f"Semua EPG berhasil digabung dan disimpan di {local_file}")
except Exception as e:
    print(f"Gagal menulis file gabungan: {e}")
