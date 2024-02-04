# 存取檔案  
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue  #繼續 非逃脫 是跳到下一回
		name,price = line.strip().split(',')
		products.append([name,price])

print(products)
		
  # 讓 使用者輸入

products = []
while True:
	name = input('請入商品名稱: ')
	if name == 'q':
		break
	price = input('請入商品價錢: ')
	products.append([name,price])
print(products)

for p in products:
	print(p[0], '的價錢是: ', p[1])

with open('products.csv ', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write( p[0] + ',' + str(p[1]) + '\n')