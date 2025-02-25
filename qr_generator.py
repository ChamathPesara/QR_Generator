import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

last_qr_data = None

# Function to generate QR code
def generate_qr():
    # Access global variable
    global last_qr_data 

    # Access data entry
    data = entry.get().strip()
    if not data:
        messagebox.showwarning("Input Error", "Please enter text or URL!")
        return
    
    # Stop if it's the same as last generated data
    if data == last_qr_data:
        messagebox.showinfo("Duplicate QR", "This QR Code has already been generated!")
        return  

    # Generate new QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white")

    # Convert QR image for display
    qr_img = qr_img.resize((200, 200))
    qr_tk = ImageTk.PhotoImage(qr_img)

    # Update the image label
    qr_label.config(image=qr_tk)
    qr_label.image = qr_tk
    
    # Store image for saving
    qr_label.qr_image = qr_img  

    # Update last generated QR data
    last_qr_data = data  

# Function to save QR code
def save_qr():
    if hasattr(qr_label, "qr_image"):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png"), ("All Files", "*.*")])
        if file_path:
            qr_label.qr_image.save(file_path)
            messagebox.showinfo("Success", "QR Code Saved Successfully!")
    else:
        messagebox.showwarning("Save Error", "No QR code to save!")

# Interface design
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x600")
root.resizable(False, False)

# Title of GUI
tk.Label(root, text="Enter Text / URL:", font=("candara", 14)).pack(pady=20)

# Data Entry
entry = tk.Entry(root, font=("candara", 14), width=30)
entry.pack(pady=10)

# Generate QR Button
tk.Button(root, text="Generate QR Code", command=generate_qr, font=("candara", 12),width=20).pack(pady=10)

# QR Code Display Label
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Save Button
tk.Button(root, text="Save QR Code", command=save_qr, font=("candara", 12),width=20).pack(pady=10)

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.quit, font=("candara", 12), width=20).pack(pady=20)

root.mainloop()
