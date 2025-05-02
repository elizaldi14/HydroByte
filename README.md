# HydroByte: Sistema de Monitoreo Hidropónico

![Logo](utils/img/logo_pi.png)

**HydroByte** es una aplicación de escritorio moderna para el monitoreo en tiempo real de sistemas hidropónicos. Permite visualizar el estado de sensores, consultar gráficas históricas, recibir alertas y personalizar la experiencia visual mediante temas claro/oscuro.

## Características principales
- Visualización en tiempo real de sensores (pH, EC, temperatura, nivel de agua)
- Gráficas interactivas y submenús temáticos
- Gestión de alertas y notificaciones
- Cambio de tema (claro/oscuro) en toda la interfaz
- Barra lateral con navegación modular
- Ícono y branding personalizados

## Instalación

### 1. Clona el repositorio
```bash
git clone https://github.com/elizaldi14/HydroByte.git
cd HydroByte
```

### 2. Crea un entorno virtual (opcional pero recomendado)
```bash
python -m venv venv
# Activa el entorno:
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 3. Instala las dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecuta la aplicación
```bash
python main.py
```

## Dependencias principales
- Python 3.12+
- PySide6
- pyqtgraph

## Estructura del proyecto
```
HydroByte/
├── app/
│   ├── main_window.py
│   ├── widgets/
│   │   ├── sensor_card.py
│   │   ├── chart_widget.py
│   │   ├── sidebar.py
│   │   └── ...
│   └── ...
├── utils/
│   └── img/
│       ├── logo_pi.png
│       └── logo_pi.ico
├── main.py
├── requirements.txt
└── README.md
```

## Documentación rápida
- **main.py:** Punto de entrada de la app.
- **app/main_window.py:** Lógica principal y gestión de temas.
- **app/widgets/**: Componentes visuales reutilizables (cards, sidebar, charts, etc).
- **utils/img/**: Recursos gráficos (íconos y logos).

## Personalización
- Cambia el logo en `utils/img/logo_pi.png` y/o `logo_pi.ico`.
- Modifica los temas en `theme_manager.py`.

## Licencia
MIT

---

# Documentación Técnica

## Estructura de la Interfaz
- **Sidebar:** Barra lateral con navegación y submenús para gráficas.
- **SensorCard:** Tarjetas para mostrar datos de sensores, rango óptimo y estado (Activo/Inactivo).
- **ChartWidget:** Gráficas interactivas para cada sensor.
- **Alertas:** Cards y tabla con alertas recientes.

## Cambio de Tema
El cambio de tema es global y afecta todos los componentes, incluidas subpáginas y menús.

## Estado de sensores
Cada tarjeta de sensor muestra su estado (Activo/Inactivo) con color verde/rojo según corresponda.

## Ejecución como ejecutable (.exe)
Para que el ícono se muestre en la barra de tareas de Windows, compila el proyecto con PyInstaller:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=utils/img/logo_pi.ico main.py
```
El ejecutable estará en `dist/main.exe`.

---

¿Dudas, sugerencias o mejoras? ¡Abre un issue o pull request en GitHub!
