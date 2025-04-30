class Score:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if not instance:
            return self
        return instance.__dict__[f"{type(self).__name__}_{self.name}"]

    def __set__(self, instance, value):
        if not type(value) == int:
            raise TypeError("Score must be an integer.")
        if value < self.min or value > self.max:
            raise ValueError(f"Score must be in the range of {self.min} and {self.max}")
        instance.__dict__[f"{type(self).__name__}_{self.name}"] = value

    def __delete__(self, instance):
        del instance.__dict__[f"{type(self).__name__}_{self.name}"]



class StudentProfile:
    gre = Score(130, 340)
    sat = Score(400, 1600)

    def __init__(self, name, gre = 130, sat = 400):
        self.name = name
        self.gre = gre
        self.sat = sat

    def __repr__(self):
        return f"{type(self).__name__}(name='{self.name}', sat='{self.sat}', gre='{self.gre}')"
    

sp = StudentProfile(name="Andrew", sat=1220, gre=130)
print(sp)
print(sp.__dict__)
sp2 = StudentProfile("Liza", gre=190)
print(sp2)
sp2.gre = 1200.2