class Point3D:

    __slots__ = ("x", "y", "z")

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        clss = [cls.__dict__ for cls in type(self).__mro__][:-1]
        attrs = []
        for dict in clss:
            if isinstance(dict["__slots__"], tuple):
                for el in dict["__slots__"]:
                    attrs.append(el)
            else:
                attrs.append(dict["__slots__"])
        
        return f"{self.__class__.__name__}({", ".join([f"{att}='{getattr(self, att)}'" for att in attrs])})"

class ColoredPoint(Point3D):
    __slots__ = ("color")

    def __init__(self, x, y, z, color = "black"):
        super().__init__(x, y, z)
        self.color = color

class ShapedPoint(Point3D):

    __slots__ = ("shape")

    def __init__(self, x, y, z, shape = "sphere"):
        super().__init__(x, y, z)
        self.shape = shape


p1 = Point3D(1,2,3)
p2 = ColoredPoint(4,5,6)
p3 = ShapedPoint(7,8,9, "square")
print(p1)
print(p2)
print(p3)