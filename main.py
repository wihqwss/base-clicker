import customtkinter as ctk
import json
import os


save_file = "data.json"

def load_data():
    if os.path.exists(save_file):
        with open(save_file, "r") as f:
            return json.load(f)
    return {"clicks": 0}

def save_data():
    with open(save_file, "w") as f:
        json.dump(data, f)

def on_click():
    data["clicks"] += 1
    label.configure(text=f"Clicks: {data['clicks']}")
    save_data()

# === GUI ===
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Base Clicker")
app.geometry("300x200")

data = load_data()

label = ctk.CTkLabel(app, text=f"Clicks: {data['clicks']}", font=ctk.CTkFont(size=24, weight="bold"))
label.pack(pady=30)

button = ctk.CTkButton(app, text="Click!", font=ctk.CTkFont(size=20), command=on_click)
button.pack(pady=10)

app.mainloop()
