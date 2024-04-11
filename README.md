# Cloud-Based Restaurant Reservation System

## Development Process

### System Architecture

For this project, a microservice architecture style approach has been adopted. This choice offers several benefits such as scalability, easier maintenance, agility, and clear separation of concerns. Each microservice handles a specific aspect of the system, enhancing manageability and scalability.

### Vision Statement

**FOR** individuals **WHO** need to manage, update, and cancel restaurant reservations, **THE** cloud-based restaurant reservation system is a tool that allows users to accomplish these tasks efficiently. **THAT** includes features like creating new reservations, updating existing ones, and registering for an account. **UNLIKE** traditional systems, our product offers a centralized platform where users can access multiple restaurants, saving time and effort. **OUR PRODUCT** ensures secure management of reservations, protecting user data and providing a seamless dining experience.


## Restaurant Reservation System Documentation

### Overview of Application

This application is a cloud-based restaurant reservation system that allows users to create, receive, update, and delete reservations. It consists of a backend written in Python using the `http.server` package and a frontend developed with Next.js. Data storage is handled using SQLite.

### Tools and Technology Used

- **Programming Languages**: Python (backend), React JSX (frontend)
- **Database**: MongoDB
- **Version Control**: Git
- **Containerization**: Docker
- **API Testing**: Postman

### Getting Started (Local Run)

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Cloud-Based-Restaurant-Reservation-System.git

2. Navigate to the project directory:
    ```bash
    cd Cloud-Based-Restaurant-Reservation-System

3. Navigate to the ./backend directory and create a .env file with the following content:
    ```bash
    MONGODB_URI = Your Mongodb URI From Mongodb Atlas
    DB_NAME = Resturant

4. Build and start the project using Docker:
    ```bash
    docker-compose up --build

5. To Stop the application and delete the container
```bash
docker-compose down

6. Access the frontend application at http://localhost:3000 and the backend API at http://localhost:8000.

### Security Precautions