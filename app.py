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