class Project:
    def __init__(self, id, team_name=None, name=None, description=None, objective=None, problem=None, hypothesis=None):
        self.id = id
        self.team_name = team_name
        self.name = name
        self.description = description
        self.objective = objective
        self.problem = problem
        self.hypothesis = hypothesis

    def to_json(self):
        return {
            'id': self.id,
            'team_name': self.team_name,
            'name': self.name,
            'description': self.description,
            'objective': self.objective,
            'problem': self.problem,
            'hypothesis': self.hypothesis,
        }
