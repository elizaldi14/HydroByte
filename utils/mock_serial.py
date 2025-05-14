import time
import threading
import random

class MockSerial:
    def __init__(self, port='MOCK', baudrate=9600, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self._is_open = True
        self.buffer = []
        # Lanzar un hilo que simula datos entrantes
        threading.Thread(target=self._generate_data, daemon=True).start()

    def _generate_data(self):
        while self._is_open:
            simulated_line = f"TEMP:{random.uniform(18, 28):.2f};PH:{random.uniform(5.5, 7.0):.2f}\n"
            self.buffer.append(simulated_line.encode('utf-8'))
            time.sleep(1)

    def readline(self):
        if self.buffer:
            return self.buffer.pop(0)
        time.sleep(0.1)
        return b""

    def write(self, data):
        print(f"[MOCK WRITE] {data}")

    def close(self):
        self._is_open = False

    def is_open(self):
        return self._is_open
