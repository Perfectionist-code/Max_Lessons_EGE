# with open('04.txt') as file:
#     n = int(file.readline())
#     cars = []
#     for s in file:
#         start_parking, parking_duration, car_class = s.split()
#         cars.append((int(start_parking), int(start_parking) + int(parking_duration), car_class))
# cars.sort()
# parking = [0] * 100
# cars_wo_parking = 0
# minibus_cnt = 0
# for start_parking, end_parking, car_class in cars:
#     if car_class == 'A':
#         for i, end_parking_time in enumerate(parking):
#             if end_parking_time <= start_parking:
#                 parking[i] = end_parking
#                 break
#         else:
#             cars_wo_parking += 1
#     else:
#         for i, end_parking_time in enumerate(parking[70:], 70):
#             if end_parking_time <= start_parking:
#                 parking[i] = end_parking
#                 minibus_cnt += 1
#                 break
#         else:
#             cars_wo_parking += 1
# print(minibus_cnt, cars_wo_parking)

with open('04.txt') as file:
    n = int(file.readline())
    cars = []
    for s in file:
        start_parking, parking_duration, car_class = s.split()
        cars.append((int(start_parking), int(start_parking) + int(parking_duration), car_class))
cars.sort()
parking = [0] * 100
cars_wo_parking = 0
minibus_cnt = 0
for start_parking, end_parking, car_class in cars:
    p = (70,0)[car_class == 'A']
    # p = 0 if car_class == 'A' else 70 # как вариант
    for i, end_parking_time in enumerate(parking[p:], p):
        if end_parking_time <= start_parking:
            parking[i] = end_parking
            if p:
                minibus_cnt +=1
            break
    else:
        cars_wo_parking += 1

print(minibus_cnt, cars_wo_parking)