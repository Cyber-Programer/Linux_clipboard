# This is a Clipbo ard History Monitor Tool
<div style="text-align:center">
    <img src="https://github.com/Cyber-Programer/Linux_clipboard/assets/125746506/d2c9f58c-6b4a-4eef-a3ca-b0dcbe1563b1" alt="Code">
</div>



This Python script serves as a convenient tool to monitor your clipboard activity, capturing and storing your copied text into a history file. It enables you to keep track of your copied content, organized with timestamps and separators for easy reference.

## Features

- Monitors your clipboard for changes in real-time.
- Captures copied text and appends it to a clipboard history file.
- Each clipboard entry is formatted with decorative separators and timestamps.
- Simple and lightweight script, designed for ease of use.

## How to Use

1. Run the script in your terminal.
2. As you copy text, the script will detect the changes and record them.
3. Clipboard entries are saved to a designated history file with timestamps.
4. Customize the interval for monitoring as needed.
5. Use the saved history file to recall previously copied content.

## Requirements

- Python 3.x
- The `pyperclip` library for clipboard interaction. Install it using:

## Usage Example

1. Open a terminal and navigate to the directory containing the script.
2. Run the script using:
3. Copy some text to your clipboard.
4. Check the `clipboard_history.txt` file to see the captured entries.

## Note

- This tool runs indefinitely, so you may want to manually stop it using Ctrl+C when you're done.
- Adjust the monitoring interval (currently set to 0.1 seconds) as per your preference.

## Adding to Startup

For continuous clipboard monitoring, you might want to add this tool to your startup applications:

1. Open your system's startup applications settings.
2. Add a new entry with the following command:


## Creating a Shortcut to View History

To easily access your clipboard history, consider creating a shortcut to open the history file:

1. Create a new launcher shortcut on your desktop or application menu.
2. Set the command to open the history file using your preferred text editor:

3. Now you can quickly view your clipboard history with just a click.
