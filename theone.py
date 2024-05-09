import subprocess
import os

# Displaying colorful ASCII art title
print("\033[1;34m")
print(r"""

 _____ _             ___             
|_   _| |__   ___   / _ \ _ __   ___ 
  | | | '_ \ / _ \ | | | | '_ \ / _ \
  | | | | | |  __/ | |_| | | | |  __/
  |_| |_| |_|\___|  \___/|_| |_|\___| By CHaloski
'''

""")
print("\033[0m")  # Reset to default color

# Asking for input
target = input("Enter an IP or URL to scan: ")

# Running subfinder
print("\033[1;33mRunning Subfinder...\033[0m")
subfinder_command = f"subfinder -d {target} -o subs.txt"
subprocess.run(subfinder_command, shell=True)

# Running httpx
print("\033[1;35mRunning Httpx...\033[0m")
httpx_command = "httpx -l subs.txt -o alivesub.txt"
subprocess.run(httpx_command, shell=True)


# Running Katana
print("\033[1;36mRunning Katana...\033[0m")
katana_command = "katana -list alivesub.txt -o katana.txt"
subprocess.run(katana_command, shell=True)

#

print("\033[1;32mScan complete. Check 'alivesub.txt', 'katana.txt', and 'subs.txt' for results.\033[0m")