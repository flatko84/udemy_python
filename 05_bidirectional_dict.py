from collections import UserDict
import unittest

class BidirectionalDict(UserDict):
    def __setitem__(self, key: str, value: str) -> None:
            if key in self.keys():
                 del self[key]
            if value in self.keys():
                 del self[value]
            super().__setitem__(key, value)
            super().__setitem__(value, key)
    
    def __len__(self) -> None:
        return super().__len__() // 2
    
    def __delitem__(self, key: str) -> None:
        super().__delitem__(self[key])
        super().__delitem__(key)

class BidirectionalDictTest(unittest.TestCase):
    def test_bidirectional_dict(self):
        bd = BidirectionalDict({"code": "more", "sleep": "less", "more": "code"})
        assert(len(bd) == 2)
        assert(bd["code"] == "more")
        assert(bd["more"] == "code")
        bd.update([("sleep", "deeper")])
        assert(bd["deeper"] == "sleep")
        bd.pop("more")
        assert(len(bd) == 1)

if __name__ == '__main__':
    unittest.main()
