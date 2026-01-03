import tkinter as tk
from math import sqrt, sin, cos, tan, log, radians, pi, exp

def click(event):
    text = event.widget.cget("text")
    current = screen_var.get()

    try:
        if text == "=":
            result = str(eval(current))
            screen_var.set(result)
        elif text == "C":
            screen_var.set("")
        elif text == "⌫":
            screen_var.set(current[:-1])
        elif text == "π":
            screen_var.set(current + str(round(pi, 5)))
        elif text == "eˣ":
            val = eval(current)
            screen_var.set(str(round(exp(val), 4)))
        elif text == "√":
            val = eval(current)
            screen_var.set(str(round(sqrt(val), 4)))
        elif text == "sin":
            val = eval(current)
            screen_var.set(str(round(sin(radians(val)), 4)))
        elif text == "cos":
            val = eval(current)
            screen_var.set(str(round(cos(radians(val)), 4)))
        elif text == "tan":
            val = eval(current)
            screen_var.set(str(round(tan(radians(val)), 4)))
        elif text == "log":
            val = eval(current)
            screen_var.set(str(round(log(val), 4)))
        elif text == "Dark":
            toggle_theme()
        else:
            screen_var.set(current + text)
    except:
        screen_var.set("Error")

def toggle_theme():
    global is_dark
    is_dark = not is_dark
    bg = "#333" if is_dark else "#F0F0F0"
    fg = "white" if is_dark else "black"
    screen.config(bg=bg, fg=fg, insertbackground=fg)
    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            for btn in widget.winfo_children():
                btn.config(bg=bg, fg=fg)

def on_key(event):
    key = event.char
    if key in "0123456789.+-*/()":
        screen_var.set(screen_var.get() + key)
    elif key == "\r":  # Enter
        try:
            screen_var.set(str(eval(screen_var.get())))
        except:
            screen_var.set("Error")
    elif key == "\x08":  # Backspace
        screen_var.set(screen_var.get()[:-1])

# GUI Setup
root = tk.Tk()
root.geometry("400x650")
root.title("Advanced Calculator")
root.bind("<Key>", on_key)  # Keyboard input support

is_dark = False
screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="Arial 20", bd=10, relief=tk.SUNKEN, justify='right')
screen.pack(fill="both", ipadx=8, ipady=20, pady=10)

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "+" , "π"],
    ["(", ")", "√", "eˣ"],
    ["sin", "cos", "tan", "log" , "cosec", "sec", "cot"],
    ["π", "C", "Dark" , "="  , "⌫" ,]
]

for row in buttons:
    f = tk.Frame(root)
    f.pack(expand=True, fill="both")
    for item in row:
        b = tk.Button(f, text=item, font="Arial 18", relief=tk.RAISED, bd=5)
        b.pack(side="left", expand=True, fill="both")
        b.bind("<Button-1>", click)

root.mainloop()


screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="Arial 20", bd=10, relief=tk.SUNKEN, justify='right')
screen.pack(fill="both", ipadx=8, ipady=20, pady=10)

# Buttons layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["√", "sin", "cos", "tan"],
    ["log","C" , "⌫" ]
]

for row in buttons:
    f = tk.Frame(root)
    f.pack(expand=True, fill="both")
    for item in row:
        b = tk.Button(f, text=item, font="Arial 18", relief=tk.RAISED, bd=5)
        b.pack(side="left", expand=True, fill="both")
        b.bind("<Button-1>", click)

root.mainloop()
