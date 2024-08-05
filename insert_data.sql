-- using the database
USE villagerentals;

-- Drop tables if they exist
DELETE FROM rentalinfo;
DELETE FROM rentalequipment;
DELETE FROM customerinfo;
DELETE FROM category;

-- insert initial data into category table
INSERT INTO category (id, category_name) VALUES 
(10, 'Power tools'), 
(20, 'Yard equipment'), 
(30, 'Compressors'), 
(40, 'Generators'), 
(50, 'Air Tools');

-- insert initial data into customerinfo table
INSERT INTO customerinfo (id, last_name, first_name, contact_phone, email) VALUES
(1001, 'Doe', 'John', '(555) 555-1212', 'jd@sample.net'), 
(1002, 'Smith', 'Jane', '(555) 555-3434', 'js@live.com'), 
(1003, 'Lee', 'Michael', '(555) 555-5656', 'ml@sample.net');

-- insert initial data into rentalequipment table
INSERT INTO rentalequipment (id, category_id, equipment_name, description, daily_rate) VALUES 
(101, 10, 'Hammer drill', 'Powerful drill for concrete and masonry', 25.99), 
(201, 20, 'Chainsaw', 'Gas-powered chainsaw for cutting wood', 49.99), 
(202, 20, 'Lawn mower', 'Self-propelled lawn mower with mulching function', 19.99), 
(301, 30, 'Small Compressor', '5 Gallon Compressor-Portable', 14.99), 
(501, 50, 'Brad Nailer', 'Brad Nailer. Requires 3/4 to 1 1/2 Brad Nails', 10.99);

-- insert initial data into rentalinfo table
INSERT INTO rentalinfo (id, customer_id, equipment_id, date, rental_date, return_date, cost) VALUES 
(1000, 1001, 201, '2024-02-15', '2024-02-20', '2024-02-23', 149.97), 
(1001, 1002, 501, '2024-02-16', '2024-02-21', '2024-02-25', 43.96);