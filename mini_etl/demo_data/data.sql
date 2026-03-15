INSERT INTO customers (first_name, last_name, email)
VALUES
   ("John", "Doe", "johndoe@email.com"),
   ("Jane", "Doe", "janedoe@email.com"),
   ("Bob", "Smith", "bobsmith@email.com");


INSERT INTO orders (product_name, quantity, price, customer_id)
VALUES
    ("Yorkshire pudding", 2, 11.00, 1),
    ("Brownie", 1, 2.50, 2),
    ("Can of beans", 4, 2.00, 3);