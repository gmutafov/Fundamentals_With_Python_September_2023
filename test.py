n_lines = int(input())
plants = {}
plant_rating = {}
for _ in range(n_lines):
    plant, rarity = input().split('<->')
    plants[plant] = rarity

while True:
    line = input()

    if line == 'Exhibition':
        break

    commands = line.split(': ')

    if commands == 'Rate':
        plant, rating = commands[1].split(' - ')
        rating = int(rating)
