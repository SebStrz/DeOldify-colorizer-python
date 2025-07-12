from tkinterdnd2 import DND_FILES, TkinterDnD
import tkinter as tk
from tkinter import Label, Button, Frame, Scale
from PIL import Image, ImageTk
import os
import platform
import subprocess
from pathlib import Path

class Front:
    def __init__(self, root):
        self.root = root
        self.root.title("Drag & Drop Obrazka")
        self.root.geometry("600x500")

        self.drop_frame = Frame(root,width=500,height=350)
        self.drop_frame.pack(pady=5)

        self.drop_frame.pack_propagate(False)
        # Ramka do przeciągania
        self.drop_label = Label(self.drop_frame, text="Przeciągnij tu zdjęcie", bg="lightgray")
        self.drop_label.pack(pady=20,expand=True,fill="both")
        self.drop_label.drop_target_register(DND_FILES)
        self.drop_label.dnd_bind('<<Drop>>', self.on_drop)

        self.button_frame = Frame(root)
        self.button_frame.pack()

        # Przycisk
        self.clear_button = Button(self.button_frame, text="Usuń zdjęcie", command=self.clear_image)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        self.colorize_button = Button(self.button_frame, text="Koloruj", command=self.colorize_image)
        self.colorize_button.pack(side=tk.LEFT, padx=5)

        self.colorize_slider = Scale(self.button_frame, from_=7,to=40,orient='horizontal',label='moc kolorowania')
        self.colorize_slider.pack(side=tk.LEFT,padx=5)

        self.tk_image = None

    def on_drop(self, event):
        filepath = event.data.strip('{}')  # usuń nawiasy klamrowe jeśli są
        if os.path.isfile(filepath) and filepath.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            self.load_image(filepath,self.drop_label)
            self.image_path = filepath
        else:
            self.drop_label.config(text="Nieobsługiwany format pliku")

    def load_image(self, path, node):
        print(Path(path))
        image = Image.open(Path(path))
        image.thumbnail((500, 350))
        self.tk_image = ImageTk.PhotoImage(image)
        node.config(image=self.tk_image)

    def clear_image(self):
        self.drop_label.config(image="")
        self.drop_label.config(text="Przeciągnij tu zdjęcie")
        self.tk_image = None
    def colorize_image(self):
        res = subprocess.run(["python","src/main.py",self.image_path,str(self.colorize_slider.get())],capture_output=True,text=True)
        print(res.stderr)
        print(res.stdout)
        if(res.stderr != ''):
            print("ligma")
            return 0
        path = res.stdout.split(":")
        print(path)
        self.result_image = Label(self.root)
        self.result_image.pack(pady=10)
        final_path = path[3].replace("\\","/")
        self.final_path = Path(final_path).parent
        self.load_image(final_path,self.result_image)

        self.folder_button = Button(self.root,text="otwórz w eksploratorze",command=self.open_file)
        self.folder_button.pack(pady=10)

    def open_file(self):
        if not self.final_path.exists():
            print("Ścieżka nie istnieje:", self.final_path)
            return

        system = platform.system()
        if system == "Windows":
            os.startfile(self.final_path)
        elif system == "Darwin":  # macOS
            subprocess.Popen(["open", self.final_path])
        elif system == "Linux":
            subprocess.Popen(["xdg-open",self.final_path])
        else:
            print("Nieobsługiwany system:", system)

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = Front(root)
    root.mainloop()

