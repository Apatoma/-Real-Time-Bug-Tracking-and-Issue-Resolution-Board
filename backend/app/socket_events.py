from app import socketio, db
from app.models import Ticket
from flask_socketio import emit

@socketio.on('create_ticket')
def handle_create_ticket(data):
    new_ticket = Ticket(
        title=data['title'],
        description=data['description'],
        status=data.get('status', 'To Do')
    )
    db.session.add(new_ticket)
    db.session.commit()
    emit('ticket_created', {
        'id': new_ticket.id,
        'title': new_ticket.title,
        'description': new_ticket.description,
        'status': new_ticket.status,
        'created_at': new_ticket.created_at.strftime('%Y-%m-%d %H:%M:%S')
    }, broadcast=True)

@socketio.on('update_ticket_status')
def handle_update_ticket_status(data):
    ticket = Ticket.query.get(data['id'])
    if ticket:
        ticket.status = data['status']
        db.session.commit()
        emit('ticket_updated', {
            'id': ticket.id,
            'status': ticket.status
        }, broadcast=True)
