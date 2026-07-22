import tkinter as tk 
from tkinter import ttk, filedialog, messagebox
import re

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
preview = tk.Text(preview_frame, wrap=tk.WORD, font=("Sagoe UI", 11), state=tk.DISABLED)
preview.pack(fill=tk.BOTH, expand=True)
paned.add(preview_frame, weight=1)

status_bar = tk.Label(main_frame, text=" Line: 1 | Words: 0 | Chars: 0", anchor=tk.W)
status_bar.pack(fill=tk.X, side=tk.BOTTOM)

def apply_theme():
    theme_name = "dark" if dark_mode else "light"
    colors = THEMES[theme_name]

    root.config(bg=colors["bg"])
    main_frame.config(bg=colors["bg"])
    toolbar.config(bg=colors["panel_bg"])

    editor.config(bg=colors["editor_bg"], fg=colors["editor_fg"], insertbackground=colors["editor_fg"])
    preview.config(bg=colors["editor_bg"], fg=colors["editor_fg"])
    status_bar.config(bg=colors["status_bg"], fg=colors["status_fg"])

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    apply_theme()

apply_theme()
btn_theme = tk.Button(toolbar, text="Toggle Theme", command=toggle_theme, relief=tk.FLAT)
btn_theme.pack(side=tk.LEFT, padx=5, pady=5)

def render_preview(event=None):
    preview.config(state=tk.NORMAL)
    preview.delete("1.0", tk.END)
    
    raw_text = editor.get("1.0", tk.END + "-1c")
    lines = raw_text.split("\n")
    
    for line in lines:
        if line.startswith("# "):
            preview.insert(tk.END, line[2:] + "\n", "h1")
        elif line.startswith("## "):
            preview.insert(tk.END, line[3:] + "\n", "h2")
        elif line.startswith("- "):
            preview.insert(tk.END, "• " + line[2:] + "\n")
        else:
            if "**" in line:
                parts = line.split("**")
                for i, part in enumerate(parts):
                    if i % 2 == 1:
                        preview.insert(tk.END, part, "bold")
                    else:
                        preview.insert(tk.END, part)
                preview.insert(tk.END, "\n")
            else:
                preview.insert(tk.END, line + "\n")

    preview.config(state=tk.DISABLED)
editor.bind("<KeyRelease>", render_preview)
if __name__ == "__main__":
    root.mainloop()