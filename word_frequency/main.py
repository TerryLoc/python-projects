from collections import Counter
import re
import os
from PyPDF2 import PdfReader


def get_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text: str = text.lower()
    words: list[str] = re.findall(r"\b\w+\b", lowered_text)
    word_counts: Counter = Counter(words)
    return word_counts.most_common(10)


def read_pdf(file_path: str) -> str:
    """Reads a PDF file and returns its content as a string"""
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        raise
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        raise


def read_file(file_path: str) -> str:
    """Reads a file and returns its content as a string"""
    if file_path.endswith(".pdf"):
        return read_pdf(file_path)
    else:
        try:
            with open(file_path, "r") as file:
                return file.read()
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            raise
        except Exception as e:
            print(f"Error reading file: {e}")
            raise


def main() -> None:
    # Print the current working directory for debugging
    print(f"Current working directory: {os.getcwd()}")

    # List files in the current directory for debugging
    print("Files in the current directory:")
    for file_name in os.listdir(os.getcwd()):
        print(file_name)

    file_path: str = input("Enter the file path: ").strip()
    # Print the file path for debugging
    print(f"File path provided: {file_path}")

    try:
        text: str = read_file(file_path)
        word_frequencies: list[tuple[str, int]] = get_frequency(text)

        for word, frequency in word_frequencies:
            print(f"{word}: {frequency}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
