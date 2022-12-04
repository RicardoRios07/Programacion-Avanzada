import pymysql as pym

try:
    conn = pym.connect(host='localhost', user='root', password='', db='crud')
    print("**************************************************")
    print("*******CREAR - LEER - ACTUALIZAR - ELIMINAR*******")
    print("**************************************************")
    menu = ("""
            1 Para registrar/Ingresar un producto
            2 Para buscar un producto
            3 Para Eliminar un Producto
            4 Para editar un producto
        """)

    print(menu)
    opcion = int(input("Ingrese un número \n"))
    nombreProducto = str(input("Ingrese el nombre del producto \n"))
    descripcion = str(input("Ingrese la descripción del producto \n"))
    cedula = str(input("Ingrese el documento del usuario \n"))
    datos = [nombreProducto, descripcion, cedula]
    if opcion == 1:
            with conn.cursor() as cursor:
                insertar = "INSERT INTO tbl_producto(nombre_producto, descripcion, documento_usuario) VALUES ( %s, %s, %s)"
                cursor.execute(insertar, datos)
                conn.commit()

    if opcion == 2:
            print(f"Digite el producto que quiere consultar {nombreProducto}")
            with conn.cursor() as cursor:

                consultar = "SELECT descripcion, documento_usuario FROM tbl_usuario where nombre_producto = %s"
                cursor.execute(opcion, (datos))
                documentos = cursor.fetchall
                for documento in documentos:
                    print(documento)
                    conn.close()

 
except (pym.err.OperationalError, pym.err.InternalError) as e:
    print("se presento el siguiente error", e)