import requests
from lxml import etree

EPG_URLS = [
    "https://raw.githubusercontent.com/AqFad2811/epg/refs/heads/main/astro.xml",
    "https://iptv-epg.org/files/epg-id.xml",
    "https://epg.pw/api/epg.xml?lang=en&timezone=QXNpYS9KYWthcnRh&date=20250831&channel_id=430425",
]

tv_root = etree.Element("tv")
channel_ids = set()

for url in EPG_URLS:
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        tree = etree.fromstring(r.content)

        for ch in tree.findall("channel"):
            cid = ch.get("id")
            if cid in channel_ids:
                continue
            channel_ids.add(cid)
            tv_root.append(ch)

        for prog in tree.findall("programme"):
            tv_root.append(prog)

        print(f"✅ EPG berhasil diambil dari {url}")
    except Exception as e:
        print(f"❌ Gagal mengambil EPG dari {url}: {e}")

# Simpan hasil gabungan
with open("epg.xml", "wb") as f:
    f.write(etree.tostring(tv_root, encoding="utf-8", xml_declaration=True, pretty_print=True))

print("🎉 Semua EPG berhasil digabung dengan format XML valid!")
