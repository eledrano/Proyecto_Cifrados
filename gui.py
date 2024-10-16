import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from cesar import cifrarCesar, descifrarCesar
from llave import cifrarLlave, descifrarLlave
from vigenere import cifrarVigenere, descifrarVigenere

class MainWindow:
    def __init__(self, root):
        root.title("MainWindow - untitled")
        root.geometry("700x600")

        # Operación a realizar
        self.operation_label = tk.Label(root, text="Operación a realizar:")
        self.operation_label.place(x=20, y=20)
        
        self.operation_combo = ttk.Combobox(root, values=["Cifrado", "Descifrado"])
        self.operation_combo.current(0)
        self.operation_combo.place(x=180, y=20)

        # Algoritmo
        self.algorithm_label = tk.Label(root, text="Algoritmo:")
        self.algorithm_label.place(x=20, y=70)
        
        self.algorithm_combo = ttk.Combobox(root, values=["César", "Llave", "Vigenere","RSA" , "Palabra Inversa", "Mensaje Inverso", "Telefónico" , "Binario", "3 DES", "AES", "Morse"])
        self.algorithm_combo.current(0)
        self.algorithm_combo.place(x=180, y=70)

        # Botón abrir archivo TXT
        self.open_file_button = tk.Button(root, text="Abrir archivo TXT", command=self.open_file)
        self.open_file_button.place(x=400, y=65)

        # Cuadro de entrada
        self.input_label = tk.Label(root, text="Entrada:")
        self.input_label.place(x=20, y=120)
        
        self.input_text = tk.Text(root, width=80, height=10)
        self.input_text.place(x=20, y=150)

        # Botón aplicar algoritmo
        self.apply_button = tk.Button(root, text="Aplicar algoritmo", command=self.apply_algorithm)
        self.apply_button.place(x=300, y=320)

        # Cuadro de salida
        self.output_label = tk.Label(root, text="Salida:")
        self.output_label.place(x=20, y=370)
        
        self.output_text = tk.Text(root, width=80, height=10)
        self.output_text.place(x=20, y=400)

        # Botón salir
        self.exit_button = tk.Button(root, text="SALIR", command=root.quit)
        self.exit_button.place(x=20, y=550)

        # Botón enviar por correo
        self.send_email_button = tk.Button(root, text="Enviar por correo", command=self.send_email)
        self.send_email_button.place(x=580, y=550)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.input_text.delete(1.0, tk.END)
                self.input_text.insert(tk.END, content)

    def apply_algorithm(self):
        input_text = self.input_text.get(1.0, tk.END).strip()
        if not input_text:
            messagebox.showwarning("Advertencia", "El campo de entrada está vacío.")
            return
        
        algorithm = self.algorithm_combo.get()
        operation = self.operation_combo.get()
        
        if algorithm == "César":
            if operation == "Cifrado":
                output_text = cifrarCesar(input_text)
            else:
                output_text = descifrarCesar(input_text)
        elif algorithm == "Llave":
            clave = "tango"  # Clave por defecto, se puede agregar un input para personalizar
            if operation == "Cifrado":
                output_text = cifrarLlave(input_text, clave)
            else:
                output_text = descifrarLlave(input_text, clave)
        elif algorithm == "Vigenere":
            if operation == "Cifrado":
                output_text = cifrarVigenere(input_text, int)
            else:
                output_text = descifrarVigenere(input_text, int)
        elif algorithm == "RSA":
            if operation == "Cifrado":
                output_text = cifrarVigenere(input_text)
            else:
                output_text = descifrarVigenere(input_text)
        elif algorithm == "Palabra Inversa":
            if operation == "Cifrado":
                output_text = cifrarVigenere(input_text)
            else:
                output_text = descifrarVigenere(input_text)
        elif algorithm == "Mensaje Inverso":
            if operation == "Cifrado":
                output_text = cifrarVigenere(input_text)
            else:
                output_text = descifrarVigenere(input_text)
        elif algorithm == "Telefónico":
            if operation == "Cifrado":
                output_text = cifrarVigenere(input_text)
            else:
                output_text = descifrarVigenere(input_text)
        elif algorithm == "Binario":
            if operation == "Cifrado":
                output_text = cifrarVigenere(input_text)
            else:
                output_text = descifrarVigenere(input_text)
        elif algorithm == "3 DES":
            if operation == "Cifrado":
                output_text = cifrarVigenere(input_text)
            else:
                output_text = descifrarVigenere(input_text)
        elif algorithm == "AES":
            if operation == "Cifrado":
                output_text = cifrarVigenere(input_text)
            else:
                output_text = descifrarVigenere(input_text)
        elif algorithm == " ":
            if operation == "Cifrado":
                output_text = cifrarVigenere(input_text)
            else:
                output_text = descifrarVigenere(input_text)
        else:
            output_text = "Algoritmo no soportado."
        
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, output_text)

    def send_email(self):
        # Placeholder for sending email functionality
        messagebox.showinfo("Enviar por correo", "Función para enviar por correo (Placeholder).")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()