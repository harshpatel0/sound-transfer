
def to_string(binary_list):
  output = ""
  uppercase = False

  count = 0
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
  for binary in binary_list:

    case_identifier = str(binary[:3])
    value = str(binary[3:])
    if case_identifier == '010':
      uppercase = True

    for digit, bit in enumerate(value):
      # print(f"Digit: {digit}, Bit: {bit}")

      if bit == "1":
        if digit == 0:
          count = count + 16
        if digit == 1:
          count = count + 8
        if digit == 2:
          count = count + 4
        if digit == 3:
          count = count + 2
        if digit == 4:
          count = count + 1

    count = count - 1
    corresponding_letter = alphabet[count]

    # print("CORRESPONDING_LETTER ", corresponding_letter)
    # print("count ", count)

    if uppercase == True:
      corresponding_letter = corresponding_letter.upper()
    output = output + corresponding_letter

    count = 0
    uppercase = False
  
  return output


def to_binary_list(binary):
  binary_list = []

  while True:
    binary_list.append(binary[:8])
    binary = binary[8:]
    if binary == '':
      break
  
  return binary_list

def to_binary(string):
  res = ''.join(format(ord(i), '08b') for i in string)
  # print(str(res))
  return to_binary_list(str(res))


if __name__ == "__main__":
  test_binary = ['01000011', '01100001', '01101011', '01100101']

  print(to_string(test_binary))
  print(to_binary("Cake"))