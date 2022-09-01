import statistics

ages=[19,22,19,24,20,25,26,24,25,24]
print("ages_beforesort:", ages)
#sorting the list
sortedlist = ages.sort()
#printing sorted list of ages
print("sorted_ages:",ages)
#printing minimum and maximum values 
minimum=min(ages)
maximum=max(ages)
print("Minimum age is:", minimum)
print("Maximum age is:",maximum)

#adding minimum and maximum values to list

ages.append(minimum)
ages.append(maximum)
print("List of ages after appeending:",ages)

#median

median_age=statistics.median(ages)
print("Median:", median_age)

#average

length=len(ages)
s=0
for i in ages:
    s+=i
print("Average:",s/length)

#range

ranges=maximum-minimum
print("Range:",ranges)