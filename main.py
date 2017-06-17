from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

# form served to user (browser); method name (e.g. "POST") can be all caps or all lowercase
form = """
<!DOCTYPE html>
<html>
    <body>
        <form action="/hello" method="POST">
            <label for="first_name">First Name: </label>
            <input id="first_name" type="text" name="first_name" />
            <input type="submit" />
        </form>
    </body>
</html>
"""

# index (page) handler - what to serve when user (browser) goes to index.html at route / (root file of website)
@app.route("/")
def index():
    return form

# form handler - how to handle input from form
@app.route("/hello", methods=['POST'])  # can include 'GET' or any number of other methods
def hello():
    first_name = request.form["first_name"]  # need to use request.form for POST methods; argument is dictionary-like object, so in square brackets
    return "<h1>Hello, " + first_name + "</h1>"  # html is coded as TEXT here, like in JQuery writing to the DOM

app.run()
