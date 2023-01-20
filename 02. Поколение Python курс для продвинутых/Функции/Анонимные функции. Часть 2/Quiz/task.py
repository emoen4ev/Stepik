# # import requests
# # from bs4 import BeautifulSoup
# # import csv
# #
# # url = 'https://www.borotrade.com/bg/products/'
# # response = requests.get(url)
# #
# # soup = BeautifulSoup(response.text, 'html.parser')
# #
# # items = soup.find_all('div', class_='product-item')
# #
# # with open('data.csv', 'w', newline='') as file:
# #     writer = csv.writer(file)
# #     writer.writerow(['КАТ. №', 'Цена'])
# #     for item in items:
# #         number = item.find('div', class_='product-item-number').text
# #         price = item.find('span', class_='price').text
# #         writer.writerow([number, price])
#
# import requests
# from bs4 import BeautifulSoup
# import openpyxl
#
# # URL of the website to scrape
# url = 'https://www.borotrade.com/bg/products/'
#
# # Send a GET request to the website
# response = requests.get(url)
#
# # Parse the HTML content of the website
# soup = BeautifulSoup(response.content, 'html.parser')
#
# # Create a new Excel workbook
# workbook = openpyxl.Workbook()
# worksheet = workbook.active
#
# # Add headers to the worksheet
# worksheet.append(['Product Number', 'Price'])
#
# # Find all product cards on the webpage
# for product_card in soup.find_all('div', class_='product-name'):
#     # Find the product number
#     product_number = product_card.find('span', class_='product-code').text
#
#     # Find the price of the product
#     price = product_card.find('div', class_='product-card__price').text
#
#     # Add the data to the worksheet
#     worksheet.append([product_number, price])
#
# # Save the workbook
# workbook.save('products.xlsx')
#
# # 16299500
# #
# # 16299500
# # /html/body/div[4]/div[1]/div[3]/div/div/div[2]/div[6]/div[1]/div[1]/span/strong/text()
# # /html/body/div[4]/div[1]/div[3]/div/div/div[2]/div[6]/div[1]/div[1]/span/strong/text()