def intro(task):
    title = f" ** {task} ** "
    print ("\n")
    print ("*" * len(title))
    print (title)
    print ("*" * len(title))
    print ("\n")

intro("School")

class Person():
    def __init__(self, firstname, lastname, keyaccess=["Entry"], gender="Not defi
        self.firstname = firstname
        self.lastname = lastname
        self.keyaccess = keyaccess
        self.gender = gender
        self.age = age
        self.phonenumber = phonenumber
        self.email = email
        if email == None:
            self.email = str.lower(firstname) + "." + str.lower(lastname) + "@sch
        if isinstance(keyaccess, list) == False:
            self.keyaccess = ["Entry"]
        if not (gender == "Male" or gender == "Female" or gender == "Not defined"
            raise ValueError("Gender should be Male, Female, Not defined")

class Student(Person):
    def __init__(self, firstname, lastname, keyaccess, gender, age=7, phonenumber
        super().__init__(firstname, lastname, keyaccess, gender, age, phonenumber
        self.year = year
        self.classname = classname
        self.grades = grades
        if isinstance(grades, dict) == False:
            raise ValueError("Subjects should be a list")
        if not (year >= 1 and year <= 9):
            raise ValueError("Year should be the number of witch year student are


access1 = ["Entry"]
access2 = ["Entry", "Classroom", "Staffroom"]
access3 = ["Entry", "Classroom", "Staffroom", "Office"]
access4 = ["Entry", "Classroom", "Staffroom", "Office", "Storage"]

annabelle = Student("Annabelle", "Blomqvist", access1, "Female", 15, 46791514293,
joanna = Student("Joanna", "Fredriksson", access1, "Female", 14, 46736997456, , 8
rahaf = Student("Rahaf", "Bergqvist", access1, "Female", 7, 46768326923, , 1, "1A
freya = Student("Freya", "Lindgren", access1, "Female", 9, 46787548429, , 3, "3C"
angelina = Student("Angelina", "Blomqvist", access1, "Female", 11, 46759535359, ,
sanja = Student("Sanja", "Lundberg", access1, "Female", 11, 46725645102, , 5, "5A
molly = Student("Molly", "Hedlund", access1, "Female", 7, 46712140016, , 1, "1A")
teodor = Student("Teodor", "Axelsson", access1, "Male", 8, 46740580800, , 2, "2C"
valter = Student("Valter", "Jakobsson", access1, "Male", 15, 46783447090, , 9, "9
hana = Student("Hana", "Nordin", access1, "Female", 15, 46778649101, , 9, "9A")
terese = Student("Terese", "Sandberg", access1, "Female", 12, 46763795848, , 6, "
aisha = Student("Aisha", "Magnusson", access1, "Female", 8, 46783710608, , 2, "2B
nour = Student("Nour", "Eklund", access1, "Female", 7, 46790606686, , 1, "1B")
bertil = Student("Bertil", "Lindqvist", access1, "Male", 7, 46772391240, , 1, "1A
tilly = Student("Tilly", "Olofsson", access1, "Female", 11, 46783878303, , 5, "5B
charles = Student("Charles", "Lundberg", access1"Male", 13, 46754132153, , 7, "7A

print(annabelle.firstname)
print(annabelle.lastname)
print(annabelle.keyaccess)
print(annabelle.gender)
print(annabelle.classname)