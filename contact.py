class Contact:
    def __init__(self, first_name, last_name, phone = None, email = None, display_mode = 'masked'):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.display_mode = display_mode

    def _obfuscated(self):
        result = {}
        params = ['first_name', 'last_name']
        for param in params:
            result[param] = f"{getattr(self, param)[0]}{''.join(["*" for l in getattr(self, param)])[1:]}"
        return result

    def __eq__(self, other):
        if not isinstance(other, Contact):
            return False
        return ((self.first_name == other.first_name and self.last_name == other.last_name) or
            (self.phone != None and self.phone == other.phone) or (self.email != None and self.email == other.email))
    
    def __hash__(self):
        return hash((self.first_name, self.last_name, self.phone, self.email))
    
    def __repr__(self):
        if self.display_mode == 'masked':
            return str(self._obfuscated())
        else:
            return str(self.__dict__)
        
    def __str__(self):
        return f"{self.last_name[0]}{self.first_name[0]}"
    
    def __format__(self, format_spec):
        if format_spec == 'unmask':
            return str(self.__dict__)
        return repr(self)


    
