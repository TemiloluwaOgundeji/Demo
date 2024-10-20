from flask import Flask, render_template, request, redirect, url_for, make_response
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the user's guess from the form
        user_guess = request.form.get('guess')
        number_to_guess = request.cookies.get('number_to_guess')

        # Check the user's guess
        if user_guess:
            user_guess = int(user_guess)
            if user_guess < int(number_to_guess):
                result = "Too low! Try again."
            elif user_guess > int(number_to_guess):
                result = "Too high! Try again."
            else:
                result = f"Congratulations! You've guessed the number {number_to_guess}!"
                return redirect(url_for('index', reset=True))

            return render_template('index.html', result=result, number_to_guess=number_to_guess)

    # Generate a random number and set a cookie
    number_to_guess = random.randint(1, 100)
    
    # Create a response object
    response = make_response(render_template('index.html', result="", number_to_guess=number_to_guess))
    
    # Set the cookie
    response.set_cookie('number_to_guess', str(number_to_guess))
    
    return response

if __name__ == '__main__':
    app.run(debug=True)

