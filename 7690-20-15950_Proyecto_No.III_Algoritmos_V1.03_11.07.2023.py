'''Esta aplicacion usa la interfaz grafica de Python para poder desplazarse hacia archivos mmediante la ubicacion directa o por clicks, el usuario puede ver, modificar, guardar y hacer varias configuraciones.
Autor: Nelson Santos // Ruben Garcia
Carnet: 7690-20-15950 // 7690-23-21898 
Universidad Mariano Galvez de Guatemala
Este programa no esta autorizado para su distribucion ni para cual quier uso que no tenga un fin academico
Prohibida su distribucion.
'''
#Importar librerias para configuracion, cajas de texto, control de la interfaz grafica, desplazamiento web
import tkinter as tk
from tkinter import filedialog, colorchooser, font, simpledialog
import webbrowser
import tkinter.messagebox as messagebox
#Definir clase para manejo de la aplicacion
class TextEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto")

        self.text_widget = tk.Text(self.root)
        self.text_widget.pack(fill="both", expand=True)

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Menú Archivo
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Guardar", command=self.save_file)
        self.file_menu.add_command(label="Guardar como", command=self.save_file_as)

        # Menú Editar
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Editar", menu=self.edit_menu)
        self.undo_stack = []
        self.redo_stack = []
        self.edit_menu.add_command(label="Deshacer", command=self.undo)
        self.edit_menu.add_command(label="Rehacer", command=self.redo)
        self.root.bind("<Control-y>", self.redo)
        self.root.bind("<Control-z>", self.undo)

        # Menú Configuración
        self.config_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Configuración", menu=self.config_menu)
        self.config_menu.add_command(label="Color de fondo", command=self.change_background_color)
        self.config_menu.add_command(label="Tamaño de letra", command=self.change_font_size)
        self.config_menu.add_command(label="Color de letra", command=self.change_text_color)
        self.config_menu.add_command(label="Color de relleno", command=self.change_highlight_color)

        # Menú Información
        self.info_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Información", menu=self.info_menu) 
        self.More_menu = tk.Menu(self.info_menu, tearoff=0)
        self.info_menu.add_cascade(label="Acerca de", menu=self.More_menu)
        self.More_menu.add_command(label="Detalle de Sistema", command=self.show_information)
        self.More_menu.add_command(label="Integrantes", command=self.open_Develoment_in_Python)
        self.info_menu.add_command(label="Terminos y Condiciones", command=self.open_terms_and_Conditions)
        self.Documentation_menu = tk.Menu(self.info_menu, tearoff=0)
        self.info_menu.add_cascade(label="Documentacion", menu=self.Documentation_menu)
        self.Documentation_menu.add_command(label="Enlace Github", command=self.open_github_documentation)
        self.Documentation_menu.add_command(label="Manual de usuario", command=self.open_user_manual)
        self.Documentation_menu.add_command(label="Manual técnico", command=self.open_technical_manual)

        self.current_file = None

        # Variables de configuración predeterminada
        self.background_color = "Black"
        self.font_family = "Verdana"
        self.font_size = 10
        self.text_color = "Orange"
        self.highlight_color = "Blue"

        # Aplicar configuración inicial
        self.update_text_widget_settings()
        self.text_widget.bind('<Key>', self.on_text_change)
        
    # Manejo de los eventos para los botones deshacer y rehacer
    def on_text_change(self, event):
        current_text = self.text_widget.get("1.0", "end-1c")
        self.undo_stack.append(current_text)
        self.redo_stack.clear()
    # Configuracion boton deshacer
    def undo(self, Event=None):
        if len(self.undo_stack) > 1:
            current_text = self.undo_stack.pop()
            self.redo_stack.append(current_text)
            self.text_widget.delete("1.0", "end")
            self.text_widget.insert("1.0", self.undo_stack[-1])
    # Configuracion boton rehacer
    def redo(self, Event=None):
        if self.redo_stack:
            current_text = self.redo_stack.pop()
            self.undo_stack.append(current_text)
            self.text_widget.delete("1.0", "end")
            self.text_widget.insert("1.0", current_text)
    # Funcion para abrir el archivo mediante un cuadro de dialogo
    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension="*.*", filetypes=[("Todo los archivos", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_widget.delete("1.0", "end")
                self.text_widget.insert("1.0", content)
            self.current_file = file_path
        self.undo_stack.clear()
        self.redo_stack.clear()
        self.undo_stack.append(self.text_widget.get("1.0", "end-1c"))

    #Funcion para guardar cambios en el archivo actual
    def save_file(self):
        if self.current_file:
            content = self.text_widget.get("1.0", "end")
            with open(self.current_file, "w") as file:
                file.write(content)
        else:
            error_message = "No ha abierto ningun archivo"
            messagebox.showinfo("Error Critico", error_message)
            
    # Funcion para guardar el archivo actual con otra extension y nombre
    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        if file_path:
            content = self.text_widget.get("1.0", "end")
            with open(file_path, "w") as file:
                file.write(content)
            self.current_file = file_path
    
    # Configuracion del color de fondo
    def change_background_color(self):
        color = colorchooser.askcolor(title="Seleccionar color de fondo")[1]
        if color:
            self.background_color = color
            self.update_text_widget_settings()
    # Configuracion del tamaño de la fuente
    def change_font_size(self):
        size_dialog = simpledialog.askinteger("Tamaño de letra", "Ingrese el tamaño de letra", initialvalue=self.font_size, minvalue=6, maxvalue=72)
        if size_dialog:
            self.font_size = size_dialog
            self.update_text_widget_settings()
    
    # Configuracion del color de la fuente
    def change_text_color(self):
        color = colorchooser.askcolor(title="Seleccionar color de letra")[1]
        if color:
            self.text_color = color
            self.update_text_widget_settings()
    # Configuracion del color del relleno
    def change_highlight_color(self):
        color = colorchooser.askcolor(title="Seleccionar color de relleno")[1]
        if color:
            self.highlight_color = color
            self.update_text_widget_settings()
    # Aplicacion de las configuraciones [Color de fondo, tamaño de letra, color de letra, color de relleno]
    def update_text_widget_settings(self):
        self.text_widget.config(
            bg=self.background_color,
            font=(self.font_family, self.font_size),
            fg=self.text_color,
            selectbackground=self.highlight_color
        )
    # Informacion acerca del programa
    def show_information(self):
        information_text = f"""\
Esta aplicación es un editor de texto simple.
Autor: Nelson Santos // Ruben Garcia
Carnet: 7690-20-15950 // 7690-23-21898 
Versión: 1.03
Licencia: Proyecto No.III Algoritmos 

Instrucciones de uso:
- Puedes abrir archivos de texto existentes usando el menú "Archivo".
- Puedes guardar archivos de texto con el menú "Archivo".
- También puedes abrir URLs desde el menú "Información".
- Puedes cambiar color, tamaño de fuente, color del rellenado en el menú "Configuracion:

¡Gracias por usar nuestra aplicación!"""

# Imprimir la informacion en una ventana emergente (Caja de texto)
        messagebox.showinfo("Información", information_text)

# Link de acceso para la documentacion (Repositorio)
    def open_github_documentation(self):
        webbrowser.open("https://github.com/nelssant/Proyecto_No.III/blob/main/README.md")

# Link de acceso para el manual de usuario
    def open_user_manual(self):
        webbrowser.open("https://github.com/nelssant/Proyecto_No.III/blob/main/User_Manual.md")

# Link de acceso para el manual tecnico
    def open_technical_manual(self):
        webbrowser.open("https://github.com/nelssant/Proyecto_No.III/blob/main/Technical_Manual.md")

# Link de acceso para los terminos y condiciones
    def open_terms_and_Conditions(self):
        webbrowser.open("https://github.com/nelssant/Proyecto_No.III/blob/main/Terms_and_Conditions.md")

# Link de acceso para los integrantes del grupo
    def open_Develoment_in_Python(self):
        webbrowser.open("https://miumg.instructure.com/groups/206218/users")

# Mantener abierta la intefaz grafica        
if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()