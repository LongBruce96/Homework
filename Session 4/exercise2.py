prices = {}

prices["banana"] = 4
prices["apple"] = 2
prices["orange"] = 1.5
prices["pear"] = 3

stock = {}

stock["banana"] = 6
stock["apple"] = 0
stock["orange"] = 32
stock["pear"] = 15

list(prices.keys())
list(prices.values())
list(prices.items())
list(stock.values())
print(prices.items())

for (k,v,i) in zip(prices.keys(),prices.values(),stock.values()):
    print(k)
    print('price:', v)
    print('stock:', i)
    print()

total = 0
for (k,v,i) in zip(prices.keys(),prices.values(),stock.values()):
    print(k)
    print('total cost', v*i)
    print()
    total += v*i

print(total)