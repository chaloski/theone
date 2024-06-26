# Subdomain Scanner THE ONE

<img src="https://github.com/chaloski/theone/assets/121198386/d3b21db6-c2ea-4230-af61-c123c88ae713" alt="Description of the image" width="400" height="400">

# Subdomain Scanner Tool

## Overview
This Python script automates the process of discovering, verifying, and scanning subdomains for vulnerabilities. It leverages a robust combination of tools—**subfinder**, **httpx**, **katana**, and now **nuclei**—to identify subdomains, verify their availability, and conduct thorough vulnerability scans, ensuring comprehensive security assessments.

## Features
- **Subdomain Discovery**: Utilizes **subfinder** to detect all subdomains associated with a given IP or URL, essential for mapping out potential attack surfaces.
- **Availability Check**: Employs **httpx** to determine the active status of discovered subdomains, focusing efforts on reachable and relevant areas.
- **Security Scanning with Katana**: Uses **katana** to perform initial vulnerability scans on active subdomains, identifying common security issues.
- **Enhanced Vulnerability Detection with Nuclei**: Integrates **nuclei** for advanced vulnerability scanning using community-driven templates that check for a wide range of known vulnerabilities, providing deeper insights and enhanced security checks.

# Features

<h1 align="center">
  <img src="https://github.com/chaloski/theone/assets/121198386/87d5fad7-5208-422d-ae75-760a5b25214f" alt="httpx" width="700px">
  <br>
</h1>

## Why Nuclei?
**Nuclei** is integrated to provide:
- **Broader Security Coverage**: Detects more vulnerabilities than traditional scanners by using a vast, community-updated template system.
- **Automated Exploitation Tests**: Automates the testing process for known vulnerabilities, essential for rigorous security audits.
- **Structured Testing**: Offers a systematic approach to vulnerability detection, valuable for maintaining compliance with stringent security standards.

## Requirements
Ensure you have the following tools installed:
- Python 3.x
- **subfinder**
- **httpx**
- **katana**
- **nuclei**

Install these tools via their respective installation guides or use standard package managers.

##Install Dependencies
Ensure all tools are installed and accessible in your system's PATH. You can typically install these tools using their respective package managers. Here is an example command to install subfinder, httpx, katana, and nuclei, assuming you are using a Unix-like operating system:

 ```console
   go install github.com/projectdiscovery/katana/cmd/katana@latest
   go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
   go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest
   go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
 ```

## Installation and Usage
1. **Clone the repository**:
   ```console
   git clone https://github.com/chaloski/theone.git

## Install dependencies:

## Ensure all tools are installed and accessible in your system's PATH
2. **Run the script**:
   ```console
   python theone.py

## Follow the prompts to enter the target IP or URL.

## Subdomain Scanner Tool   

## Installation and Usage

## Output Files
- **subs.txt: Lists all discovered subdomains.**
- **alivesub.txt: Lists subdomains confirmed as active.**
- **katana.txt: Results from initial vulnerability scans.**
- **nuclei_results.txt: Detailed vulnerability findings from advanced scans.**

## Contributing
Contributions are welcome! Please fork the repository, make your improvements, and submit a pull request.

## License
This project is licensed under the MIT License. See LICENSE for more details.

## Author
By Chaloski
