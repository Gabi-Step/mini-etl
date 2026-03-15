INSERT INTO customers (first_name, last_name, email, status)
VALUES
   ("John", "Doe", "johndoe@email.com", "active"),
   ("Jane", "Doe", "janedoe@email.com", "active"),
   ("Bob", "Smith", "bobsmith@email.com", "inactive"),
   ("Sarah", "Jane", "sarahjane@email.com", "inactive");


INSERT INTO orders (product_name, quantity, price, customer_id)
VALUES
    ("Yorkshire pudding", 2, 11.00, 1),
    ("Sausage roll", 4, 6.00, 1),
    ("Brownie", 1, 2.50, 2),
    ("Can of beans", 4, 2.00, 3);