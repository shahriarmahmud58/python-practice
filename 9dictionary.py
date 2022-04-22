#dictionary name ={
   # key:value,
    # key:value,
     # key:value
#}

person ={
    "first_name":"rahim",
    "last_name":"karim",
    "age":"40"
}

#get_method=person.get("first_name")
#print(get_method)

#adding_Item
#person["hobby"]="playing cricket"
#print(person)

#chanaging_Item
#person["first_name"]="Ahnaf"
#print(person)

#delete Item
#person.pop("age")
#print(person)

employee_data ={
    
"manager":{
    "name":"Rahim",
    "age":34
    
},
"programmer":{
    "name":"Arif",
    "age":34
},
"salary":{
    "manager_salary":2300,
    
    "programmer_salary":2400
}

}
print("manager name",employee_data["manager"]["name"],
      "manager age",employee_data["manager"]["age"],
      "manager salary",employee_data["salary"]["manager_salary"]
      )