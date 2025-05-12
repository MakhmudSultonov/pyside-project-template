import os
import shutil
import sys

# Virtual muhitdagi Python interpretatorini aniqlash
venv_python = os.path.join(os.path.dirname(os.path.abspath(__file__)), "env", "Scripts", "python.exe")
print(venv_python)

print("QML resurslarini yangilash...")
os.system("pyside6-rcc rc.qrc -o py/rc.py")

print("\nDasturni ishga tushirish...")
os.system(f'"{venv_python}" py/main.py') 

