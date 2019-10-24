import os, datetime, shutil

class SQLDumpService:
	def __init__(self, appRoot, dbConnInfo):
		self.appRoot = appRoot
		self.dbConnInfo = dbConnInfo

	def dump(self):
		self.__checkTmpPath__()
		dmpPath = self.__dumpMySqlDatabase__()
		return dmpPath

	def __checkTmpPath__(self):
		shutil.rmtree(os.path.join(self.appRoot, 'tmp'))
		if (os.path.isdir(os.path.join(self.appRoot, 'tmp')) == False):
			os.mkdir(os.path.join(self.appRoot, 'tmp'))

	def __dumpMySqlDatabase__(self):
		dmpPath = "{0}/tmp/{1}_{2}.sql".format(self.appRoot, self.dbConnInfo.database, datetime.datetime.now().strftime("%m%d%Y%H%M%S"))

		dumpcmd = "mysqldump -u {0} -p{1} {2} > {3}".format(self.dbConnInfo.user, self.dbConnInfo.password, self.dbConnInfo.database, dmpPath)
		os.system(dumpcmd)

		return dmpPath