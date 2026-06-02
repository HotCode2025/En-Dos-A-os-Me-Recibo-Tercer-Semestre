from core.database import db

def crearTablasDB():
    
   with db.get_connection() as conn:
    conn.executescript("""
        -- 1. Información de la Empresa
        CREATE TABLE IF NOT EXISTS empresa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            razon_social TEXT NOT NULL,
            direccion TEXT,
            email TEXT,
            telefono TEXT
        );

        -- 2. Categorías de Productos
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descripcion TEXT NOT NULL,
            observacion TEXT
        );

        -- 3. Usuarios del Sistema
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            nombre TEXT NOT NULL,
            rol TEXT DEFAULT 'vendedor',
            observacion TEXT
        );

        -- 4. Clientes
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            documento TEXT UNIQUE,
            email TEXT,
            telefono TEXT,
            direccion TEXT,
            compras INTEGER DEFAULT 0,
            observacion TEXT
        );

        -- 5. Productos (Actualizada con id_categoria)
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_categoria INTEGER,
            uuid TEXT UNIQUE NOT NULL,
            descripcion TEXT NOT NULL,
            precio REAL NOT NULL CHECK(precio >= 0),
            stock INTEGER NOT NULL DEFAULT 0 CHECK(stock >= 0),
            fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
            observacion TEXT,
            FOREIGN KEY (id_categoria) REFERENCES categorias(id) ON DELETE SET NULL
        );

        -- 6. Ventas (Cabecera)
        CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            uuid TEXT UNIQUE NOT NULL,
            id_cliente INTEGER,
            id_vendedor INTEGER,
            tipo_factura TEXT DEFAULT 'A',
            total REAL NOT NULL DEFAULT 0,
            fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (id_cliente) REFERENCES clientes(id),
            FOREIGN KEY (id_vendedor) REFERENCES usuarios(id)
        );

        -- 7. Productos Vendidos (Detalle)
        CREATE TABLE IF NOT EXISTS productos_vendidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_venta INTEGER NOT NULL,
            id_producto INTEGER NOT NULL,
            cantidad INTEGER NOT NULL CHECK(cantidad > 0),
            precio_unitario REAL NOT NULL,
            FOREIGN KEY (id_venta) REFERENCES ventas(id) ON DELETE CASCADE,
            FOREIGN KEY (id_producto) REFERENCES productos(id)
        );

        -- 8. Pagos
        CREATE TABLE IF NOT EXISTS pagos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            id_venta INTEGER NOT NULL,
            importe_pagado REAL NOT NULL,
            importe_vuelto REAL DEFAULT 0,
            total_venta REAL NOT NULL,
            fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (id_venta) REFERENCES ventas(id) ON DELETE CASCADE
        );
    """)

    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(ventas)")
    columnas = [row[1] for row in cursor.fetchall()]
    if "tipo_factura" not in columnas:
        cursor.execute("ALTER TABLE ventas ADD COLUMN tipo_factura TEXT DEFAULT 'A'")
        conn.commit()
