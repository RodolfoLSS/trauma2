def main():
	tableName = input('Table name: ')

	if tableName == 'AcctHist':
		getTuplesFromAcctHist()
	elif tableName == 'ADM_INPT':
		getTuplesFromAdm_inpt()
	elif tableName == 'BURNS': 
		getTuplesFromBurns()
	elif tableName == 'comments': 
		getTuplesFromComments() 
	elif tableName == 'CULTURE': 
		getTuplesFromCulture()
	elif tableName == 'dellog': 
		getTuplesFromDellog()
	elif tableName == 'DIAGS': 
		getTuplesFromDiags()
	elif tableName == 'EMERG':
	    getTuplesFromEmerg()
	elif tableName == 'FINANCE': 
		getTuplesFromFinance()
	elif tableName == 'FLDDETAI': 
		getTuplesFromFlddetai()
	elif tableName == 'GENMACH': 
		getTuplesFromGenmach()
	elif tableName == 'HEMO': 
		getTuplesFromHemo()
	elif tableName == 'HOSPREV':
		getTuplesFromHosprev()
	elif tableName == 'ICU':
		getTuplesFromIcu()
	elif tableName == 'INJDETS':
		getTuplesFromInjdets()
	elif tableName == 'INJDIAG':
		getTuplesFromInjdiag()
	elif tableName == 'INJMECH':
		getTuplesFromInjmech()
	elif tableName == 'LAB':
		getTuplesFromLab()
	elif tableName == 'MAINDATA':
		getTuplesFromMaindata()
	elif tableName == 'MORTDETS':
		getTuplesFromMortdets()
	elif tableName == 'MTOS':
		getTuplesFromMtos()
	elif tableName == 'NARRATIV':
		getTuplesFromNarrativ()
	elif tableName == 'OPRM':
		getTuplesFromOprm()
	elif tableName == 'ORGANS':
		getTuplesFromOrgans()
	elif tableName == 'PERHIST':
		getTuplesFromPerhist()
	elif tableName == 'POSTHOSP':
		getTuplesFromPosthosp()
	elif tableName == 'PRECONDS':
		getTuplesFromPreconds()
	elif tableName == 'PROTECT':
		getTuplesFromProtect()
	elif tableName == 'QAISSUE':
		getTuplesFromQaissue()
	elif tableName == 'RADIOLOG':
		getTuplesFromRadiolog()
	elif tableName == 'READMIT':
		getTuplesFromReadmit()
	elif tableName == 'STEP':
		getTuplesFromStep()
	elif tableName == 'SURG':
		getTuplesFromSurg()
	elif tableName == 'sysdefs':
		getTuplesFromSysdefs()
	elif tableName == 'TLogComm':
		getTuplesFromTLogComm()
	elif tableName == 'TOXIANAL':
		getTuplesFromToxianal()
	elif tableName == 'TRA':
		getTuplesFromTra()
	elif tableName == 'tranlog':
		getTuplesFromTranlog()
	elif tableName == 'TRANSFER':
		getTuplesFromTransfer()
	elif tableName == 'TRANSPRT':
		getTuplesFromTransprt()
	elif tableName == 'TREATMEN':
		getTuplesFromTreatmen()
	elif tableName == 'TRICRIT':
		getTuplesFromTricrit()
	elif tableName == 'TRMTEAM':
		getTuplesFromTrmteam()
	elif tableName == 'TTDETLS':
		getTuplesFromTtdetls()
	elif tableName == 'VITALS':
		getTuplesFromVitals()
	elif tableName == 'WARD':
		getTuplesFromWard()
	else: 
		print ('Type a valid table name.\n')

	myConnection.close()
	myCursor.close()

def getTuplesFromAcctHist():
	print ('Testing AcctHist!') 
	myCursor = myConnection.cursor()
	SQLSelectCommand = "SELECT * \
						FROM TRAUMA2.AcctHist"
	# Getting tuples
	numberOfTuples = 0
	try:
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()
		for row in results:
			patient[numberOfTuples] = Tuples(str(row[0]), 'AcctHist', str(row[2]), 'acctno = ' + str(row[1]) + ', acttime = ' + str(row[3]) + ', action = ' + str(row[4]) + ', acuser = ' + str(row[5]) + ', acstation = ' + str(row[6]))
			numberOfTuples = numberOfTuples + 1
	except:
		print ("ERROR: unable to fetch data")

