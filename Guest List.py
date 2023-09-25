


#list
Guest_List = ["Kepa Arizabalaga", "Enzo Fernandes", "Lewi Colwill"]
dash = (40*"-")

#print invite to guest
print(f"Dear {Guest_List[0]}, i would like to invete you to dinner at the restaurant.")
print(f"Dear {Guest_List[1]}, i would like to invete you to dinner at the restaurant.")
print(f"Dear {Guest_List[2]}, i would like to invete you to dinner at the restaurant.")
#len guest in list
len_list = len(Guest_List)
print(f"len Guest is: {len_list}")
print(dash)

#message for who cant 
Guest_who_cant_come = Guest_List.pop(2)
print(f"Unfortunately, {Guest_who_cant_come} cant make it to dinner.")
print(dash)

#new guest who can come
Guest_List.append("Reece James")

print(f"Dear {Guest_List[0]}, i would like to invete you to dinner at the restaurant.")
print(f"Dear {Guest_List[1]}, i would like to invete you to dinner at the restaurant.")
print(f"Dear {Guest_List[2]}, i would like to invete you to dinner at the restaurant.")
#new len guest in list
len_list = len(Guest_List)
print(f"len Guest is: {len_list}")
print(dash)

#new message for guest
print("Good news! I found a bigger dinner table.")
print(dash)

#add 3 new guest in list
Guest_List.insert(0, "Ben Chillwel")
Guest_List.insert(1, "Christopher Nkunku")
Guest_List.append("Samuel Jackson")

#invite for all guest
print(f"Dear {Guest_List[0]}, i would like to invete you to dinner at the restaurant.")
print(f"Dear {Guest_List[1]}, i would like to invete you to dinner at the restaurant.")
print(f"Dear {Guest_List[2]}, i would like to invete you to dinner at the restaurant.")
print(f"Dear {Guest_List[3]}, i would like to invete you to dinner at the restaurant.")
print(f"Dear {Guest_List[4]}, i would like to invete you to dinner at the restaurant.")
print(f"Dear {Guest_List[5]}, i would like to invete you to dinner at the restaurant.")
#new len guest
len_list = len(Guest_List)
print(f"len Guest is: {len_list}")
print(dash)

#update for guests
print("Bad news! The new dinner table won't arrive in time, so i can only invete two guests.")
print(dash)

#do new list uninvited guests
univited_guests = []
univited_guests.append(Guest_List.pop())
univited_guests.append(Guest_List.pop())
univited_guests.append(Guest_List.pop())
univited_guests.append(Guest_List.pop())

#message for guests, i cant invite
print(f"Dear {univited_guests[0]}, Im sorry u cant invite you to dinner.")
print(f"Dear {univited_guests[1]}, Im sorry u cant invite you to dinner.")
print(f"Dear {univited_guests[2]}, Im sorry u cant invite you to dinner.")
print(f"Dear {univited_guests[3]}, Im sorry u cant invite you to dinner.")
#new len
len_list = len(Guest_List)
print(f"len Guest is: {len_list}")
print(dash)

#deleted all list (last 2 gusest)
del Guest_List[0]
del Guest_List[0]

#pritnt list and len list
print(Guest_List)
len_list = len(Guest_List)
print(f"len Guest is: {len_list}")