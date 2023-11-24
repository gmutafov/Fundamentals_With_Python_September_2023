pieces = {}
n = int(input())

for _ in range(n):
    pianist_info = input().split('|')
    piece, composer, key = pianist_info
    pieces[piece] = {'composer': composer, 'key': key}

while True:
    command = input().split('|')
    action = command[0]

    if action == 'Stop':
        break

    piece_name = command[1]
    if action == 'Add':
        composer = command[2]
        key = command[3]
        if piece_name not in pieces:
            pieces[piece_name] = {'composer': composer, 'key': key}
            print(f"{piece_name} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece_name} is already in the collection!")

    elif action == 'Remove':
        if piece_name in pieces:
            del pieces[piece_name]
            print(f'Successfully removed {piece_name}!')
        else:
            print(f"Invalid operation! {piece_name} does not exist in the collection.")

    elif action == 'ChangeKey':
        new_key = command[2]
        if piece_name in pieces:
            old_key = pieces[piece_name]['key']
            pieces[piece_name]['key'] = new_key
            print(f"Changed the key of {piece_name} to {new_key}!")
        else:
            print(f'Invalid operation! {piece_name} does not exist in the collection.')
for piece, info in pieces.items():
    composer = info["composer"]
    key = info['key']
    print(f"{piece} -> Composer: {composer}, Key: {key}")