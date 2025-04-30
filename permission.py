from enum import Enum, Flag, auto

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

class BaseUser:

    roles = {"admin": Permission.READ | Permission.WRITE | Permission.EXECUTE,
    "user": Permission.READ,
    "manager": Permission.READ | Permission.WRITE,
    "support": Permission.EXECUTE}


    def validate_permission(self, permission):
        if not self.permissions & permission:
            raise PermissionError(f"You do not have {permission.name} permission.")


    def read(self, file):
        self.validate_permission(Permission.READ)
        with open(file) as fl:
            print(fl.read()) 

    def write(self, file, content):
        self.validate_permission(Permission.WRITE)
        with open(file, "w") as fl:
            fl.write(content)

    def execute(self, file):
        self.validate_permission(Permission.EXECUTE)
        with open(file) as fl:
            eval(fl.read())

class User(BaseUser):


    def __init__(self, name, user_role):
        self.name = name
        if user_role not in self.roles.keys():
            raise ValueError("Not a valid user role.")
        self.user_role = user_role

    @property
    def permissions(self):
        return self.roles[self.user_role]

    def __repr__(self):
        return f"{type(self).__name__}(name='{self.name}', user_role='{self.user_role}', permissions='{self.permissions}')"


u1 = User("Vlad", "manager")
print(u1)
print(u1.permissions)
u1.write("test.py", "print(''.join([str(n) for n in range(10)]))")
u1.read("test.py")
u1.execute("test.py")
