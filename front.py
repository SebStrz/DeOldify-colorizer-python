from tkinterdnd2 import DND_FILES, TkinterDnD
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
import os

class DragDropApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drag & Drop Obrazka")
        self.root.geometry("600x500")

        # Ramka do przeciągania
        self.drop_label = Label(root, text="Przeciągnij tu zdjęcie", bg="lightgray")
        self.drop_label.pack(pady=20)
        self.drop_label.drop_target_register(DND_FILES)
        self.drop_label.dnd_bind('<<Drop>>', self.on_drop)

        # Label na obrazek
        self.image_label = Label(root)
        self.image_label.pack(pady=10)

        # Przycisk
        self.clear_button = Button(root, text="Usuń zdjęcie", command=self.clear_image)
        self.clear_button.pack(pady=10)

        self.tk_image = None

    def on_drop(self, event):
        filepath = event.data.strip('{}')  # usuń nawiasy klamrowe jeśli są
        if os.path.isfile(filepath) and filepath.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            self.load_image(filepath)
        else:
            self.drop_label.config(text="Nieobsługiwany format pliku")

    def load_image(self, path):
        image = Image.open(path)
        image.thumbnail((500, 350))
        self.tk_image = ImageTk.PhotoImage(image)
        self.drop_label.config(image=self.tk_image)

    def clear_image(self):
        self.drop_label.config(image="")
        self.drop_label.config(text="Przeciągnij tu zdjęcie")
        self.tk_image = None


if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = DragDropApp(root)
    root.mainloop()

