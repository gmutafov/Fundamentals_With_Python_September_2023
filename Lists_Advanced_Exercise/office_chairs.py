def checking_rooms(numbers_of_rooms):
    free_chairs = 0
    for number_of_rooms in range(1, numbers_of_rooms + 1):
        free_chairs_in_room, visitors = input().split()
        difference = len(free_chairs_in_room) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {number_of_rooms}")
        free_chairs += difference
    return free_chairs


count_of_rooms = int(input())
total_free_chairs = checking_rooms(count_of_rooms)

if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")