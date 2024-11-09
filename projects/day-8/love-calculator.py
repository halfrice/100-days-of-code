def calculate_love_score(name1, name2):
    truelove = {
        'T': 0,
        'R': 0,
        'U': 0,
        'E': 0,
        'L': 0,
        'O': 0,
        'V': 0,
    }

    for c in (name1 + name2).upper():
        if c in truelove.keys():
            truelove[c] += 1

    true_score = 0
    for c in 'TRUE':
        if truelove[c]:
            true_score += truelove[c]

    love_score = 0
    for c in 'LOVE':
        if truelove[c]:
            love_score += truelove[c]

    print(str(true_score) + str(love_score))


# Output should equal '42'
calculate_love_score('Kanye West', 'Kim Kardashian')
