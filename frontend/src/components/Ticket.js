import React from 'react';

function Ticket({ ticket, updateStatus }) {
  const nextStatus = {
    'To Do': 'In Progress',
    'In Progress': 'Done',
    'Done': 'To Do',
  };

  return (
    <div className="ticket" onClick={() => updateStatus(ticket.id, nextStatus[ticket.status])}>
      <h3>{ticket.title}</h3>
      <p>{ticket.description}</p>
      <small>Created at: {ticket.created_at}</small>
    </div>
  );
}

export default Ticket;
