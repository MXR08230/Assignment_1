it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Find the length of the set it_companies
print("Length of set it_companies is:",len(it_companies))
#Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)
#Insert multiple IT companies at once to the set it_companies
multiple_companies=['mindtree','cognizant','UHG']
it_companies.update(multiple_companies)
print("updated it_companies list",it_companies)
#Removing one of the companies from the set it_companies
it_companies.remove('IBM')
print(it_companies)
#Difference between remove and discard
#Remove:
#Discard:

#Join A and B
print("Joining A and B:",A.union(B))

#Find A intersection B
print("Intersection of A and B",A.intersection(B))

#Is A subset of B
print("Is A subset of B?:",A.issubset(B))

#Are A and B disjoint sets
print("Are A and B disjoint sets:",A.isdisjoint(B))

#Join A with B and B with A
print("joining A with B ",A.union(B))
print("joining B with A",B.union(A))

# symmetric difference between A and B
print("symmetric difference is",A.symmetric_difference(B))

#Delete the sets completely
A.clear()
print(A)
B.clear()
print(B)
print("A and B sets are deleted")

#Converting the ages to a set and compare the length of the list and the set
print("length of age list is:",len(age))
print("Length of age set is:", len(set(age)))
print("length of age list is greater than age set")