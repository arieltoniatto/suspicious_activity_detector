# Suspicious Activity Detector

This Python script aims to detect suspicious activity on the system by checking for suspicious processes, files, and autostart scripts. It supports both Windows and Linux operating systems.

## Requirements

- Python 3.x
- `psutil` library (for Linux process detection)

## Usage

1. Clone the repository: `git clone https://github.com/username/suspicious_activity_detector.git`
2. Navigate to the project directory: `cd suspicious_activity_detector`
3. Install the required library: `pip install psutil`
4. Run the script: `python main.py`

## Features

The script includes the following functions:

### `check_processes()`

This function checks for suspicious processes running on the system. The list of suspicious processes can be modified by updating the `suspicious_process_list` variable within the function.

### `check_file_system()`

The `check_file_system()` function looks for suspicious files in specific paths on the system. Paths are defined based on the operating system (Windows or Linux). You can customize the list of suspicious file paths for each platform.

### `check_autostart()`

The `check_autostart()` function scans for suspicious autostart scripts on both Windows and Linux. The autostart paths differ depending on the operating system. Modify the `suspicious_scripts_autostart` list to include the names of suspicious autostart scripts.

### `main()`

The `main()` function orchestrates the detection process by invoking the above functions. If any suspicious activity is detected, it prints the details; otherwise, it displays a message indicating no suspicious activity.

## Notes

- The script utilizes the `platform` and `os` libraries for platform-specific operations and information.
- For Linux, the `psutil` library is used for process information.

## Disclaimer

This script is intended for educational and informational purposes only. Please use it responsibly and avoid using it for any malicious activities. The authors are not responsible for any misuse or damages resulting from the usage of this script.

## Contributions

Contributions to enhance and extend this script are welcome! Feel free to open pull requests or submit issues for improvements or bug fixes.
