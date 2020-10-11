# methods == functions that belong to string type
city = "vancouver"

# func() -> execute, call, run
print(city.capitalize())
upper = city.upper()
lower = city.lower()
print(upper)
print(lower)

# index: returns the index of substrings, but if it doesn't exist, error!
print(city.index("an"))
# print(city.index("xxx"))  # error

# find(sub): returns the index of the first occurance of substring
# no match will return -1
print(city.find("an"))
print(city.find("xxx"))  # -1

# count(sub[, start[, end]]): returns the occurances of substring in string
# case-sensitive (o) vs case-insentitive (x)
greetings = "hello hello hello"
print(greetings.count("hello", 5, 12))



