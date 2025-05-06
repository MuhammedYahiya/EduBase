# EduBase - Intelligent Learning Tracker

**EduBase** is a command-line-based intelligent learning tracker that helps users monitor their learning progress across subjects and topics. Designed to grow from beginner to advanced, this project demonstrates a strong grasp of Python, SQL, and CLI application architecture.

## 🚀 Features (Implemented & Planned)
- ✅ **Register & login system via CLI** — User authentication with MySQL integration.
- 🔜 **Add subjects and topics** — Organize learning content by subject.
- 🔜 **Mark topics as completed** — Track and update learning progress.
- 🔜 **Store progress in local files** — Save/load progress using CSV or text files.

## 🛠️ Tech Stack
- **Language**: Python 3.12
- **Database**: MySQL (using `mysql-connector-python`)
- **Libraries**:
  - `InquirerPy`: CLI menu interaction
  - `python-dotenv`: Load DB credentials securely
  - `pandas`, `numpy`: For analytics (future phases)
  - `tabulate`, `rich`: (optional) for better CLI formatting

## 📦 Project Structure
```bash
EduBase/
├── main.py                # Entry point
├── src/                   # Core logic
│   ├── auth.py            # Register/Login functions
│   └── ...                # Future modules (subject, tracker, etc.)
├── db/
│   └── connection.py      # MySQL connection logic
├── .env                   # DB credentials
└── README.md              # Project overview
