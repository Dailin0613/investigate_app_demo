from flask import Blueprint, jsonify, request
from models.ProjectModels import ProjectModel
from models.entities.Project import Project
import uuid

sec = Blueprint('project_bp', __name__)


@sec.route('/')
def index():
    try:
        projects = ProjectModel.get_project()
        return jsonify(projects)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@sec.post('/add')
def create():
    try:
        id = uuid.uuid4()
        team_name = request.form.get('team_name')
        name = request.form.get('name')
        description = request.form.get('description')
        objective = request.form.get('objective')
        problem = request.form.get('problem')
        hypothesis = request.form.get('hypothesis')
        project = Project(str(id), team_name, name, objective, description, problem, hypothesis)

        affected_rows = ProjectModel.add_project(project)

        if affected_rows == 1:
            return jsonify(project.name)
        else:
            return jsonify({'message': 'Error in insert'}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@sec.delete('/delete/<id>')
def delete(id):
    try:
        project = Project(str(id))

        affected_rows = ProjectModel.delete_project(project)

        if affected_rows == 1:
            return jsonify(project.id)
        else:
            return jsonify({'message': 'Error in delete'}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@sec.put('/update/<id>')
def update(id):
    try:
        team_name = request.form.get('team_name')
        name = request.form.get('name')
        description = request.form.get('description')
        objective = request.form.get('objective')
        problem = request.form.get('problem')
        hypothesis = request.form.get('hypothesis')
        project = Project(id, team_name, name, objective, description, problem, hypothesis)

        affected_rows = ProjectModel.update_project(project)

        if affected_rows == 1:
            return jsonify(project.id)
        else:
            return jsonify({'message': 'Error in updated'}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
