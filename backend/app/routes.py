from flask import request, jsonify
from app import app, db
from app.models import Ticket

@app.route('/tickets', methods=['GET'])
def get_tickets():
    tickets = Ticket.query.all()
    return jsonify([{
        'id': ticket.id,
        'title': ticket.title,
        'description': ticket.description,
        'status': ticket.status,
        'created_at': ticket.created_at.strftime('%Y-%m-%d %H:%M:%S')
    } for ticket in tickets])

@app.route('/tickets', methods=['POST'])
def create_ticket():
    data = request.json
    new_ticket = Ticket(
        title=data['title'],
        description=data['description'],
        status=data.get('status', 'To Do')
    )
    db.session.add(new_ticket)
    db.session.commit()
    return jsonify({"message": "Ticket created successfully!"}), 201
