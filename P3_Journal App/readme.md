# 📔 JournalApp – Daily Journal with Login using Tkinter

**JournalApp** is a simple desktop journal/diary application built using Python and Tkinter. It allows users to register and log in securely, write daily journal entries, and manage (edit/delete) them via a clean GUI. Data operations are abstracted into a custom database class (`myDB.py`).

---

## ✨ Features

- 🔐 User Authentication (Register/Login)
- 📅 Write and save daily journal entries
- ✍️ Edit or delete past entries
- 🧠 Simple and modular codebase (easy to extend)
- 📦 In-memory DB structure (can be upgraded to SQLite/JSON)

---

## 🛠 Tech Stack

- **Python 3.x**
- **Tkinter** – GUI framework
- **Custom Python Class** – for managing users and journal entries

---

## 📁 Project Structure

JournalApp/
├── journal_app.py # Main GUI app
├── myDB.py # Handles user and journal entry logic
├── assets/ # Optional for icons/images
└── README.md # Project documentation

## 🧩 Possible Future Enhancements
   - Encrypt journal content (AES encryption)

   - Add tags or categories to entries

   - Date-based filtering or calendar view

   - Export entries to PDF or Markdown

   - Add cloud sync support (Firebase or SQLite + remote)