import threading
import time
import sys
import curses
from colorama import just_fix_windows_console
from colorama import Fore, Style

just_fix_windows_console()

def countdown():
    for i in range(5):
        sys.stdout.write(Fore.RED + f"\rLoading... {i}")
        sys.stdout.flush()
        time.sleep(1)
    print("\nDone!")

def countup():
    print('\n')
    for i in range(10):
        sys.stdout.write(Fore.GREEN + f"\rLoading... {i}")
        sys.stdout.flush()
        time.sleep(1)
    print("\nDone!")

count1 = threading.Thread(target=countdown)
count1.start()
count2 = threading.Thread(target=countup)
count2.start()

count2.join()
print(Style.RESET_ALL)
