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
```
# Testing The API 

This document describes the API endpoints available in our web service.

## Registration

To register a new user, send a POST request to `/register` with the username, password, and email.

![Registration Request]

Upon successful registration, you should receive a confirmation message:


![1](https://github.com/AhmadMashal1/BTP-Project-2/assets/157860187/aa4e07f4-4d6f-494a-bf19-cde1ce2b033b)



## Login

Send a POST request to `/login` with your username and password to receive an authentication token.

Here's what the response will look like upon a successful login:

![2](https://github.com/AhmadMashal1/BTP-Project-2/assets/157860187/6b000c30-4bb8-4172-ba12-96f963a4832d)

![3](https://github.com/AhmadMashal1/BTP-Project-2/assets/157860187/13a09b17-32b5-4228-9279-f0c479ced5b9)



## Add Reservation

To update a reservation, send a POST request to `/reservations

![add Reservation Request]


![4](https://github.com/AhmadMashal1/BTP-Project-2/assets/157860187/80419ad9-c06f-42b2-886d-2a3cce9b8b90)

## To See Reservation
To see a reservation, send a get request to `/reservations

![5](https://github.com/AhmadMashal1/BTP-Project-2/assets/157860187/0bb7217d-0cf5-4540-af0b-856891bc832d)


## Update Reservation

To update a reservation, send a PUT request to `/reservations/{id}`.



A successful update will return the following message:


![6](https://github.com/AhmadMashal1/BTP-Project-2/assets/157860187/1e75875f-cb15-4502-b4e3-e4209b1acc78)


## Delete Reservation

To delete a reservation, send a DELETE request to `/reservations/{id}`.

A successful Delete will return the following message:

![7](https://github.com/AhmadMashal1/BTP-Project-2/assets/157860187/6c10a350-e514-4564-8487-9e13cdb2feb9)

