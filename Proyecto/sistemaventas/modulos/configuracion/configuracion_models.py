from core.database import db


class ConfiguracionModels:
    def __init__(self):
        self.conexion = db.get_connection()

    def getEmpresa(self):
        try:
            with db.get_connection() as conexion:
                cursor = conexion.cursor()
                cursor.execute("""
                    SELECT id, razon_social, direccion, email, telefono
                    FROM empresa
                    ORDER BY id ASC
                    LIMIT 1
                """)
                fila = cursor.fetchone()
                if fila:
                    return {
                        "id": fila[0],
                        "razon_social": fila[1] or "",
                        "direccion": fila[2] or "",
                        "email": fila[3] or "",
                        "telefono": fila[4] or ""
                    }
                return None
        except Exception as e:
            print(f"Error al leer datos de la empresa: {e}")
            return None

    def guardarEmpresa(self, empresa):
        try:
            with db.get_connection() as conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT id FROM empresa ORDER BY id ASC LIMIT 1")
                fila = cursor.fetchone()
                if fila:
                    cursor.execute(
                        """
                            UPDATE empresa
                            SET razon_social = ?, direccion = ?, email = ?, telefono = ?
                            WHERE id = ?
                        """,
                        (
                            empresa["razon_social"],
                            empresa["direccion"],
                            empresa["email"],
                            empresa["telefono"],
                            fila[0],
                        ),
                    )
                else:
                    cursor.execute(
                        """
                            INSERT INTO empresa (razon_social, direccion, email, telefono)
                            VALUES (?, ?, ?, ?)
                        """,
                        (
                            empresa["razon_social"],
                            empresa["direccion"],
                            empresa["email"],
                            empresa["telefono"],
                        ),
                    )
                conexion.commit()
                return True
        except Exception as e:
            print(f"Error al guardar datos de la empresa: {e}")
            return False
