# EnCryptohome

EnCryptohome is a folder encryptor/decryptor<br>
This does NOT work on files
## Installation
- Windows<br>
Either download main.exe from downloads and run it in the terminal OR run main.py with python in the terminal
- Other OS<br>
Run main.py with python I guess?
## Dependencies for running from source
Python, cryptography library (download via pip)
## How it works
- For encryption
It generates a hash with sha256 along with the password you give it, then it zips the folder and then encrypts that zip file and renames it to .enczip
- For decryption
It does what the encryption thing does in reverse
## Usage
- `main.exe encrypt <folder>` - encrypts a folder and makes it an .enczip file
- `main.exe decrypt <enczip>` - decrypts an .enczip file and makes it a regular .zip file
## Credits
- Me for mostly everything
- Sonnet 4.6 for helping me with the idea and stuff