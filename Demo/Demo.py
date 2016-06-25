"""import pypyodbc
# Database connection
print('Trying to connect')
try:
	myConnection = pypyodbc.connect('Driver={SQL Server};'
								    'Server=localhost;'
								    'Database=Trauma2;'
                                    'uid=Rodolfo;pwd=Trauma2')
	print('Connected')

except:
	print('Could not connect')"""



def main():
	tableName = input('Table name: ')

	if tableName == 'AcctHist':
		createClassAcctHist()
	elif tableName == 'ADM_INPT':
		createClassAdm_inpt()
	elif tableName == 'BURNS': 
		createClassBurns()
	elif tableName == 'comments': 
		createClassComments() 
	elif tableName == 'CULTURE': 
		createClassCulture()
	elif tableName == 'dellog': 
		createClassDellog()
	elif tableName == 'DIAGS': 
		createClassDiags()
	elif tableName == 'EMERG':
	    createClassEmerg()
	elif tableName == 'FINANCE': 
		createClassFinance()
	elif tableName == 'FLDDETAI': 
		createClassFlddetai()
	elif tableName == 'GENMACH': 
		createClassGenmach()
	elif tableName == 'HEMO': 
		createClassHemo()
	elif tableName == 'HOSPREV':
		createClassHosprev()
	elif tableName == 'ICU':
		createClassIcu()
	elif tableName == 'INJDETS':
		createClassInjdets()
	elif tableName == 'INJDIAG':
		createClassInjdiag()
	elif tableName == 'INJMECH':
		createClassInjmech()
	elif tableName == 'LAB':
		createClassLab()
	elif tableName == 'MAINDATA':
		createClassMaindata()
	elif tableName == 'MORTDETS':
		createClassMortdets()
	elif tableName == 'MTOS':
		createClassMtos()
	elif tableName == 'NARRATIV':
		createClassNarrativ()
	elif tableName == 'OPRM':
		createClassOprm()
	elif tableName == 'ORGANS':
		create

def createClassAcctHist():
    # Creating class
    dois = 'falou'
    print (dois)

"""class AcctHist:
				def __init__(self, patientId, task, timestamp, otherAttributes):
					self.patientId = patientId
					self.task = task
					self.timestamp = timestamp
					self.otherAttributes = otherAttributes

    myCursor = myConnection.cursor()
	SQLSelectCommand = "SELECT * \
						FROM '%s'"  % (tableName)

    # Getting tuples
	try:
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()
		for row in results:


	except:
		print "ERROR: unable to fetch data"

	myConnection.close()
  	myCursor.close()

def filter():

def output2File():"""


if __name__ == '__main__':
	main()