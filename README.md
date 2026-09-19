# project2
# Student Management REST API

A lightweight **RESTful API** built with **Python and Flask** for managing student records. The project demonstrates the implementation of CRUD operations through standard HTTP methods and JSON-based data exchange.

## Overview

The Student Management REST API provides a simple backend interface for managing student information. It allows users to retrieve, create, update, and delete student records through dedicated API endpoints.

The project is designed to demonstrate fundamental concepts of **Flask, REST API development, HTTP methods, JSON, and CRUD operations**.

## Features

* Retrieve all student records
* Add new students
* Update existing student information
* Delete student records
* JSON-based request and response handling
* RESTful API endpoints
* Simple and lightweight Flask implementation

## Technologies

* **Python**
* **Flask**
* **REST API**
* **JSON**

## Getting Started

### Prerequisites

Make sure **Python** is installed on your system.

### Installation

Clone the repository:


git clone YOUR_REPOSITORY_URL


Navigate to the project directory:
cd student-api

Install Flask:
pip install flask


### Run the Application

Start the Flask development server:


python app.py


The API will be available at:


http://127.0.0.1:5000


## API Usage

### Get All Students

**Request:**

GET /api/students

Returns the list of all available students.

### Add a Student

**Request:**


POST /api/students


**JSON Body:**


{
  "name": "Ahmed",
  "department": "Computer Science",
  "age": 22
}


### Update a Student

**Request:**


PUT /api/students/1


### Delete a Student

**Request:**


DELETE /api/students/1


API requests can be tested using **Postman** or another REST API client.


## Project Purpose

This project was developed to gain practical experience with:

* Flask application development
* RESTful API design
* HTTP methods
* JSON data handling
* CRUD operations
* API testing


## Author

**Iqra Shaukat**
Computer Science Student
