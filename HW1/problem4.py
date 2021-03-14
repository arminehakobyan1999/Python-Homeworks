market = {"dairy": ["yogurt", "cheese"], 
          "fruits": ["banana", "apple", "orange", "lemon", "apple", "banana", "banana"]}
print(market)

market["candies"] = ["mars", "kinder", "twix"]
market['fruits'].sort()
market['fruits'] = set(market['fruits'])

print(market)