# # harflarni listda chiqaradigan dastur

# ism = input("ismingizni kiriting:>")
# letters = []

# for i in ism:
#     letters.append(i)

# print("natija", letters)





# listdagi oxshash elementlarni o'chiriladi
# letters = [1, 2, 2, 3, 4, 4, 5]

# new_list = []

# for i in letters:
#     if i not in new_list:
#         new_list.append(i)
# print("natija", new_list)










# # set bilan ishlashni boshladik
# tupple = [1, 2, 3, 3, 4, 5, 5]

# new_set = set(tupple)


# print(new_set)




# new_set = set()  ### bosh set ochadi
# new_set2 = {}    ### bu belgi {} setniki lekin bu holatda dikt ochadi



my_set = {1, 2, 3, 4, 5}
print(my_set)                     ### {1, 2, 3, 4, 5}ni ekranga chiqaradi




my_set.add(6)                    
print(my_set)                    ### {1, 2, 3, 4, 5, 6} ekranga chiqaradi


my_set.update([7, 8, 9])
print(my_set)                   ### {1, 2, 3, 4, 5, 6, 7, 8, 9}ni ekranga chiqaradi




my_set.remove(3)               
print(my_set)                  ### berilgan elementni o'chiradi agar setda berilgan element topilmasa xatolik chiqadi





my_set.discard(10)
print(my_set)                  ### berilgan elementni o'chiradi agar setda berilgan element topilmasa xatolik chiqmaydi





my_set.pop()
print(my_set)                 ### random elementni o'chiradi va o'chirilgan elementni qaytaradi






for item in my_set:
    print("Set item:", item)  ### forni set ichida ham ishlatsa buladi





set_length = len(my_set)
print(set_length)              ### set elentlari sonni chiqaradi



my_set.clear()
print(my_set)                 ### barcha elementlarni ochiradi




del my_set
print(my_set)               ### ozgaruvchiga qo'shib o'chiradi





