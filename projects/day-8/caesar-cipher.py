import string

alphabet = list(string.ascii_lowercase)


def caesar(text, shift, code):
    s = ''

    if code == 'decode':
        shift *= -1

    for c in text:
        if c in alphabet:
            i = (alphabet.index(c) + shift) % len(alphabet)
            s += alphabet[i]
        else:
            s += c

    print(s)


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input('Enter your message:\n').lower()
    shift = int(input('Enter the shift number:\n'))

    caesar(text, shift, direction)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise, type 'no'\n"
    ).lower()
    if restart == 'no':
        should_continue = False
        print('Bye.')
