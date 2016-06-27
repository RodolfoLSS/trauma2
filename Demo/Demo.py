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
		createClassOrgans()
	elif tableName == 'PERHIST':
		createClassPerhist()
	elif tableName == 'POSTHOSP':
		createClassPosthosp()
	elif tableName == 'PRECONDS':
		createClassPreconds()
	elif tableName == 'PROTECT':
		createClassProtect()
	elif tableName == 'QAISSUE':
		createClassQaissue()
	elif tableName == 'RADIOLOG':
		createClassRadiolog()
	elif tableName == 'READMIT':
		createClassReadmit()
	elif tableName == 'STEP':
		createClassStep()
	elif tableName == 'SURG':
		createClassSurg()
	elif tableName == 'sysdefs':
		createClassSysdefs()
	elif tableName == 'TLogComm':
		createClassTLogComm()
	elif tableName == 'TOXIANAL':
		createClassToxianal()
	elif tableName == 'TRA':
		createClassTra()
	elif tableName == 'tranlog':
		createClassTranlog()
	elif tableName == 'TRANSFER':
		createClassTransfer()
	elif tableName == 'TRANSPRT':
		createClassTransprt()
	elif tableName == 'TREATMEN':
		createClassTreatmen()
	elif tableName == 'TRICRIT':
		createClassTricrit()
	elif tableName == 'TRMTEAM':
		createClassTrmteam()
	elif tableName == 'TTDETLS':
		createClassTtdetls()
	elif tableName == 'VITALS':
		createClassVitals()
	elif tableName == 'WARD':
		createClassWard()
	else: 
		print ('Type a valid table name.\n')

	myConnection.close()
	myCursor.close()

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
						FROM TRAUMA2.AcctHist" 
	
    # Getting tuples
	numberOfTuples = 0
	try:
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()
		for row in results:
			patient[numberOfTuples] = AcctHist()
			patient[numberOfTuples].patientId = str(row[0])
			patient[numberOfTuples].timestamp = str(row[2])
			patient[numberOfTuples].task = ?????
			patient[numberOfTuples].otherAttributes = 'acctno = "' + str(row[1]) + '", acttime = "' + str(row[3]) + '", action = "' + str(row[4]) + '", acuser = "' + str(row[5]) + '", acstation = "' + str(row[6]) + '"'
			numberOfTuples++
	except:
		print "ERROR: unable to fetch data"

def filter():

def output2File():"""


if __name__ == '__main__':
	main()