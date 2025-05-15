
b, c, d = map(int, input().split())
burger = sorted(map(int, input().split()), reverse=True)
side = sorted(map(int, input().split()), reverse=True)
drink = sorted(map(int, input().split()), reverse=True)

total_price = sum(burger) + sum(side) + sum(drink)
print(total_price)

set_count = min(b, c, d)

discounted_price = 0
for i in range(set_count):
    discounted_price += int((burger[i] + side[i] + drink[i]) * 0.9)
discounted_price += sum(burger[set_count:]) + sum(side[set_count:]) + sum(drink[set_count:])

print(discounted_price)
