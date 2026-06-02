import os
import uuid
import datetime
from core.database import db


class FacturacionModels:
	def crear_venta(self, id_cliente, carrito, total, tipo_factura="A"):
		try:
			with db.get_connection() as conexion:
				cursor = conexion.cursor()
				uuid_venta = str(uuid.uuid4())
				cursor.execute(
					"INSERT INTO ventas (uuid, id_cliente, total, tipo_factura) VALUES (?, ?, ?, ?)",
					(uuid_venta, id_cliente, total, tipo_factura)
				)
				id_venta = cursor.lastrowid

				for item in carrito:
					cursor.execute(
						"INSERT INTO productos_vendidos (id_venta, id_producto, cantidad, precio_unitario) VALUES (?, ?, ?, ?)",
						(id_venta, item["id"], item["cantidad"], item["precio"])
					)
					cursor.execute(
						"UPDATE productos SET stock = stock - ? WHERE id = ?",
						(item["cantidad"], item["id"])
					)

				cursor.execute(
					"UPDATE clientes SET compras = compras + 1 WHERE id = ?",
					(id_cliente,)
				)

			conexion.commit()
			return True, id_venta, uuid_venta
		except Exception as e:
			print(f"Error al registrar venta: {e}")
			return False, None, None

	def generar_pdf_venta(self, empresa, cliente, carrito, total, tipo_factura, numero_factura):
		try:
			from reportlab.lib.pagesizes import letter
			from reportlab.pdfgen import canvas
		except ImportError:
			return False, "La dependencia 'reportlab' no está instalada. Instale reportlab con 'pip install reportlab'."

		try:
			root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
			pdf_dir = os.path.join(root_dir, "facturas")
			os.makedirs(pdf_dir, exist_ok=True)
			filename = os.path.join(pdf_dir, f"factura_{str(numero_factura).zfill(8)}.pdf")

			page_width, page_height = letter
			canvas_obj = canvas.Canvas(filename, pagesize=letter)
			margin = 40
			y = page_height - margin

			canvas_obj.setFont("Helvetica-Bold", 16)
			canvas_obj.drawString(margin, y, "Comprobante de Venta")
			y -= 30

			canvas_obj.setFont("Helvetica-Bold", 12)
			canvas_obj.drawString(margin, y, f"Tipo de factura: {tipo_factura}")
			canvas_obj.drawRightString(page_width - margin, y, f"Número: {str(numero_factura).zfill(8)}")
			y -= 16

			canvas_obj.setFont("Helvetica", 9)
			canvas_obj.drawString(margin, y, f"Fecha: {datetime.date.today().strftime('%d/%m/%Y')}")
			y -= 20

			canvas_obj.setFont("Helvetica", 10)
			if empresa:
				canvas_obj.drawString(margin, y, f"Empresa: {empresa.get('razon_social', '')}")
				y -= 16
				canvas_obj.drawString(margin, y, f"Dirección: {empresa.get('direccion', '')}")
				y -= 16
				canvas_obj.drawString(margin, y, f"DNI/CUIT: {empresa.get('documento', '')}")
				y -= 16
				canvas_obj.drawString(margin, y, f"Email: {empresa.get('email', '')}   Tel: {empresa.get('telefono', '')}")
				y -= 24
			else:
				canvas_obj.drawString(margin, y, "Empresa: No especificada")
				y -= 24

			cliente_nombre = cliente.get('razon_social', 'N/A') if cliente else 'N/A'
			cliente_documento = cliente.get('documento', '') if cliente else ''
			cliente_email = cliente.get('email', '') if cliente else ''
			cliente_telefono = cliente.get('telefono', '') if cliente else ''
			cliente_direccion = cliente.get('direccion', '') if cliente else ''

			canvas_obj.drawString(margin, y, f"Cliente: {cliente_nombre}")
			y -= 16
			canvas_obj.drawString(margin, y, f"DNI/CUIT: {cliente_documento}")
			y -= 16
			canvas_obj.drawString(margin, y, f"Email: {cliente_email}")
			y -= 16
			canvas_obj.drawString(margin, y, f"Teléfono: {cliente_telefono}")
			y -= 16
			canvas_obj.drawString(margin, y, f"Dirección: {cliente_direccion}")
			y -= 24

			canvas_obj.setFont("Helvetica-Bold", 11)
			canvas_obj.drawString(margin, y, "Producto")
			canvas_obj.drawString(margin + 260, y, "Precio")
			canvas_obj.drawString(margin + 360, y, "Cantidad")
			canvas_obj.drawString(margin + 460, y, "Subtotal")
			y -= 18
			canvas_obj.setLineWidth(0.5)
			canvas_obj.line(margin, y, page_width - margin, y)
			y -= 14
			canvas_obj.setFont("Helvetica", 10)

			for item in carrito:
				if y < margin + 60:
					canvas_obj.showPage()
					y = page_height - margin
				canvas_obj.drawString(margin, y, item.get("descripcion", ""))
				canvas_obj.drawString(margin + 260, y, f"${float(item.get('precio', 0)):.2f}")
				canvas_obj.drawString(margin + 360, y, str(item.get("cantidad", "")))
				canvas_obj.drawString(margin + 460, y, f"${float(item.get('subtotal', 0)):.2f}")
				y -= 16

			y -= 20
			if y < margin + 40:
				canvas_obj.showPage()
				y = page_height - margin

			canvas_obj.setFont("Helvetica-Bold", 12)
			canvas_obj.drawRightString(page_width - margin, y, f"Total: ${float(total):.2f}")
			canvas_obj.save()
			return True, filename
		except Exception as e:
			return False, f"Error generando PDF: {e}"
