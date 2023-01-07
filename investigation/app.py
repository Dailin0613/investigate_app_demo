import app
from flask import Flask, request, jsonify, render_template
from routes import Team, Project

app = Flask(__name__)

def page_not_found(error):
    return render_template('not_found.html'), 404

if __name__ == '__main__':
    app.register_error_handler(404, page_not_found)
    app.register_blueprint(Team.main, url_prefix='/team')
    app.register_blueprint(Project.sec, url_prefix='/project')

    app.run(debug=True)