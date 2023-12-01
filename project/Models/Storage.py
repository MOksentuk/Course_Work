class Storage:
    def __init__(self, *args):
        self.amount = 0
        models = [arg for arg in args]
        for model in models:
            self.amount += float(model.amount)
