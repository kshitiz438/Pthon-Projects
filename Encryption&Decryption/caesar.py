from logo import logo


def caesar(start_text, shift_amount, start_direction):
    end_text = ""
    if start_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {start_direction}d text is {end_text}. ")


print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue:
    direction = input("Enter 'encode' to Encrypt, 'decode' to Decrypt:\n")
    text = input("Enter the text to encrypt:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(text, shift, direction)
    replay = input("Enter 'yes' to replay and 'no' to quit.\n")
    if replay == "no":
        should_continue = False
