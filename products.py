import os # operation system

#讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r',) as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products


#輸入相關資料
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請商入商品價格:')
        products.append([name, price])
    print(products)
    return products

#印出購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '售價為', p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', ) as f: #encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')


def main():
    filename = 'products.csv'
    if os.path.isfile(filename): #檢查檔案是否存在，但不影響後續檔案持續運作
        print('yes. you got the file')
        products = read_file(filename)
    else:
        print('lost file')

    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()