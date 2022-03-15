from flask_app import app

# from flask import Flask, session

from flask_app.controllers import emails




if __name__ == "__main__":
    app.run(debug=True)