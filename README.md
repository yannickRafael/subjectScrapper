# SubjectScrapper

## 📌 Overview
**SubjectScrapper** is a Python-based tool designed to scrape and store academic subject data efficiently. It extracts information about subjects and saves it in Firebase Firestore for easy access and management.

## 🚀 Features
- Scrapes subject data from a specified source
- Stores subject details in Firebase Firestore
- Uses Firebase references for better data structure
- Simple and efficient Python implementation

## 🛠️ Installation
### 1. Clone the Repository
```sh
git clone https://github.com/yannickRafael/subjectScrapper.git
cd subjectScrapper
```

### 2. Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

## 🔧 Configuration
1. **Set Up Firebase**
   - Create a Firebase project at [Firebase Console](https://console.firebase.google.com/)
   - Enable Firestore Database
   - Download the `serviceAccountKey.json` file from Firebase and place it in the project directory

2. **Update `config.py`**
   - Ensure `key_path` points to your Firebase service account key.

## 🏃 Usage
Run the script to scrape and store subjects:
```sh
python main.py
```

## 📂 Project Structure
```
subjectScrapper/
│── config.py           # Firebase configuration
│── main.py             # Main script to run scrapper
│── subject.py          # Subject model
│── requirements.txt    # Dependencies
│── README.md           # Documentation
```

## 🔗 Firebase Firestore Data Structure
- **Collection:** `cadeiras` (Subjects)
  - `codigo`: Unique subject identifier
  - `nome`: Subject name
  - `cursoId`: Reference to the `cursos` collection

## 📜 License
This project is licensed under the MIT License.

## 📞 Contact
For issues or improvements, feel free to open an [issue](https://github.com/yannickRafael/subjectScrapper/issues) or contribute with a pull request!

