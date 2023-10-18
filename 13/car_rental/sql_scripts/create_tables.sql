CREATE TABLE Cars (
    car_id INTEGER PRIMARY KEY,
    make TEXT,
    model TEXT,
    year INTEGER,
    status TEXT -- Available, Rented, Maintenance
);

CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    license_number TEXT UNIQUE,
    email TEXT UNIQUE
);

CREATE TABLE Rentals (
    rental_id INTEGER PRIMARY KEY,
    car_id INTEGER,
    customer_id INTEGER,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY(car_id) REFERENCES Cars(car_id),
    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Maintenance (
    maintenance_id INTEGER PRIMARY KEY,
    car_id INTEGER,
    description TEXT,
    date DATE,
    FOREIGN KEY(car_id) REFERENCES Cars(car_id)
);