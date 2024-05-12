import time
import re
import pyautogui
import os
from dotenv import load_dotenv
from fish import *

load_dotenv()

CONSOLE_FILE = os.getenv('CONSOLE_FILE')
EXEC_FILE = os.getenv('EXEC_FILE')

def listen(logFile):
    logFile.seek(0,2)
    while True:
        line = logFile.readline()
        if not line:
            time.sleep(0.1)
            continue
        print(line)
        parse(line)

def parse(line):
    regex = re.findall(r"(!\w+(?:\s+\S+)*)", line)
    user_regex = re.search(r"\[ALL\]\s+(\w+)‎:", line)
    if user_regex:
        username = user_regex.group(1)
    else:
        username = ""

    if regex:
        command_with_args = regex[0]
        command_args_split = command_with_args.split(maxsplit=1)
        command = command_args_split[0]
        args = command_args_split[1] if len(command_args_split) > 1 else ''
    else:
        command = ""
        args = ""

    match command:
        case "!disconnect":
            write_command("disconnect")
            press_key()
        case "!i":
            if args:
                inspect_link = re.search(r"steam:\/\/rungame\/730\/[0-9]+\/\+csgo_econ_action_preview%20([A-Za-z0-9]+)", args)
                if inspect_link:
                    write_command(f"gameui_activate;csgo_econ_action_preview {inspect_link.group(1)}\n say Opened inspect link on my client.")
                    del inspect_link
                else:
                    write_command("say Invalid inspect link.")
            else:
                write_command("say No inspect link provided.")
            press_key()
        case "!switchhands":
            write_command("switchhands \n say Switched viewmodel.")
            press_key()
        case "!play": #i recommend setting snd_toolvolume lower (i use 0.2)
            if args:
                write_command(f"play {args}\n say Playing {args}.")
                press_key()
            else:
                write_command("say No sound provided")
                press_key()
        case "!flash":
            write_command("say fuck you.")
            press_key()
            write_command("flashbangs")
            for _ in range(13):
                press_key_no_delay()
                time.sleep(0.01 / 13)
        case "!fish":
            cast_line(username)

def write_command(command):
    with open(EXEC_FILE, 'w', encoding='utf-8') as f:
        f.write(command)

def press_key():
    time.sleep(0.15)
    pyautogui.press('multiply')

def press_key_no_delay():
    pyautogui.press('multiply')

if __name__ == '__main__':
    logFile = open(CONSOLE_FILE,"r", encoding="utf-8")
    logLines = listen(logFile)