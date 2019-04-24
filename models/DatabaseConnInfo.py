class DatabaseConnInfo:
	def __init__(self, config):
		self.host = config["host"]
		self.user = config["user"]
		self.password = config["password"]
		self.database = config["database"]