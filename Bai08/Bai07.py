import numpy as np
import random
sales = np.array([[random.randint(50, 150) for _ in range(7)] for _ in range(2)])
print("Số lượng hàng bán ra trong tuần:")
print(sales)
max_day = -1
max_sales = 0
for day in range(7):
    total_sales = sales[0][day] + sales[1][day]
    if total_sales > max_sales:
        max_sales = total_sales
        max_day = day + 1
print(f"Ngày bán được nhiều hàng nhất là ngày {max_day} với tổng số lượng {max_sales}.")
max_session = ""
max_day_session = -1
max_session_sales = 0
for session in range(2):
    for day in range(7):
        if sales[session][day] > max_session_sales:
            max_session_sales = sales[session][day]
            max_session = "sáng" if session == 0 else "chiều"
            max_day_session = day + 1
print(f"Thời điểm bán được nhiều nhất là buổi {max_session}, ngày {max_day_session}, với số lượng {max_session_sales}.")
morning_better = 0
afternoon_better = 0
for day in range(7):
    if sales[0][day] > sales[1][day]:
        morning_better += 1
    elif sales[0][day] < sales[1][day]:
        afternoon_better += 1
if morning_better > afternoon_better:
    trend = "Buổi sáng bán nhiều hơn buổi chiều."
elif morning_better < afternoon_better:
    trend = "Buổi chiều bán nhiều hơn buổi sáng."
else:
    trend = "Cả hai buổi bán như nhau."
print(trend)