# EduBase - Intelligent Learning Tracker

**EduBase** is a command-line-based intelligent learning tracker that helps users monitor their learning progress across subjects and topics. Designed to grow from beginner to advanced, this project demonstrates a strong grasp of Python, SQL, and CLI application architecture.

## 🚀 Features (Implemented & Planned)
✅ Completed:

- 🔐 **Register & login system** via CLI with MySQL authentication  
- 📚 **Add subjects** to track various learning areas  
- 📝 **Add topics** under each subject  
- ✅ **Mark topics as completed** to track progress  
- 📁 **Export progress** to CSV (`Reports/`) with subject, topic, and status  
- 🔍 Subject & topic search (case-insensitive, partial matching)
- 🔃 **Sort subjects** alphabetically (A-Z, Z-A)
- 🔃 **Sort topics** by name (A-Z, Z-A) or by completion status (Completed/Incomplete)
- 🔧 Modular OOP structure using Python classes (User, Subject, Topic, ProgressManager)
- ⚙️ MySQL Integration for persistent storage
- 📂 Organized project structure with clean separation of concerns
- 🛑 Error handling and validations for DB and input operations

🧠 Upcoming (Planned):

- 📊 Analytics and summaries of learning progress  
- 📈 Graphs using `matplotlib` or `pandas`  
- 🔄 Topic dependency system (e.g., "Learn A before B") 
- ⏳ Queue system for pending topics
- 🌳 Tree/nested hierarchy for subjects (if applicable)
- 📅 Scheduling/reminders via CLI
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
```
---

## 🔍 Search Features & Sort Features
- ✅ Case-insensitive subject & topic search
- ✅ Partial match support (e.g., typing phy finds Physics)
- ✅ Sort subjects: Alphabetical A-Z or Z-A
- ✅ Sort topics:
    - Alphabetically (A-Z / Z-A)
    - By completion status (Completed / Incomplete)
- ✅ Results include match count and completion status (✅ / ❌)


---
## 💡 How to Use

1. Clone the repo  
2. Set up your MySQL and `.env` file  
```bash
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=edubase
```
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

## ✅ Phase Progress

| Phase     | Description                               | Status                                        |
|-----------|-------------------------------------------|-----------------------------------------------|
| Phase 1   | CLI System + CSV logic                    | ✅ Completed                                  |
| Phase 2   | OOP + Modular Python                      | ✅ Completed                                  |
| Phase 3   | Data Structures/Algorithms                | 🟡 In Progress (search and sort implemented)  |
| Phase 4   | MySQL Integration                         | 🟡 Partially Done (Basic CRUD & schema ready) |
| Phase 5   | Advanced Python (argparse, decorators)    | 🔜 Upcoming                                   |
| Phase 6   | Analytics (pandas, performance analysis)  | 🔜 Upcoming                                   |
| Phase 7   | Role-Based Access (Admin/User)            | 🔜 Upcoming                                   |


---

## 🤝 Contributions
- Feel free to suggest new features or improvements!
- Pull requests and forks are welcome.