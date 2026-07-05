name = {"Abdul":"Jabbar"}
print(name["Abdul"])

info = {"name":"Abdul Jabbar",
        "Age":21,
        "City":"Ahmedabad",
        "course":"Python"
    }

info["College"] = "BTU"

# print(info["name"],info["Age"])
# print(info["course"])
# print(info["College"])
# print(info)

# info["Age"] = 22
# print(info["Age"])

# del info["course"]
# print(info)

for key,value in info.items():
    print(f"{key} is {value}")


