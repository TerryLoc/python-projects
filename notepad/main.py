import os

os.environ["TK_SILENCE_DEPRECATION"] = "1"

import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button


class SimpleNotePad:
    def __init__(self, root: tk) -> None:
        self.root = root
        self.root.title("Terry's Notepad")

        # Create a text widget
        # self.text_area: Text = Text(self.root, wrap="word", bg="white", fg="black")
        # self.text_area: Text = Text(self.root, wrap="word", font=("Helvetica", 12))
        self.text_area: Text = Text(self.root, wrap="word")
        self.text_area.pack(expand=True, fill="both")
        self.root.tk.call("tk", "scaling", 2.0)

        # Create a frame to hold the buttons
        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack()

        # Create a button to open a file
        self.save_button: Button = Button(
            self.button_frame, text="Save", command=self.save_file
        )
        self.save_button.pack(side="left")

        # Create a button to open a file
        self.open_button: Button = Button(
            self.button_frame, text="Open", command=self.open_file
        )
        self.open_button.pack(side="right")

    def save_file(self) -> None:
        """This method saves the content of the text area to a file"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        )
        with open(file_path, "w") as file:
            file.write(self.text_area.get("1.0", "end"))

        print(f"File saved to {file_path}")

    def open_file(self) -> None:
        """This method opens a file and displays its content in the text area"""
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        with open(file_path, "r") as file:
            content: str = file.read()
            self.text_area.delete("1.0", "end")
            self.text_area.insert("insert", content)

        print(f"File opened from {file_path}")

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    tk_root = Tk()
    app = SimpleNotePad(tk_root)
    app.run()


if __name__ == "__main__":
    main()  # This is the entry point of the program
