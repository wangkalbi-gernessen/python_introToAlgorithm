def f(x): # function header (prototype)
    # function body
    return x + 2

print(f(3))
print(f(5))
print(f(7))


def print_one():
    print(1)

print_one()



def get_fullname(fn, ln):
    full = fn + " " + str(ln)
    return full

print(get_fullname("Derrick", 2))
print(get_fullname("Leo", "Park"))
print(get_fullname("Sean", "Park"))
john = get_fullname("John", "Smith")
print(john)

def print_menu():
    print("===== Menu =====")
    print("| 1. Paella")
    print("| 2. Paella")
    print("| 3. Paella")
    print("| 4. Paella")
    print("| 5. Paella")
    print("| 6. Paella")

print_menu()