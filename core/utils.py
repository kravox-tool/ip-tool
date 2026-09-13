# -*- coding: utf-8 -*-

import os
import socket

def clear_screen():
    os.system('clear')

def validate_ip(ip):
    """Valida que sea una dirección IP correcta"""
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

def get_service_name(port):
    """Obtiene el nombre de un servicio común por puerto"""
    services = {
        21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP',
        53: 'DNS', 80: 'HTTP', 110: 'POP3', 143: 'IMAP',
        443: 'HTTPS', 445: 'SMB', 3306: 'MySQL',
        3389: 'RDP', 5432: 'PostgreSQL', 5900: 'VNC',
        6379: 'Redis', 8080: 'HTTP-Proxy', 8443: 'HTTPS-Alt'
    }
    return services.get(port, 'Unknown')
