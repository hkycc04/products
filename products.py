products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請商入商品價格:')
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '售價為', p[1])