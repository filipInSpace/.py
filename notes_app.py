
#Author: Filip Navrkal 

import tkinter as tk
import tkinter.scrolledtext as tkst
import time

class NotesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notes App")
        # Create a scrolled text widget and pack it into the main window
        self.text_widget = tkst.ScrolledText(self, wrap='word')
        self.text_widget.pack(fill='both', expand=True)
        # Create buttons for saving and creating new notes and pack them into the main window
        self.save_button = tk.Button(self, text="Save", command=self.save_notes)
        self.new_button = tk.Button(self, text="New Note", command=self.new_note)
        self.save_button.pack(side='left')
        self.new_button.pack(side='left')

    def save_notes(self):
        # Generate a unique filename based on the current time
        timestamp = int(time.time())
        filename = f'notes_{timestamp}.txt'
        # Get the notes text from the scrolled text widget and save it to a file
        notes = self.text_widget.get('1.0', 'end-1c')
        with open(filename, 'w') as f:
            f.write(notes)

    def new_note(self):
        # Clear the text in the scrolled text widget
        self.text_widget.delete('1.0', 'end')

if __name__ == '__main__':
    app = NotesApp()
    app.mainloop()
