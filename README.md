# 🔍 IP Tools & Network Reconnaissance (Modular)

`ip_tools` es una herramienta avanzada desarrollada en Python con una estructura modular, orientada al análisis de redes, escaneo de puertos y pruebas de conectividad en **Termux (Android)** o sistemas Linux.

## 📂 Estructura del Proyecto

```text
ip-tools/
├── ip_tools.py          # Script principal (Punto de entrada)
├── requirements.txt     # Dependencias de Python
├── LICENSE              # Licencia MIT
├── README.md            # Documentación
├── core/                # Núcleo del sistema
│   ├── __init__.py
│   ├── config.py        # Banners y configuración general
│   └── utils.py         # Funciones de validación y utilidades
└── modules/             # Módulos funcionales de la herramienta
    ├── __init__.py
    ├── ip_info.py       # Reconocimiento y geolocalización de IP
    ├── port_scanner.py  # Escáner de puertos multihilo
    └── attacks.py       # Módulos de estrés de red (SYN, UDP, Brute-force)
```

---

## ⚙️ Instalación en Termux

Abre tu aplicación **Termux** y ejecuta los siguientes comandos:

```bash
# 1. Actualizar paquetes del sistema
pkg update && pkg upgrade -y

# 3. clonar repo
git clone https://github.com/kravox-tool/ip-tool.git

# 3. entrar al repo
cd ip-tool 

# 4. Ejecutar la herramienta 
python ip.py
```
