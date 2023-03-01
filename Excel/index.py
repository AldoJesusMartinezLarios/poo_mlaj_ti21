"""
    Nombre: Aldo Jesús Martínez Larios
    Fecha: 28/02/2023
    Descripción: Programa que crea un libro de excel y añade datos a las celdas.
"""
from openpyxl import Workbook #Importacion de la libreria

book = Workbook() #Inicializacion del libro de excel
sheet = book.active #sheet es la hoja activa que esta por defecto al crear el libro

sheet ['A1'] = 'SKU' #En esa hoja en la celda A1 escribe SKU
sheet ['B1'] = 'NOMBRE' #En esa hoja en la celda B1 escribe NOMBRE
sheet ['C1'] = 'UNIDAD' #En esa hoja en la celda C1 escribe UNIDAD
sheet ['A2'] = '1' #En esa hoja en la celda A2 escribe 1
sheet ['B2'] = 'Producto1' #En esa hoja en la celda B2 escribe Producto1
sheet ['C2'] = 'Pieza' #En esa hoja en la celda C2 escribe Pieza
sheet ['A3'] = '2' #En esa hoja en la celda A3 escribe 2
sheet ['B3'] = 'Producto2' #En esa hoja en la celda B3 escribe Producto2
sheet ['C3'] = 'Pieza' #En esa hoja en la celda C3 escribe Pieza

book.save('producto.xlsx') #Comando para guardar el archivo creado


