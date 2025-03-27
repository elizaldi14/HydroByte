import socket
from PySide6.QtCore import QTimer, QObject, Signal


class SocketClient(QObject):
    datos_actualizados = Signal(dict)  # Señal para enviar datos al UI

    def __init__(self, host="192.168.136.140", port=12345, parent=None):
        super().__init__(parent)
        self.host = host
        self.port = port
        self.client_socket = None

        self.buffer_datos = {}  # Acumula los datos hasta que estén completos

        # Temporizador para leer datos periódicamente
        self.timer = QTimer()
        self.timer.timeout.connect(self.leer_datos_socket)
        self.timer.start(5000)  # Se ejecuta cada 2 segundos

        self.init_socket()

    def init_socket(self):
        """Inicia la conexión con el socket."""
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, self.port))
            self.client_socket.settimeout(1)  # Tiempo de espera
            print("✅ Conectado al servidor")
        except Exception as e:
            print(f"❌ Error al conectar: {e}")
            self.client_socket = None

    def leer_datos_socket(self):
        """Lee datos del socket sin bloquear la interfaz."""
        if not self.client_socket:
            print("⚠️ No hay conexión con el servidor.")
            return

        try:
            data = self.client_socket.recv(1024).decode('utf-8')
            if data:
                self.procesar_datos(data)
        except socket.timeout:
            print("⏳ Esperando datos...")
        except Exception as e:
            print(f"❌ Error al recibir datos: {e}")

    def procesar_datos(self, data):
        """Procesa los datos y espera a tener todos antes de emitir la señal."""
        data_lines = data.strip().split("\n")

        for line in data_lines:
            line = line.strip()
            if line.startswith("Ph:"):
                self.buffer_datos["ph"] = float(line.replace("Ph:", "").strip())
            elif line.startswith("PPM:"):
                self.buffer_datos["ppm"] = float(line.replace("PPM:", "").strip())
            elif line.startswith("Temp:"):
                self.buffer_datos["temp"] = float(line.replace("Temp:", "").strip())
            elif line.startswith("Distancia:"):
                self.buffer_datos["distancia"] = float(line.replace("Distancia:", "").strip())

        # Emitir solo cuando tenemos todos los valores
        if all(key in self.buffer_datos for key in ["ph", "ppm", "temp", "distancia"]):
            self.datos_actualizados.emit(self.buffer_datos.copy())  # Enviar copia a la UI
            print(f"📊 Datos completos enviados: {self.buffer_datos}")
            self.buffer_datos.clear()  # Limpiar buffer después de enviar

    def cerrar_conexion(self):
        """Cierra la conexión del socket."""
        if self.client_socket:
            self.client_socket.close()
