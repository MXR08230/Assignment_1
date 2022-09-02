#creating empty dictionary called dog
dog={}
#Adding name, color, breed, legs, age to the dog dictionary
dog={'name':'snoopy','color':'lavender','breed':'german_sheperd','legs':'4','age':'2'}
print("dog=",dog)

#creating student dictionary
student={"first_name":"mounika","last_name":"Rayapudi","gender":"female","age":"21","martial status":"single",
"skills":["java","c","python"],"country":"India","city":"Miryalaguda","address":"6708w apt 3001"}
print("student=",student)

#length of student dictionary
print("length of student:",len(student))

#get values of skills and checking datatype
print("student skills are:",student["skills"])
print(type(student['skills']))


#modifying skills by adding one or more
student["skills"].append("javascript")
print(student["skills"])

#get dictionary keys as list
print("student dictionary keys:",list(student.keys()))

#get dictionary values as list
print("student dictionary values:",list(student.values()))