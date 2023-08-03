from flask import Flask, render_template, Blueprint

app = Flask(__name__)

app_bp = Blueprint("app_bp", __name__) # app_bp = name of blueprint

@app_bp.route('/')
def index():
    # return 'Hello World!'
    # return render_template("index.html", mountain="Everest")
    
    mountains = ["Everest", "K2", "Kilimanjaro"]
    return render_template("index.html", mountains=mountains)

@app_bp.route('/mountain/<mt>')
def mountain(mt):
    return "This is " + str(mt)

app.register_blueprint(app_bp)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=2000,debug=True)