import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

def save_notes():
    notes = text_area.get('1.0', tk.END)
    if notes.strip() == '':
        messagebox.showwarning('Empty Notes', 'Cannot save empty notes.')
    else:
        file_path = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '*.txt')])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(notes)
                messagebox.showinfo('Notes Saved', 'Notes saved successfully.')
            except Exception as e:
                messagebox.showerror('Error', f'Failed to save notes.\nError: {str(e)}')

root = tk.Tk()
root.title('Note Taking App')

text_area = ScrolledText(root, height=10, width=40)
text_area.pack(padx=10, pady=10)

save_button = tk.Button(root, text='Save Notes', command=save_notes)
save_button.pack(pady=5)

root.mainloop()
