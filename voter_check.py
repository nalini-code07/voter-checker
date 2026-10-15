# One voter at the polling station
age = 17
is_citizen = True
voter_id = 1001

print("Voter ID:", voter_id)
print("Age:", age)
if age >= 65 and is_citizen:
    print("Eligible")
    print("Senior")
elif age >= 18 and is_citizen:
    print("Eligible")
    print("General")
else:
    print("Not eligible")
    print("Cannot vote")

print("---")

# Three more voters in line, all citizens
ages = [17, 18, 70]
for voter_age in ages:
    print("Age:", voter_age)
    if voter_age >= 65 and is_citizen:
        print("Eligible")
        print("Senior")
    elif voter_age >= 18 and is_citizen:
        print("Eligible")
        print("General")
    else:
        print("Not eligible")
        print("Cannot vote")

print("---")

# Countdown to closing time
minutes = 5
while minutes >= 1:
    print("Polling station closes in", minutes, "minutes")
    minutes = minutes - 1
print("Closed")
