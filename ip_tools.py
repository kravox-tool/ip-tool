#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time

from core.utils import clear_screen
from core.config import IP_BANNER, MENU_BANNER
from modules.ip_info import get_ip_info
from modules.port_scanner import port_scanner
from modules.attacks import syn_flood_attack, udp_flood_attack, connection_bruteforce

def main():
    while True:
        clear_screen()
        print("[94m" + IP_BANNER + "[0m")
        print("[92m" + MENU_BANNER + "[0m")
        
        choice = input("[96m[?] Selecciona opción: [0m")
        
        if choice == '1':
            get_ip_info()
        elif choice == '2':
            port_scanner()
        elif choice == '3':
            syn_flood_attack()
        elif choice == '4':
            udp_flood_attack()
        elif choice == '5':
            connection_bruteforce()
        elif choice == '6':
            print("\n[93m[*] Saliendo...[0m")
            sys.exit(0)
        else:
            print("[91m[!] Opción inválida[0m")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[93m[*] Programa interrumpido[0m")
        sys.exit(0)
