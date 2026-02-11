from flask import Blueprint, render_template, request, redirect, url_for
from .models import Ticket
from . import db

main = Blueprint('main', __name__)


@main.route('/')
def home():
    tickets = Ticket.query.order_by(Ticket.created_at.desc()).all()
    return render_template("dashboard.html", tickets=tickets)


@main.route('/submit', methods=['GET', 'POST'])
def submit_ticket():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

        # ---- Automatic Priority Triage ----
        priority = "Low"
        text = description.lower()

        if "server" in text or "down" in text:
            priority = "Critical"
        elif "vpn" in text:
            priority = "High"
        elif "printer" in text:
            priority = "Medium"
        elif "password" in text:
            priority = "Low"

        # ---- Technician Assignment ----
        assigned_to = "Helpdesk"
        
        if priority == "Critical":
            assigned_to = "System Administrator"
        elif "vpn" in text:
            assigned_to = "Network Team"
        elif "printer" in text:
            assigned_to = "Desktop Support"
        elif "password" in text:
            assigned_to = "Helpdesk"

        # ---- Create Ticket ----
        ticket = Ticket(
            title=title,
            description=description,
            priority=priority,
            assigned_to=assigned_to
        )

        db.session.add(ticket)
        db.session.commit()

        print("TICKET SAVED")

        return redirect(url_for('main.home'))

    return render_template("submit_ticket.html")


@main.route('/ticket/<int:ticket_id>', methods=['GET', 'POST'])
def ticket_detail(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)

    if request.method == 'POST':
        ticket.status = request.form['status']
        db.session.commit()
        return redirect(url_for('main.ticket_detail', ticket_id=ticket.id))

    return render_template("ticket_detail.html", ticket=ticket)

@main.route('/queue/<tech>')
def technician_queue(tech):
    tickets = Ticket.query.filter_by(assigned_to=tech).all()
    return render_template("tech_queue.html", tickets=tickets, tech=tech)
