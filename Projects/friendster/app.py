# Friendster Application
from flask import Flask

application_name = "Friendster"
version = "1.0"

welcome_message = "Welcome to the {}. Version v{}!".format(application_name, version)

app = Flask(__name__)

@app.route("/")
def index():
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Friendster</title>
</head>
<body>
    <h1>{welcome_message}</h1>
</body>
</html>
"""

@app.route("/about")
def about():
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>Friendster</title>
</head>
<body>
    <h1>About page</h1>
</body>
</html>
"""

if __name__ == "__main__":
    print(welcome_message)
    app.run()