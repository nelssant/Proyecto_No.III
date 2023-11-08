# Proyecto III Algoritmos - Manejo de archivos, interfaz gráfica, cajas de texto, etiquetas, entre otros

Este programa utiliza algunos algunas librerias y atributos. El usuario podra inicializar la aplicación dando click al botón ejecutar en su editor de texto; la aplicacion mostrará una interfaz gráfica con forma de ventana la cual incluye algunas opciones de personalizacion:

  - Archivo:
    
      - Muestra las opciones: Abrir, Guardar y Guardar como.
        
  - Editar:
    
      -Muestra las opciones: Rehacer y Deshacer.
    
  - Configuración:
    
      - Muestra las opciones: Color de fondo, Color de fuente, Tamaño de Fuente y Color de Relleno.
        
  -Información:
  
  - Muestra las opciones:
    
      - Acerca de: Se despliega una lista de dos items; Detalle del sistema e Integrantes.
        
      - Términos y condiciones.
        
      - Documentación: Se despliega una lista de tres items; El enlace del repositorio Github, Manual de Usuario y Manual Técnico (Todos estan cargados en Github).

### Resumen técnico

Python utiliza la interfaz gráfica:

```python
import tkinter as tk
```

Para poder usar los cuadros de diálogo y demaás opciones agregadas y por agregar que la librería permita.

Se crea una clase para poder utilizarla con el manejo del editor de texto

```python
class TextEditorApp:
```

Se inicializa la funcion para poder realizar todas las demas funciones.

```python
          def __init__(self, root):
```
El cádigo se subdivide en varios bloques:

  - Menú de archivo: Sirve para crear la opción archivo en la ventana.
  - Menú Editar: Sirve para crear la opción editar en la ventana.
  - Menú Configuración: Sirve para crear la opción Configuración en la ventana.
  - Menú información: Sirve para crear la opción Información en la ventana.
  - Configuración Predeterminada: Sirve para poder mostrar una ventana con un formato diferente al tradicional.
  - Funciones:

- Manejo de eventos para los botones Rehacer y Deshacer
```python
   def on_text_change(self, event):
```
- Configuración del botón deshacer
```python
   def undo(self, Event=None):
```
- Configuración del botón rehacer
```python
   def redo(self, Event=None):
```
- Abre el archivo dentro del cuadro de diálogo, ya sea mediante los point clicks o mediante el path ingresado por el usuario.
```python
    def open_file(self):
```
- Guarda cambios en el archivo actual
```python
    def save_file(self):
```
- Guarda el archivo con otro nombre u otra extensión elegida por el usuario.
```python
    def save_file_as(self):
```
- Cambia el color de fondo de la ventana.
```python
    def change_background_color(self):
```
- Cambia el tamaño de la letra.
```python
    def change_font_size(self):
```
- Cambia el color de la letra.
```python
    def change_text_color(self):
```
- Cambia el color del relleno.
```python
    def change_highlight_color(self):
```
- Aplica las configuraciones del botón configuración [Color de letra, tamaño, color de fondo, color de relleno]
```python
    def update_text_widget_settings(self):
```
- Muestra la información del sistema [Version, autor, licencia, carnet, instrucciones de uso]
```python
    def show_information(self):
```
- Direcciona al usuario al repositorio inicial [Readme.md]
```python
    def open_github_documentation(self):
```
- Direcciona al usuario al repositorio del manual de usuario [User_Manual.md]
```python
    def open_user_manual(self):
```
- Direcciona al usuario al repositorio del manual técnico [Technical_Manual.md]
```python
    def open_technical_manual(self):
```
- Direcciona al usuario al repositorio de los términos y condiciones [Terms_and_Conditions.md]
```python
    def open_terms_and_Conditions(self):
```
- Direcciona al usuario a Canvas [Grupos -> Personas]
```python
    def open_Develoment_in_Python(self):
```
- Inicia la aplicación
```python
    if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()
```

**Para más información sobre el uso de la aplicacón, consulte [el manual de usuario](https://github.com/nelssant/Proyecto_No.III/blob/main/User_Manual.md)**
# Créditos:

| Carnet | Nombres y Apellidos | Nombre del grupo |
|---------------|--------------|--------------|
| 7690-23-21898 | Celda 1,2   | Celda 1,3   |
| 7690-20-15950 | Celda 2,2   | Celda 2,3   |


# Mejora Continua:

1. Mantenimiento y soporte.
2. Depuración y optimización.
3. Manejo de más excepciones
4. Creación de atajos de teclado.
5. Más opciones de configuración.
