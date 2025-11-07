# # harflarni listda chiqaradigan dastur

# ism = input("ismingizni kiriting:>")
# letters = []

# for i in ism:
#     letters.append(i)

# print("natija", letters)





# listdagi oxshash elementlarni o'chiriladi
letters = [1, 2, 2, 3, 4, 4, 5]

new_list = []

for i in letters:
    if i not in new_list:
        new_list.append(i)
print("natija", new_list)