from fastapi import FastAPI, HTTPException
from .p2 import RecipePlanner
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
planner = RecipePlanner()

# Allow CORS for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RecipeRequest(BaseModel):
    ingredients: str

class MealPlanRequest(BaseModel):
    preferences: str
    dietary_restrictions: str = None

class SubstituteRequest(BaseModel):
    ingredient: str

class CalorieCounterRequest(BaseModel):
    foods: str

@app.post("/generate-recipe")
def generate_recipe(req: RecipeRequest):
    try:
        result = planner.generate_recipe(req.ingredients)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/meal-plan")
def meal_plan(req: MealPlanRequest):
    try:
        result = planner.create_meal_plan(req.preferences, req.dietary_restrictions)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/substitute")
def substitute(req: SubstituteRequest):
    try:
        result = planner.suggest_substitutions(req.ingredient)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/calorie-counter")
def calorie_counter(req: CalorieCounterRequest):
    try:
        result = planner.calorie_counter(req.foods)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def read_root():
    return {"message": "AI Recipe Generator API is running."} 