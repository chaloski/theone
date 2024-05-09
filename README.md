# Subdomain Scanner THE ONE

<img src="[path_to_image.jpg](https://github.com/chaloski/theone/assets/121198386/d3b21db6-c2ea-4230-af61-c123c88ae713))" alt="Description of the image" width="100" height="100">

## Overview
This Python script automates the process of discovering, verifying, and scanning subdomains for vulnerabilities. It uses a combination of tools (`subfinder`, `httpx`, and `katana`) to identify subdomains, check their availability, and scan for potential security issues.

## Features
- **Subdomain Discovery**: Utilizes `subfinder` to find all subdomains associated with the given IP or URL.
- **Availability Check**: Uses `httpx` to verify which subdomains are active.
- **Security Scanning**: Employs `katana` to scan active subdomains for known vulnerabilities.

## Requirements
To run this script, you'll need:
- Python 3.x
- `subfinder`
- `httpx`
- `katana`

You can install `subfinder`, `httpx`, and `katana` using their respective installation guides or package managers.

## Usage
1. Clone this repository or download the script.
2. Ensure all dependencies are installed and properly configured.
3. Run the script from your command line:
   ```bash
   python theone.py
Follow the on-screen prompts to enter the target IP or URL.
Output Files
subs.txt: Contains all discovered subdomains.
alivesub.txt: Contains all active subdomains verified by httpx.
katana.txt: Contains results from the katana vulnerability scan.
Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Author
CHaloski
