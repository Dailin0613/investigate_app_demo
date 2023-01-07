from flask import Blueprint, jsonify, request
from models.TeamModels import TeamModel
from models.entities.Team import Team
import uuid

main = Blueprint('team_bp', __name__)


@main.route('/')
def index():
    try:
        teams = TeamModel.get_team()
        return jsonify(teams)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.post('/add')
def create():
    try:
        id = uuid.uuid4()
        name = request.form.get('name')
        objective = request.form.get('objective')
        description = request.form.get('description')
        goal = request.form.get('goal')
        team = Team(str(id), name, objective, description, goal)

        affected_rows = TeamModel.add_team(team)

        if affected_rows == 1:
            return jsonify(team.name)
        else:
            return jsonify({'message': 'Error in insert'}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.delete('/delete/<id>')
def delete(id):
    try:
        team = Team(str(id))

        affected_rows = TeamModel.delete_team(team)

        if affected_rows == 1:
            return jsonify(team.id)
        else:
            return jsonify({'message': 'Error in delete'}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.put('/update/<id>')
def update(id):
    try:
        name = request.form.get('name')
        objective = request.form.get('objective')
        description = request.form.get('description')
        goal = request.form.get('goal')
        team = Team(id, name, objective, description, goal)

        affected_rows = TeamModel.update_team(team)

        if affected_rows == 1:
            return jsonify(team.id)
        else:
            return jsonify({'message': 'Error in updated'}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
