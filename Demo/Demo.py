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
	elif tableName == 'CONSULT': 
		getTuplesFromConsult(myCursor)
	elif tableName == 'CULTURE': 
		getTuplesFromCulture(myCursor)
	elif tableName == 'dellog': 
		getTuplesFromDellog(myCursor)
	elif tableName == 'DIAGS': 
		getTuplesFromDiags(myCursor)
	elif tableName == 'EMERG':
	    getTuplesFromEmerg(myCursor)
	elif tableName == 'FINANCE': 
		getTuplesFromFinance(myCursor)
	elif tableName == 'FLDDETAI': 
		getTuplesFromFlddetai(myCursor)
	elif tableName == 'GENMACH': 
		getTuplesFromGenmach(myCursor)
	elif tableName == 'HEMO': 
		getTuplesFromHemo(myCursor)
	elif tableName == 'HOSPREV':
		getTuplesFromHosprev(myCursor)
	elif tableName == 'ICU':
		getTuplesFromIcu(myCursor)
	elif tableName == 'INJDETS':
		getTuplesFromInjdets(myCursor)
	elif tableName == 'INJDIAG':
		getTuplesFromInjdiag(myCursor)
	elif tableName == 'INJMECH':
		getTuplesFromInjmech(myCursor)
	elif tableName == 'LAB':
		getTuplesFromLab(myCursor)
	elif tableName == 'MAINDATA':
		getTuplesFromMaindata(myCursor)
	elif tableName == 'MORTDETS':
		getTuplesFromMortdets(myCursor)
	elif tableName == 'MTOS':
		getTuplesFromMtos(myCursor)
	elif tableName == 'NARRATIV':
		getTuplesFromNarrativ(myCursor)
	elif tableName == 'OPRM':
		getTuplesFromOprm(myCursor)
	elif tableName == 'ORGANS':
		getTuplesFromOrgans(myCursor)
	elif tableName == 'PERHIST':
		getTuplesFromPerhist(myCursor)
	elif tableName == 'POSTHOSP':
		getTuplesFromPosthosp(myCursor)
	elif tableName == 'PRECONDS':
		getTuplesFromPreconds(myCursor)
	elif tableName == 'PROTECT':
		getTuplesFromProtect(myCursor)
	elif tableName == 'QAISSUE':
		getTuplesFromQaissue(myCursor)
	elif tableName == 'RADIOLOG':
		getTuplesFromRadiolog(myCursor)
	elif tableName == 'READMIT':
		getTuplesFromReadmit(myCursor)
	elif tableName == 'STEP':
		getTuplesFromStep(myCursor)
	elif tableName == 'SURG':
		getTuplesFromSurg(myCursor)
	elif tableName == 'sysdefs':
		getTuplesFromSysdefs(myCursor)
	elif tableName == 'TLogComm':
		getTuplesFromTLogComm(myCursor)
	elif tableName == 'TOXIANAL':
		getTuplesFromToxianal(myCursor)
	elif tableName == 'TRA':
		getTuplesFromTra(myCursor)
	elif tableName == 'tranlog':
		getTuplesFromTranlog(myCursor)
	elif tableName == 'TRANSFER':
		getTuplesFromTransfer(myCursor)
	elif tableName == 'TRANSPRT':
		getTuplesFromTransprt(myCursor)
	elif tableName == 'TREATMEN':
		getTuplesFromTreatmen(myCursor)
	elif tableName == 'TRICRIT':
		getTuplesFromTricrit(myCursor)
	elif tableName == 'TRMTEAM':
		getTuplesFromTrmteam(myCursor)
	elif tableName == 'TTDETLS':
		getTuplesFromTtdetls(myCursor)
	elif tableName == 'VITALS':
		getTuplesFromVitals(myCursor)
	elif tableName == 'WARD':
		getTuplesFromWard(myCursor)
	else: 
		print ('Type a valid table name.\n')

	myConnection.close()
	myCursor.close()

