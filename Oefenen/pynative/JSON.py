# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 10:38:52 2023

@author: mhouts
"""

#------------------------------------------------------------------------------
# Exercise 1 Convert the following dictionary into JSON format
#------------------------------------------------------------------------------
import json
data = {"key1" : "value1", "key2" : "value2"}
jsonData = json.dumps(data)
print(jsonData)

#------------------------------------------------------------------------------
# Exercise 2 Access the value of key2 from the following JSON
#------------------------------------------------------------------------------
import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""

data = json.loads(sampleJson)
print(data["key2"])

#------------------------------------------------------------------------------
# Exercise 3 PrettyPrint following JSON data
#------------------------------------------------------------------------------
import json
sampleJson = {"key1": "value1", "key2": "value2", "key3" : "value3"}
data = json.dumps(sampleJson, indent=2, separators=(",", " = "))
print(data)

#------------------------------------------------------------------------------
# Exercise 4 Sort JSON keys in and write them into a file
#------------------------------------------------------------------------------
import json
sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
jsonData = json.dumps(sampleJson)
with open("sampleJson.json", "w") as write_file:
    write_file.write(json.dumps(dict(sorted(sampleJson.items()))))

#------------------------------------------------------------------------------
# Exercise 5 Sort JSON keys in and write them into a file
#------------------------------------------------------------------------------
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

data = json.loads(sampleJson)
print(data["company"]["employee"]["payble"]["salary"])

#------------------------------------------------------------------------------
# Exercise 6 Sort JSON keys in and write them into a file
#------------------------------------------------------------------------------
import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

print(json.dumps(vehicle.__dict__, indent=4))

#------------------------------------------------------------------------------
# Exercise 7 Convert the following JSON into Vehicle Object
#------------------------------------------------------------------------------
import json
myJson = { "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price
        
load = json.loads(myJson)
vehicle_instance = Vehicle(load)

print(vehicle_instance.name)

#------------------------------------------------------------------------------
# Exercise 8 Check whether following json is valid or invalid. If Invalid correct it
#------------------------------------------------------------------------------
import json
{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}

#------------------------------------------------------------------------------
# Exercise 9 Parse the following JSON to get all the values of a key ‘name’ within an array
#------------------------------------------------------------------------------
import json
json_data = '''[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]'''

data = json.loads(json_data)
print([item.get('name') for item in data])

