# RESTFUL-API-DEVELOPMENT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: SHASHANKSARAN R

*INTERN ID*: CT4MVTZ

*DOMAIN*: SOFTWARE DEVELOPMENT

*DURATION*: 4 MONTHS (16 WEEKS)

*MENTOR*: NEELA SANTOSH


# 🧾 Inventory Management System

A responsive web-based inventory dashboard designed to manage stock items, allowing users to add, update, and delete products with an intuitive interface. Built using modern web development practices and styled with Bootstrap for an elegant, user-friendly experience.

---

## 📌 Description

The **Inventory Management System** provides a simple yet powerful interface to track product data including item name, quantity, and price. The system dynamically interacts with a backend API to display data and perform CRUD operations in real time. It includes client-side validation, responsive design, and loading indicators to enhance the user experience.

---

## 🔧 Tools and Technologies Used

### Frontend:

- HTML5
- CSS3
- JavaScript (ES6)
- Bootstrap 5

### Backend:

- FastAPI (Postman API)

---

## ✨ Key Features

- 🚀 **Add, update, and delete inventory items**
  
- 🔒 **Prevents negative quantity or price entries**
  
- ⚡ **AJAX-based interaction with the backend API**
  
- 📱 **Fully responsive design**
  
- 🔄 **Loading spinners and toast notifications for feedback**
  
- 🧼 **Client-side form validation**
  
- 🧠 **Reusable modal form for editing items**

---

## 🎨 Design Philosophy

- **Clean and Minimal UI**: Focused on clarity and usability with gentle colors and shadows.
  
- **Responsive First**: Designed to work across all screen sizes using Bootstrap's grid system.
  
- **Component Reuse**: Modal-based editing and dynamic table rendering promote clean code practices.
  
- **Feedback-Centric**: Real-time feedback via toast alerts and loading spinners for better UX.

---

## 🛠️ Steps to Run the Project

### 1. Clone the Repository

git clone https://github.com/shashanksaranr/restful-api-development.git

cd restful-api-development

### 2. Start the Backend API (if not already running)

A. If you're using FastAPI:

    uvicorn main:app --reload

B. If you're using Django REST Framework:

    python manage.py runserver
    
    Ensure your API is running at http://127.0.0.1:8000


## 🔌 API Endpoints

| Method | Endpoint       | Description             |
|--------|----------------|-------------------------|
| GET    | `/items/`      | Get all inventory items |
| POST   | `/items/`      | Add a new item          |
| PUT    | `/items/{id}`  | Update item by ID       |
| DELETE | `/items/{id}`  | Delete item by ID       |


## Output

1. Inventory Management Dashboard:

  <img width="1728" alt="Image" src="https://github.com/user-attachments/assets/df575e5e-7c0c-469e-954a-46e62b7b2be1" />


2. Adding List/s:

  <img width="1728" alt="Image" src="https://github.com/user-attachments/assets/e869a8b6-7b95-4463-82ef-3bf482750e55" />


3. View List/s:

  <img width="1728" alt="Image" src="https://github.com/user-attachments/assets/b58b9f11-cc2c-40e0-addf-be6d52adc337" />


4. Update List:

 <img width="1728" alt="Image" src="https://github.com/user-attachments/assets/cdee4218-9b0b-440a-b9cd-41d99ce757c2" />


5. Delete List/s:

 <img width="1728" alt="Image" src="https://github.com/user-attachments/assets/f5cc1044-27ac-409b-805a-3d9b74fab8cf" />




