def calculate_love_score(name1, name2):
    truelove = 'TRUELOVE'
    freq = [0 for _ in truelove]

    for nc in (name1 + name2).upper():  # nc = name_char
        for i, tc in enumerate(truelove):  # tc = truelove_char
            if nc == tc:
                freq[i] += 1

    true_score = 0
    for i in freq[:4]:
        true_score += i

    love_score = 0
    for i in freq[4:]:
        love_score += i

    print(str(true_score) + str(love_score))


"""
I coded this exercise initially to use a dictionary, but then realized the course had
not introduced them yet. However, I'll leave it here for you to check out.
"""
# def calculate_love_score(name1, name2):
#     truelove = {
#         'T': 0,
#         'R': 0,
#         'U': 0,
#         'E': 0,
#         'L': 0,
#         'O': 0,
#         'V': 0,
#     }
#
#     for c in (name1 + name2).upper():
#         if c in truelove:
#             truelove[c] += 1
#
#     true_score = 0
#     for c in 'TRUE':
#         if truelove[c]:
#             true_score += truelove[c]
#
#     love_score = 0
#     for c in 'LOVE':
#         if truelove[c]:
#             love_score += truelove[c]
#
#     print(str(true_score) + str(love_score))


# Output should equal '53'
calculate_love_score('Angela Yu', 'Jack Bauer')

# Output should equal '42'
calculate_love_score('Kanye West', 'Kim Kardashian')
