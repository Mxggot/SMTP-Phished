<div align="center">
  <h1>Phished</h1>
</div>

<div align="center">
 
  [![Last Commit](https://img.shields.io/github/last-commit/Mxggot/SMTP-Phished/main)](https://github.com/Mxggot/SMTP-Phished/commits/main/)
  [![License](https://img.shields.io/badge/License-MIT-violet.svg)](https://github.com/Mxggot/SMTP-Phished/blob/main/LICENSE)
  [![Twitter](https://img.shields.io/twitter/follow/yoboireica)](https://twitter.com/yoboireica)
</div>


<div align="center">
  <a href="#disclaimer">Disclaimer</a> |
  <a href="#user-manual">User Manual</a> |
  <a href="#donations">Donations</a>
</div>

---

![Phished Alert](https://github.com/Mxggot/SMTP-Phished/blob/main/photos/phished-alert.png)

![Phished Main Menu](https://github.com/Mxggot/SMTP-Phished/blob/main/photos/phished-mainmenu.png)

# Disclaimer

This repository contains a sample tool intended solely for educational and awareness purposes regarding the dangers of phishing. The creation and use of phishing tools are illegal and unethical activities. The author of this repository neither encourages nor endorses the practice of phishing.

## Risks of Phishing

Phishing is a malicious technique used by cybercriminals to obtain confidential information, such as passwords and personal data, by deceiving users. This repository aims to educate about the risks associated with phishing and highlight the importance of cyber awareness. Instead of conducting real attacks, this tool simulates the process of a phishing attack in a controlled manner (allowing the selection of the recipient), so users understand how these attacks work and learn to protect themselves.

## Responsible Use

The use of this tool should be strictly limited to controlled environments and with the explicit consent of the involved parties. It is not permitted to use this tool to send phishing emails without explicit authorization.

## How to Protect Yourself

- Never click on suspicious links.
- Always verify the authenticity of received emails.
- Keep your security software up to date.
- Use two-factor authentication whenever possible.

# User Manual

## Introduction

This manual is designed to guide users through the installation and execution of the tool. Whether you're a beginner or an experienced user, this guide will help you navigate through Phished effortlessly.

### Important Warning

> Before proceeding, it is crucial to understand that the misuse of this tool may violate laws and ethical principles. By executing the tool, you agree to use it ethically, responsibly, and only in controlled environments, with proper consent.

### Requirements

- Python 3.12.x installed
- Git installed 
- Permissions to execute scripts in the environment
    
### Installation

    Open a terminal or command prompt.    
    `git clone https://github.com/Mxggot/SMTP-Phished.git`
    `cd SMTP-Phished`

### Running the Tool

    Navigate to the directory where the script is located.
    Run the script using the command `python3 phished.py` or `./phished.py`.
    If the script failed to run you should try setting permissions by typing `chmod +x phished.py`.

### Main Menu

#### Upon running the tool, you will be presented with the Main Menu. This menu offers the following options:

    1) Single Target: Simulated phishing email sending to a single address.
    2) Multiple Targets: Simulated phishing email sending to a list of addresses.
    3) Help: Display additional information about the tool.
    99) Exit: Terminate the tool execution.

#### Target Selection:

> When selecting option 1 or 2, provide the requested information, such as email addresses, fake sender, email subject, and message path.

> NOTE: The list of EMAILS must be in .txt format, with emails separated by ';' (semicolon).

> NOTE: The message to be sent must be in a .txt file, but its writing must be in HTML.

#### SMTP Configuration:

> Provide the SMTP server, login, and password when prompted. Make sure this information is valid and that you have permission to use the provided SMTP server.

#### Sending Test Emails:

> The tool will send simulated phishing emails only to the provided addresses, causing no real harm. This allows understanding phishing signs and enhancing awareness.
> After sending the emails, the tool will provide feedback on the success or failure of the process.

---

# Donations

If you found this tool useful and want to support its development, consider buying me a coffee through PayPal:

[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-Donate-blue.svg)](https://paypal.me/rainierteoxon7?country.x=PH&locale.x=en_US)

<img src="https://gifdb.com/images/high/dancing-roach-insect-796v3spbhd1lipzk.webp" alt="Cute GIF" width="101">

Your support is greatly appreciated! ☕️🙏 
