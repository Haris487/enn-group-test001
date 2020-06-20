from calculator import Calculator

def test1():

	pricing_rules = [
		dict(lead_code = "b" , price = 10 , bonus_rules = lambda qty,tot : 10 if qty > 5 else 0),
		dict(lead_code = "r" , price = 5, bonus_rules = lambda qty,tot : tot * 0.1 if qty > 8 else 0),
		dict(lead_code = "st" , price = 2.5 )
	]

	calculator = Calculator(pricing_rules)

	calculator.add("b")
	calculator.add("b")
	calculator.add("b")
	calculator.add("b")
	calculator.add("b")
	calculator.add("b")
	calculator.add("r")
	calculator.add("r")
	calculator.add("st")

	total = calculator.total()
	assert total == 82.5 
	print("test1 sucessfull total = " , total)

def test2():
	pricing_rules = [
		dict(lead_code = "b" , price = 10 , bonus_rules = lambda qty,tot : 10 if qty > 5 else 0),
		dict(lead_code = "r" , price = 5, bonus_rules = lambda qty,tot : tot * 0.1 if qty > 8 else 0),
		dict(lead_code = "st" , price = 2.5 )
	]

	calculator = Calculator(pricing_rules)

	calculator.add("b")
	calculator.add("r")
	calculator.add("r")
	calculator.add("r")
	calculator.add("r")
	calculator.add("r")
	calculator.add("r")
	calculator.add("r")
	calculator.add("r")
	calculator.add("r")
	calculator.add("r")

	total = calculator.total()
	assert total == 65
	print("test2 sucessfull total = " , total)


test1()
test2()
