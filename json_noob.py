import json

person = {"name" : "Bob", "languages" : ["English", "French"]}
person_dict = json.dumps(person)

print(person_dict)

print(person_dict["languages"])


with open(r"C:\Users\Anik\Desktop\json1.json")as f:
	data = json.load(f)

	print(data)

person = {"name":"Bob", 
"languages":["English", "French"],
"married":True,
"age":32}

with open(r"C:\Users\Anik\Desktop\person.txt", "w") as json_file:
	json.dump(person, json_file)

with open(r"C:\Users\Anik\Desktop\json1.json")as f:
	data = json.load(f)
	print(data)