def main():
	import pypyodbc
	import sys

	# Database connection
	print('Trying to connect to the database...')

	try:
		myConnection = pypyodbc.connect('Driver={SQL Server};'
									'Server=localhost;'
									'Database=Trauma2;'
									'uid=Rodolfo;pwd=Trauma2')
		myCursor = myConnection.cursor()
		print('Connected.')
	except:
		print('Could not connect:', sys.exc_info()[0])

	tableName = input('Table name: ')

	if tableName == 'AcctHist':
		getTuplesFromAcctHist(myCursor)
	elif tableName == 'ADM_INPT':
		getTuplesFromAdm_inpt(myCursor)
	elif tableName == 'BURNS': 
		getTuplesFromBurns(myCursor)
	elif tableName == 'comments': 
		getTuplesFromComments(myCursor) 
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

def getTuplesFromAcctHist(myCursor):
	print ('Testing AcctHist!') 

	# Getting tuples
	numberOfTuples = 0

	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TRAUMA2.AcctHist')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()
		#print(results)
		#print(results[0], results[1], results[2], results[3], results[4], results[5])
		#id = str(results[0])
		#print(type(results[0]))
		#print(type(id))
		#patient[numberOfTuples] = Tuples(str(results[0]), 'AcctHist', str(results[2]), 'acctno = ' + str(results[1]) + ', acttime = ' + str(results[3]) + ', action = ' + str(results[4]) + ', acuser = ' + str(results[5]) + ', acstation = ' + str(results[6]))
		#print ('Id: %s, timestamp: %s, task: %s, otherAttributes: %s' % patient[numberOfTuples].patientId, patient[numberOfTuples].timestamp, patient[numberOfTuples].task, patient[numberOfTuples].otherAttributes)
			
		for row in results:
			patient[numberOfTuples] = Tuples(str(row[0]), 'AcctHist', str(row[2]), 'acctno = ' + str(row[1]) + ', acttime = ' + str(row[3]) + ', action = ' + str(row[4]) + ', acuser = ' + str(row[5]) + ', acstation = ' + str(row[6]))
			print ('Id: %s, timestamp: %s, task: %s, otherAttributes: %s' % patient[numberOfTuples].patientId, patient[numberOfTuples].timestamp, patient[numberOfTuples].task, patient[numberOfTuples].otherAttributes)
			numberOfTuples = numberOfTuples + 1
	except:
		print ("ERROR: unable to fetch data")

def getTuplesFromAdm_inpt(myCursor):
	print('Testing ADM_INPT!') 
	
    # Getting tuples
	numberOfTuples = 0
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.ADM_INPT')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()
		for row in results:
			patient[numberOfTuples] = Tuples(str(row[34]), 'ADM_INPT', str(row[2]), 'PT_LOCAT = ' + str(row[0]) + ', ROOM_NO = ' + str(row[1]) + ', DATE_OUT = ' + str(row[3]) + ', PROVDER_IN = ' + str(row[4]) + ', LOS_IN = ' + str(row[5]) + ', CAREPHASE = ' + str(row[6]) + ', DUMFLD1 = ' + str(row[7]) + ', DUMFLD2 = ' + str(row[8]) + ', DUMFLD3 = ' + str(row[9]) + ', DUMFLD4 = ' + str(row[10]) + ', DUMFLD5 = ' + str(row[11]) + ', DUMFLD6 = ' + str(row[12]) + ', DUMFLD7 = ' + str(row[13]) + ', DUMFLD8 = ' + str(row[14]) + ', DUMFLD9 = ' + str(row[15]) + ', DUMFLD10 = ' + str(row[16]) + ', DUMFLD11 = ' + str(row[17]) + ', DUMFLD12 = ' + str(row[18]) + ', DUMFLD13 = ' + str(row[19]) + ', DUMFLD14 = ' + str(row[20]) + ', DUMFLD15 = ' + str(row[21]) + ', DUMFLD16 = ' + str(row[22]) + ', DUMFLD17 = ' + str(row[23]) + ', DUMFLD18 = ' + str(row[24]) + ', DUMFLD19 = ' + str(row[25]) + ', DUMFLD20 = ' + str(row[26]) + ', INPT_SER = ' + str(row[27]) + ', ACCTNO = ' + str(row[28]),  + ', DE_STATUS = ' + str(row[29]),  + ', DECOMMFLAG = ' + str(row[30]) + ', PARENTID = ' + str(row[31]) + ', PARENTREC = ' + str(row[32]),  + ', COPYNO = ' + str(row[33]))
			numberOfTuples = numberOfTuples + 1
	except:
		print ("ERROR: unable to fetch data")

