# Tradify

This simple tool is a Python script that detects Simplified Chinese characters in a given paragraph.  
It uses the **OpenCC** library to convert Simplified Chinese text to Traditional Chinese and then checks for any differences, identifying the Simplified Chinese characters. The script has a dynamic **whitelist** where you can add or remove specific characters that should not be flagged as Simplified Chinese.

## Features
- **Simplified Chinese Detection**: Uses OpenCC to convert and compare text, identifying Simplified characters.
- **Customizable Whitelist**: Add or remove characters so they won't be flagged.
- **Interactive CLI**:
  - `help` – Show command list  
  - `add` – Add character to whitelist  
  - `remove` – Remove character from whitelist  
  - `check` – Show current whitelist  
  - `stop` – Exit the program
- **Graceful Handling**: Automatically creates or resets `whitelist.json` if missing or unreadable.

## Requirements
- Python 3.8+
- Install OpenCC via pip:
  ```bash
  pip install opencc-python-reimplemented
  ```

## Usage
Run the script:
```bash
python tradify.py
```
## Attribution
This project uses [OpenCC](https://github.com/BYVoid/OpenCC), licensed under the Apache License 2.0.
