
# JSON file handling (Java Script Object Notation).
# JSON is a syntax for storing and exchanging data. JSON is text, written with JavaScript object notation.
import json

# Parse JSON - Convert from json to python
# If you have JSON string, you can parse it by using the	json.loads() method.
x = '{"name":"John", "age":30, "city":"New York"}'
# Parse x:
y = json.loads(x)
# The result is a python dictionary:
print(y["city"])

# Convert from Python to JSON:
# If you have a python object, you can convert into a Json string by using the 	json.dumps() method.
# A python object(dict):
j = {
	"name":"John",
	"age":30,
	"city":"New York"
}
# Convert into Json:
k = json.dumps(j)
# The result is a Json string:
print(k)