def getTuplesFromAcctHist(myCursor):
	print ('Testing AcctHist!') 

	# Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TRAUMA2.AcctHist')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[0])
			task = 'AcctHist'
			timestamp = str(row[2])
			otherAttributes = 'acctno = ' + str(row[1]) + ', acttime = ' + str(row[3]) + ', action = ' + str(row[4]) + ', acuser = ' + str(row[5]) + ', acstation = ' + str(row[6])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)
			
	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromAdm_inpt(myCursor):
	print('Testing ADM_INPT!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.ADM_INPT')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[34])
			task = 'ADM_INPT'
			timestamp = str(row[2])
			otherAttributes =  'PT_LOCAT = ' + str(row[0]) + ', ROOM_NO = ' + str(row[1]) + ', DATE_OUT = ' + str(row[3]) + ', PROVDER_IN = ' + str(row[4]) + ', LOS_IN = ' + str(row[5]) + ', CAREPHASE = ' + str(row[6]) + ', DUMFLD1 = ' + str(row[7]) + ', DUMFLD2 = ' + str(row[8]) + ', DUMFLD3 = ' + str(row[9]) + ', DUMFLD4 = ' + str(row[10]) + ', DUMFLD5 = ' + str(row[11]) + ', DUMFLD6 = ' + str(row[12]) + ', DUMFLD7 = ' + str(row[13]) + ', DUMFLD8 = ' + str(row[14]) + ', DUMFLD9 = ' + str(row[15]) + ', DUMFLD10 = ' + str(row[16]) + ', DUMFLD11 = ' + str(row[17]) + ', DUMFLD12 = ' + str(row[18]) + ', DUMFLD13 = ' + str(row[19]) + ', DUMFLD14 = ' + str(row[20]) + ', DUMFLD15 = ' + str(row[21]) + ', DUMFLD16 = ' + str(row[22]) + ', DUMFLD17 = ' + str(row[23]) + ', DUMFLD18 = ' + str(row[24]) + ', DUMFLD19 = ' + str(row[25]) + ', DUMFLD20 = ' + str(row[26]) + ', INPT_SER = ' + str(row[27]) + ', ACCTNO = ' + str(row[28]) + ', DE_STATUS = ' + str(row[29]) + ', DECOMMFLAG = ' + str(row[30]) + ', PARENTID = ' + str(row[31]) + ', PARENTREC = ' + str(row[32]) + ', COPYNO = ' + str(row[33])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromBurns(myCursor):
	print('Testing BURNS!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.BURNS')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[30])
			task = 'BURNS'
			timestamp = 'None'
			otherAttributes = 'PART_BURN = ' + str(row[0]) + ', PERC_BURN = ' + str(row[1]) + ', PHASE_COPY = ' + str(row[2]) + ', CAREPHASE = ' + str(row[3]) + ', DUMFLD1 = ' + str(row[4]) + ', DUMFLD2 = ' + str(row[5]) + ', DUMFLD3 = ' + str(row[6]) + ', DUMFLD4 = ' + str(row[7]) + ', DUMFLD5 = ' + str(row[8]) + ', DUMFLD6 = ' + str(row[9]) + ', DUMFLD7 = ' + str(row[10]) + ', DUMFLD8 = ' + str(row[11]) + ', DUMFLD9 = ' + str(row[12]) + ', DUMFLD10 = ' + str(row[13]) + ', DUMFLD11 = ' + str(row[14]) + ', DUMFLD12 = ' + str(row[15]) + ', DUMFLD13 = ' + str(row[16]) + ', DUMFLD14 = ' + str(row[17]) + ', DUMFLD15 = ' + str(row[18]) + ', DUMFLD16 = ' + str(row[19]) + ', DUMFLD17 = ' + str(row[20]) + ', DUMFLD18 = ' + str(row[21]) + ', DUMFLD19 = ' + str(row[22]) + ', DUMFLD20 = ' + str(row[23]) + ', ACCTNO = ' + str(row[24])  + ', DE_STATUS = ' + str(row[25])  + ', DECOMMFLAG = ' + str(row[26]) + ', PARENTID = ' + str(row[27]) + ', PARENTREC = ' + str(row[28])  + ', COPYNO = ' + str(row[29])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromComments(myCursor): # PROBLEM WITH A CHARACTER IN otherAttributes
	print('Testing comments!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.comments')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[1])
			task = 'comments'
			timestamp = 'NULL'
			otherAttributes = 'fileid = ' + str(row[0]) + ', fieldname = ' + str(row[2]) + ', ccomment = ' + str(row[3]) #+ ', cimage = ' + str(results[4]) + ', copyno = ' + str(results[5]) + ', acctno = ' + str(results[6])
			#otherAttributes = 'Teste'
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromConsult(myCursor):
	print('Testing CONSULT!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.CONSULT')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[39])
			task = 'CONSULT'
			timestamp = str(row[1])
			otherAttributes = 'CAREPHASE = ' + str(row[0]) + ', TIME = ' + str(row[2]) + ', PROBLEMS = ' + str(row[3]) + ', CNSLT_DOC = ' + str(row[4]) + ', SPECIALITY = ' + str(row[5]) + ', REQ_DATE = ' + str(row[6]) + ', DOC_REQ = ' + str(row[7]) + ', MMCALL = ' + str(row[8]) + ', PHNE_RSP = ' + str(row[9]) + ', DEP_TIME = ' + str(row[10]) + ', TT_OTHER = ' + str(row[11]) + ', PHASE_COPY = ' + str(row[12]) + ', DUMFLD1 = ' + str(row[13]) + ', DUMFLD2 = ' + str(row[14]) + ', DUMFLD3 = ' + str(row[15]) + ', DUMFLD4 = ' + str(row[16]) + ', DUMFLD5 = ' + str(row[17]) + ', DUMFLD6 = ' + str(row[18]) + ', DUMFLD7 = ' + str(row[19]) + ', DUMFLD8 = ' + str(row[20]) + ', DUMFLD9 = ' + str(row[21]) + ', DUMFLD10 = ' + str(row[22]) + ', DUMFLD11 = ' + str(row[23]) + ', DUMFLD12 = ' + str(row[24]) + ', DUMFLD13 = ' + str(row[25]) + ', DUMFLD14 = ' + str(row[26]) + ', DUMFLD15 = ' + str(row[27]) + ', DUMFLD16 = ' + str(row[28]) + ', DUMFLD17 = ' + str(row[29]) + ', DUMFLD18 = ' + str(row[30]) + ', DUMFLD19 = ' + str(row[31]) + ', DUMFLD20 = ' + str(row[32]) + ', ACCTNO = ' + str(row[33]) + ', DE_STATUS = ' + str(row[34]) + ', DECOMMFLAG = ' + str(row[35]) + ', PARENTID = ' + str(row[36]) + ', PARENTREC = ' + str(row[37]) + ', COPYNO = ' + str(row[38])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromCulture(myCursor):
	print('Testing CULTURE!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.CULTURE')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[38])
			task = 'CULTURE'
			timestamp = 'None'
			otherAttributes = 'CAREPHASE = ' + str(row[0]) + ', ORD_DATE = ' + str(row[1]) + ', ORD_TIME = ' + str(row[2]) + ', DRAW_DATE = ' + str(row[3]) + ', DRAW_TIME = ' + str(row[4]) + ', ORD_BY = ' + str(row[5]) + ', RESLT_DATE = ' + str(row[6]) + ', RESLT_TIME = ' + str(row[7]) + ', DESCRIPT = ' + str(row[8]) + ', CULT_SITE = ' + str(row[9]) + ', CULT_BUG = ' + str(row[10]) + ', PHASE_COPY = ' + str(row[11]) + ', DUMFLD1 = ' + str(row[12]) + ', DUMFLD2 = ' + str(row[13]) + ', DUMFLD3 = ' + str(row[14]) + ', DUMFLD4 = ' + str(row[15]) + ', DUMFLD5 = ' + str(row[16]) + ', DUMFLD6 = ' + str(row[17]) + ', DUMFLD7 = ' + str(row[18]) + ', DUMFLD8 = ' + str(row[19]) + ', DUMFLD9 = ' + str(row[20]) + ', DUMFLD10 = ' + str(row[21]) + ', DUMFLD11 = ' + str(row[22]) + ', DUMFLD12 = ' + str(row[23]) + ', DUMFLD13 = ' + str(row[24]) + ', DUMFLD14 = ' + str(row[25]) + ', DUMFLD15 = ' + str(row[26]) + ', DUMFLD16 = ' + str(row[27]) + ', DUMFLD17 = ' + str(row[28]) + ', DUMFLD18 = ' + str(row[29]) + ', DUMFLD19 = ' + str(row[30]) + ', DUMFLD20 = ' + str(row[31]) + ', ACCTNO = ' + str(row[32]) + ', DE_STATUS = ' + str(row[33]) + ', DECOMMFLAG = ' + str(row[34]) + ', PARENTID = ' + str(row[35]) + ', PARENTREC = ' + str(row[36]) + ', COPYNO = ' + str(row[37])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromDellog(myCursor): # PROBLEM WITH A CHARACTER IN otherAttributes
	print('Testing dellog!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TRAUMA2.dellog')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[0])
			task = 'dellog'
			timestamp = str(row[11])
			otherAttributes = 'acctno = ' + str(row[1]) + ', acc_path = ' + str(row[2]) + ', copyid = ' + str(row[3]) + ', action = ' + str(row[4]) + ', fieldname = ' + str(row[5]) + ', fieldtype = ' + str(row[6]) + ', fieldval = ' + str(row[7]) + ', fieldstat = ' + str(row[8]) + ', memofldval = ' + str(row[9]) + ', genfldval = ' + str(row[10]) + ', trantime = ' + str(row[12]) + ', tranuser = ' + str(row[13]) + ', transtn = ' + str(row[14])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromDiags(myCursor):
	print('Testing DIAGS!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.DIAGS')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[39])
			task = 'DIAGS'
			timestamp = 'None'
			otherAttributes = 'DIAG_T_BSA = ' + str(row[0]) + ', CAREPHASE = ' + str(row[1]) + ', TIME = ' + str(row[3]) + ', AIS_FACE = ' + str(row[4]) + ', AIS_HEAD = ' + str(row[5]) + ', AIS_ABD = ' + str(row[6]) + ', AIS_EXTRMY = ' + str(row[7]) + ', AIS_CHEST = ' + str(row[8]) + ', AIS_EXTRNL = ' + str(row[9]) + ', DRG_DX = ' + str(row[10]) + ', PHASE_COPY = ' + str(row[11]) + ', DUMFLD1 = ' + str(row[12]) + ', DUMFLD2 = ' + str(row[13]) + ', DUMFLD3 = ' + str(row[14]) + ', DUMFLD4 = ' + str(row[15]) + ', DUMFLD5 = ' + str(row[16]) + ', DUMFLD6 = ' + str(row[17]) + ', DUMFLD7 = ' + str(row[18]) + ', DUMFLD8 = ' + str(row[19]) + ', DUMFLD9 = ' + str(row[20]) + ', DUMFLD10 = ' + str(row[21]) + ', DUMFLD11 = ' + str(row[22]) + ', DUMFLD12 = ' + str(row[23]) + ', DUMFLD13 = ' + str(row[24]) + ', DUMFLD14 = ' + str(row[25]) + ', DUMFLD15 = ' + str(row[26]) + ', DUMFLD16 = ' + str(row[27]) + ', DUMFLD17 = ' + str(row[28]) + ', DUMFLD18 = ' + str(row[29]) + ', DUMFLD19 = ' + str(row[30]) + ', DUMFLD20 = ' + str(row[31]) + ', NISS = ' + str(row[32]) + ', ACCTNO = ' + str(row[33]) + ', DE_STATUS = ' + str(row[34]) + ', DECOMMFLAG = ' + str(row[35]) + ', PARENTID = ' + str(row[36]) + ', PARENTREC = ' + str(row[37]) + ', COPYNO = ' + str(row[38])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromDiags(myCursor): # WITH PROBLEMS 
	print('Testing DIAGS!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.DIAGS')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[69])
			task = 'DIAGS'
			timestamp = 'None'
			otherAttributes = 'EM_NOTIFID = ' + str(row[0]) + ', EM_NOTF_DT = ' + str(row[1]) + ', EM_NOTF_TM = ' + str(row[2]) + ', EM_DOA = ' + str(row[3]) + ', EM_MJR = ' + str(row[4]) + ', EM_ENT_DT = ' + str(row[5]) + ', EM_ENT_TM = ' + str(row[6]) + ', EM_EXIT_DT = ' + str(row[7]) + ', EM_EXIT_TM = ' + str(row[8]) + ', EM_ENT_FRM = ' + str(row[9]) + ', EM_EXIT_TO = ' + str(row[10]) + ', EM_ADM_TYP = ' + str(row[11]) + ', EM_ADM_SRC = ' + str(row[12]) + ', EM_DISPO = ' + str(row[13]) + ', EM_LFT_VIA = ' + str(row[14]) + ', EM_REBG_TM = ' + str(row[15]) + ', EM_REEN_TM = ' + str(row[16]) + ', EM_DOCTOR = ' + str(row[17]) + ', EM_SERVICE = ' + str(row[18]) + ', EM_UNCPROB = ' + str(row[19]) + ', EM_LOS = ' + str(row[20]) + ', EM_SUB_CT = ' + str(row[21]) + ', EM_SEV_HD = ' + str(row[22]) + ', TM_CT = ' + str(row[23]) + ', R_TOT_TME = ' + str(row[24]) + ', IVFLUIDS = ' + str(row[25]) + ', BLOODPRO = ' + str(row[26]) + ', AUTOTRANS = ' + str(row[27]) + ', TOTIVBLD = ' + str(row[28]) + ', HEADCTTM = ' + str(row[29]) + ', HEADCTRES = ' + str(row[30]) + ', CSPINETM = ' + str(row[31]) + ', CSPINERES = ' + str(row[32]) + ', ETTIME = ' + str(row[33]) + ', ERTHORTIME = ' + str(row[34]) + ', DPLTIME = ' + str(row[34]) + ', CHTUBELTM = ' + str(row[35]) + ', CHTUBERTM = ' + str(row[36]) + ', CRICHTIME = ' + str(row[37]) + ', TRACHTIME = ' + str(row[38]) + ', TOX = ' + str(row[39]) + ', SIGNSLIFE = ' + str(row[40]) + ', DUMFLD1 = ' + str(row[41]) + ', DUMFLD2 = ' + str(row[42]) + ', DUMFLD3 = ' + str(row[43]) + ', DUMFLD4 = ' + str(row[44]) + ', DUMFLD5 = ' + str(row[45]) + ', DUMFLD6 = ' + str(row[46]) + ', DUMFLD7 = ' + str(row[47]) + ', DUMFLD8 = ' + str(row[48]) + ', DUMFLD9 = ' + str(row[49]) + ', DUMFLD10 = ' + str(row[50]) + ', DUMFLD11 = ' + str(row[51]) + ', DUMFLD12 = ' + str(row[52]) + ', DUMFLD13 = ' + str(row[53]) + ', DUMFLD14 = ' + str(row[54]) + ', DUMFLD15 = ' + str(row[55]) + ', DUMFLD16 = ' + str(row[56]) + ', DUMFLD17 = ' + str(row[57]) + ', DUMFLD18 = ' + str(row[58]) + ', DUMFLD19 = ' + str(row[59]) + ', DUMFLD20 = ' + str(row[60]) + ', E_AR_FROM = ' + str(row[61]) + ', E_TRANSPOR = ' + str(row[62]) + ', ACCTNO = ' + str(row[63]) + ', DE_STATUS = ' + str(row[64]) + ', DECOMMFLAG = ' + str(row[65]) + ', PARENTID = ' + str(row[66]) + ', PARENTREC = ' + str(row[67]) + ', COPYNO = ' + str(row[68])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

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