import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';
import Ticket from './Ticket';

const socket = io.connect('http://localhost:5000');

function Board() {
  const [tickets, setTickets] = useState([]);
  const columns = ['To Do', 'In Progress', 'Done'];

  useEffect(() => {
    fetch('/tickets')
      .then(response => response.json())
      .then(data => setTickets(data));

    socket.on('ticket_created', (ticket) => {
      setTickets((prevTickets) => [...prevTickets, ticket]);
    });

    socket.on('ticket_updated', (updatedTicket) => {
      setTickets((prevTickets) =>
        prevTickets.map(ticket =>
          ticket.id === updatedTicket.id ? { ...ticket, status: updatedTicket.status } : ticket
        )
      );
    });
  }, []);

  const updateTicketStatus = (id, status) => {
    socket.emit('update_ticket_status', { id, status });
  };

  return (
    <div className="board">
      {columns.map((column) => (
        <div key={column} className="column">
          <h2>{column}</h2>
          {tickets
            .filter(ticket => ticket.status === column)
            .map(ticket => (
              <Ticket key={ticket.id} ticket={ticket} updateStatus={updateTicketStatus} />
            ))}
        </div>
      ))}
    </div>
  );
}

export default Board;
