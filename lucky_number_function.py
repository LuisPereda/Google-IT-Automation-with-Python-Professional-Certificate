def lucky_number(name):
  number = len(name) * 9
  fortune = "Hello " + name + ". Your lucky number is " + str(number)
  return fortune
	    
print(lucky_number("Kay"))
print(lucky_number("Cameron"))