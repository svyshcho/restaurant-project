"# restaurant-project" 

Models -> 
![img.png](..%2Fdjango-restaurant-service%2Fimg.png)<img src="im">

Project Description:

Culinary Forum is an innovative online platform for all those interested in culinary arts.
The project offers the opportunity to register and interact as a cook, to add, modify, and exchange recipes of dishes.
Additionally, users can search for recipes, view their details, and even choose the most delectable ideas for cooking.


Key Features:

Registration and login: Users can create an account on the platform by choosing the role of a chef or be an unauthorized user interested in the culinary arts.

Recipe Submission: Registered cooks have the ability to add their favorite recipes for dishes. They can specify the name, ingredients, preparation description, and other important details.

Recipe Editing: Cooks can modify the recipes they've added in case of any necessary adjustments or the addition of new informational sections.

Search and Viewing of Recipes: All users, including regular individuals, can search for recipes using dish names. After finding a recipe, users can thoroughly explore it.


Guide how I can set up and run your project locally:
1. git clone
2. Open that project in your IDE
3. Create virtual environment: 
   Run command in your terminal:
   python -m venv venv
   venv\Scripts\activate
   pip install -r requiremetns.txt
4. Also, You should run makemigrations to generate the migration files based on 
   your model changes and then run migrate to apply those changes to the database. This ensures 
   that your database schema is updated according to the changes you made to your models.
   run this commands: python manage.py makemigrations, python manage.py migrate
5. Run coomand -> python manage.py runserver

How to use the .env:
You need to create an .env file where you will write all the fields that are in the .env_sample file. 
