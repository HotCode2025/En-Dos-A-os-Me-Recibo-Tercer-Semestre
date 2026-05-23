from core.database import db


class ClientesModels:
    def __init__(self):
        self.conexion = db.get_connection()

    def getClientes(self):
        try:
            with db.get_connection() as conexion:
                cursor = conexion.cursor()
                cursor.execute("""
                    SELECT id, nombre, documento, email, telefono, direccion, compras, observacion
                    FROM clientes
                    ORDER BY id DESC
                """)
                filas = cursor.fetchall()
                clientes = [
                    {
                        "id": fila[0],
                        "razon_social": fila[1],
                        "documento": fila[2] or "",
                        "email": fila[3] or "",
                        "telefono": fila[4] or "",
                        "direccion": fila[5] or "",
                        "compras": fila[6] or 0,
                        "observacion": fila[7] or ""
                    }
                    for fila in filas
                ]
                return clientes
        except Exception as e:
            print(f"Error al leer clientes: {e}")
            return []

    def inserterCliente(self, cliente):
        try:
            with db.get_connection() as conexion:
                cursor = conexion.cursor()
                cursor.execute(
                    """
                        INSERT INTO clientes (nombre, documento, email, telefono, direccion, observacion)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        cliente["razon_social"],
                        cliente["documento"],
                        cliente["email"],
                        cliente["telefono"],
                        cliente["direccion"],
                        cliente["observacion"],
                    ),
                )
                conexion.commit()
                return True
        except Exception as e:
            print(f"Error al insertar cliente: {e}")
            return False

    def buscarClientes(self, texto):
        try:
            with db.get_connection() as conexion:
                cursor = conexion.cursor()
                patron = f"%{texto}%"
                cursor.execute(
                    """
                        SELECT id, nombre, documento, email, telefono, direccion, compras, observacion
                        FROM clientes
                        WHERE nombre LIKE ?
                        OR documento LIKE ?
                        OR email LIKE ?
                        OR telefono LIKE ?
                    """,
                    (patron, patron, patron, patron),
                )
                filas = cursor.fetchall()
                return [
                    {
                        "id": fila[0],
                        "razon_social": fila[1],
                        "documento": fila[2] or "",
                        "email": fila[3] or "",
                        "telefono": fila[4] or "",
                        "direccion": fila[5] or "",
                        "compras": fila[6] or 0,
                        "observacion": fila[7] or ""
                    }
                    for fila in filas
                ]
        except Exception as e:
            print(f"Error al buscar clientes: {e}")
            return []

    def eliminarCliente(self, cliente_id):
        try:
            with db.get_connection() as conexion:
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
                conexion.commit()
                return True
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")
            return False

    def actualizarCliente(self, cliente_id, cliente):
        try:
            with db.get_connection() as conexion:
                cursor = conexion.cursor()
                cursor.execute(
                    """
                    UPDATE clientes
                    SET nombre = ?, documento = ?, email = ?, telefono = ?, direccion = ?, observacion = ?
                    WHERE id = ?
                    """,
                    (
                        cliente["razon_social"],
                        cliente["documento"],
                        cliente["email"],
                        cliente["telefono"],
                        cliente["direccion"],
                        cliente["observacion"],
                        cliente_id
                    ),
                )
                conexion.commit()
                return True
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
            return False