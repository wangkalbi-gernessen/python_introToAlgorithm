# Nested loops
# loop inside another loop

# for i in range(5):
#     for j in range(5):
#         print(i + j)

# i = 0  -> j = 0, 1, 2, 3, 4
# i = 1  -> j = 0, 1, 2, 3, 4
# i = 2  -> j = 0, 1, 2, 3, 4
# i = 3  -> j = 0, 1, 2, 3, 4
# i = 4  -> j = 0, 1, 2, 3, 4

i = 0
while i < 5:
    j = 0
    while j < 5:
        print(i + j)
        j += 1
    i += 1

# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             print(i + j + k)

# i = 0, j = 0, k = 0, 1, 2
#        j = 1, k = 0, 1, 2
#        j = 2, k = 0, 1, 2
# i = 1, j = 0, k = 0, 1, 2
#        j = 1, k = 0, 1, 2
#        j = 2, k = 0, 1, 2
# i = 2, j = 0, k = 0, 1, 2
#        j = 1, k = 0, 1, 2
#        j = 2, k = 0, 1, 2