from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/<num>")
def nNumbers(num: int):
    try:
        if int(num) < 1:
            return "<p>Oops! This function only returns numbers greater than or equal to 1.</p>"
        return render_template('n_numbers.html', n = int(num))
    except ValueError:
        return "<p>Oops! Passed value is not an int.</p>"

@app.route("/<num>/odd")
def oddNumbers(num: int):
    try:
        if int(num) < 1:
            return "<p>Oops! This function only returns numbers greater than or equal to 1.</p>"
        return render_template('odd_numbers.html', n = int(num))
    except ValueError:
        return "<p>Oops! Passed value is not an int.</p>"


@app.route("/<num>/even")
def evenNumbers(num: int):
    try:
        if int(num) < 1:
            return "<p>Oops! This function only returns numbers greater than or equal to 1.</p>"
        return render_template('even_numbers.html', n = int(num))
    except ValueError:
        return "<p>Oops! Passed value is not an int.</p>"


@app.route("/<num>/prime")
def primeNumbers(num: int):
    try:
        if int(num) < 1:
            return "<p>Oops! This function only returns numbers greater than or equal to 1.</p>"
        if int(num) == 1:
            return "<p>No prime numbers in this range.</p>"
        
        numInt = int(num)
        primes = [1] * (numInt+1)
        primes[0] = primes[1] = 0

        for i in range(2, int((numInt+1)**0.5)+1):
            if primes[i]:
                lowerbound = i**2
                while lowerbound < numInt+1:
                    primes[lowerbound] = 0
                    lowerbound += i

        return render_template('prime_numbers.html', primes = primes, n = numInt)
    except ValueError:
        return "<p>Oops! Passed value is not an int.</p>"
    

if __name__ == "__main__":
    app.run(debug=True)