# Simplified Chinese Detector

This simple tool is a Python script that detects Simplified Chinese characters in a given paragraph.
It uses the **OpenCC** library to convert Simplified Chinese text to Traditional Chinese and then checks for any differences, identifying the Simplified Chinese characters.
The script has a dynamic **whitelist** where you can add or remove specific characters that should not be flagged as Simplified Chinese.

## Features
- **Simplified Chinese Detection**: Converts Simplified Chinese to Traditional Chinese and compares both versions to identify Simplified Chinese characters.
- **Customizable Whitelist**: A whitelist feature allows you to add or remove specific characters from detection, so they won't be flagged.
- **Interactive Command-Line Interface**: 
  - Add/remove characters to/from the whitelist.
  - Check the current whitelist.
  - Continuously process paragraphs for Simplified Chinese detection.

## Requirements
- Python 3.x
- OpenCC library

## Attribution
This project uses OpenCC (https://github.com/BYVoid/OpenCC), which is licensed under the Apache License 2.0.
