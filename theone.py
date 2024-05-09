import subprocess
import os

def run_command(command):
    """Execute a command using subprocess, capturing output and errors."""
    try:
        print("\033[1;36m")  # Cyan color for running commands
        result = subprocess.run(command, shell=True, text=True, capture_output=False)  # Real-time output
        print("\033[0m")  # Reset to default color
        if result.returncode != 0:
            print("\033[1;31m")  # Red color for errors
            print(f"Error: {result.stderr}")
            print("\033[0m")  # Reset to default color
            return None
        return result.stdout
    except Exception as e:
        print("\033[1;31m")  # Red color for unexpected errors
        print(f"An unexpected error occurred: {e}")
        print("\033[0m")  # Reset to default color
        return None

def select_urls(file_name, tool_name):
    """Allow the user to select specific URLs from a file for scanning or choose to scan all."""
    try:
        with open(file_name, 'r') as file:
            urls = file.readlines()
        
        print("\033[1;33m")  # Yellow color for URL listing
        print(f"Available URLs for {tool_name} scanning:")
        for idx, url in enumerate(urls):
            print(f"{idx + 1}: {url.strip()}")
        print("\033[0m")  # Reset to default color
        
        choice = input("Type 'all' to scan all URLs or enter the numbers of the URLs you want to scan (comma separated): ").strip()
        if choice.lower() == 'all':
            return file_name
        
        selected_indexes = choice.split(',')
        selected_urls = [urls[int(index) - 1].strip() for index in selected_indexes]
        
        # Save the selected URLs to a new file
        selected_file_name = f"selected_{tool_name}_urls.txt"
        with open(selected_file_name, 'w') as file:
            for url in selected_urls:
                file.write(url + '\n')
        
        return selected_file_name
    except Exception as e:
        print("\033[1;31m")  # Red color for file processing errors
        print(f"Error during URL selection: {e}")
        print("\033[0m")  # Reset to default color
        return None

# Displaying colorful ASCII art title
print("\033[1;34m")  # Blue color for title
print(r"""
 _____ _             ___             
|_   _| |__   ___   / _ \ _ __   ___ 
  | | | '_ \ / _ \ | | | | '_ \ / _ \
  | | | | | |  __/ | |_| | | | |  __/
  |_| |_| |_|\___|  \___/|_| |_|\___| By CHaloski
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

# User interaction to select specific URLs for Katana
katana_file = select_urls("alivesub.txt", "katana")
if katana_file:
    print("\033[1;36mRunning Katana...\033[0m")
    katana_command = f"katana -list {katana_file} -o katana_results.txt"
    run_command(katana_command)
    print("\033[1;32mKatana scan complete. Check 'katana_results.txt' for results.\033[0m")
else:
    print("\033[1;31mSkipping Katana scan.\033[0m")

# User interaction to select specific URLs for Nuclei
nuclei_file = select_urls("alivesub.txt", "nuclei")
if nuclei_file:
    print("\033[1;32mRunning Nuclei with selected URLs...\033[0m")
    nuclei_command = f"nuclei -list {nuclei_file} -o nuclei_results.txt -v"
    run_command(nuclei_command)
    print("\033[1;32mNuclei scan complete. Check 'nuclei_results.txt' for results.\033[0m")
else:
    print("\033[1;31mSkipping Nuclei scan.\033[0m")

print("\033[1;32mOverall scan complete. Check the result files for each tool.\033[0m")
