# E-Commerce API

This project is a **Django-based e-commerce platform** with a RESTful API, designed to manage products, shopping carts, orders, and user authentication.

## ⚙️ Technologies Used

- **Python:** for the back-end logic and handling data.
- **HTML:** to create a user-friendly interface.
- **JavaScript:** to enhance interactivity on the front-end.

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

### 👑 Superuser
Superusers have full access to the entire backend through the Django Admin interface.  
They can manage all models, users, and permissions without restrictions.

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

> 📝 **Note for the reviewer**:  
> User roles are managed using Django's built-in group and permission system.

## 🔐 Admin Test Accounts

To test the different roles and their permissions, you can use the following pre-registered accounts:

| Role                | Username      | Password     |
|---------------------|---------------|--------------|
| Superuser           | mattia        | passmat123   |
| Moderator           | gabriele      | passgab123   |
| Product Manager     | filippo       | passfil123   |
| Regular User        | martino       | passmar123   |

## 🧪 How to Test Backend Functionalities

All backend features can be tested by accessing the **Django Admin panel** at http://127.0.0.1:8000/admin using the credentials provided above.
Once logged in, each user will only see the sections and actions permitted by their role.

Please note that **Regular Users do not have access to the backend admin panel** and can only use the frontend features.
Only Superuser, Moderator, and Product Manager accounts have backend access with different permission levels.
