
# constant for packages
HOT_DOG_PACK = 10
BUNS_PACK = 8

#get the quantity of hot dogs in total needed for the cookout
attendants = int(input(("Enter the number of people that are going to attend to the cookout: ")))
hotDogPerPerson = int(input(("Enter the quantity of hot dogs per person: ")))

hotDogNeeded = attendants * hotDogPerPerson

# get quantity of hot dogs needed
packOfHotDog = hotDogNeeded // HOT_DOG_PACK
hotDogAdd = hotDogNeeded % HOT_DOG_PACK

hotDogLeftOver = 0

if (hotDogAdd > 0): 
    packOfHotDog += 1
    hotDogLeftOver = HOT_DOG_PACK - hotDogAdd

# get quantity of buns needed
packOfBuns = hotDogNeeded // BUNS_PACK
bunsAdd = hotDogNeeded % BUNS_PACK

bunsLeftOver = 0

if (bunsAdd > 0):
    packOfBuns += 1
    bunsLeftOver = BUNS_PACK - bunsAdd

#show results
print("This cookout will require this minimum of: ")
print("Packages of Hot Dogs: " + str(packOfHotDog))
print("Packages of Buns: " + str(packOfBuns))

print("\nThere will be these left overs: ")
print("Hot Dogs: " + str(hotDogLeftOver))
print("Buns: " + str(bunsLeftOver))

input("Please enter to exit ")

