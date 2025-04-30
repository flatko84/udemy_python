from collections import UserDict

class BidirectionalDict(UserDict):
    def __setitem__(self, key, value):
            if key in self:
                 del self[key]
            if value in self:
                 del self[value]
            super().__setitem__(key, value)
            super().__setitem__(value, key)
    
    def __len__(self):
        return super().__len__() // 2
    
    def __delitem__(self, key):
        super().__delitem__(self[key])
        super().__delitem__(key)


bd = BidirectionalDict({"code": "more", "sleep": "less", "more": "code", "less": "sleep"})
print(len(bd))
print(bd["code"])
print(bd["more"])
bd.update([("sleep", "deeper")])
bd.pop("sleep")
print(bd)
print(len(bd))
del(bd["better"])
print(bd)


# needs better understanding, not all tests are working