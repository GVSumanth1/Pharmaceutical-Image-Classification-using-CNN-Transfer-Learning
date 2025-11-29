import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import random
import csv
import re
import pandas as pd

# CONFIG

DATASET_DIR = r"c:\Users\suman\Desktop\Masters  Courses\Advanced Program\Advance Programming 11 projects\GROUP2\GROUP2\Pharmaceutical Image Classification\Pharmaceutical Image Classification\pharmaceutical_dataset\Drug Vision\Data Combined"
CSV_FILE = r"c:\Users\suman\Desktop\Masters  Courses\Advanced Program\Advance Programming 11 projects\GROUP2\GROUP2\Pharmaceutical Image Classification\pharma_data.csv"
BG_COLOR = "#82ccf7"

# Custom Hover Button Class
class HoverButton(tk.Button):
    def __init__(self, master, **kwargs):
        self.defaultBackground = kwargs.pop('bg', '#4CAF50')
        self.hoverBackground = kwargs.pop('hover_bg', '#45a049')
        super().__init__(master, bg=self.defaultBackground, **kwargs)

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

        self.configure(
            relief="flat",
            font=("Arial", 12, "bold"),
            activebackground=self.hoverBackground,
            bd=0,
            highlightthickness=0,
            padx=15,
            pady=5
        )

    def on_enter(self, e):
        self['background'] = self.hoverBackground

    def on_leave(self, e):
        self['background'] = self.defaultBackground

# Helper
def normalize_name(name):
    name = name.lower().replace("-", "").replace(".", "").replace(" ", "")
    name = re.sub(r"[^\w]", "", name)
    return name

