class Team:
    def __init__(self, id, name=None, objective=None, description=None, goal=None):
        self.id = id
        self.name = name
        self.objective = objective
        self.description = description
        self.goal = goal

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'objective': self.objective,
            'description': self.description,
            'goal': self.goal,
        }
