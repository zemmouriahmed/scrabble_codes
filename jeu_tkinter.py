import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Scrabble Game with Tkinter")

tiles_frame = tk.Frame(root)
tiles_frame.pack(side="top", fill="x")

word_frame = tk.Frame(root, height=50)
word_frame.pack(side="bottom", fill="x", expand=False)

tiles_distribution = {'A': 9, 'B': 2, 'C': 2}  # Exemple simplifié
tiles = []

def draw_tiles():
    for widget in tiles_frame.winfo_children():
        widget.destroy()
    for letter, count in tiles_distribution.items():
        for _ in range(count):
            lbl = tk.Label(tiles_frame, text=letter, bg="lightblue", width=2, height=1)
            lbl.pack(side="left", padx=5, pady=5)

draw_tiles()

root.mainloop()
