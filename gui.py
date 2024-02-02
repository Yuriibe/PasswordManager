import tkinter as tk
import sys

# Assuming PasswordManager is a class you've defined in another file
# with a static method createNewDb that creates a new database
from password import PasswordManager

pw = PasswordManager()
class SimpleTkinterUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Tkinter UI")
        self.root.geometry('700x400')

        # Main frame that will hold the initial UI components
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.initialize_main_frame()

    def initialize_main_frame(self):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        self.label = tk.Label(self.main_frame, text="Hello, Tkinter!")
        self.label.pack()

        self.button_create = tk.Button(self.main_frame, text="Add Database", command=self.open_create_db_view)
        self.button_create.pack()

        self.button_load = tk.Button(self.main_frame, text="Load Database", command=self.displayAllDb)
        self.button_load.pack()

        self.button_exit = tk.Button(self.main_frame, text="Exit", command=sys.exit)
        self.button_exit.pack()

    def open_create_db_view(self):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create a new set of widgets for creating a database
        self.db_name_label = tk.Label(self.main_frame, text="Enter Database Name:")
        self.db_name_label.pack()

        self.db_name_entry = tk.Entry(self.main_frame)
        self.db_name_entry.pack()

        self.create_button = tk.Button(self.main_frame, text="Create Database", command=self.create_db)
        self.create_button.pack()

        # Button to cancel and return to the main menu
        self.cancel_button = tk.Button(self.main_frame, text="Cancel", command=self.initialize_main_frame)
        self.cancel_button.pack()

    def displayAllDb(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        files = pw.get_files_from_folder()    
        for key, file in enumerate(files):
            self.label = tk.Label(self.main_frame, text=file)
            self.label.pack()
          
        self.cancel_button = tk.Button(self.main_frame, text="Cancel", command=self.initialize_main_frame)
        self.cancel_button.pack()
          


    def create_db(self):
        db_name = self.db_name_entry.get()
        if db_name:
            print(db_name)
            pw.createNewDb(db_name)  # Assuming this method exists and works as intended
            self.initialize_main_frame()  # Return to the main view
            self.label.config(text=f"Database '{db_name}' created!")  # Update the label in the main view

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleTkinterUI(root)
    root.mainloop()
