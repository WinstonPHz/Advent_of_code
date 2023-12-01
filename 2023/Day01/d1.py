
def part1(puz_string):
  ans1 = 0
  for line in puz_string:
    digits = get_digits(line)
    ans1 += int(digits)
  print(f"Answer 1: {ans1}")

def get_digits(some_string):
  numbers = ["1","2","3","4","5","6","7","8","9"]
  for char in some_string:
    if char in numbers:
      d1 = char
      break
  for char in some_string[::-1]:
    if char in numbers:
      d2 = char
      break
  hex = d1 + d2
  return hex

def check_segment(segment):
  number_conversion = { "one":'o1e', "two":"t2o", "three":"th3ee", "four":"fo4ur", "five":"fi5ve", "six":"si6x", "seven":"sev7en", "eight":"ei8ght", "nine":"9"}
  for key, value in number_conversion.items():
    if key in segment:
      return True, key, value
  return False, 0, 0

def part2(puz_string):
  cum_sum = 0
  for line in puz_string:
    while True:
      old = line
      for i in range(len(line) - 4):
        line_segment = line[i:i + 5]
        check_bool, number, to_repalce = check_segment(line_segment)
        if check_bool:
          nl = line_segment.replace(number, to_repalce)
          line = line.replace(line_segment, nl, 1)
          break
      if old == line:
        break

    digits = get_digits(line)
    cum_sum += int(digits)
  print("Answer 2", cum_sum)




puz_string = []
with open("input.txt", "r") as file:
  for line in file:
    line = line.strip('\n')
    puz_string.append(line)

part1(puz_string)
part2(puz_string)

# 53592

