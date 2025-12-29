# pokemon-autorun

An application that makes pokemon shiny hunting easier through a real-time audio detection tool that listens to system audio, analyzes sound features, and triggers automated actions when a specific reference tone is detected.

This project uses audio signal processing (MFCC and chroma features), a Tkinter GUI, and screen automation to react to sounds in real time.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/QwertyuiopIsTaken/pokemon-autorun.git
```
2. Install dependencies:
```bash
pip install numpy scipy librosa soundcard pyautogui opencv-python keyboard
```
3. Run the program:
```bash
python main.py
```

## Controls

* **Start button** or hotkey: Begin detection
* **Stop button** or hotkey: Stop detection
* **Chroma slider**: Weight of chroma similarity
* **Threshold slider**: Detection sensitivity

## How it works

1. Records short chunks of system audio
2. Extracts:
    * MFCC features
    * Chroma features
3. Finds the loudest frame
4. Computes cosine similarity against a reference sound
5. Uses a rolling average for stability
6. A notification is shown and the detector stops automatically when thresholds are exceeded

## Notes and Warnings

* This project must be run with Python 3.12. Some dependencies used in this project (notably audio and system-level libraries) do not currently support Python 3.14+. You can install Python 3.12 [here](https://www.python.org/downloads/release/python-3120/) and make sure to check "Add Python to PATH" during installation.
* Requires a working loopback audio device
* Screen matching depends on resolution and scaling