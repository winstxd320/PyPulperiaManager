def InsertarRegistros(self, id, NombreProducto, Cantidad, NombreProveedor) -> None:
        con.execute("INSERT INTO Productos(Id, Nombre, Cantidad, NombreProveedor) VALUES ({}, '{}', '{}', '{}')".format(id, NombreProducto, Cantidad, NombreProveedor))
        con.commit()
