import time
import pyperclip
import sys

clipboard_file = "clipboard_history.txt"

def save_to_clipboard_history(text):
    with open(clipboard_file, "a") as f:
        f.write(text + "\n")

def format_clipboard_entry(entry_text):
    design = "---" * 30
    formatted_entry = f"{design}\n{entry_text}\n{design}"
    return formatted_entry

def monitor_clipboard():
    last_copied_text = ""
    while True:
        current_copied_text = pyperclip.paste()
        if current_copied_text != last_copied_text:
            last_copied_text = current_copied_text
            formatted_entry = format_clipboard_entry(current_copied_text)
            save_to_clipboard_history(formatted_entry)
        time.sleep(0.1)  # Adjust the interval as needed

if __name__ == "__main__":
    try:
        monitor_clipboard()
    except KeyboardInterrupt:
        sys.exit()