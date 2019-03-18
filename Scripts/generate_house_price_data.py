import csv
import random

IS_DEBUG_MODE = True
BASE_HOUSE_PRICE = 100

# function to generate house price with variance
def generate_house_price(bedroom_count: int) -> int:
  variance_start = -(random.randint(0,33))
  variance_end = random.randint(0,33)
  variance = random.randint(variance_start, variance_end)
  house_price = BASE_HOUSE_PRICE + (bedroom_count * 50) + variance
  if IS_DEBUG_MODE:
    print('Variance between (',variance_start,'...', variance_end,') is ', variance)
    print('Bedrooms: ', bedroom_count,' Price= ', house_price)
	
  return house_price

#bedroom_cnt = random.randint(1,10)
#print(generate_house_price(bedroom_cnt))

with open('Data/house_price_data.csv', 'w', newline='') as csvfile:
  csvFileWriter =  csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
  csvFileWriter.writerow(['#', 'Bedrooms', 'Price'])
  for itr in range(1, 100):
    bdrm_count = random.randint(1,10)
    csvFileWriter.writerow([itr, bdrm_count, generate_house_price(bdrm_count)])