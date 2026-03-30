'''eccommerce to check most bought product each day
most sold today == featured product next day
- if multiple products have same number of purchases
- sort alphabetically A-Z
- return Last name in sorted list

Input & output are in  stdin and stdout respectively
n=number of products

'''

from tifffile import product


products1 = ["redShirt","greenPants", "redShirt", "orangeShoes", "blackPants"]     #redShirt=2 -> redShirt = featured product
products2 = ["yellowShirt","redHat","blackShirt", "bluePants", "redHat", "pinkHat","blackShirt","yellowShirt","greenPants","greenPants"]     #yellowShirt=2, blackShirt=2,redHat=2, greenPants=2, A-Z order ->yellowShirt = featured product

def featured_product(products):
    freq={}

    for p in products:
        freq[p] = freq.get(p, 0) + 1

    max_freq = max(freq.values())
    final = [p for p  in freq if freq[p] == max_freq]
    final.sort()
    return final[-1]

'''
if __name__ == "__main__":
    products_count = int(input().strip())
    products = []
    for _ in range(products_count):
        products_item = input()
        products.append(products_item)
    
    result = featured_product(products)
    print(result)
'''
print(featured_product(products1))
print(featured_product(products2))