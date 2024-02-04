import os # operating system
 
 # 讓 使用者輸入
# 讀取檔案
products = []
if os.path.isfile('products.csv'): # 檢查檔案 在不在
	print('yeah! 找到檔案了')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue  #繼續 非逃脫 是跳到下一回
			name,price = line.strip().split(',')
			products.append([name,price])

	print(products)
else:
	print('找不到檔案....')


# 存取檔案  
products = []

		
 
while True:
	name = input('請入商品名稱: ')
	if name == 'q':
		break
	price = input('請入商品價錢: ')
	price = int(price)
	products.append([name,price])
print(products)

# 印出購買紀錄
for p in products:
	print(p[0], '的價錢是: ', p[1])

＃　寫入檔案

with open('products.csv ', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write( p[0] + ',' + str(p[1]) + '\n')