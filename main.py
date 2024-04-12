import random
from pynput.mouse import Listener, Button
import pyautogui
import pyperclip

randomcode = None
codes_list = []
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

def on_click(x, y, button, pressed):
    if pressed:
        if button == Button.middle:
            random_code()
        elif button in [Button.x1, Button.x2]:
            get_codes()

def random_code():
    global codes_list
    if codes_list:
        if not codes_list: 
            print("Error: No codes available. Copy some codes and press a side mouse button to load them.")
            return
        if len(codes_list) == 1:
            randomcode = codes_list[0]
            pyautogui.click(clicks=2, interval=0)
            pyautogui.typewrite(randomcode, interval=0)
            pyautogui.press('enter', interval=0)
            print(f"Code '{randomcode.strip()}' used.")
            codes_list = []
        else:
            random.shuffle(codes_list)
            randomcode = codes_list.pop()
            pyautogui.click(clicks=2, interval=0)
            pyautogui.typewrite(randomcode, interval=0)
            pyautogui.press('enter', interval=0)
            print(f"Code '{randomcode.strip()}' used.")

    else:
        print("Error: No codes available. Copy some codes and press a side mouse button to load them.")

def get_codes():
    global codes_list
    clipboard_content = pyperclip.paste()
    lines = clipboard_content.split('\n')
    codes_list = [line for line in lines if line.strip()]
    codes_list = codes_list[5:]

    if len(codes_list) >= 10:
        print('Codes list successfully loaded!')
    else:
        print('Error: Codes might not have been loaded correctly (List of codes is shorter than 10). To restart, press any side mouse button!')

def main():
    get_codes()
    with Listener(on_click=on_click) as listener:
        listener.join()

if __name__ == "__main__":
    main()
