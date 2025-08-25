import requests

EPG_URL = "https://raw.githubusercontent.com/public-epg/xmltv/master/epg.xml"
LOCAL_FILE = "epg.xml"

try:
    response = requests.get(EPG_URL)
    response.raise_for_status()
    with open(LOCAL_FILE, "wb") as f:
        f.write(response.content)
    print(f"EPG berhasil diambil dan disimpan di {LOCAL_FILE}")
except Exception as e:
    print(f"Gagal mengambil EPG: {e}")
