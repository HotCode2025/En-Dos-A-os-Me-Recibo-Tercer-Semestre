from core.database import db

class DashboardModels:
    def __init__(self):
        self.conexion = db.get_connection()

    def obtener_estadisticas(self):
        estadisticas = {
            "ventas": 0,
            "clientes": 0,
            "productos": 0
        }
        try:
            with db.get_connection() as conexion:
                cursor = conexion.cursor()
                
                # Cantidad de ventas
                cursor.execute("SELECT COUNT(id) FROM ventas")
                resultado_ventas = cursor.fetchone()
                if resultado_ventas:
                    estadisticas["ventas"] = resultado_ventas[0]
                    
                # Total de clientes
                cursor.execute("SELECT COUNT(id) FROM clientes")
                resultado_clientes = cursor.fetchone()
                if resultado_clientes:
                    estadisticas["clientes"] = resultado_clientes[0]
                    
                # Total de productos distintos
                cursor.execute("SELECT COUNT(id) FROM productos")
                resultado_productos = cursor.fetchone()
                if resultado_productos:
                    estadisticas["productos"] = resultado_productos[0]
                    
        except Exception as e:
            print(f"Error al obtener estadísticas del dashboard: {e}")
            
        return estadisticas