def getTuplesFromAdm_inpt():
	print('Testing ADM_INPT!') 

	myCursor = myConnection.cursor()
	SQLSelectCommand = "SELECT * \
						FROM TR02_TRANS.ADM_INPT" 
	
    # Getting tuples
	numberOfTuples = 0
	try:
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()
		for row in results:
			patient[numberOfTuples] = Tuples(str(row[34]), 'ADM_INPT', str(row[2]), 'PT_LOCAT = ' + str(row[0]) + ', ROOM_NO = ' + str(row[1]) + ', DATE_OUT = ' + str(row[3]) + ', PROVDER_IN = ' + str(row[4]) + ', LOS_IN = ' + str(row[5]) + ', CAREPHASE = ' + str(row[6]) + ', DUMFLD1 = ' + str(row[7]) + ', DUMFLD2 = ' + str(row[8]) + ', DUMFLD3 = ' + str(row[9]) + ', DUMFLD4 = ' + str(row[10]) + ', DUMFLD5 = ' + str(row[11]) + ', DUMFLD6 = ' + str(row[12]) + ', DUMFLD7 = ' + str(row[13]) + ', DUMFLD8 = ' + str(row[14]) + ', DUMFLD9 = ' + str(row[15]) + ', DUMFLD10 = ' + str(row[16]) + ', DUMFLD11 = ' + str(row[17]) + ', DUMFLD12 = ' + str(row[18]) + ', DUMFLD13 = ' + str(row[19]) + ', DUMFLD14 = ' + str(row[20]) + ', DUMFLD15 = ' + str(row[21]) + ', DUMFLD16 = ' + str(row[22]) + ', DUMFLD17 = ' + str(row[23]) + ', DUMFLD18 = ' + str(row[24]) + ', DUMFLD19 = ' + str(row[25]) + ', DUMFLD20 = ' + str(row[26]) + ', INPT_SER = ' + str(row[27]) + ', ACCTNO = ' + str(row[28]),  + ', DE_STATUS = ' + str(row[29]),  + ', DECOMMFLAG = ' + str(row[30]) + ', PARENTID = ' + str(row[31]) + ', PARENTREC = ' + str(row[32]),  + ', COPYNO = ' + str(row[33]))
			numberOfTuples = numberOfTuples + 1
	except:
		print ("ERROR: unable to fetch data")

def getTuplesFromBurns():
	print('Testing BURNS!') 

	myCursor = myConnection.cursor()
	SQLSelectCommand = "SELECT * \
						FROM TR02_TRANS.BURNS" 
	
    # Getting tuples
	numberOfTuples = 0
	try:
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()
		for row in results:
			patient[numberOfTuples] = Tuples(str(row[30]), 'BURNS', str(row[2]), 'PT_LOCAT = ' + str(row[0]) + ', ROOM_NO = ' + str(row[1]) + ', DATE_OUT = ' + str(row[3]) + ', PROVDER_IN = ' + str(row[4]) + ', LOS_IN = ' + str(row[5]) + ', CAREPHASE = ' + str(row[6]) + ', DUMFLD1 = ' + str(row[7]) + ', DUMFLD2 = ' + str(row[8]) + ', DUMFLD3 = ' + str(row[9]) + ', DUMFLD4 = ' + str(row[10]) + ', DUMFLD5 = ' + str(row[11]) + ', DUMFLD6 = ' + str(row[12]) + ', DUMFLD7 = ' + str(row[13]) + ', DUMFLD8 = ' + str(row[14]) + ', DUMFLD9 = ' + str(row[15]) + ', DUMFLD10 = ' + str(row[16]) + ', DUMFLD11 = ' + str(row[17]) + ', DUMFLD12 = ' + str(row[18]) + ', DUMFLD13 = ' + str(row[19]) + ', DUMFLD14 = ' + str(row[20]) + ', DUMFLD15 = ' + str(row[21]) + ', DUMFLD16 = ' + str(row[22]) + ', DUMFLD17 = ' + str(row[23]) + ', DUMFLD18 = ' + str(row[24]) + ', DUMFLD19 = ' + str(row[25]) + ', DUMFLD20 = ' + str(row[26]) + ', INPT_SER = ' + str(row[27]) + ', ACCTNO = ' + str(row[28]),  + ', DE_STATUS = ' + str(row[29]),  + ', DECOMMFLAG = ' + str(row[30]) + ', PARENTID = ' + str(row[31]) + ', PARENTREC = ' + str(row[32]),  + ', COPYNO = ' + str(row[33]))
			numberOfTuples = numberOfTuples + 1					#NOT READYY
	except:
		print ("ERROR: unable to fetch data")
"""
def filter():

def output2File():
"""
if __name__ == '__main__':
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

	class Tuples:
		def __init__(self, patientId, task, timestamp, otherAttributes):
			self.patientId = patientId
			self.task = task
			self.timestamp = timestamp
			self.otherAttributes = otherAttributes
	main()