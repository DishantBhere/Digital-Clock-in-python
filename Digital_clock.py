import tkinter as tk
from time import strftime

# Root window setup
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x140")

# Global clock label and frame reference
current_frame = None
clock_label = None

def update_time():
    """Update the clock every second."""
    current_time = strftime('%I:%M:%S %p')
    if clock_label:
        clock_label.config(text=current_time)
    root.after(1000, update_time)

def apply_theme(bg_color, fg_color):
    """Reusable function to apply theme."""
    global current_frame, clock_label

    # Destroy previous frame if exists
    if current_frame:
        current_frame.destroy()

    current_frame = tk.Frame(root, bg=bg_color)
    current_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

    clock_label = tk.Label(
        current_frame,
        font=('calibri', 40, 'bold'),
        background=bg_color,
        foreground=fg_color
    )
    clock_label.pack(anchor="center")

def light_theme():
    apply_theme(bg_color="white", fg_color="black")

def dark_theme():
    apply_theme(bg_color="#22478a", fg_color="white")

# Set default theme and start clock
dark_theme()
update_time()

# Theme menu setup
menubar = tk.Menu(root)
theme_menu = tk.Menu(menubar, tearoff=0)
theme_menu.add_command(label="Light", command=light_theme)
theme_menu.add_command(label="Dark", command=dark_theme)
menubar.add_cascade(label="Theme", menu=theme_menu)
root.config(menu=menubar)

root.mainloop()
