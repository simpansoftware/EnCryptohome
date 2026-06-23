import zipfile
import sys
from pathlib import Path
from cryptography.fernet import Fernet
import hashlib
import base64
import os

helptext = """usage:
    python main.py encrypt <folder> - encrypts a folder
    python main.py decrypt <enczip> - decrypts an .enczip file"""

print("EnCryptohome")
if len(sys.argv) < 3:
    print(helptext)
    sys.exit(1)
elif sys.argv[1] == "encrypt":
    folder = sys.argv[2]
    folder2 = Path(folder)
    password = input("what password do you want to encrypt it with? (enter randompass as the password to generate a random hash)\n> ")
    with zipfile.ZipFile(f"{folder2}.zip", "w", zipfile.ZIP_DEFLATED) as zippy:
        for file in folder2.rglob("*"):
            zippy.write(file, arcname=file.relative_to(folder))
    if password == "randompass":
        password = os.urandom(32).hex()
        print(f"generated password is {password}, SAVE THIS")
    
    key = base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())
    ferrynet = Fernet(key)
    with open(f'{folder2}.zip', 'rb') as f:
        original = f.read()
    encrypted = ferrynet.encrypt(original)
    with open(f'{folder2}.enczip', 'wb') as f:
        f.write(encrypted)
    os.remove(f"{folder2}.zip")
    print(f"{folder2} encrypted as {folder2}.enczip!")

elif sys.argv[1] == "decrypt":
    enczip = Path(sys.argv[2])
    if enczip.suffix == ".enczip":
        password = input("what password do you want to decrypt it with?\n> ")
        key = base64.urlsafe_b64encode(hashlib.sha256(password.encode()).digest())
        ferrynet = Fernet(key)
        with open(enczip, 'rb') as f:
            original = f.read()
        try:
            ogzip = ferrynet.decrypt(original)
        except Exception:
            print("uhh yeah file is either corrupt or you entered the wrong password")
            sys.exit()
        
        zippy = enczip.with_suffix(".zip")
        with open(zippy, "wb") as f:
            f.write(ogzip)
        os.remove(enczip)
        print(f"{enczip} decrypted as {zippy}!")
    else:
        print("not an enczip file, stop proceeding")
else:
    print(helptext)