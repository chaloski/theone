# Subdomain Scanner THE ONE

<img src="https://github.com/chaloski/theone/assets/121198386/d3b21db6-c2ea-4230-af61-c123c88ae713" alt="Description of the image" width="400" height="400">


Overview
This Python script automates the process of discovering, verifying, and scanning subdomains for vulnerabilities. It uses a robust combination of tools—subfinder, httpx, katana, and now nuclei—to identify subdomains, check their availability, and scan for potential security issues. Each tool is specialized to perform distinct tasks, ensuring a comprehensive assessment of network security.

Features
Subdomain Discovery: Utilizes subfinder to find all subdomains associated with the given IP or URL. This is crucial for mapping the attack surface of a target.
Availability Check: Uses httpx to verify which subdomains are active, narrowing down the list to those that are accessible and potentially vulnerable.
Security Scanning with Katana: Employs katana to scan active subdomains for known vulnerabilities, providing an initial layer of security assessment.
Enhanced Vulnerability Detection with Nuclei: Integrates nuclei to perform a deeper and more detailed vulnerability analysis on the selected subdomains. This tool uses templates to check for a wide range of known vulnerabilities, offering a more thorough security check.
Why Use Nuclei?
Nuclei is integrated into this script to enhance the depth of security testing. It excels in quickly scanning for known vulnerabilities based on a continuously updated community-driven template system. This makes it incredibly effective for:

Detecting a broader range of security weaknesses that katana might not cover.
Automating the exploitation and confirmation of vulnerabilities, which can be crucial for security audits.
Providing a structured and reproducible way to test for vulnerabilities, which is valuable for both penetration testing and ensuring compliance with security policies.
Requirements
To run this script, you'll need:

Python 3.x
subfinder
httpx
katana
nuclei
These tools can be installed using their respective installation guides or package managers.

Usage
Clone this repository or download the script.
Ensure all dependencies are installed and properly configured.
Run the script from your command line:
bash
Copy code
python theone.py
Follow the on-screen prompts to enter the target IP or URL.
Output Files
subs.txt: Contains all discovered subdomains.
alivesub.txt: Contains all active subdomains verified by httpx.
katana.txt: Contains results from the katana vulnerability scan.
nuclei_results.txt: Contains detailed findings from the nuclei scan, providing insights into potential vulnerabilities.
Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Author
CHaloski
