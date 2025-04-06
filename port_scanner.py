import socket
import threading
import json
from colorama import Fore, Style, init
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor
import os
import ssl 

init()

lock = threading.Lock()

# Reverse DNS Lookup
def get_reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "Çözüm Yok"


# banner

def get_banner(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip, port))

        # SSL Portları
        if port in [993, 995, 465, 587, 443]:
            context = ssl.create_default_context()
            sock = context.wrap_socket(sock, server_hostname=ip)

        # Gönderilecek Komut
        if port == 21:
            sock.send(b'HELP\r\n')
        elif port in [25, 465, 587]:
            sock.send(b'EHLO test\r\n')
        elif port in [110, 995]:
            sock.send(b'CAPA\r\n')
        elif port in [143, 993]:
            sock.send(b'. CAPABILITY\r\n')
        else:
            sock.send(b'HEAD / HTTP/1.0\r\n\r\n')

        try:
            banner = sock.recv(2048).decode(errors='ignore').strip()
        except:
            banner = "Banner alınamadı"

        sock.close()
        return banner if banner else "Banner alınamadı"

    except Exception as e:
        return "Banner alınamadı"



# Servis Tespiti
def get_service(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Bilinmiyor"

# Port Tarama
def scan_port(ip, port, open_ports):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            banner = get_banner(ip, port)
            service = get_service(port)
            reverse_dns = get_reverse_dns(ip)
            with lock:
                open_ports.append((ip, port, service, banner, reverse_dns))
        sock.close()
    except:
        pass

# Sonuçları Kaydet

def save_results(open_ports, output_format):
    log_dir = "/logs"  
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)


    if output_format == 'txt' or output_format == 'all':
        with open(f"{log_dir}/sonuclar.txt", "w") as file:
            for ip, port, service, banner, reverse_dns in open_ports:
                banner = " ".join(banner.splitlines()).strip()
                line = f"{ip}:{port} açık --> Servis: {service} | Reverse DNS: {reverse_dns}\nBanner: {banner}\n{'-'*60}\n"
                file.write(line)

    if output_format == 'html' or output_format == 'all':
        with open(f"{log_dir}/sonuclar.html", "w") as file:
            file.write("<html><body><pre>\n")
            for ip, port, service, banner, reverse_dns in open_ports:
                banner = " ".join(banner.splitlines()).strip()
                line = f"{ip}:{port} açık --> Servis: {service} | Banner: {banner} | Reverse DNS: {reverse_dns}\n"
                file.write(line)
            file.write("</pre></body></html>")

    if output_format == 'json' or output_format == 'all':
        with open(f"{log_dir}/sonuclar.json", "w") as file:
            json.dump(open_ports, file, indent=4)




# Menü
print("=== Port Scanner ===\n")

print("Sonuçları nasıl kaydetmek istersin?")
print("1- TXT (Klasik)")
print("2- HTML (Renkli - Browser ile aç)")
print("3- JSON (API ve Developer için)")
print("4- Hepsi")
secim = input("Seçim: ")

formats = {"1": "txt", "2": "html", "3": "json", "4": "all"}
output_format = formats.get(secim, "txt")

print("\n1- Tek IP Tara")
print("2- Çıkış")
mode = input("Seçim: ")

if mode == "1":
    hedef_ip = input("Hedef IP: ")
    bas_port = int(input("Başlangıç Port: "))
    bit_port = int(input("Bitiş Port: "))

    open_ports = []

    print(f"\n{hedef_ip} adresinde {bas_port}-{bit_port} portları taranıyor...\n")

    with ThreadPoolExecutor(max_workers=100) as executor:
        list(tqdm(executor.map(lambda port: scan_port(hedef_ip, port, open_ports), range(bas_port, bit_port + 1)), total=bit_port - bas_port + 1))

    print(Fore.GREEN + f"\nTarama Bitti! {len(open_ports)} açık port bulundu." + Style.RESET_ALL)

    save_results(open_ports, output_format)
    print(Fore.YELLOW + f"\nSonuçlar 'logs' klasörüne kaydedildi.\n" + Style.RESET_ALL)

else:
    print("Çıkılıyor...")

