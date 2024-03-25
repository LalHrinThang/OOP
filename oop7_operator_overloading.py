class Employee:
    def __init__(self,id,age):
        self.id = id
        self.age = age

    def __add__(self,self2):
        id_data = self.id + self2.id

        age_data = self.age + self2.age

        return id_data , age_data
    
p1 = Employee(200,50)

p2 = Employee(250,50)

p3 = Employee(250,200)
total = p1 + p2
d_id , d_age = total
print(d_id,d_age)

p4 = Employee(d_id,d_age)

final_total = p3 + p4
d_id , d_age = final_total

print(d_id,d_age)


result = d_age + d_id

print(f"final result : {result}")