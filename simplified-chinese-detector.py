import opencc

whitelist = []

def simplified_text_check(paragraph, whitelist):

    traditionalizer = opencc.OpenCC('s2tw')
    converted_paragraph = traditionalizer.convert(paragraph)

    simplified_text_found = []
    for original_text, converted_text in zip(paragraph, converted_paragraph):
        if original_text != converted_text and converted_text not in whitelist and original_text not in whitelist:
            simplified_text_found.append(original_text)

    print("[RESULT]")
    if simplified_text_found:
        print("Simplified Chinese characters found::", ', '.join(simplified_text_found))
        print("Original paragraph:", paragraph)
        print("Converted paragraph:", converted_paragraph)

    else:
        print("No Simplified Chinese detected!")


while True:
    print("==========\n[Simplified Chinese Detector]")
    paragraph = input("Enter a paragraph (type 'help' for more info):")
    if paragraph.lower() == "help":
        print("\"add\" - add a character to whitelist")
        print("\"remove\" - remove a character from whitelist")
        print("\"check\" - check current whitelist")
        print("\"stop\" - stop the program")
        continue
    elif paragraph.lower() == "add":
        add_char = input("Enter a character to add:").strip()
        if add_char and add_char not in whitelist:
            whitelist.append(add_char)
            print(f"{add_char} is added to whitelist.")
        else:
            print("Invalid input or character is already in the whitelist.")
        continue
    elif paragraph.lower() == "remove":
        remove_char = input("Enter a character to remove:").strip()
        if remove_char in whitelist:
            whitelist.remove(remove_char)
            print(f"{remove_char} is removed from whitelist.")
        else:
            print(f"{remove_char} is not in the whitelist.")
        continue
    elif paragraph.lower() == "check":
        print("Whitelist:", whitelist)
        continue
    elif paragraph.lower() == "stop":
        print("Stopping the program.")
        break
    simplified_text_check(paragraph, whitelist)