# -*- coding: utf-8 -*-

import socket
import requests
import time
from core.utils import clear_screen, validate_ip
from core.config import IP_BANNER

def get_ip_info():
    """Obtiene información completa de una IP"""
    clear_screen()
    print("[94m" + IP_BANNER + "[0m")
    
    print("[96m" + "="*50 + "[0m")
    print("[96m  INFORMACIÓN COMPLETA DE IP[0m")
    print("[96m" + "="*50 + "[0m")
    print()
    
    target = input("[93m[>] Ingresa la IP o dominio: [0m").strip()
    
    if not target:
        print("[91m[!] Debes ingresar una IP o dominio[0m")
        time.sleep(1)
        return
    
    try:
        if not validate_ip(target):
            print(f"[93m[*] Resolviendo dominio {target}...[0m")
            ip_address = socket.gethostbyname(target)
            print(f"[92m[✓] IP resuelta: {ip_address}[0m")
        else:
            ip_address = target
    except Exception as e:
        print(f"[91m[!] Error resolviendo: {str(e)}[0m")
        time.sleep(1)
        return
    
    print()
    print("[92m" + "="*50 + "[0m")
    print("[92m  OBTENIENDO DATOS...[0m")
    print("[92m" + "="*50 + "[0m")
    print()
    
    apis = [
        f"http://ip-api.com/json/{ip_address}",
        f"https://ipinfo.io/{ip_address}/json",
    ]
    
    all_data = {}
    for api_url in apis:
        try:
            response = requests.get(api_url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                all_data.update(data)
        except:
            pass
    
    print("[96m" + "="*50 + "[0m")
    print("[96m  📊 INFORMACIÓN COMPLETA[0m")
    print("[96m" + "="*50 + "[0m")
    print()
    
    info_mapping = {
        'ip': 'IP Objetivo',
        'city': 'Ciudad',
        'region': 'Región/Estado',
        'regionName': 'Nombre Región',
        'country': 'País',
        'countryCode': 'Código País',
        'lat': 'Latitud',
        'lon': 'Longitud',
        'timezone': 'Zona Horaria',
        'isp': 'Proveedor ISP',
        'org': 'Organización',
        'as': 'Sistema Autónomo (AS)',
        'asname': 'Nombre AS',
        'query': 'IP Consultada',
        'postal': 'Código Postal',
        'loc': 'Ubicación (lat,lon)',
        'hostname': 'Hostname',
        'company': 'Compañía',
        'carrier': 'Operador Móvil',
        'proxy': 'Es Proxy/VPN',
        'hosting': 'Es Hosting/Datacenter',
        'mobile': 'Es Conexión Móvil'
    }
    
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
    except:
        hostname = "No disponible"
    
    print(f"[93m{'IP Objetivo:':<25}[0m {ip_address}")
    print(f"[93m{'Hostname:':<25}[0m {hostname}")
    
    for key, label in info_mapping.items():
        if key in all_data and all_data[key]:
            value = all_data[key]
            if isinstance(value, bool):
                value = "Sí" if value else "No"
            print(f"[93m{label:<25}[0m {value}")
    
    print()
    print("[96m" + "="*50 + "[0m")
    print("[96m  🔧 INFORMACIÓN DE RED[0m")
    print("[96m" + "="*50 + "[0m")
    print()
    
    try:
        ip_parts = ip_address.split('.')
        first_octet = int(ip_parts[0])
        if first_octet < 128:
            ip_class = "A"
        elif first_octet < 192:
            ip_class = "B"
        elif first_octet < 224:
            ip_class = "C"
        else:
            ip_class = "D/E (Multicast/Experimental)"
        
        print(f"[93m{'Clase de IP:':<25}[0m {ip_class}")
        print(f"[93m{'Primera octeto:':<25}[0m {first_octet}")
        print(f"[93m{'Rango privado:':<25}[0m {'Sí' if ip_address.startswith(('10.', '172.16.', '192.168.')) else 'No'}")
    except:
        pass
    
    print()
    print("[92m[✓] Información completa obtenida[0m")
    print()
    input("Presiona Enter para continuar...")
