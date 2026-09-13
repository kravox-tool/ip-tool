# -*- coding: utf-8 -*-

import socket
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from core.utils import clear_screen, validate_ip, get_service_name
from core.config import IP_BANNER

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        
        if result == 0:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                sock.connect((ip, port))
                sock.send(b'HEAD / HTTP/1.0\r\n\r\n')
                banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
                sock.close()
                return port, True, banner[:100]
            except:
                return port, True, "No banner"
        return port, False, ""
    except:
        return port, False, ""

def port_scanner():
    clear_screen()
    print("[94m" + IP_BANNER + "[0m")
    
    print("[96m" + "="*50 + "[0m")
    print("[96m  ESCANER DE PUERTOS[0m")
    print("[96m" + "="*50 + "[0m")
    print()
    
    target = input("[93m[>] IP objetivo: [0m").strip()
    
    if not validate_ip(target):
        try:
            target = socket.gethostbyname(target)
            print(f"[92m[✓] Resuelto a: {target}[0m")
        except:
            print("[91m[!] IP/Dominio inválido[0m")
            time.sleep(1)
            return
    
    print()
    print("[93mRangos de puertos:[0m")
    print("  [1] Puertos comunes (1-1024)")
    print("  [2] Todos los puertos (1-65535) - LENTO")
    print("  [3] Puertos específicos (ej: 80,443,8080)")
    print("  [4] Top 100 puertos más comunes")
    
    option = input("\n[93m[>] Selecciona: [0m")
    
    ports = []
    if option == '1':
        ports = range(1, 1025)
    elif option == '2':
        ports = range(1, 65536)
    elif option == '3':
        custom = input("[93m[>] Ingresa puertos (ej: 80,443,3306): [0m")
        try:
            ports = [int(p.strip()) for p in custom.split(',')]
        except:
            print("[91m[!] Formato inválido[0m")
            time.sleep(1)
            return
    elif option == '4':
        ports = [21, 22, 23, 25, 53, 80, 81, 110, 111, 113, 135, 139, 143, 179, 199, 443, 445, 465, 514, 515, 548, 554, 587, 631, 646, 873, 990, 993, 995, 1025, 1026, 1027, 1028, 1029, 1110, 1433, 1720, 1723, 1755, 1900, 2000, 2001, 2049, 2121, 2717, 3000, 3128, 3306, 3389, 3986, 4899, 5000, 5001, 5009, 5051, 5060, 5101, 5190, 5357, 5432, 5631, 5666, 5800, 5900, 5901, 6000, 6001, 6646, 7070, 8000, 8008, 8009, 8080, 8081, 8443, 8888, 9100, 9200, 9443, 9999, 10000, 32768, 49152, 49153, 49154, 49155, 49156, 49157]
    else:
        print("[91m[!] Opción inválida[0m")
        time.sleep(1)
        return
    
    threads_input = input("[93m[>] Hilos (recomendado 50-200): [0m")
    try:
        max_workers = int(threads_input)
    except:
        max_workers = 100
    
    print()
    print("[92m" + "="*50 + "[0m")
    print(f"[92m  ESCANEANDO {len(ports)} PUERTOS EN {target}[0m")
    print(f"[92m  Usando {max_workers} hilos...[0m")
    print("[92m" + "="*50 + "[0m")
    print()
    
    open_ports = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_port = {executor.submit(scan_port, target, port): port for port in ports}
        for future in as_completed(future_to_port):
            port, is_open, banner = future.result()
            if is_open:
                service = get_service_name(port)
                print(f"[92m[+] Puerto {port}/tcp ABIERTO - {service}[0m")
                if banner and banner != "No banner":
                    print(f"    [93mBanner: {banner}[0m")
                open_ports.append((port, service, banner))
    
    print()
    print("[96m" + "="*50 + "[0m")
    print(f"[96m  RESUMEN: {len(open_ports)} PUERTOS ABIERTOS[0m")
    print("[96m" + "="*50 + "[0m")
    
    if open_ports:
        print("\n[93mPuerto\tServicio\t\tBanner[0m")
        print("-" * 50)
        for port, service, banner in sorted(open_ports):
            banner_str = banner[:30] if banner else "N/A"
            print(f"[92m{port}\t{service:<15}\t{banner_str}[0m")
    else:
        print("[91m[!] No se encontraron puertos abiertos[0m")
    
    print()
    input("Presiona Enter para continuar...")
