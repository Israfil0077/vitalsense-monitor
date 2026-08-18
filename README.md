# VitalSense Monitor

VitalSense Monitor is a simple Streamlit application designed to display two health sensor readings from an ESP32:

- Heart Rate (BPM)
- SpO₂ / Blood Oxygen (%)

The current version uses demo values so the application can be tested without an ESP32. The ESP32 connection will be added separately.

## Project Structure

After extracting the project, the folder should look like this:

```text
vital_readings_streamlit/
│
├── app.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.9 or newer installed on your computer
- (Windows users) make sure "Add python.exe to PATH" was checked during Python install

Check your Python version:

```bash
python --version
```

## How to Run

1. **Open a terminal / command prompt** inside the `vital_readings_streamlit` folder.

2. **Create a virtual environment** (keeps this project's packages separate from everything else on your system):

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - Windows (Command Prompt):
     ```bash
     venv\Scripts\activate
     ```
   - Windows (PowerShell):
     ```bash
     venv\Scripts\Activate.ps1
     ```
   - macOS / Linux:
     ```bash
     source venv/bin/activate
     ```

   You'll know it worked if you see `(venv)` at the start of your terminal line.

4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the app:**

   ```bash
   streamlit run app.py
   ```

6. A browser tab should open automatically at `http://localhost:8501`. If it doesn't, just copy that link into your browser.

## Stopping the App

Go back to the terminal and press `Ctrl + C`.

## Next Time You Run It

You don't need to recreate the virtual environment or reinstall packages every time — just:

```bash
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

streamlit run app.py
```

## Notes

- This app currently shows **demo/random values**, not real ESP32 data yet.
- The dashboard auto-refreshes every couple of seconds.
- This interface is for display purposes only and is **not a diagnostic tool**.