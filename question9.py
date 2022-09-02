import math

N = int(input("Enter No.of students:"))
print("Enter", N, "students weights")
W_lbs = []
for i in range(0, N):
    weight = int(input())
    W_lbs.append(weight)

print(N)
print("weights in lbs", W_lbs)

# converting lbs to kgs
W_kgs = []
for i in range(0, N):
    W_kgs.append(math.floor((W_lbs[i] / 2.2046) * 100) / 100)
print("Weights in kgs", W_kgs)
