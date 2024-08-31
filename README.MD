# 🐛 Real-Time Bug Tracking and Issue Resolution Board

Welcome to the **Real-Time Bug Tracking and Issue Resolution Board**! This web application is designed to help development teams manage and resolve bugs collaboratively, featuring a real-time interactive board that keeps everyone in sync. Perfect for dynamic environments where efficient task management is key.

## ✨ Features

- ⚡ **Real-Time Updates**: Instantly reflect changes to tickets across all users' boards.
- 📝 **Interactive Kanban Board**: Manage tickets effortlessly with drag-and-drop functionality across stages (To Do, In Progress, Done).
- 🌐 **WebSocket Integration**: Enjoy real-time communication between the frontend and backend, ensuring instant ticket updates.
- 🔗 **RESTful API**: Easily create, retrieve, and update tickets via HTTP requests.

## 🛠️ Technologies Used

- **Backend**: Python, Flask (Flask-SocketIO for real-time features, Flask-SQLAlchemy for ORM)
- **Frontend**: React.js
- **Database**: SQLite
- **Styling**: HTML/CSS

## 🚀 Getting Started

Follow these steps to set up the project locally.

### Prerequisites

- **Python 3.x**
- **Node.js & npm**

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Apatoma/-Real-Time-Bug-Tracking-and-Issue-Resolution-Board.git
    cd bug-tracking-board
    ```

2. **Set up the backend**:
    ```bash
    cd backend
    pip install -r requirements.txt
    python run.py
    ```

3. **Set up the frontend**:
    ```bash
    cd frontend
    npm install
    npm start
    ```

4. **Access the application**:
    - The backend will be running on `http://localhost:5000`
    - The frontend will be running on `http://localhost:3000`

## 📝 Usage

- **Creating Tickets**: Click on the "Add Ticket" button to create a new bug ticket. Fill in the details and assign it to the appropriate stage.
- **Updating Ticket Status**: Drag and drop tickets between the "To Do," "In Progress," and "Done" columns to update their status.
- **Real-Time Collaboration**: Any updates made to the board are instantly visible to all connected users.

## 🛤️ Future Enhancements

- 🔐 **User Authentication**: Add user roles and permissions to restrict access to certain features.
- 🕒 **History Tracking**: Implement a history log to track changes made to each ticket.
- 🛠️ **Integration with Version Control Systems**: Automatically create tickets based on issues in GitHub or GitLab.
- 🔔 **Notifications**: Add email or in-app notifications for updates on specific tickets.

## 🧑‍💻 Contributing

Contributions are welcome! Please fork the repository and create a pull request with your feature or bug fix.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Made with ❤️ by Alejandro (https://github.com/Apatoma)
