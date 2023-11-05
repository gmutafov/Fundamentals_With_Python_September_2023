n = int(input())
parking_lot = {}

for _ in range(n):
    command = input().split()
    action, name = command[0], command[1]
    if action == 'register':
        license_plate = command[2]
        if name in parking_lot.keys():
            print(f"ERROR: already registered with plate number: {license_plate}")
        else:
            parking_lot[name] = license_plate
            print(f"{name} registered {license_plate} successfully")

    elif action == 'unregister':
        if name not in parking_lot.keys():
            print(f"ERROR: user {name} not found")
        else:
            parking_lot.pop(name)
            print(f"{name} unregistered successfully")

for username, license_plate_number in parking_lot.items():
    print(f"{username} => {license_plate_number}")