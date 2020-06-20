class LeadCode():
	"""docstring for LeadCode"""
	def __init__(self, name, val , bonusRules=None):
		self.name = name
		self.val = val
		self.bonusRules = bonusRules
		self.qty = 0

	def total(self):
		total = self.val * self.qty
		if self.bonusRules is not None:
			return total + self.bonusRules(self.qty,total)
		else:
			return total

	def add(self):
		self.qty = self.qty + 1
		

class Calculator():
	"""docstring for Calculator"""
	def __init__(self, pricing_rules):
		self.rules = {}
		for rule in pricing_rules:
			leadName = rule.get("lead_code")
			leadVal = rule.get("price")
			leadBonusRules = rule.get("bonus_rules",None)
			self.rules[leadName] = LeadCode(leadName,leadVal,leadBonusRules)

	def add(self,leadName):
		leadCode = self.rules[leadName]
		leadCode.add()

	def total(self):
		total = 0
		for rule in self.rules.items():
			leadCode = rule[1]
			total = total + leadCode.total()

		return total
	
		