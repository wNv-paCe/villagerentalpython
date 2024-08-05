# Village Rentals Application

## Project Overview
This is a Tkinter-based graphical user interface (GUI) application for managing rental equipment and customer information. The application connects to a MySQL database to store and retrieve data.

## Prerequisites
- Python installed
- MySQL database installed and running

## Install Dependencies
1. Install the `mysql-connector-python` library:
   ```bash
   pip install mysql-connector-python
   ```

## Database Initialization
1.	Start your MySQL server and ensure it is running.
   - Starting and Stoping MySQL Service
      - #### On Windows
         To start the MySQL Service:
         ```bash
         net start mysql
         ```

         To stop the MySQL Service:
         ```bash
         net stop mysql
         ```

      - #### On MacOS
         To start the MySQL Service:
         ```bash
         brew services start mysql
         ```

         To stop the MySQL Service:
         ```bash
         brew services stop mysql
         ```

2.	Manually run the following commands to initialize the database and insert initial data:
    ```bash
    mysql -u root -p < init_data.sql
    ```
    ```bash
    mysql -u root -p < insert_data.sql
    ```