while True:
  user_input = input()

  if user_input == 'exit':
    break

  decimal = int(user_input)

  if decimal == 0:
    print(0)
    continue

  binary_result = ''

  while decimal > 0:
    remainder = decimal % 2
    binary_result = str(remainder) + binary_result
    decimal = decimal // 2

  print(binary_result)
