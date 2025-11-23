# Business Management System

A comprehensive Business Management Software built with Python (CustomTkinter) and MySQL. This application is designed to manage Inventory, Sales (POS), HR, and User Roles for a small to medium-sized business.

## Features
- **Inventory Management**: Add, update, delete, and view products.
- **Sales / POS**: Process sales, manage cart, and automatically deduct stock.
- **HR & Payroll**: Manage employee records and details.
- **User Management**: Admin-controlled user creation with role-based access (Admin, Manager, Staff).
- **Authentication**: Secure login system.

## Tech Stack
- **Frontend**: Python (CustomTkinter)
- **Backend**: Python
- **Database**: MySQL

## Prerequisites
- Python 3.x
- MySQL Server

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd "directory of the file saved"
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**:
   - Create a file named `.env` in the root directory.
   - Add your MySQL credentials:
     ```env
     DB_HOST=localhost
     DB_USER=root
     DB_PASSWORD=your_password
     DB_NAME=business_mgmt_db
     ```
   - Run the initialization script to create tables:
     ```bash
     python init_db.py
     ```

## Usage
Run the main application:
```bash
python main.py
```

## Login Credentials (Default)
- **Username**: `admin`
- **Password**: `admin123`
