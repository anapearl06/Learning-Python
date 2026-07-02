daily_sales = [45, 30, 25, 50, 40, 35, 20, 55]

total_cups = (sales for sales in daily_sales if sales > 30)

print(sum(total_cups))