class Tablet:

    models = ['lite', 'pro', 'max']

    def __init__(self, model):
        self.model = model
        self._added_storage = 0

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if value not in self.models:
            raise ValueError("Model can only be lite, pro or max.")
        self._model = value

    @property
    def base_storage(self):
        return 2 ** (5 + self.models.index(self._model))

    @property
    def memory(self):
        return 2 + self.models.index(self._model)
    
    added_storage = property()

    @added_storage.getter
    def added_storage(self):
        return self._added_storage

    @added_storage.setter
    def added_storage(self, value):
        print(f"to add {value}")
        if value < self.base_storage:
            raise ValueError("Total storage cannot be less than the base storage.")
        if value + self.base_storage > 1024:
            raise ValueError("Maximum allowed total memory is 1024.")
        self._added_storage = value - self.base_storage

    def add_storage(self, storage):
        self.added_storage += storage + self.base_storage

    def __repr__(self):
        return f"{Tablet.__name__}(model='{self.model}', base_storage='{self.base_storage}', added_storage'{self.added_storage}', memory='{self.memory}')"
    
t1 = Tablet('pro')
print(t1.base_storage)
print(t1.memory)
print(t1)
t1.added_storage = 400
print(t1.added_storage)
t1.add_storage(30)
print(t1.added_storage)
print(t1)
t1.model = 'max'
print(t1)
