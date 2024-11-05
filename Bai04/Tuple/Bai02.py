input_data = []
while True:
    user_input = input("Nhập vào (name, age, score) hoặc nhấn Enter để dừng: ")
    if not user_input:
        break
    input_data.append(tuple(user_input.split(',')))
sorted_data = sorted(input_data, key=lambda input_data: (input_data[0], int(input_data[1]), int(input_data[2])))
print("Danh sách đã sắp xếp:", sorted_data)