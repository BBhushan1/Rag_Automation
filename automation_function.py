import os
import webbrowser
import psutil


def open_chrome():
    webbrowser.open("https://www.google.com")

def open_calculator():
    os.system("calc" if os.name == "nt" else "gnome-calculator")

def open_notepad():
    os.system("notepad" if os.name == "nt" else "gedit")

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    return psutil.virtual_memory().percent

def run_shell_command(command):
    return os.popen(command).read()