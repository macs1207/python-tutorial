import json

'''
Serialize
'''
a_dict = {
    "程式語言": ["C", "C++", "Python", "Go", "Rust"],
    "水果": ["西瓜", "蘋果"]
}

serialzation = json.dumps(a_dict)
print(serialzation)
print(type(serialzation))
print("\n--------------------\n")

# Output:
# {"\u7a0b\u5f0f\u8a9e\u8a00": ["C", "C++", "Python", "Go", "Rust"], "\u6c34\u679c": ["\u897f\u74dc", "\u860b\u679c"]}
# <class 'str'>

# --------------------

'''
Deserialize
'''
json_string = '{"\u7a0b\u5f0f\u8a9e\u8a00": ["C", "C++", "Python", "Go", "Rust"], "\u6c34\u679c": ["\u897f\u74dc", "\u860b\u679c"]}'

deserialzation = json.loads(json_string)
print(deserialzation)
print(type(deserialzation))
print("\n--------------------\n")

# Output:
# {'程式語言': ['C', 'C++', 'Python', 'Go', 'Rust'], '水果': ['西瓜', '蘋果']}
# <class 'dict'>

# --------------------

f = open("./ch2/example.json", "r", encoding="utf-8")
load_from_file = json.load(f)
print(load_from_file)
print(type(load_from_file))

# Output:
# {'程式語言': ['C', 'C++', 'Python', 'Go', 'Rust'], '水果': ['西瓜', '蘋果']}
# <class 'dict'>
