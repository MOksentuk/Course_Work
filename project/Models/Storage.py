class Storage:
    amount = 0

    def __init__(self, *args):
        models = [arg for arg in args]
        for model in models:
            if model.amount != '':
                self.amount += model.amount
