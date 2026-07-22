import tkinter as tk 
from tkinter import ttk, filedialog, messagebox

current_file = None
dark_mode = True

THEMES = {
    "dark": {
        "bg": "#1e1e1e",
        "fg": "#d4d4d4",
        "editor_bg": "#252526",
        "editor_fg": "#d4d4d4",
        "panel_bg": "#2d2d2d",
        "status_bg": "#007acc",
        "status_fg": "#ffffff"
    },
    "light": {
            "bg": "#f3f3f3",
            "fg": "#333333",
            "editor_bg": "#ffffff",
            "editor_fg": "#000000",
            "panel_bg": "#e5e5e5",
            "status_bg": "#007acc",
            "status_fg": "#ffffff"
        }
}

root = tk.Tk()
root.title("Markdown Previewer")
root.geometry("1100x700")

main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)
toolbar = tk.Frame(main_frame, height=40)
toolbar.pack(fill=tk.X, side=tk.TOP)

paned = ttk.PanedWindow(main_frame, height=40)
paned.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

editor_frame = tk.Frame(paned)
editor = tk.Text(editor_frame, wrap=tk.WORD, undo=True, font=("Consolas", 11))
editor.pack(fill=tk.BOTH, expand=True)
paned.add(editor_frame, weight=1)

preview_frame = tk.Frame(paned)
preview = tk.Text(preview_frame, wrap=tk.WORD, font=("Sagoe UI", 11), state=tk.dis)
preview.pack(fill=tk.BOTH, expand=True)
paned.add(preview_frame, weight=1)

status_bar = tk.Label(main_frame, text=" Line: 1 | Words: 0 | Chars: 0", anchor=tk.W)
status_bar.pack(fill=tk.X, side=tk.BOTTOM)

def apply_theme():
    theme_name = "dark" if dark_mode else "light"