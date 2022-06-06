class Contact:
    def __init__(self, name, phone, birth, genre):
        self.name = name
        self.phone = phone
        self.birth = birth
        self.genre = genre

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setPhone(self, phone):
        self.phone = phone

    def getPhone(self):
        return self.phone
    
    def setBirth(self, birth):
        self.birth = birth

    def getBirth(self):
        return self.birth
    
    def setGenre(self, genre):
        self.genre = genre

    def getGenre(self):
        return self.genre

    def to_json(self):
        var = {
                    "name"   : self.name,
                    "number" : self.phone,
                    "birth"  : self.birth,
                    "gender" : self.genre
                }
        return var

    def getAdult(self, edad):
        year = int(self.birth[:4])
        edad = int(edad)
        if (2022-year < edad):
            return self.to_json(self)

    def isAdult(self, edad) -> bool:
        year = int(self.birth[:4])
        edad = int(edad)
        if (2022-year < edad):
            return True
        else:
            return False
        
        

    