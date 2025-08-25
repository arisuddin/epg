import os
import requests

EPG_URL = "https://epg.pw/xmltv/epg_ID.xml"

# Simpan file di root repo
LOCAL_FILE = os.path.join(os.getcwd(), "epg.xml")  # absolute path writeable

try:
    r = requests.get(EPG_URL, timeout=30)
    r.raise_for_status()

    with open(LOCAL_FILE, "wb") as f:
        f.write(r.content)

    print(f"EPG berhasil diambil dan disimpan di {LOCAL_FILE}")
except Exception as e:
    print(f"Gagal mengambil EPG: {e}")
