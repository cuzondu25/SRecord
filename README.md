# Your Ultimate Sales Management Solution
![img5](https://github.com/cuzondu25/SRecord/assets/113671308/8ad3b735-f25e-40ac-bacc-59e26c351d2b)

## Introduction
SRecord is a full-stack web application designed to help small businesses track daily sales and generate weekly sales reports. The application provides a simple yet powerful tool to manage sales data efficiently, offering secure user authentication, easy sales entry, and detailed weekly reports.

### Deployed Site: [SRecord Live](https://s-record-three.vercel.app/)

### Final Project Blog Article: [SRecord Project Blog](https://www.linkedin.com/pulse/automating-small-business-sales-tracking-srecord-project-uzondu-ebube-avtcf)

### Authors LinkedIn:
* [Uzondu Chidiebube](https://www.linkedin.com/in/uzondu-ebube-739472108)

## Installation 
### Prerequisites
* Node.js
* npm
* Python 3.x
* PostgreSQL

## Backend Setup
Clone the repository:
```
git clone https://github.com/cuzondu25/SRecord.git
cd SRecord
```
Set up a virtual environment:
```
python3 -m venv srec
source srec/bin/activate
```
Install backend dependencies:
```
pip install -r requirements.txt
```
Set up PostgreSQL database:
```
CREATE DATABASE srecord_db;
```
Configure the database connection in config.py:
```
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/srecord_db'
```
Run the backend server:
```
flask run  # python run.py
```
## Frontend Setup
Navigate to the frontend directory:
```
cd srecord-frontend
```
Install frontend dependencies:
```
npm install
```
Run the frontend development server:
```
npm start
```
## Usage
* Register a new user account on the SRecord Live:
* Log in with your registered account.
* Navigate to the Sales Entry page to submit daily sales data.
* View the Weekly Report page to see detailed sales reports.
<picture>
  <img width='65%, center' src='https://github.com/cuzondu25/SRecord/assets/113671308/2e61a35e-2299-4fa5-a974-5bfee8c5e826' />
</picture>

## Contributing
We welcome contributions from the community. To contribute, please follow these steps:
* Fork the repository.
* Create a new branch for your feature or bugfix.
* Commit your changes with descriptive messages.
* Push your changes to your forked repository.
* Create a pull request with a detailed description of your changes.
## Related Projects
Here are some related projects that might interest you:
* Sales Tracker
* Weekly Sales Reports
* Sales Management System
## Licensing
This project is licensed under the MIT License.

