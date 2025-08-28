function showTab(tab) {
  document.querySelectorAll('.tab').forEach(t => t.style.display = 'none');
  document.getElementById(tab).style.display = 'block';
}

// API base URL
const API = "http://127.0.0.1:8000";

function generateRecipe() {
  const ingredients = document.getElementById('ingredients').value;
  document.getElementById('recipe-result').textContent = "Generating recipe...";
  fetch(`${API}/generate-recipe`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ingredients})
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById('recipe-result').textContent = data.result || data.detail || "No result.";
  })
  .catch(err => {
    document.getElementById('recipe-result').textContent = 'Error: ' + err;
  });
}

function generateMealPlan() {
  const preferences = document.getElementById('preferences').value;
  const dietary_restrictions = document.getElementById('restrictions').value;
  document.getElementById('meal-result').textContent = "Creating meal plan...";
  fetch(`${API}/meal-plan`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({preferences, dietary_restrictions})
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById('meal-result').textContent = data.result || data.detail || "No result.";
  })
  .catch(err => {
    document.getElementById('meal-result').textContent = 'Error: ' + err;
  });
}

function generateSub() {
  const ingredient = document.getElementById('ingredient').value;
  document.getElementById('sub-result').textContent = "Finding substitutions...";
  fetch(`${API}/substitute`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ingredient})
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById('sub-result').textContent = data.result || data.detail || "No result.";
  })
  .catch(err => {
    document.getElementById('sub-result').textContent = 'Error: ' + err;
  });
}

function toggleMenu() {
  const menu = document.getElementById('dropdownMenu');
  menu.classList.toggle('active');
}

function generateCalories() {
  const foods = document.getElementById('foods').value;
  document.getElementById('calorie-result').textContent = "Estimating calories...";
  fetch(`${API}/calorie-counter`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({foods})
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById('calorie-result').textContent = data.result || data.detail || "No result.";
  })
  .catch(err => {
    document.getElementById('calorie-result').textContent = 'Error: ' + err;
  });
}

