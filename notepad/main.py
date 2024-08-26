import os

os.environ["TK_SILENCE_DEPRECATION"] = "1"

import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button


class SimpleNotePad:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("Terry's Notepad")

        # Initialize the current file path
        self.current_file_path = None

        # Create a text widget
        self.text_area: Text = Text(self.root, wrap="word")
        self.text_area.pack(expand=True, fill="both")
        self.root.tk.call("tk", "scaling", 2.0)

        # Create a frame to hold the buttons
        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack()

        # Create a button to save a file
        self.save_button: Button = Button(
            self.button_frame, text="Save As", command=self.save_file_as
        )
        self.save_button.pack(side="left")

        # Create a button to open a file
        self.open_button: Button = Button(
            self.button_frame, text="Open", command=self.open_file
        )
        self.open_button.pack(side="right")

        # Create a button to save over the existing file
        self.save_over_button: Button = Button(
            self.button_frame, text="Save", command=self.save_over_file
        )
        self.save_over_button.pack(side="left")

    def open_file(self) -> None:
        """This method opens a file and displays its content in the text area"""
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
            self.text_area.delete("1.0", "end")  # Clear the text area
            self.text_area.insert("1.0", content)  # Insert the file content
            self.current_file_path = file_path  # Update the current file path
            print(f"File opened from {file_path}")

    def save_file_as(self) -> None:
        """This method saves the content of the text area to a new file"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get("1.0", "end"))
            self.current_file_path = file_path  # Update the current file path
            print(f"File saved to {file_path}")

    def save_over_file(self) -> None:
        """This method saves the content of the text area to the currently opened file"""
        if self.current_file_path:
            with open(self.current_file_path, "w") as file:
                file.write(self.text_area.get("1.0", "end"))
            print(f"File saved to {self.current_file_path}")
        else:
            self.save_file_as()  # If no file is opened, use save as

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    root: Tk = tk.Tk()
    app: SimpleNotePad = SimpleNotePad(root)
    app.run()


if __name__ == "__main__":
    main()
