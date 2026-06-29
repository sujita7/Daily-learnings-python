"""
- Constructor is also known as __init__ method,
- python provides a special method called __init__ that gets called automatically every time we create an object.
- __init__ runs the moment Class is called ,
- required values become mandotary parameter , we can't skip that,
- because of this no more " forgot to initialize" bugs,
- the double underscore " __ " make it a special dunder method,
- use it to set up object's initial state,
- it doesn't return anything - it just configures the new object.
"""




class Student:

    def __init__(self,name: str, age: int, marks: list[int]) -> None:
        self.name: str = name
        self.age: int = age
        self.marks: list[int] = marks

    def total(self) -> int:
        return sum(self.marks)

    def avg(self) -> float:
        return sum(self.marks) / len(self.marks)

    def grade(self) -> None:
        avg = self.avg()
        if avg >= 90:
            print("A")
        elif avg >= 50 and avg <= 89:
            print("B")
        else:
            print("C")
    
student1 = Student("Sujita", 23, [78,54,19,63])
total = student1.total()
print(total)
avg = student1.avg()
print(avg)
grades = student1.grade()
print(grades)


# OUTPUT : 214 53.5 B None
