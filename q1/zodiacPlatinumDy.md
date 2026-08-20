**Name:** Shaun Rodric B. Dy
**Section:** 9 - Platinim
**Last Name:** Dy
**Date:** August 20, 2026

def get_chinese_zodiac():
    
zodiac_signs = [
  "Rat (鼠 / Shǔ)",
  "Ox (牛 / Niú)",
  "Tiger (虎 / Hǔ)",
  "Rabbit (兔 / Tù)",
  "Dragon (龙 / Lóng)",
  "Snake (蛇 / Shé)",
  "Horse (马 / Mǎ)",
  "Goat (羊 / Yáng)",
  "Monkey (猴 / Hóu)",
  "Rooster (鸡 / Jī)",
  "Dog (狗 / Gǒu)",
  "Pig (猪 / Zhū)"
  ]

  user_input = input("Enter your birth year: ")

  if not user_input.isdigit() or int(user_input) < 1900:
        print("Invalid Year, it should not be earlier than 1900")
        return

  birth_year = int(user_input)
  zodiac_index = (birth_year - 1900) % 12
  result_sign = zodiac_signs[zodiac_index]

  print(f"Your Chinese Zodiac Sign is: {result_sign}")

if __name__ == "__main__":
    get_chinese_zodiac()
