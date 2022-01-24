
details = [{"name":"Ram","age":25,"salary":25000},
{"name":"Nam","age":35,"salary":25000},
{"name":"Dam","age":45,"salary":29000}]
new = []
for dict in details:
    if dict["age"] > 25:

        print("Name and salary is : ",dict["name"],dict["salary"])
        
