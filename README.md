# PySide6 Loyiha Shabloni

Bu loyiha PySide6 yordamida zamonaviy desktop ilovalar yaratish uchun tayyor shablon hisoblanadi.

## O'rnatish va Sozlash

1. **Qt Creator-ni ochish**
   - Qt Creator-ni ishga tushiring
   - "Create Project" tugmasini bosing
   - "Application (Qt for Python)" tanlang
   - "Qt Quick Application - Empty" ni tanlang

2. **Loyiha sozlamalari**
   - Loyiha nomini kiriting
   - PySide versiyasi sifatida "PySide6" ni tanlang
   - Kit Selection bo'limida "Python 3.12" ni tanlang
   - Virtual Environment manzilini `.qtcreator\Python_3_12_2venv` dan `env\` ga o'zgartiring

3. **Loyiha tuzilishi**
   - `main.py` va `main.qml` fayllarini o'chirib tashlang
   - Gitdan ko'chirilgan fayllarni loyiha papkasiga joylang
   - "Add Existing Files" orqali `qml.qrc` va `run.py` fayllarini qo'shing

4. **Ishga tushirish sozlamalari**
   - Project -> Python3.12 -> Run -> Run Configuration
   - `run.py` faylini ko'rsating

5. **Kerakli paketlarni o'rnatish**
   ```bash
   .\env\Scripts\activate
   pip install pyside6
   ```

## Loyiha tuzilishi

```
project/
├── env/                    # Virtual environment
├── py/                     # Python kodlari
│   ├── main.py             # Asosiy Python fayli
│   ├── rc.py               # QML resurslarini Python kodiga o`girilgan fayl
├── qml/                    # QML fayllari
│   └── main.qml            # Asosiy QML fayli
├── .gitignore              # Git uchun e'tiborga olinmasligi kerak bo'lgan fayllar
├── rc.qrc                  # QML resurslari
├── requirements.txt        # Kerakli Python paketlari
├── run.py                  # Ishga tushirish uchun Python skripti
├── project.pyproject       # Qt Creator loyiha fayli
└── project.pyproject.user  # Qt Creator foydalanuvchi sozlamalari
```

## Ishga tushirish

Loyihani ishga tushirish uchun Qt Creator-da "Run" tugmasini bosing yoki terminal orqali:

```bash
.\env\Scripts\activate
python run.py
```
