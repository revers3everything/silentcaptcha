# SilentCaptcha Tool

It is a tool that automates the solving of CAPTCHAs to perform brute-force attacks on login pages. It solves CAPTCHAs on websites protected with Google reCAPTCHA, using Selenium and the noCaptcha extension. It is ideal for educational and research purposes in controlled environments, enabling brute-force attacks and bypassing CAPTCHA protection since the solving process is automated with this bot.

![silentCaptcha](https://github.com/user-attachments/assets/79502eb7-6e91-4279-a351-220646bcfec4)

See the tool in action: https://youtu.be/KxnmY7Hw24k
![silentcatpcha2](https://github.com/user-attachments/assets/7be15c7a-5d93-47b7-957a-62d827b5c763)


## Features

- Automation of credential submission on websites with CAPTCHA protection.
- Use of Selenium for browser interaction.
- reCAPTCHA bypass using the noCaptcha extension.

## Requirements

Before running the script, make sure you meet the following requirements:

- **Python**: Version 3.12.6 or higher.
- **Geckodriver**: Driver required to control Firefox with Selenium.
- **Selenium**: Library for automating web browsers.
- **noCaptcha Extension**: Extension used to bypass CAPTCHA. (The extension is in the repo, but if you want to download the latest, check https://www.youtube.com/watch?v=-Lz-acPIrek)

## Installation

Follow the steps below to install the dependencies and set up the environment.

### 1. Clone the repository

Clone this repository to your local machine:

```bash
git clone https://github.com/revers3everything/silentcaptcha.git
cd silentcaptcha
```

### 2. Install dependencies

Run the `Install.sh` script to automatically install all necessary dependencies, activate the virtual environment, and install Selenium.

```bash
source Install.sh
```
This script will:
- Install `python3-venv` if it is not already present.
- Create and activate a virtual environment.
- Install `selenium` within the virtual environment.
- Verify the installation of **Geckodriver**.

### 3. Run the script

Once the environment is set up, run the `NoCaptcha.py` script with the necessary parameters:

```bash
python3 NoCaptcha.py https://web-with-reCaptcha/ usuarios.txt contraseñas.txt
```

- **Website URL with CAPTCHA**: The first argument is the URL of the website where you want to attempt the bypass.
- **Usernames file**: The second argument is the file that contains a list of usernames.
- **Password file**: The third argument is the file that contains a list of passwords.

## Important notes

- **Educational use**: This script is intended for educational and research purposes in controlled environments. It should not be used on websites where you do not have explicit permission to conduct testing.
- **Updates**: Make sure to have the latest versions of Selenium and Geckodriver to avoid compatibility issues.

## Contributions

If you have suggestions or improvements, feel free to open a pull request or create an issue in this repository.

## Authors

- Principal Author: Anthony Lopez @sk8ware
- Danilo Erazo @revers3vrything
- This tool was first presented in 2024 at the '8.8 Computer Security Conference' in October, Ecuador.
