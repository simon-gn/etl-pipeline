## ETL Pipeline with Visual Sales Dashboard (WIP)

### Overview
This project is an **ETL pipeline** that processes and visualizes sales data, providing insights through a sleek and interactive dashboard. It is built using modern technologies including **Flask** (Backend), **React** (Frontend), and is hosted on **AWS** to leverage cloud infrastructure.

### Key Features
- **Backend (Flask)**: The backend is built using Flask, providing an API that handles data processing, database interactions, and more.
- **Frontend (React)**: The frontend is a modern React application that communicates with the backend API to visualize data and present it in a user-friendly manner.
- **Database (PostgreSQL)**: The project uses **PostgreSQL** hosted on AWS for storing and querying the processed data.

### Recent Updates
- **Dockerization**: The entire project (both the frontend and backend) has been containerized using **Docker**. This enables easy deployment, scaling, and consistency across environments by encapsulating the application into isolated containers.
  
- **AWS Deployment**: The project has been deployed on **AWS Cloud** using **Amazon ECS (Elastic Container Service)** and **AWS Fargate**, which ensures that both the backend and frontend containers are run in a fully managed, serverless environment. This allows for seamless scaling and management of the containers in production.

- **CI/CD Pipeline**: A **CI/CD pipeline** has been set up using **GitHub Actions**. This pipeline automates the process of building, testing, and deploying the application to AWS every time changes are pushed to the `main` branch. It integrates **Docker**, **Amazon ECR (Elastic Container Registry)** for image storage, and **Amazon ECS** for container orchestration, providing a fully automated and smooth deployment process.

### Technologies Used:
- **Backend**: Flask, Python
- **Frontend**: React, Nginx
- **Database**: PostgreSQL (hosted on AWS RDS)
- **Cloud Infrastructure**: AWS (ECS, ECR, Fargate, RDS)
- **Containerization**: Docker
- **CI/CD**: GitHub Actions, AWS

### How It Works:
1. **ETL Pipeline**: 
    - Data is extracted from a source (CSV files for now).
    - The data is transformed, cleaned, and processed in the backend.
    - The data is loaded into the PostgreSQL database, ready to be queried.
   
2. **Frontend Dashboard**: 
    - The React frontend fetches data from the Flask backend and presents the processed sales data through charts and graphs.
    - The dashboard is interactive and will allow users to filter and visualize the data based on various parameters in the near future.

3. **Docker & AWS Deployment**:
    - Both the backend and frontend are Dockerized and pushed to **Amazon ECR**.
    - The containers are deployed to **AWS ECS** using **Fargate** for automated scaling and management.
  
4. **CI/CD**:
    - GitHub Actions automates the entire process of building the Docker images, pushing them to ECR, and deploying the updated containers to ECS whenever changes are made to the codebase.

### Future Improvements:
- **Data Pipeline Enhancements**: Expand the ETL pipeline with more data sources, transformation capabilities, and complex data processing tasks.
- **User Authentication**: Add user authentication and role-based access control to the dashboard for different users.
- **Real-time Data**: Implement real-time data updates and visualizations in the frontend dashboard.


<p>&nbsp;</p>

<img src="./client/images/Dashboard.png" alt="Dashboard preview" />
