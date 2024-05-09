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

## Installation and Usage
1. **Clone the repository**:
   ```bash
   git clone https://github.com/chaloski/theone.git
