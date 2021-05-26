import random

# random.seed(123)
# interestingly if we specify a particular seed then the random number generated will
# always be the same

# note that rand module uses the current timestamp as the seed, but we could alway 
# modify the seed
# the randint(a,b) returns random integer number between a and b, with a and b included


# a virtual coin toast program
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

generated_random_number = random.randint(0, 1)
print(generated_random_number)

if generated_random_number == 1:
    print(f"Heads")
else:
    print("Tails")
