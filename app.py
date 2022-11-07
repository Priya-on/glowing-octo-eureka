from random_profile import RandomProfile

rp = RandomProfile()

# Get a random profile

profile = rp.full_profile()[0]


for i in profile.keys():
    print(i, ":", profile[i])
