users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(users["Jonathan"]["twitter"])

# 2. Get Erik's hometown
print(users["Erik"]["home_town"])

# 3. Get the list of Erik's lottery numbers
print(users["Erik"]["lottery_numbers"])

# 4. Get the species of Avril's pet Monty
print(users["Avril"]["pets"][0]["species"])

# 5. Get the smallest of Erik's lottery numbers
erik_numbers = users["Erik"]["lottery_numbers"]
erik_numbers.sort()
#print(erik_numbers[0])

# 6. Return an list of Avril's lottery numbers that are even
avril_numbers = users["Avril"]["lottery_numbers"]
avril_even_numbers = []
for number in avril_numbers:
  if (number % 2 == 0):
    avril_even_numbers.append(number)
#print(avril_even_numbers)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
erik_numbers = users["Erik"]["lottery_numbers"]
erik_numbers.append(7)
#print(erik_numbers)

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["hometown"] = "Edinburgh"
#print(users["Erik"]["hometown"])

# 9. Add a pet dog to Erik called "fluffy"
users["Erik"]["pets"].append({"name" : "fluffy", "species" : "dog"})
#print(users["Erik"]["pets"])

# 10. Add another person to the users dictionary
users["Alistair"] = {
   "twitter": "randomal",
    "lottery_numbers": [7, 11, 13, 25, 45, 30],
    "home_town": "Jakarta",
    "pets": [
      {
        "name": "breno",
        "species": "dog"
      }
    ]
  }
print(users)