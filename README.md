# VitalSense Monitor

VitalSense Monitor is a simple Streamlit application designed to display two health sensor readings from an ESP32:

- Heart Rate (BPM)
- SpO₂ / Blood Oxygen (%)

The ESP32 isn't connected yet. Until it is, the dashboard shows `--` and "Place finger on sensor" instead of a real reading — it does not generate fake numbers. See **Testing Without the ESP32** below to simulate a reading locally.

## Project Structure

After extracting the project, the folder should look like this:

```text
vital_readings_streamlit/
│
├── app.py
├── simulate_reading.py
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

## Testing Without the ESP32

The app reads from a file called `latest_reading.json` in the project folder. If that file is missing, or its reading is older than 5 seconds, the dashboard shows `--` for both values — this is the normal state until the ESP32 is wired up.

To simulate a reading and see the dashboard show real-looking numbers, run this in a **second terminal** (with the venv activated) while `streamlit run app.py` is running:

```bash
python simulate_reading.py            # writes one reading, expires after 5s
python simulate_reading.py --loop     # keeps sending a reading every 2s, like a finger staying on the sensor
```

Stop it with `Ctrl + C` and wait a few seconds — the dashboard should fall back to `--`.

**For the real ESP32 integration later:** whatever script talks to the ESP32 just needs to write the same JSON shape to `latest_reading.json`:

```json
{"heart_rate": 78, "spo2": 98, "timestamp": 1755600000.123}
```

`timestamp` must be `time.time()` (unix seconds) at the moment the reading was taken. No changes to `app.py` should be needed once that's in place.

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

- The dashboard shows `--` until a real reading arrives — it never displays fake/random values.
- The dashboard auto-refreshes every couple of seconds.
- This interface is for display purposes only and is **not a diagnostic tool**.
