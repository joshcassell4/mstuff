import os
   
def use_clipboard(paste_text=None):
    import tkinter # For Python 2, replace with "import Tkinter as tkinter".
    tk = tkinter.Tk()
    tk.withdraw()
    if type(paste_text) == str: # Set clipboard text.
        tk.clipboard_clear()
        tk.clipboard_append(paste_text)
    try:
        clipboard_text = tk.clipboard_get()
    except tkinter.TclError:
        clipboard_text = ''
    r.update() # Stops a few errors (clipboard text unchanged, command line program unresponsive, window not destroyed).
    tk.destroy()
    return clipboard_text



