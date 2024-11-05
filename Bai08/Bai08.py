import numpy as np
def combine_rooms(room_1, room_2):
    final_list = []
    for i in range(len(room_1)):
        if room_1[i] > 0:
            final_list.append(room_1[i])
        elif room_2[i] > 0:
            final_list.append(room_2[i])
        else:
            final_list.append(None)
    return final_list
room_1 = np.array([1, 2, -3, 4, 5, 6, -7])
room_2 = np.array([8, 9, 10, 11, 12, -13, -14])
print("Danh sách thí sinh cuối cùng:", combine_rooms(room_1, room_2))