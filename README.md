# 🍳 NutriChef Pro

NutriChef Pro is an **AI-powered recipe generator and meal planner** designed to help users create personalized meal plans based on their preferences, dietary restrictions, and nutritional goals.  
It uses **OpenAI** for recipe generation, wrapped inside a modern **FastAPI backend** with a clean **HTML/CSS/JavaScript frontend**.  

---

## 🚀 Features

- 🥗 **Personalized Recipes** – Generate recipes tailored to user preferences.  
- 📅 **Meal Planning** – Create day/week-based meal plans.  
- 🔎 **Ingredient-based Search** – Get recipes using available ingredients.  
- ⚡ **FastAPI Backend** – Handles requests efficiently.  
- 🌐 **Frontend Interface** – Simple and intuitive UI (HTML, CSS, JS).  
- 🐳 **Docker Support** – Containerized for easy deployment.  

---

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)  
- **Frontend:** HTML, CSS, JavaScript  
- **AI Model:** OpenAI (GPT)  
- **Containerization:** Docker  
- **Deployment-ready:** Can be hosted on any cloud or local server  

---

## 📂 Project Structure

```bash
NutriChef/
│── backend/
│   ├── main.py          # FastAPI app
│   ├── requirements.txt # Dependencies
│   ├── Dockerfile       # Backend Docker config
│
│── frontend/
│   ├── index.html       # Main UI
│   ├── style.css        # Styling
│   ├── script.js        # Client-side logic
│
│── docker-compose.yml   # Multi-container setup (if used)
│── README.md            # Project documentation
