import tkinter as tk

# Function to be called when button is clicked
def on_button_click():
    label.config(text="Button Clicked!")

# Create the main window
window = tk.Tk()
window.title("Simple Tkinter Example")
window.geometry("300x200")

# Create a label widget
label = tk.Label(window, text="Hello, Tkinter!")
label.pack(pady=20)

# Create a button widget
button = tk.Button(window, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
