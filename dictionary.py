# # dict={"name":"smith","panda":"goat","colour":"yellow"}
# # print(dict.get("name"))

# # num={"many":12,"smith":35,}
# # print(num)
# # print(num.get("35"))

# # cars={
#     # "brand":"BMW",
#     # "year":2022,
#     # "value":200000
#     # }

# # print(cars["brand"]) 

# # updating dictionary

# # cars.update({"brand":"mercedes"})
# # cars.update({"colour":"white"})
# # print(cars)

# # pop an item in a dictionary or delete using delete function

# # cars.pop("brand")
# # print(cars)

# # cars={"mercedes":{"coupe":63},
# #        "toyota" :{"cambri":102},
# #        "Bmw":{"couoe":210}
#     #   }
# # print(cars["mercedes"]["coupe"])

# light_theme={
#     "button":"pink",
#     "title":"black"
# }

# pawn={
#     "direction":["forward,back"],
#     "level":"one"
# }
# # name=input("enter name: ")
# # print(name.split())
# # print(len(name))
# # 
# # def average(x,y):
#     # av=(x+y)/2
#     # return av
# # car={
# #     "model":"mercedes",
# #     "make":"gle 63 coupe",
# #     "year":2023,
# #     "colour":"matt green",
# #     "country":"germany",
# # }

# # # accessing dictionary items(use keys)
# # # print(car["country"])
# # person={
# #     "name":"bobfranzis",
# #     "age":"86",
# #     "pets": {"dog":"x",
# #              "cat":"y",
# #              "camel":"fred"
# #              }
            

# # }
# # print(person["pets"]["camel"])

# # profile={}
# # profile["username"]="user:panda"
# # profile["age"]="21"
# # profile["email"]="panda@gmail.com"
# # profile["repository"]={
#     # "name":"python",
#     # "files":2
    
# # }

# data={}
# def register():
#     # ask name
#     # ask email
#     # ask password

#     username=input("enter username: ")
#     email=input("enter email: ")
#     password=input("enter password: ")

#     # store in dictionary

#     data["username"]=username
#     data["email"]=email
#     data["password"]=password
    
# def get_profile():
#     print(data)

# def change_username():
#     new_username=input("enter new username: ")
#     data["username"]=new_username


# register()
# get_profile()
# change_username()
# get_profile()



# # check dictionary methods
# # 1 clear
# # 2 pop
# # 3 keys
# # 4 values
# # 5 get
# # 6 popitem
# # 7 update

# 1:clear-removes elements from a list
list={"name":"fred",
      "age":"26",
      "Sclass":"bussiness studies",
      }
list.clear
# print(list)

# 2.dict() creates an empty dictionary
# student=dict()
# print(student)

# 3 pop/ del-removes an element from a dictionary
st=dict({"name":"john",
         "gender":"male",
         "age":25},
         )
del st["gender"]
print(st)

# 4 