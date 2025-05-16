# EduBase - Intelligent Learning Tracker

**EduBase** is a command-line-based intelligent learning tracker that helps users monitor their learning progress across subjects and topics. The project is now evolving to incorporate a modern web backend using Django and PostgreSQL, alongside the existing CLI version.

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
- 📂 Organized Project Structure for CLI version
- 🛑 Error handling and validations for DB and input operations

🧠 Upcoming (Planned):
- 🚀 Started Django backend project for API and admin panel (backend/edubase_backend/)
- 🐘 Migrating database to PostgreSQL for scalable production use
- 🌐 Planning React frontend integration for a modern web UI
- 🔄 Preparing transition from CLI-only to full web app architecture
- 📊 Analytics and summaries of learning progress  
- 📈 Graphs using `matplotlib` or `pandas`  
- 🔄 Topic dependency system (e.g., "Learn A before B") 
- ⏳ Queue system for pending topics
- 🌳 Tree/nested hierarchy for subjects (if applicable)
- 📅 Scheduling/reminders via CLI
- ☁️ Export to cloud storage or sync with GitHub  

---

## 🛠️ Tech Stack
- **CLI Version**: Python 3.12, MySQL, mysql-connector-python
- **New Backend**: Python 3.12, Django, PostgreSQL
- **Frontend** (Planned): React.js
- **Libraries**:
  - CLI: InquirerPy, python-dotenv  
  - Backend: Django ORM, REST Framework (planned)
  - Analytics planned with pandas, matplotlib 

---
## 📦 Project Structure
```bash
EduBase/
├── backend/                # Django backend project root
│   ├── edubase_backend/    # Django project folder
│   └── manage.py           # Django management commands
├── legacy_cli/             # Original CLI application
│   ├── main.py             # CLI entry point
│   ├── src/                # Core CLI business logic modules
│   ├── db/                 # Database connection and schema for CLI
│   ├── Reports/            # CSV export folder for CLI
│   └── requirements.txt    # CLI dependencies
├── README.md               # Project overview and documentation
└── .gitignore              # Git ignore rules (including .venv, reports, env files)

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

### Legacy CLI

1. Clone the repository  
2. Configure your `.env` file with MySQL credentials:
    ```bash
    DB_HOST=localhost
    DB_USER=root
    DB_PASSWORD=yourpassword
    DB_NAME=edubase
    ```
3. Install dependencies and activate the Python virtual environment inside the `legacy_cli/` folder:
    ```bash
    cd legacy_cli
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```
4. Run the CLI application:
    ```bash
    python main.py
    ```

---

### Django + React Application

#### Backend (In Progress)

1. Navigate to the `backend/` directory  
2. Set up PostgreSQL and your Django environment (install dependencies, configure settings)  
3. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

#### Frontend

- React frontend integration is planned for upcoming phases.

---


## 📤 CSV Export Sample

When exporting progress, you get a file like:
Saved to: `Reports/user_<user_id>_progress.csv`

---
## 📌 Notes

- .venv environments are separate for CLI and backend projects
- CLI reports are saved under legacy_cli/Reports/ and .gitignored
- .env files contain sensitive DB credentials and are excluded from Git
- Transition to Django + React planned for improved UX and scalability


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
| Phase 8   | Django Backend + React Frontend Migration | 🟡 Started (backend setup done)               |

---

## 🤝 Contributions
- Suggestions and pull requests are highly welcome!
- Collaboration encouraged for new backend features and frontend development.
