-- Create database and tables for villagerentals
CREATE DATABASE IF NOT EXISTS villagerentals;

-- Using the database
USE villagerentals;

-- Drop tables if they exist
DROP TABLE IF EXISTS rentalinfo;
DROP TABLE IF EXISTS rentalequipment;
DROP TABLE IF EXISTS customerinfo;
DROP TABLE IF EXISTS category;

-- Create category table
CREATE TABLE IF NOT EXISTS category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL
);

-- Create customerinfo table
CREATE TABLE IF NOT EXISTS customerinfo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    contact_phone VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

-- Create rentalequipment table
CREATE TABLE IF NOT EXISTS rentalequipment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT,
    equipment_name VARCHAR(255) NOT NULL,
    description TEXT,
    daily_rate DECIMAL(10, 2),
    FOREIGN KEY (category_id) REFERENCES category(id)
);

-- Create rentalinfo table
CREATE TABLE IF NOT EXISTS rentalinfo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    equipment_id INT,
    date DATE,
    rental_date DATE,
    return_date DATE,
    cost DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customerinfo(id),
    FOREIGN KEY (equipment_id) REFERENCES rentalequipment(id)
);