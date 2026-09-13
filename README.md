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

# 2. Instalar dependencias necesarias (Python, Git)
pkg install python git -y

# 3. Instalar los requerimientos de Python
pip install -r requirements.txt

# 4. Ejecutar la herramienta (Python reconocerá la estructura de paquetes gracias a los archivos __init__.py)
python3 ip_tools.py
```

---

## ⚠️ Aviso Legal (Disclaimer)
> *Esta herramienta ha sido creada estrictamente con **fines educativos, de auditoría interna y diagnóstico de redes**. El uso de las funciones de estrés contra objetivos externos sin autorización previa y explícita es ilegal.*

## 📄 Licencia
Distribuido bajo la Licencia MIT. Consulta el archivo `LICENSE` para más información.
