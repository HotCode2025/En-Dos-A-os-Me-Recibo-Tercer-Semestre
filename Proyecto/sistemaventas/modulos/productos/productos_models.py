from core.database import db


class ProductosModels:
    
    def __init__(self):
        
        self.conexion = db.get_connection()

    # métodos CRUD de las categorías
    def getCategorias(self):
        try:
            # Abrimos, with. Abre y cierra la conexión a la DB 
            with db.get_connection() as conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT id, descripcion, observacion FROM categorias")
                
                # Traemos los datos y los transformamos
                categorias = [{"id": f[0], "descripcion": f[1], "observacion": f[2]} for f in cursor.fetchall()]
                
            # Al salir del 'with', la conexión se cierra sola
            return categorias
        except Exception as e:
            print(f"Error al leer categorías: {e}")
            return [] # Devolvemos lista vacía en caso de error 
        
    def insertarCategoria(self, descripcion, observacion):
        try:
            with db.get_connection() as conexion:
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO categorias (descripcion, observacion) VALUES (?, ?)", (descripcion, observacion))
                conexion.commit()
                return True, "Categoría añadida correctamente."
        except Exception as e:
            return False, f"Error: {e}"

    def actualizarCategoria(self, id_categoria, descripcion, observacion):
        try:
            with db.get_connection() as conexion:
                cursor = conexion.cursor()
                cursor.execute("UPDATE categorias SET descripcion=?, observacion=? WHERE id=?", (descripcion, observacion, id_categoria))
                conexion.commit()
                return True, "Categoría actualizada."
        except Exception as e:
            return False, f"Error: {e}"

    def eliminarCategoria(self, id_categoria):
        try:
            with db.get_connection() as conexion:
                cursor = conexion.cursor()
                # Verificar si está en uso por algún producto
                cursor.execute("SELECT COUNT(*) FROM productos WHERE id_categoria=?", (id_categoria,))
                if cursor.fetchone()[0] > 0:
                    return False, "La categoría está asignada a productos y no puede eliminarse."
                
                cursor.execute("DELETE FROM categorias WHERE id=?", (id_categoria,))
                conexion.commit()
                return True, "Categoría eliminada."
        except Exception as e:
            return False, f"Error: {e}"
    
    # métodos CRUD de los productos. 
    def getProductos(self):
        try:
            # Abrimos, with. Abre y cierra la conexión a la DB 
            with db.get_connection() as conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT productos.id AS id, categorias.descripcion AS categoria, productos.uuid AS codigo, productos.descripcion AS descipcion, productos.precio AS precio, productos.stock AS stock FROM productos INNER JOIN categorias ON productos.id_categoria = categorias.id")
                
                # Traemos los datos y los transformamos
                productos = [{"id": p[0], "categoria": p[1], "codigo": p[2], "descripcion": p[3], "precio": p[4], "stock": p[5],} for p in cursor.fetchall()]
                
            # Al salir del 'with', la conexión se cierra sola
            return productos
        except Exception as e:
            print(f"Error al leer categorías: {e}")
            return [] # Devolvemos lista vacía en caso de error 
    
    def inserterProducto(self, producto):
        try:
            # 1. Obtener conexión y crear cursor
            with db.get_connection() as conexion:
                cursor = conexion.cursor()
                
                # 2. Definir la consulta SQL con placeholders (?)
                sql = """INSERT INTO productos 
                        (descripcion, uuid, id_categoria, precio, stock, observacion) 
                        VALUES (?, ?, ?, ?, ?, ?)"""
                
                # 3. Organizar los valores en una tupla (en el mismo orden que el SQL)
                valores = (
                    producto["descripcion"],
                    producto["uuid"],
                    producto["id_categoria"],
                    producto["precio"],
                    producto["stock"],
                    producto["observacion"]
                )
                
                # 4. Ejecutar y confirmar
                cursor.execute(sql, valores)
                conexion.commit()
                
                print("Producto insertado con éxito en la BD")
                return True
            
        except Exception as e:
            print(f"Error al insertar producto: {e}")
            return False

    def actualizarProducto(self, producto):
        try:
            with db.get_connection() as conexion:
                cursor = conexion.cursor()
                sql = """UPDATE productos 
                         SET descripcion=?, uuid=?, id_categoria=?, precio=?, stock=?, observacion=? 
                         WHERE id=?"""
                valores = (
                    producto["descripcion"],
                    producto["uuid"],
                    producto["id_categoria"],
                    producto["precio"],
                    producto["stock"],
                    producto["observacion"],
                    producto["id"]
                )
                cursor.execute(sql, valores)
                conexion.commit()
                return True
        except Exception as e:
            print(f"Error al actualizar producto: {e}")
            return False

    def buscarProductos(self, texto):
        try:
            with db.get_connection() as conexion:
                cursor = conexion.cursor()
                # El % es el "comodín" en SQL: busca el texto en cualquier parte
                busqueda = f"%{texto}%"
                cursor.execute("""
                    SELECT productos.id, categorias.descripcion, productos.uuid,
                        productos.descripcion, productos.precio, productos.stock
                    FROM productos
                    INNER JOIN categorias ON productos.id_categoria = categorias.id
                    WHERE productos.descripcion LIKE ?
                    OR categorias.descripcion LIKE ?
                    OR productos.uuid LIKE ?
                """, (busqueda, busqueda, busqueda))
                
                productos = [{"id": p[0], "categoria": p[1], "codigo": p[2],
                            "descripcion": p[3], "precio": p[4], "stock": p[5]}
                            for p in cursor.fetchall()]
            return productos
        except Exception as e:
            print(f"Error al buscar productos: {e}")
            return []
