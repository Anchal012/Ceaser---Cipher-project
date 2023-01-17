from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

should_continue= True
while should_continue:
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt: ")
  text = input("\nType your message:\n").lower()
  shift = int(input("\nType the shift number: "))

  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  result = input("\nType 'yes' if you want to go again. Otherwise type 'no': ")
  if result == 'no':
    should_continue = False
    print("Good Bye!")
  