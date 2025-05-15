import opencc
import json

# Load whitelist
try:
    with open("whitelist.json", "r") as f:
        whitelist = json.load(f)
except:
    whitelist = []

# Function: Save whitelist
def save_whitelist():
    with open("whitelist.json", "w") as f:
        json.dump(whitelist, f, ensure_ascii=False)

# Function: Check for Simplified Chinese
def simplified_text_check(text):
    converter = opencc.OpenCC('s2tw')
    converted = converter.convert(text)
    found = []
    for original_char, converted_char in zip(text, converted):
        if original_char != converted_char and original_char not in whitelist:
            found.append(original_char)

    print("[RESULT]")
    if found:
        print("Simplified chars:", ', '.join(found))
        print("Original:", text)
        print("Converted:", converted)
    else:
        print("No Simplified Chinese!")

# Main loop
while True:
    print("\n[Tradify]")
    text = input("Input text (or type 'help'): ").strip()

    if text.lower() == "help":
        print("'add' - add to whitelist")
        print("'remove' - remove from whitelist")
        print("'check' - show whitelist")
        print("'stop' - exit")
    elif text.lower() == "add":
        c = input("Char to add: ").strip()
        if c and c not in whitelist:
            whitelist.append(c)
            save_whitelist()
            print("Added:", c)
    elif text.lower() == "remove":
        c = input("Char to remove: ").strip()
        if c in whitelist:
            whitelist.remove(c)
            save_whitelist()
            print("Removed:", c)
    elif text.lower() == "check":
        print("Whitelist:", whitelist)
    elif text.lower() == "stop":
        print("Program ended.")
        break
    else:
        simplified_text_check(text)