# Build dataset
pharma_dict = {}
for folder in os.listdir(DATASET_DIR):
    folder_path = os.path.join(DATASET_DIR, folder)
    if os.path.isdir(folder_path):
        images = [os.path.join(folder_path, f) for f in os.listdir(folder_path)
                  if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if images:
            key = normalize_name(folder)
            pharma_dict[key] = images

# GUI Setup
root = tk.Tk()
root.title("Pharmaceutical Drug Viewer")
root.geometry("1000x750")
root.configure(bg=BG_COLOR)

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

main_frame = tk.Frame(notebook, bg=BG_COLOR)
notebook.add(main_frame, text="🔍 Search Drug")

top_frame = tk.Frame(main_frame, bg=BG_COLOR)
top_frame.pack(pady=10)

entry = tk.Entry(top_frame, font=("Arial", 16), width=30)
entry.pack(side="left", padx=10)

HoverButton(top_frame, text="Search", command=lambda: show_drug(entry.get()),
            bg="#81EC84", hover_bg="#78fb7f").pack(side="left", padx=5)

HoverButton(top_frame, text="Random Drug", command=lambda: show_drug(random.choice(list(pharma_dict.keys()))),
            bg="#2196F3", hover_bg="#1E88E5").pack(side="left", padx=5)

center_frame = tk.Frame(main_frame, bg=BG_COLOR)
center_frame.pack(padx=20, pady=10, fill="both", expand=True)

left_frame = tk.Frame(center_frame, bg=BG_COLOR)
left_frame.grid(row=0, column=0, sticky="n")

fields = {}
field_names = [
    ("Dosage (mg)", "dosage"),
    ("Active Ingredient(s)", "ingredient"),
    ("Drug Type", "type"),
    ("Side Effects", "effects"),
    ("Notes", "notes")
]

tooltips = {
    "dosage": "Dosage in milligrams (e.g., 500mg)",
    "ingredient": "Active chemical(s), e.g. Paracetamol",
    "type": "Drug category (e.g. Antibiotic, Vitamin)",
    "effects": "Common side effects (e.g. dizziness)",
    "notes": "Any relevant notes about the drug"
}

def create_tooltip(widget, text):
    tooltip = tk.Label(root, text=text, bg="black", fg="white", font=("Arial", 9), padx=5, pady=2, bd=1, relief="solid")
    def show_tooltip(event):
        x = widget.winfo_rootx() - root.winfo_rootx()
        y = widget.winfo_rooty() - root.winfo_rooty() - 30
        tooltip.place(x=x, y=y)
    def hide_tooltip(event):
        tooltip.place_forget()
    widget.bind("<Enter>", show_tooltip)
    widget.bind("<Leave>", hide_tooltip)

for label_text, key in field_names:
    tk.Label(left_frame, text=label_text, bg=BG_COLOR, font=("Arial", 14)).pack(anchor="w", pady=2)
    entry_widget = tk.Entry(left_frame, font=("Arial", 12), width=25)
    entry_widget.pack(pady=2)
    fields[key] = entry_widget
    create_tooltip(entry_widget, tooltips.get(key, ""))

HoverButton(left_frame, text="💾 Save Info", command=lambda: save_info(),
            bg="#FFCD82", hover_bg="#F7A33D").pack(pady=10)

center_panel = tk.Frame(center_frame, bg=BG_COLOR)
center_panel.grid(row=0, column=1, padx=20)

image_label = tk.Label(center_panel, bg=BG_COLOR)
image_label.pack()

name_label = tk.Label(center_panel, text="", font=("Arial", 22, "bold"), bg=BG_COLOR)
name_label.pack(pady=10)

image_count_label = tk.Label(center_panel, text="", font=("Arial", 12), bg=BG_COLOR)
image_count_label.pack()

right_frame = tk.Frame(center_frame, bg=BG_COLOR)
right_frame.grid(row=0, column=2, sticky="n")

HoverButton(right_frame, text="📁 View Saved Data", command=lambda: [load_saved_data(), notebook.select(saved_frame)],
            bg="#A571FF", hover_bg="#7C3BFF").pack(pady=100)

saved_frame = tk.Frame(notebook, bg=BG_COLOR)
notebook.add(saved_frame, text="📄 Saved Data")

current_drug_name = None

def show_drug(raw_name):
    global current_drug_name
    key = normalize_name(raw_name)
    if key in pharma_dict:
        images = pharma_dict[key]
        image_path = random.choice(images)
        try:
            img = Image.open(image_path)
            img.thumbnail((350, 350))
            photo = ImageTk.PhotoImage(img)
            image_label.config(image=photo)
            image_label.image = photo
            current_drug_name = raw_name
            name_label.config(text=raw_name.capitalize())
            image_count_label.config(text=f"{len(images)} image(s) found")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image.\n{e}")
    else:
        current_drug_name = None
        image_label.config(image='')
        name_label.config(text="")
        image_count_label.config(text="")
        messagebox.showerror("Not Found", f"No images found for '{raw_name}'.")

def save_info():
    global current_drug_name
    if not current_drug_name:
        messagebox.showerror("Error", "Please search and display a drug first.")
        return

    row = {
        "Name": current_drug_name
    }
    for key in fields:
        row[key.capitalize()] = fields[key].get()

    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=row.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

    messagebox.showinfo("Saved", f"Data saved for {current_drug_name}")
    load_saved_data()

def load_saved_data():
    for widget in saved_frame.winfo_children():
        widget.destroy()

    if not os.path.exists(CSV_FILE):
        return

    df = pd.read_csv(CSV_FILE)
    if df.empty:
        return

    headers = list(df.columns) + ["Delete"]
    for col_idx, header in enumerate(headers):
        tk.Label(saved_frame, text=header, font=("Arial", 12, "bold"),
                 bg=BG_COLOR, fg="black", borderwidth=1, relief="solid", padx=5, pady=5
                 ).grid(row=0, column=col_idx, sticky="nsew", padx=1, pady=1)

    for row_idx, row in df.iterrows():
        for col_idx, value in enumerate(row):
            tk.Label(saved_frame, text=value, font=("Arial", 11),
                     bg="#e0f7fa", borderwidth=1, relief="solid", padx=5, pady=3
                     ).grid(row=row_idx+1, column=col_idx, sticky="nsew", padx=1, pady=1)

        HoverButton(saved_frame, text="❌ Delete",
                    command=lambda idx=row_idx: delete_row(idx),
                    bg="#FF6459", hover_bg="#E53935", width=10).grid(row=row_idx+1, column=len(headers)-1, padx=5, pady=2)

def delete_row(index):
    if not os.path.exists(CSV_FILE):
        return
    df = pd.read_csv(CSV_FILE)
    if index >= 0 and index < len(df):
        df.drop(index, inplace=True)
        df.to_csv(CSV_FILE, index=False)
        load_saved_data()
        messagebox.showinfo("Deleted", "Entry deleted successfully.")

load_saved_data()
root.mainloop()
