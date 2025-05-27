import sqlite3
from typing import Dict, List, Tuple, Optional, Any
import logging

class SensorService:
    """Service class to handle database operations for sensor ranges."""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._initialize_database()
    
    def _get_connection(self):
        """Create and return a database connection."""
        conn = sqlite3.connect(self.db_path)
        conn.execute('PRAGMA journal_mode=WAL')
        conn.execute('PRAGMA busy_timeout=5000')
        return conn
    
    def _initialize_database(self):
        """Initialize the database tables if they don't exist."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            
            # Crear la tabla si no existe
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sensors (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    optimal_min REAL,
                    optimal_max REAL
                )
            """)
            
            # Verificar si la tabla está vacía
            cursor.execute("SELECT COUNT(*) FROM sensors")
            count = cursor.fetchone()[0]
            
            # Si está vacía, insertar valores predeterminados
            if count == 0:
                logging.info("Inicializando base de datos con valores predeterminados")
                # Valores predeterminados para los sensores
                # ID, nombre, mínimo, máximo
                default_values = [
                    (1, 'ph', 5.5, 7.5),           # Rango de pH típico para hidroponía
                    (2, 'ec', 0.5, 3.0),           # Conductividad eléctrica en mS/cm
                    (3, 'temperature', 18.0, 28.0), # Temperatura en °C
                    (4, 'water_level', 5.0, 30.0)   # Nivel de agua en cm
                ]
                cursor.executemany(
                    "INSERT INTO sensors (id, name, optimal_min, optimal_max) VALUES (?, ?, ?, ?)",
                    default_values
                )
            
            conn.commit()
    
    def get_sensor_ranges(self) -> Dict[str, Dict[str, float]]:
        """Get all sensor ranges from the database."""
        ranges = {}
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id, name, optimal_min, optimal_max 
                    FROM sensors 
                    WHERE id IN (1, 2, 3, 4)
                    ORDER BY id
                """)
                
                # Mapeo de IDs a claves de sensores
                id_to_key = {
                    1: 'ph',
                    2: 'ec',
                    3: 'temperature',
                    4: 'water_level'
                }
                
                for sensor_id, name, min_val, max_val in cursor.fetchall():
                    if min_val is not None and max_val is not None:
                        # Usar el mapeo por ID como respaldo si el nombre no está disponible
                        sensor_key = id_to_key.get(sensor_id, name.lower() if name else f'sensor_{sensor_id}')
                        ranges[sensor_key] = {
                            'min': float(min_val),
                            'max': float(max_val)
                        }
                        logging.info(f"Cargado rango para {sensor_key}: min={min_val}, max={max_val}")
        except Exception as e:
            logging.error(f"Error getting sensor ranges: {e}")
        
        return ranges
    
    def update_sensor_ranges(self, sensor_updates: Dict[int, Dict[str, float]]) -> bool:
        """Update sensor ranges in the database.
        
        Args:
            sensor_updates: Dictionary mapping sensor IDs to their min/max values
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        if not sensor_updates:
            return False
            
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                
                for sensor_id, ranges in sensor_updates.items():
                    min_val = ranges.get('min')
                    max_val = ranges.get('max')
                    
                    if min_val is None or max_val is None:
                        continue
                        
                    cursor.execute("""
                        UPDATE sensors 
                        SET optimal_min = ?, optimal_max = ?
                        WHERE id = ?
                    """, (min_val, max_val, sensor_id))
                    
                    if cursor.rowcount == 0:
                        # Sensor doesn't exist, try to insert
                        cursor.execute("""
                            INSERT INTO sensors (id, optimal_min, optimal_max)
                            VALUES (?, ?, ?)
                        """, (sensor_id, min_val, max_val))
                
                conn.commit()
                return True
                
        except Exception as e:
            logging.error(f"Error updating sensor ranges: {e}")
            if 'conn' in locals():
                conn.rollback()
            return False
