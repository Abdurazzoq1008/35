class User:
    def __init__(self,foydalanuvchi,ismi,email):
        self.foydalanuvchi=foydalanuvchi
        self.ismi=ismi
        self.email=email

    def get_info(self):
        return f"{self.foydalanuvchi}  {self.ismi} {self.email}"

info = User(input("Foydalanuvchi nomini kiriting:"), input("Foydalanuvchi ismini kiriting:"), input("Foydalanuvchi emailini kiriting:"))

print(info.get_info())


class Talaba:
    def __init__(self,ism):
        self.ism=ism
        self.kurs=1

    def chiqar(self):
        return f"{self.ism} {self.kurs}"
