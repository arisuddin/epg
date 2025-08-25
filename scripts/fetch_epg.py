import requests

# URL EPG public yang pasti ada
EPG_URL = "https://raw.githubusercontent.com/public-epg/xmltv/master/epg.xml"
LOCAL_FILE = "epg.xml"

try:
    r = requests.get(EPG_URL, timeout=30)
    r.raise_for_status()
    with open(LOCAL_FILE, "wb") as f:
        f.write(r.content)
    print(f"EPG berhasil diambil dan disimpan di {LOCAL_FILE}")
except Exception as e:
    print(f"Gagal mengambil EPG: {e}")
    raise
