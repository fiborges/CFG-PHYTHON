import requests
import webbrowser
import random

APP_ID = "4026e5c2"
APP_KEY = "a3af67a4e3f0980b1b048f3c1dd795f5"

def recipe_search(ingredient):
    url = f'https://api.edamam.com/search?q={ingredient}&app_id={APP_ID}&app_key={APP_KEY}'
    result = requests.get(url)
    data = result.json()
    return data['hits']

def welcome_animation():
    print(r'''
             .---. .---. 
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.    
   .'   "   '  "  .    "  . '  "  `.  
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.
      .'`-._'    " .     " _.-'`. :       o  :
    .'      ```--.....-----    ' `:_ o       :
  .'    "     '         "     "   ; `.;";";";'
 ;         '       "       '     . ; .' ; ; ;
;     '         '       '   "    .'      .-'
'  "     "   '      "           "    _.-'
                                  ''''')


def display_recipe(recipe):
    print(f"Recipe: {recipe['label']}")
    print(f"URI: {recipe['uri']}")
    print()

def display_detailed_recipe(recipe):
    print(f"\033[1m\033[92mRECIPE: \033[0m {recipe['label']}")
    print(f"\033[1m\033[92mURI: \033[0m {recipe['uri']}")
    print(f"\033[1m\033[92mYIELD: \033[0m {recipe['yield']}")
    print(f"\033[1m\033[92mCALORIES: \033[0m {recipe['calories']:.2f} kcal")

    # Display Ingredients in Bold
    print("\n\033[1m\033[92mIngredients:\033[0m")
    for ingredient in recipe['ingredientLines']:
        print(f"- {ingredient}")
    
    print("\n \033[1m\033[92mHealth Labels:\033[0m", ", ".join(recipe['healthLabels']))
    print("\n")
    
    # Display additional nutrition information
    print("\033[1m\033[32mNutrition Information:\033[0m")
    for nutrient, value in recipe['totalNutrients'].items():
        print(f"- {nutrient}: {value['quantity']:.2f} {value['unit']}")

    print()

def main():
    welcome_animation()
    ingredient = input("\033[1m\033[95mEnter an ingredient to search for: \033[0m \n")
    results = recipe_search(ingredient)

    save_to_file = input("\033[1m\033[95mDo you want to save the results to a file? (yes/no): \033[0m \n").lower() == "yes"
    if save_to_file:
        with open("recipe_results.txt", "w") as file:
            for result in results:
                recipe = result['recipe']
                file.write(f"Recipe: {recipe['label']}\n")
                file.write(f"URI: {recipe['uri']}\n")
                file.write("\n")

    order_by_calories = input("\033[1m\033[34mDo you want to order results by calories? (yes/no): \033[0m").lower() == "yes"
    if order_by_calories and results:
        results = sorted(results, key=lambda x: x['recipe']['calories'])

    print("\n\033[1m\033[95mSearch Results:\033[0m")
    for index, result in enumerate(results, start=1):
        recipe = result['recipe']
        calories = recipe['calories']
        print(f"\033[1m\033[91m{index}.\033[0m \033[1m\033[94mCalories:\033[0m {calories:.2f} kcal : \n {recipe['label']}")

    choice = int(input("\033[1m\033[95mSelect a recipe by entering its number: \033[0m"))
    if 1 <= choice <= len(results):
        selected_recipe = results[choice - 1]['recipe']
        display_detailed_recipe(selected_recipe)
    else:
        print("\033[1m\033[91mInvalid choice.\033[0m")

    show_random_suggestion = input("\033[1m\033[95mDo you want to see a random recipe suggestion? (yes/no): \033[0m").lower() == "yes"
    print("\n")
    if show_random_suggestion and results:
        random_recipe = random.choice(results)['recipe']
        print("\n\033[1m\033[95mRandom Recipe Suggestion:\033[0m")
        print("\n")
        display_recipe(random_recipe)

    filter_by_diet = input("\033[1m\033[95mDo you want to filter results by diet label? (yes/no): \033[0m").lower() == "yes"
    print("\n")
    if filter_by_diet and results:
        diet_label = input("\033[1m\033[95mEnter the diet label (e.g., vegetarian, vegan, gluten-free): \033[0m").lower()
        print("\n")
        filtered_results = [result for result in results if diet_label in result['recipe']['dietLabels']]
        if filtered_results:
            print("\n\033[1m\033[95mFiltered Results:\033[0m")
            for index, result in enumerate(filtered_results, start=1):
                print(f"{index}. {result['recipe']['label']} (Diet Labels: {', '.join(result['recipe']['dietLabels'])})")
        else:
            print("\033[91mNo recipes match the specified diet label.\033[0m")
            print("\n")
    
    open_link = input("\033[1m\033[95mDo you want to open the recipe link in your browser? (yes/no): \033[0m").lower() == "yes"
    if open_link and selected_recipe:
        webbrowser.open(selected_recipe['url'])
        print("\033[93mOpening recipe link in your default web browser...\033[0m")
        print("\n")

if __name__ == "__main__":
    main()