def getTuplesFromBurns(myCursor):
	print('Testing BURNS!') 
	
    # Getting tuples
	numberOfTuples = 0
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.BURNS')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()
		for row in results:
			patient[numberOfTuples] = Tuples(str(row[30]), 'BURNS', 'NULL', 'PART_BURN = ' + str(row[0]) + ', PERC_BURN = ' + str(row[1]) + ', PHASE_COPY = ' + str(row[2]) + ', CAREPHASE = ' + str(row[3]) + ', DUMFLD1 = ' + str(row[4]) + ', DUMFLD2 = ' + str(row[5]) + ', DUMFLD3 = ' + str(row[6]) + ', DUMFLD4 = ' + str(row[7]) + ', DUMFLD5 = ' + str(row[8]) + ', DUMFLD6 = ' + str(row[9]) + ', DUMFLD7 = ' + str(row[10]) + ', DUMFLD8 = ' + str(row[11]) + ', DUMFLD9 = ' + str(row[12]) + ', DUMFLD10 = ' + str(row[13]) + ', DUMFLD11 = ' + str(row[14]) + ', DUMFLD12 = ' + str(row[15]) + ', DUMFLD13 = ' + str(row[16]) + ', DUMFLD14 = ' + str(row[17]) + ', DUMFLD15 = ' + str(row[18]) + ', DUMFLD16 = ' + str(row[19]) + ', DUMFLD17 = ' + str(row[20]) + ', DUMFLD18 = ' + str(row[21]) + ', DUMFLD19 = ' + str(row[22]) + ', DUMFLD20 = ' + str(row[23]) + ', ACCTNO = ' + str(row[24]),  + ', DE_STATUS = ' + str(row[25]),  + ', DECOMMFLAG = ' + str(row[26]) + ', PARENTID = ' + str(row[27]) + ', PARENTREC = ' + str(row[28]),  + ', COPYNO = ' + str(row[29]))
			numberOfTuples = numberOfTuples + 1	
	except:
		print ("ERROR: unable to fetch data")

def getTuplesFromComments(myCursor):
	print('Testing comments!') 
	
    # Getting tuples
	numberOfTuples = 0
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.comments')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()
		for row in results:
			patientId = str(row[1])
			task = 'comments'
			timestamp = 'NULL'
			otherAttributes = 'fileid = ' + str(row[0]) + ', fieldname = ' + str(row[2]) + ', ccomment = ' + str(row[3]) + ', cimage = ' + str(row[4]) + ', copyno = ' + str(row[5]) + ', acctno = ' + str(row[6])
			#print(patientId, task, timestamp, otherAttributes)
			#patient[numberOfTuples] = Tuples(str(row[1]), 'comments', 'NULL', 'fileid = ' + str(row[0]) + ', fieldname = ' + str(row[2]) + ', ccomment = ' + str(row[3]) + ', cimage = ' + str(row[4]) + ', copyno = ' + str(row[5]) + ', acctno = ' + str(row[6]))
			patient[0] = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			#patient[numberOfTuples] = Tuples(patientId, task, timestamp, otherAttributes)
			#print(patient[numberOfTuples].patientId, patient[numberOfTuples].task, patient[numberOfTuples].timestamp, patient[numberOfTuples].otherAttributes)
			numberOfTuples = numberOfTuples + 1	
	except:
		print ("ERROR: unable to fetch data")
"""
def filter():

def output2File():
"""
if __name__ == '__main__':
	class Tuples:
		def __init__(self, patientId, task, timestamp, otherAttributes):
			self.patientId = patientId
			self.task = task
			self.timestamp = timestamp
			self.otherAttributes = otherAttributes
	main()