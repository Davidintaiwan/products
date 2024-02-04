products = []
while True:
	name = input('請入商品名稱: ')
	if name == 'q':
		break
	price = input('請入商品價錢: ')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)
print(products)

for thing in products:
	print(thing[0], '的價錢是: ', thing[1])
