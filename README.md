# Macro++

Macro++ is a Python script that allows you to easily select and input codes by listening to mouse button clicks. This can be useful for scenarios where you need to input various codes quickly, such as in testing environments or applications that require frequent code inputs.

**Important Note:**
This project was originally created for a very specific scenario for a friend of mine, and it was not initially intended for public use. However, I've decided to upload it & share it anyways.


## Features

- Listen to mouse button clicks to trigger actions.
- Load codes from the clipboard and select them randomly.
- Automatically remove the first few rows of copied codes to exclude additional unwanted text.
- Simple and easy to use.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Sampise/Macro-.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```bash
    python main.py
    ```

2. Copy the codes to your clipboard.
3. Press the side mouse button to load the codes.
4. Click the middle mouse button to select a random code from the loaded list and instantly enter it.

## Dependencies

- [pynput](https://pypi.org/project/pynput/): 1.7.3
- [pyautogui](https://pypi.org/project/PyAutoGUI/): 0.9.53
- [pyperclip](https://pypi.org/project/pyperclip/): 1.8.2

## Contribution

I consider this project finished but contributions are welcome! Feel free to open issues or submit pull requests.

