
""" 
OOP : It is a way of thinking about our code as a collection of Objects.
Why we need OOPS: 
- When for a big project it is hard to manage methods,
- Data and Function lives seperately,
- Code duplication,
- Difficult to modal real - world entities.


Class: It is a blueprint for creating things.
Object : It is a specific instance created ftom that blueprint,

Example :- The cookie cutter is a class , and the actual cokkie is an abject.

Defining Class:
- class Student:
        pass

Creating an Object:
- class Student:
        pass

  student1 = Student()  -> student1 is one object,
  student2 = Student()  -> student2 is another object,



Self : First parameter of an instance method, It refers to the specific object the method is called on,
Why?
- Class id=s one blueprint, but it produces many objects,
- Self tells the method which object it is working with,
- without it , Python would not know whose data to read or modify.

Self = the specific object the method is called on.
"""


class Student:
    #Attributes
   
    # Method-1
    def set_details(self,r: int,n: str,g: str,a: int) -> None:
        self.name = n
        self.roll_no = r
        self.gender = g
        self.age = a

    # Method- 2
    def display_details(self) -> None:
        print(self.name)
        print(self.roll_no)
        print(self.age)
        print(self.gender)


#Objects/Instance
student1 = Student()
student1.set_details(77,"Sujita Kumari","Female",23)
student1.display_details()
