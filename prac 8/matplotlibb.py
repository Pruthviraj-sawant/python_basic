import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Create the main window
root = tk.Tk()
root.title("Matplotlib in Tkinter Example")
root.geometry("800x600")

# Create a figure for the plot
fig, ax = plt.subplots(figsize=(6, 4))

# Generate some data to plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Plot the data
ax.plot(x, y, label="Sine Wave")
ax.set_title("Matplotlib Plot in Tkinter")
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
ax.legend()

# Embed the Matplotlib figure in the Tkinter window using FigureCanvasTkAgg
canvas = FigureCanvasTkAgg(fig, master=root)  # A Tkinter Canvas widget
canvas.draw()

# Pack the canvas into the Tkinter window
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Create a simple button to update the plot (demonstration of interactivity)
def update_plot():
    ax.clear()
    y_new = np.cos(x)  # Update the data (cosine curve)
    ax.plot(x, y_new, label="Cosine Wave", color='orange')
    ax.set_title("Updated Matplotlib Plot")
    ax.set_xlabel("X-Axis")
    ax.set_ylabel("Y-Axis")
    ax.legend()
    canvas.draw()

# Add an "Update Plot" button
update_button = ttk.Button(root, text="Update Plot", command=update_plot)
update_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
