import platform
import os
import subprocess
import time
import psutil

def check_processes():
    try:
        system = platform.system()
        
        suspicious_process_list = ["suspicious_process_1", "suspicious_process_2", "suspicious_process_3"]  # Add suspicious process names here

        if system == "Windows":
            process_list = subprocess.check_output(["tasklist"], shell=True)
        
            process_list = process_list.decode("utf-8", errors="ignore") # Use 'ignore' error handling to skip invalid UTF-8 characters

            for unreliable_process in suspicious_process_list:
                if unreliable_process in process_list:
                    print(f"Detected suspicious process: {unreliable_process}")
                    return True

        if system == "Linux":
            for process in psutil.process_iter(["pid", "name"]):
                if process.info["name"] in suspicious_process_list:
                    print(f"Detected suspicious process: {process.info['name']}")
                    return True

        print(f"No suspicious processes detected.")
        return False
    except subprocess.CalledProcessError:
        print("Failed to retrieve process list.")
        return False

def check_file_system():
    system = platform.system()
 
    if system == "Windows":
        suspicious_paths = [
            "C:\\Windows\\System32\\suspicious_file.dll",  # Add suspicious file paths for Windows here
            "C:\\Program Files\\Suspicious Dir\\suspicious_file.exe"
        ]

    elif system == "Linux":
        suspicious_paths = [
            "/usr/bin/suspicious_file",  # Add suspicious file paths for Linux here
            "/usr/local/bin/suspicious_file"
        ]
    
    else:
        print(f"Unsupported OS: {system}")
    
    for path in suspicious_paths:
        if os.path.exists(path):
            print(f"Detected suspicious file: {path}")
            return True
            

    print("No suspicious files detected.")
    return False

def check_autostart():
    autostart_path = None

    suspicious_scripts_autostart = ["suspicious_script.bat", "suspicious_file.py"]  # Add suspicious autostart script names here

    system = platform.system()
    if system == "Windows":
        autostart_path = "C:\\Users\\<YourUsername>\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"  # Replace <YourUsername> with your actual username

        if os.path.exists(autostart_path):
            files = os.listdir(autostart_path)
    
            for suspicious_script in suspicious_scripts_autostart:
                if suspicious_script in files:
                    print(f"Detected suspicious autostart script: {suspicious_script}")
                    return True
    
    if system == "Linux":
        system_autostart_path = "/etc/xdg/autostart" # System-wide autostart

        if os.path.exists(system_autostart_path):
            files = os.listdir(system_autostart_path)

            for suspicious_script in suspicious_scripts_autostart:
                if suspicious_script in files:
                    print(f"Detected suspicious system-wide autostart script: {suspicious_script}")
                    return True

        user_autostart_path = os.path.expanduser("~/.config/autostart") # User autostart

        if os.path.exists(user_autostart_path):
            files = os.listdir(user_autostart_path)

            for suspicious_script in suspicious_scripts_autostart:
                if suspicious_script in files:
                    print(f"Detected suspicious user-specific autostart script: {suspicious_script}")
                    return True

    print("No suspicious autostart scripts detected.")
    return False

def main():
    print("Checking for suspicious presence...")
    time.sleep(1)  # Give some time to read the message

    found_suspicious = False
    found_suspicious = check_processes() or found_suspicious
    found_suspicious = check_file_system() or found_suspicious
    found_suspicious = check_autostart() or found_suspicious

    if not found_suspicious:
        print("No suspicious activity detected on the system.")

if __name__ == "__main__":
    main()