📌 HostelMate – Hostel Management System

A role-based web application for managing hostel activities, built using Django. The system provides separate functionalities for admins and hostelites, enabling smooth hostel management and communication.

✨ Features

🔐 Role-Based Access – Separate roles for Admin and Hostelite.

🏠 Room Management – Admins can manage hostel rooms.

📝 Request Box – Hostelites can raise requests/issues to admins.

🚪 Gate Pass System – Hostelites can apply for gate passes, admins can approve/reject.

💬 Feedback System – Hostelites can submit feedback, admins can review.

👤 Profile Management – Users can update and manage their profiles.

🔑 Secure Authentication – Custom user model with role-based access control.

🛠️ Tech Stack

Backend: Python, Django

Frontend: HTML, CSS, Django Templates

Database: SQLite (default, can be configured to MySQL/PostgreSQL)

Authentication: Django’s built-in Auth system with custom roles

⚙️ Installation & Setup

Clone the Repository

git clone https://github.com/Harmi-kotak22/HostelMate.git
cd HostelMate/Hostel_Management


Create Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt


Run Database Migrations

python manage.py makemigrations
python manage.py migrate


Create Superuser

python manage.py createsuperuser


Run the Development Server

python manage.py runserver


Open http://127.0.0.1:8000
 in browser 🚀

📂 Project Structure
Hostel_Management/
│── hostel/           # Main Django app
│   ├── models.py     # Database models
│   ├── views.py      # Views and business logic
│   ├── forms.py      # Django forms for login/signup/profile
│   ├── urls.py       # URL routing
│   └── templates/    # HTML templates
│
├── Hostel_Management/ # Django project settings
├── manage.py          # Project entrypoint

🤝 Contribution

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

👩‍💻 Author

Harmi Kotak

GitHub: Harmi-kotak22
