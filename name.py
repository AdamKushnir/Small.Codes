name = "adam kushnir"
tab = "="*50
New_name = (name.title())
First_Name = "adam"
Last_Name = "kushnir"
Full_Name = f"{First_Name} {Last_Name}"
message = (f"Hello, {Full_Name.title()}, we are happy than are you here.")


print(message)
print(Full_Name)
print(New_name)
print(New_name.upper())
print(New_name.lower())
print(tab)

print("Languages: \nPython\nC\nJavaScript")
print(tab)

favorite_langueage = " python "
new_favorite_langueage = favorite_langueage.strip()
print(favorite_langueage == new_favorite_langueage)

nostarch_url = 'httpps://www.chelseafc.com'
print(nostarch_url.removeprefix('httpps://'))