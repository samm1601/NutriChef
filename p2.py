from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv
from pathlib import Path
import json

# Load environment variables from multiple likely locations
# 1) Current working directory (default)
load_dotenv()
# 2) Directory of this file: NutriChef/
_this_dir = Path(__file__).resolve().parent
load_dotenv(_this_dir / ".env")
# 3) Project root: one level up from NutriChef/
load_dotenv(_this_dir.parent / ".env")

# Validate presence of the OpenAI key early for clearer errors
if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError(
        "OPENAI_API_KEY not found. Add it to a .env in project root or NutriChef/."
    )

class RecipePlanner:
    def __init__(self):
        self.llm = ChatOpenAI(temperature=0.7)
        self.memory = ConversationBufferMemory(memory_key="chat_history")
        
    def generate_recipe(self, ingredients):
        """Generate a recipe based on available ingredients"""
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a professional chef and nutritionist. 
            Create a detailed recipe using the provided ingredients.
            Include:
            1. Recipe name
            2. Ingredients list with quantities
            3. Step-by-step instructions
            4. Cooking time
            5. Servings
            6. Nutritional information per serving, including total calories per serving (make calories prominent)
            Format the response in a clear, structured way."""),
            ("human", "Here are the ingredients I have: {ingredients}")
        ])
        
        chain = LLMChain(llm=self.llm, prompt=prompt)
        response = chain.invoke({"ingredients": ingredients})
        return response['text']
    
    def create_meal_plan(self, preferences, dietary_restrictions=None):
        """Create a weekly meal plan"""
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a meal planning expert. 
            Create a weekly meal plan based on the preferences and restrictions provided.
            Include:
            1. Breakfast, lunch, and dinner for each day, with calories for each meal (make calories prominent)
            2. Snack suggestions
            3. Shopping list
            4. Nutritional goals (including total daily calories)
            Format the response in a clear, structured way."""),
            ("human", "Preferences: {preferences}\nDietary Restrictions: {dietary_restrictions}")
        ])
        
        chain = LLMChain(llm=self.llm, prompt=prompt)
        response = chain.invoke({
            "preferences": preferences,
            "dietary_restrictions": dietary_restrictions or "None"
        })
        return response['text']
    
    def suggest_substitutions(self, ingredient):
        """Suggest ingredient substitutions"""
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a culinary expert. 
            Suggest possible substitutions for the given ingredient.
            Include:
            1. Multiple substitution options
            2. Ratio/quantity adjustments
            3. Flavor profile changes
            4. Dietary considerations
            Format the response in a clear, structured way."""),
            ("human", "I need a substitution for: {ingredient}")
        ])
        
        chain = LLMChain(llm=self.llm, prompt=prompt)
        response = chain.invoke({"ingredient": ingredient})
        return response['text']

    def calorie_counter(self, foods):
        """Ask GPT to estimate calories for a list of foods/ingredients."""
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a nutrition expert. For each food or ingredient provided, estimate the calories as accurately as possible. 
            If you are unsure, make your best guess and state that it is an estimate. 
            For each item, provide:
            - Food name
            - Estimated calories per typical serving (state the serving size)
            - A short note if the estimate is rough
            At the end, provide the total estimated calories for all items combined.
            Format the response in a clear, structured way."""),
            ("human", "Foods/Ingredients: {foods}")
        ])
        chain = LLMChain(llm=self.llm, prompt=prompt)
        response = chain.invoke({"foods": foods})
        return response['text']

def main():
    planner = RecipePlanner()
    
    print("\nWelcome to the AI Recipe Generator & Meal Planner!")
    print("------------------------------------------------")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Generate a recipe from ingredients")
        print("2. Create a weekly meal plan")
        print("3. Get ingredient substitutions")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            ingredients = input("\nEnter your ingredients (comma-separated): ")
            print("\nGenerating recipe...")
            recipe = planner.generate_recipe(ingredients)
            print("\n" + recipe)
            
        elif choice == "2":
            preferences = input("\nEnter your food preferences: ")
            restrictions = input("Enter any dietary restrictions (or press Enter for none): ")
            print("\nCreating meal plan...")
            meal_plan = planner.create_meal_plan(preferences, restrictions)
            print("\n" + meal_plan)
            
        elif choice == "3":
            ingredient = input("\nEnter the ingredient you want to substitute: ")
            print("\nFinding substitutions...")
            substitutions = planner.suggest_substitutions(ingredient)
            print("\n" + substitutions)
            
        elif choice == "4":
            print("\nThank you for using the AI Recipe Generator & Meal Planner!")
            break
            
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
