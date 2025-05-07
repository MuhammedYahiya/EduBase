# EduBase - Intelligent Learning Tracker

**EduBase** is a command-line-based intelligent learning tracker that helps users monitor their learning progress across subjects and topics. Designed to grow from beginner to advanced, this project demonstrates a strong grasp of Python, SQL, and CLI application architecture.

## 🚀 Features (Implemented & Planned)
✅ Completed:

- 🔐 **Register & login system** via CLI with MySQL authentication  
- 📚 **Add subjects** to track various learning areas  
- 📝 **Add topics** under each subject  
- ✅ **Mark topics as completed** to track progress  
- 📁 **Export progress** to CSV (`Reports/`) with subject, topic, and status  

🧠 Upcoming (Planned):

- 📊 Analytics and summaries of learning progress  
- 📈 Graphs using `matplotlib` or `pandas`  
- 📅 Scheduling or reminders  
- ☁️ Export to cloud storage or sync with GitHub  

---

## 🛠️ Tech Stack
- **Language**: Python 3.12
- **Database**: MySQL (via `mysql-connector-python`)
- **Libraries**:
  - [`InquirerPy`](https://github.com/kazhala/InquirerPy): Interactive CLI  
  - [`python-dotenv`](https://pypi.org/project/python-dotenv/): Secure .env loading  
  - `csv`, `os`: Local file operations  
  - `pandas`, `matplotlib` (for later phases)

---
## 📦 Project Structure
```bash
EduBase/
├── main.py # Entry point CLI interface
├── src/ # Core business logic
│ ├── user.py # Register/Login logic
│ ├── subject.py # Add/view subjects
│ ├── topic.py # Add/view/mark topics
│ └── report.py # Export progress to CSV
├── db/
│ └── connection.py # MySQL DB connection
├── Reports/ # Folder for exported CSV reports
├── .env # Environment variables (DB credentials)
├── .gitignore # Ignoring reports, credentials, etc.
└── README.md # Project overview

---

## 💡 How to Use

1. Clone the repo  
2. Set up your MySQL and `.env` file  
3. Run `python main.py`  
4. Navigate through the CLI to register, add subjects/topics, and track progress  

---

## 📤 CSV Export Sample

When exporting progress, you get a file like:
Saved to: `Reports/user_<user_id>_progress.csv`

---
## 📌 Notes

- Use a `.env` file to store DB credentials (`DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`)
- Reports are saved in a dedicated `Reports/` folder (auto-created if missing)
- Git tracks only code; reports are `.gitignore`d

---

## ✅ Progress

You're currently in **Phase 1: Core CLI & MySQL Integration**, with partial parallel progress on **Phase 4: Analytics-ready SQL Structure**.

---

Feel free to suggest or contribute new features!