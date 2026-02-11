# ITSM Ticketing System

A full-stack IT Service Management (ITSM) helpdesk platform built with **Python and Flask** that automates ticket triage, routing, and technician workflow.

This application simulates an internal corporate service desk where employees submit technical issues and IT teams manage, track, and resolve them.

---

## Overview

This project models a real-world enterprise support workflow:

1. Employees submit support requests
2. The system analyzes the issue description
3. Priority is automatically assigned
4. Tickets are routed to the correct technical team
5. Technicians update status and leave work notes
6. Activity history is stored for auditing

The goal of this project is to demonstrate backend development, database design, and workflow automation similar to internal business platforms used in corporate environments.

---

## Features

### Ticket Management
- Submit IT support tickets
- View ticket dashboard
- Open individual tickets
- Update ticket status (Open, In Progress, Resolved, Closed)

### Automated Triage
The system analyzes ticket descriptions and automatically assigns priority:

| Keyword | Priority |
|--------|------|
| server/down | Critical |
| vpn | High |
| printer | Medium |
| password | Low |

### Automatic Routing
Tickets are routed to the appropriate team:

- Helpdesk
- Network Team
- Desktop Support
- System Administrator

### Technician Queues
Each technical team has its own queue page displaying assigned tickets.

### Work Notes (Audit Log)
Technicians can leave notes on a ticket, creating a historical activity log for troubleshooting and accountability.

---

## Tech Stack

**Backend**
- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Login

**Database**
- SQLite (development)

**Frontend**
- HTML5
- Jinja2 Templates
- CSS

---

## Project Structure

```
itsm-ticketing-system/
│
├── app/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── routes.py
│   └── __init__.py
│
├── run.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/YOURUSERNAME/itsm-ticketing-system.git
cd itsm-ticketing-system
```

Create a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Create the database:

```
python
```

Then run:

```
from app import create_app, db
app = create_app()
app.app_context().push()
db.create_all()
exit()
```

Run the application:

```
python run.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## What This Demonstrates

This project demonstrates:

- RESTful routing
- Relational database modeling
- One-to-many relationships
- Workflow automation logic
- Form handling
- Server-side rendering
- Business rule processing

---

## Future Improvements
- User authentication (employee vs technician login)
- Email notifications
- File attachments
- Role-based permissions
- PostgreSQL deployment
- Cloud hosting

---

## Author
Corey Shamburger  
Full-Stack Developer | Software Developer
