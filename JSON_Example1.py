import json
#import request

#
# Conversion Table
# Always converts Key:Value pairs of DICT to STRINGS
# https://docs.python.org/3/library/json.html#py-to-json-table
#

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it


def add_employee(json_salaries, name, salary):
    salaries = json.loads(json_salaries)
    salaries[name] = salary

    return json.dumps(salaries)

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])


with open("json_salaries.json", "r") as jsonfile:
    o = json.load(jsonfile)
    print(o)
    for name in o:
        print("{} has a Salary of ${}".format(name, str(o[name])))



# def default(self):
#     try:
#         o = json.load("json_salaries.json")
#         iterable = iter(o)
#         for i in o:
#             print(o.name + " : " + o.salary)
#     except TypeError:
#         pass
#     else:
#         return list(iterable)
#     # Let the base class default method raise the TypeError
#     return json.JSONEncoder.default(self, o)



#if __name__ == '__main__':
#    default()

# https://realpython.com/python-json/
#response = requests.get("https://jsonplaceholder.typicode.com/todos")
#todos = json.loads(response.text)
