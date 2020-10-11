# What is a dictionary
# - a "set" of key: value pairs
# - not ordered
# - key must be unique

#   key              value
# "apple" : "the round fruit of a tree of the rose family,
#            which typically has this red or green skin and crisp flesh."
# "orange" : "the round fruit of a tree of the

# lists, tuples ,strings (position, 0-index based)

contacts = {"Derrick": [(0, "123-456-7890"), (1, "429-123-2124")],
          "Kazu": {"Canada": "778-645-5943", "Japan": "212-123-1234"},
          "Adriano": ["684-923-5943", "778-329-1248"],
          "Shintaro": 1231123110, 7: "Hello"
        #duplicate
}

print(type(contacts))

# Access dictionary by key to get value
print(contacts["Kazu"])
# print(contacts[0]) # error Don't put index number -wrong! there's no key 0
print(contacts["Adriano"])
print(contacts["Adriano"][0])
print(contacts["Kazu"]["Canada"])

# 2. Add a new entry (key - value pair)
contacts["Ariel"] = "3783737388"
print(contacts)

# 3. Update a value for existing key
contacts["Shintaro"] = "1998129283"
print(contacts)

# 4. Delete an entry from a dictionary
del contacts[7]
print(contacts)

# 5. Get a list of keys
for key in contacts.keys():
    print(contacts[key])

print(contacts.keys()) # this is not a list (dict_keys)
# print(contacts.keys()[0])
key_list = list(contacts.keys())
print(key_list)
print(key_list[1])


# 6. Get list of values
for val in contacts.values():
    print(val)

print(type(contacts.values())) # not a list, dict_values
value_list = list(contacts.values())
print(value_list)

# 7. Check if a dictionary contains a specific key
# `in` keyword
if "John" in contacts:
    print("I have John's contact info")
elif "Kazu" in contacts:
    print("I have Kazu's contact info")


# values = list(contacts.values())
# i = values.index("3783737300")
# print

# 8. iterate through a dictionary with a (key, value) pair
# contacts.items() -> [(k1, v1), (k2, v2), ...]
for(key, val) in contacts.items():
    if val == "3783737300":
        print(key)

print(type(contacts.items())) # not a list (dict_items)
print(list(contacts.items()))