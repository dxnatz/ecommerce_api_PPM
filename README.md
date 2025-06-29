# E-Commerce API

This project is a **Django-based e-commerce platform** with a RESTful API, designed to manage products, shopping carts, orders, and user authentication.

## ⚙️ Technologies Used

- Django 4.2
- Django REST Framework
- Simple JWT for authentication
- SQLite (pre-populated for demo purposes)
- Python 3.9

## 🔐 Authentication

Authentication is handled via **JSON Web Tokens (JWT)** using `SimpleJWT`.

## 🛒 Available Features

### 🛍️ Frontend (public API usage)

- User registration and login
- Product listing
- Add products to cart
- Checkout and place orders

### 🛠️ Backend (admin panel)

Available through the Django Admin interface:

- Add / edit / delete products  
- Manage discounts on products  
- Add / edit / delete orders and order items  
- Add / edit / delete carts and cart items  
- Add / edit / delete users  
- Assign or remove user roles (e.g., moderators, product managers)  
- Ban / unban users  
- Full access to all data and models

## 👥 User Roles and Permissions

### 🛡️ Moderator
Moderators have access to:

- View all products and users  
- Add, edit, and delete:
  - Orders  
  - Order items  
  - Carts  
  - Cart items

### 📦 Product Manager
Product managers have access to:

- View all orders, order items, carts, cart items, and users
- Add, edit, and delete:
  - Products
 
### 👑 Superuser
Superusers have full access to the entire backend through the Django Admin interface.  
They can manage all models, users, and permissions without restrictions.

> 📝 **Note for the reviewer**:  
> User roles are managed using Django's built-in group and permission system.
