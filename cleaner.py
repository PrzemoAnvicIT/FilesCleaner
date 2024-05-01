import os
import shutil
from tkinter import Tk, ttk, messagebox, scrolledtext, filedialog
from tkinter.font import Font

# Using ttkthemes for better themes
from ttkthemes import ThemedTk

# Map of common file extensions to directory names in Polish
extension_mapping = {
    "exe": "Programy", "bat": "Programy", "msi": "Programy",
    "jpg": "Obrazy", "png": "Obrazy", "gif": "Obrazy", "bmp": "Obrazy",
    "doc": "Dokumenty", "docx": "Dokumenty", "txt": "Dokumenty",
    "pdf": "Dokumenty", "pptx": "Prezentacje", "ppt": "Prezentacje",
    "bz2": "Archiwa", "zip": "Archiwa", "gz": "Archiwa",
    "iso": "Obrazy ISO", "img": "Obrazy ISO",
    "log": "Logi"
}

class App:
    def __init__(self, root):
        self.root = root
        root.title("Organizator Plików")
        
        # Set a theme
        root.set_theme('arc')

        # Custom fonts
        custom_font = Font(family="Helvetica", size=12)
        
        # Adjust layout and styling
        style = ttk.Style()
        style.configure('TButton', font=custom_font, padding=6)
        style.configure('TLabel', font=custom_font, padding=6)
        
        self.path = os.path.expanduser('~/Downloads/')
        
        self.output = scrolledtext.ScrolledText(root, width=80, height=20, font=custom_font)
        self.output.pack(pady=20, padx=20, fill='both', expand=True)
        
        self.folder_button = ttk.Button(root, text="Wybierz Folder", command=self.select_folder)
        self.folder_button.pack(side='top', pady=(10, 0), expand=True)
        
        self.scan_button = ttk.Button(root, text="Wyczyść", command=self.scanDir)
        self.scan_button.pack(side='top', pady=10, expand=True)
    
    def select_folder(self):
        self.path = filedialog.askdirectory()
        if self.path:
            self.output.insert('end', f"Wybrany folder: {self.path}\n")
        else:
            self.output.insert('end', "Nie wybrano folderu. Używanie domyślnego.\n")
    
    def scanDir(self):
        self.output.insert('end', "Rozpoczynanie skanowania...\n")
        dirInfo = os.listdir(self.path)
        for filename in dirInfo:
            fullFilePath = os.path.join(self.path, filename)
            if os.path.isfile(fullFilePath):  # Only process if it's a file
                extension = filename.rsplit(".", 1)[-1].lower()
                dir_name = extension_mapping.get(extension, "Pozostałe")
                target_path = os.path.join(self.path, dir_name)
                if not os.path.exists(target_path):
                    os.mkdir(target_path)
                    self.output.insert('end', f"Utworzono folder: {dir_name}\n")
                shutil.move(fullFilePath, target_path)
                self.output.insert('end', f"Przeniesiono {filename} do {dir_name}\n")
        messagebox.showinfo("Zakończono", "Czyszczenie zakończone sukcesem!")

# Run the application with a theme
root = ThemedTk(theme="arc")
app = App(root)
root.mainloop()
