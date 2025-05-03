📘 Inventory Management System – API Documentation

📌 Overview
This API allows users to manage inventory items with the ability to create, read, update, and delete (CRUD) inventory records.

⚙️ Base URL
http://127.0.0.1:8000

📦 Endpoints

🔍 GET /items/
Description: Retrieve all inventory items.

Response:
[
  {
    "id": 1,
    "name": "Laptop",
    "quantity": 5,
    "price": 45000.00
  }
]

➕ POST /items/
Description: Add a new inventory item.

Request Body:
{
  "name": "Mouse",
  "quantity": 10,
  "price": 500.00
}

Constraints:

quantity must be ≥ 0

price must be ≥ 0

Response:
{
  "id": 2,
  "name": "Mouse",
  "quantity": 10,
  "price": 500.00
}

🔄 PUT /items/{id}
Description: Update an existing inventory item.

Request Body:
{
  "name": "Wireless Mouse",
  "quantity": 15,
  "price": 600.00
}

Response:
{
  "id": 2,
  "name": "Wireless Mouse",
  "quantity": 15,
  "price": 600.00
}

❌ DELETE /items/{id}
Description: Delete an inventory item by its ID.

Response:
{
  "message": "Item deleted successfully"
}

🛠️ Validation Rules

Field	Rule
-----------------------------------|
name	|Required, non-empty string|
quantity|	Must be ≥ 0            |
price	|Must be ≥ 0               |
-----------------------------------|
