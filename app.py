# standard flask boilerplate

# import the Flask server object
from flask import Flask, request

# create new Flask instance and assign it a root directory of the 
# working file (should be named 'main.py')
app = Flask(__name__)

# routes can be created using @app.route('routeName')
# NOTE: Flask uses Python's decorator syntax so a function must 
# be defined directly beneath the route declaration
@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f"<h2>How did you know I liked {users_dessert}?</h2>"

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return f"{noun} is a {adjective} word!"

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    try:
        result = int(number1) * int(number2)
        return f"{number1} times {number2} is {result}"
    except ValueError:
        return "Invalid inputs. Please try again by entering 2 numbers!"

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    try:
        n = int(n)
        return word * n
    except ValueError:
        return "Invalid input. Please try again by entering a word and a number!"
    
@app.route('/dicegame')
def dicegame():
    import random
    dice_roll = random.randint(1, 6)
    if dice_roll == 6:
        return "You rolled a 6. You won!"
    else:
        return f"You rolled a {dice_roll}. You lost!"

# the server can be accessed in your web browser using the URL localhost:3000/
if __name__ == '__main__':
    app.run(debug=True)

# TODO: Follow the assignment instructions to complete the required routes!
# (And make sure to delete this TODO message when you're done!)
