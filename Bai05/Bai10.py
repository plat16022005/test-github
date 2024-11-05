def filter_speeds(speeds, min_value):
    result = []
    for i, speed in enumerate(speeds):
        if speed < min_value:
            result.append((speed, i))
    return result
speeds = []
min_value = int(input("Nhập giá trị nhỏ: "))
while True:
    x = input("Nhập tốc độ quay (Không nhập gì và nhấn enter để kết thúc): ")
    if x == "":
        break
    speeds.append(int(x))
filtered_speeds = filter_speeds(speeds, min_value)
print(filtered_speeds)