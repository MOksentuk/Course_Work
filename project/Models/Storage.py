class Storage:
    def __init__(self, *args):
        self.amount = 0
        models = [arg for arg in args]
        for model in models:
            if model.amount != '':
                self.amount += model.amount
