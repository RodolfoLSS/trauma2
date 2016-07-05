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
	elif tableName == 'GENMECH': 
		getTuplesFromGenmech(myCursor)
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

def getTuplesFromEmerg(myCursor):
	print('Testing EMERG!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.EMERG')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[69])
			task = 'EMERG'
			timestamp = 'None'
			otherAttributes = 'EM_NOTIFID = ' + str(row[0]) + ', EM_NOTF_DT = ' + str(row[1]) + ', EM_NOTF_TM = ' + str(row[2]) + ', EM_DOA = ' + str(row[3]) + ', EM_MJR = ' + str(row[4]) + ', EM_ENT_DT = ' + str(row[5]) + ', EM_ENT_TM = ' + str(row[6]) + ', EM_EXIT_DT = ' + str(row[7]) + ', EM_EXIT_TM = ' + str(row[8]) + ', EM_ENT_FRM = ' + str(row[9]) + ', EM_EXIT_TO = ' + str(row[10]) + ', EM_ADM_TYP = ' + str(row[11]) + ', EM_ADM_SRC = ' + str(row[12]) + ', EM_DISPO = ' + str(row[13]) + ', EM_LFT_VIA = ' + str(row[14]) + ', EM_REBG_TM = ' + str(row[15]) + ', EM_REEN_TM = ' + str(row[16]) + ', EM_DOCTOR = ' + str(row[17]) + ', EM_SERVICE = ' + str(row[18]) + ', EM_UNCPROB = ' + str(row[19]) + ', EM_LOS = ' + str(row[20]) + ', EM_SUB_CT = ' + str(row[21]) + ', EM_SEV_HD = ' + str(row[22]) + ', TM_CT = ' + str(row[23]) + ', R_TOT_TME = ' + str(row[24]) + ', IVFLUIDS = ' + str(row[25]) + ', BLOODPRO = ' + str(row[26]) + ', AUTOTRANS = ' + str(row[27]) + ', TOTIVBLD = ' + str(row[28]) + ', HEADCTTM = ' + str(row[29]) + ', HEADCTRES = ' + str(row[30]) + ', CSPINETM = ' + str(row[31]) + ', CSPINERES = ' + str(row[32]) + ', ETTTIME = ' + str(row[33]) + ', ERTHORTIME = ' + str(row[34]) + ', DPLTIME = ' + str(row[35]) + ', CHTUBELTM = ' + str(row[36]) + ', CHTUBERTM = ' + str(row[37]) + ', CRICHTIME = ' + str(row[38]) + ', TRACHTIME = ' + str(row[39]) + ', TOX = ' + str(row[40]) + ', SIGNSLIFE = ' + str(row[41]) + ', DUMFLD2 = ' + str(row[42]) + ', DUMFLD3 = ' + str(row[43]) + ', DUMFLD4 = ' + str(row[44]) + ', DUMFLD5 = ' + str(row[45]) + ', DUMFLD6 = ' + str(row[46]) + ', DUMFLD7 = ' + str(row[47]) + ', DUMFLD8 = ' + str(row[48]) + ', DUMFLD9 = ' + str(row[49]) + ', DUMFLD10 = ' + str(row[50]) + ', DUMFLD11 = ' + str(row[51]) + ', DUMFLD12 = ' + str(row[52]) + ', DUMFLD13 = ' + str(row[53]) + ', DUMFLD14 = ' + str(row[54]) + ', DUMFLD15 = ' + str(row[55]) + ', DUMFLD16 = ' + str(row[56]) + ', DUMFLD17 = ' + str(row[57]) + ', DUMFLD18 = ' + str(row[58]) + ', DUMFLD19 = ' + str(row[59]) + ', DUMFLD20 = ' + str(row[60]) + ', E_AR_FROM = ' + str(row[61]) + ', E_TRANSPOR = ' + str(row[62]) + ', ACCTNO = ' + str(row[63]) + ', DE_STATUS = ' + str(row[64]) + ', DECOMMFLAG = ' + str(row[65]) + ', PARENTID = ' + str(row[66]) + ', PARENTREC = ' + str(row[67]) + ', COPYNO = ' + str(row[68])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromFinance(myCursor):
	print('Testing FINANCE!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.FINANCE')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[40])
			task = 'FINANCE'
			timestamp = 'None'
			otherAttributes = 'T_HOS_COST = ' + str(row[0]) + ', T_HOS_CHRG = ' + str(row[1]) + ', T_HOS_BILL = ' + str(row[2]) + ', T_HOS_RECP = ' + str(row[3]) + ', T_PHY_COST = ' + str(row[4]) + ', T_PHY_CHRG = ' + str(row[5]) + ', T_PHY_BILL = ' + str(row[6]) + ', T_PHY_RECP = ' + str(row[7]) + ', CHG_PRLS = ' + str(row[8]) + ', CST_PRLS = ' + str(row[9]) + ', VVC_APP = ' + str(row[10]) + ', TT_REIM = ' + str(row[11]) + ', TT_ADDL = ' + str(row[12]) + ', TT_TOTAL = ' + str(row[13]) + ', DUMFLD1 = ' + str(row[14]) + ', DUMFLD2 = ' + str(row[15]) + ', DUMFLD3 = ' + str(row[16]) + ', DUMFLD4 = ' + str(row[17]) + ', DUMFLD5 = ' + str(row[18]) + ', DUMFLD6 = ' + str(row[19]) + ', DUMFLD7 = ' + str(row[20]) + ', DUMFLD8 = ' + str(row[21]) + ', DUMFLD9 = ' + str(row[22]) + ', DUMFLD10 = ' + str(row[23]) + ', DUMFLD11 = ' + str(row[24]) + ', DUMFLD12 = ' + str(row[25]) + ', DUMFLD13 = ' + str(row[26]) + ', DUMFLD14 = ' + str(row[27]) + ', DUMFLD15 = ' + str(row[28]) + ', DUMFLD16 = ' + str(row[29]) + ', DUMFLD17 = ' + str(row[30]) + ', DUMFLD18 = ' + str(row[31]) + ', DUMFLD19 = ' + str(row[32]) + ', DUMFLD20 = ' + str(row[33]) + ', ACCTNO = ' + str(row[34]) + ', DE_STATUS = ' + str(row[35]) + ', DECOMMFLAG = ' + str(row[36]) + ', PARENTID = ' + str(row[37]) + ', PARENTREC = ' + str(row[38]) + ', COPYNO = ' + str(row[39])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromFlddetai(myCursor):
	print('Testing FLDDETAI!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.FLDDETAI')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[39])
			task = 'FLDDETAI'
			timestamp = str(row[0])
			otherAttributes = 'FL_ENT_TM = ' + str(row[1]) + ', TRM_LEVEL = ' + str(row[2]) + ', NUM_VICTIM = ' + str(row[3]) + ', PRE_FORM = ' + str(row[4]) + ', FL_EXIT_TO = ' + str(row[5]) + ', DESIG_BY = ' + str(row[6]) + ', TRIAGE = ' + str(row[7]) + ', PT_STATUS = ' + str(row[8]) + ', FL_UNCPROB = ' + str(row[9]) + ', RELFACTOR = ' + str(row[10]) + ', TPS_RATNL = ' + str(row[11]) + ', INTUBATE = ' + str(row[12]) + ', DUMFLD1 = ' + str(row[13]) + ', DUMFLD2 = ' + str(row[14]) + ', DUMFLD3 = ' + str(row[15]) + ', DUMFLD4 = ' + str(row[16]) + ', DUMFLD5 = ' + str(row[17]) + ', DUMFLD6 = ' + str(row[18]) + ', DUMFLD7 = ' + str(row[19]) + ', DUMFLD8 = ' + str(row[20]) + ', DUMFLD9 = ' + str(row[21]) + ', DUMFLD10 = ' + str(row[22]) + ', DUMFLD11 = ' + str(row[23]) + ', DUMFLD12 = ' + str(row[24]) + ', DUMFLD13 = ' + str(row[25]) + ', DUMFLD14 = ' + str(row[26]) + ', DUMFLD15 = ' + str(row[27]) + ', DUMFLD16 = ' + str(row[28]) + ', DUMFLD17 = ' + str(row[29]) + ', DUMFLD18 = ' + str(row[30]) + ', DUMFLD19 = ' + str(row[31]) + ', DUMFLD20 = ' + str(row[32]) + ', ACCTNO = ' + str(row[33]) + ', DE_STATUS = ' + str(row[34]) + ', DECOMMFLAG = ' + str(row[35]) + ', PARENTID = ' + str(row[36]) + ', PARENTREC = ' + str(row[37]) + ', COPYNO = ' + str(row[38])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromGenmech(myCursor):
	print('Testing GENMECH!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.GENMECH')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[31])
			task = 'GENMECH'
			timestamp = 'None'
			otherAttributes = 'GEN_DSRPT = ' + str(row[0]) + ', ECODE_ICD9 = ' + str(row[1]) + ', MEC_DISCP = ' + str(row[2]) + ', E_ACTIVITY = ' + str(row[3]) + ', DUMFLD2 = ' + str(row[4]) + ', DUMFLD3 = ' + str(row[5]) + ', DUMFLD4 = ' + str(row[6]) + ', DUMFLD5 = ' + str(row[7]) + ', DUMFLD6 = ' + str(row[8]) + ', DUMFLD7 = ' + str(row[9]) + ', DUMFLD8 = ' + str(row[10]) + ', DUMFLD9 = ' + str(row[11]) + ', DUMFLD10 = ' + str(row[12]) + ', DUMFLD11 = ' + str(row[13]) + ', DUMFLD12 = ' + str(row[14]) + ', DUMFLD13 = ' + str(row[15]) + ', DUMFLD14 = ' + str(row[16]) + ', DUMFLD15 = ' + str(row[17]) + ', DUMFLD16 = ' + str(row[18]) + ', DUMFLD17 = ' + str(row[19]) + ', DUMFLD18 = ' + str(row[20]) + ', DUMFLD19 = ' + str(row[21]) + ', DUMFLD20 = ' + str(row[22]) + ', CDC_MOI = ' + str(row[23]) + ', CDC_INT = ' + str(row[24]) + ', ACCTNO = ' + str(row[25])  + ', DE_STATUS = ' + str(row[26])  + ', DECOMMFLAG = ' + str(row[27]) + ', PARENTID = ' + str(row[28]) + ', PARENTREC = ' + str(row[29])  + ', COPYNO = ' + str(row[30])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromHemo(myCursor):
	print('Testing HEMO!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.HEMO')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[56])
			task = 'HEMO'
			timestamp = 'None'
			otherAttributes = 'CAREPHASE = ' + str(row[0]) + ', ORD_DATE = ' + str(row[1]) + ', ORD_TIME = ' + str(row[2]) + ', DRAW_DATE = ' + str(row[3]) + ', DRAW_TIME = ' + str(row[4]) + ', ORDER_BY = ' + str(row[5]) + ', RESLT_DATE = ' + str(row[6]) + ', RESLT_TIME = ' + str(row[7]) + ', DESCRIPT = ' + str(row[8]) + ', HEME_STPL = ' + str(row[9]) + ', HEME_STPL = ' + str(row[10]) + ', HEME_SICL = ' + str(row[11]) + ', HEME_RETC = ' + str(row[12]) + ', HEME_SED = ' + str(row[13]) + ', WBC_SEGS = ' + str(row[14]) + ', WBC_BANDS = ' + str(row[15]) + ', WBC_LYMPH = ' + str(row[16]) + ', WBC_MONO = ' + str(row[17]) + ', WBC_EOSIN = ' + str(row[18]) + ', WBC_BASO = ' + str(row[19]) + ', WBC_META = ' + str(row[20]) + ', WBC_MYELO = ' + str(row[21]) + ', WBC_ALYMPH = ' + str(row[22]) + ', HEME_HCT = ' + str(row[23]) + ', HEME_RBC = ' + str(row[24]) + ', HEME_MCV = ' + str(row[25]) + ', HEME_HGB = ' + str(row[26]) + ', HEME_MCH = ' + str(row[27]) + ', HEME_MCHC = ' + str(row[28]) + ', PHASE_COPY = ' + str(row[29]) + ', DUMFLD1 = ' + str(row[30]) + ', DUMFLD2 = ' + str(row[31]) + ', DUMFLD3 = ' + str(row[32]) + ', DUMFLD4 = ' + str(row[33]) + ', DUMFLD5 = ' + str(row[34]) + ', DUMFLD6 = ' + str(row[35]) + ', DUMFLD7 = ' + str(row[36]) + ', DUMFLD8 = ' + str(row[37]) + ', DUMFLD9 = ' + str(row[38]) + ', DUMFLD10 = ' + str(row[39]) + ', DUMFLD11 = ' + str(row[40]) + ', DUMFLD12 = ' + str(row[41]) + ', DUMFLD13 = ' + str(row[42]) + ', DUMFLD14 = ' + str(row[43]) + ', DUMFLD15 = ' + str(row[44]) + ', DUMFLD16 = ' + str(row[45]) + ', DUMFLD17 = ' + str(row[46]) + ', DUMFLD18 = ' + str(row[47]) + ', DUMFLD19 = ' + str(row[48]) + ', DUMFLD20 = ' + str(row[49]) + ', ACCTNO = ' + str(row[50]) + ', DE_STATUS = ' + str(row[51]) + ', DECOMMFLAG = ' + str(row[52]) + ', PARENTID = ' + str(row[53]) + ', PARENTREC = ' + str(row[54]) + ', COPYNO = ' + str(row[55])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromHosprev(myCursor):
	print('Testing HOSPREV!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.HOSPREV')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[29])
			task = 'HOSPREV'
			timestamp = 'None'
			otherAttributes = 'PAYOR = ' + str(row[0]) + ', H_CHARGES = ' + str(row[1]) + ', H_RECEIPTS = ' + str(row[2]) + ', DUMFLD1 = ' + str(row[3]) + ', DUMFLD2 = ' + str(row[4]) + ', DUMFLD3 = ' + str(row[5]) + ', DUMFLD4 = ' + str(row[6]) + ', DUMFLD5 = ' + str(row[7]) + ', DUMFLD6 = ' + str(row[8]) + ', DUMFLD7 = ' + str(row[9]) + ', DUMFLD8 = ' + str(row[10]) + ', DUMFLD9 = ' + str(row[11]) + ', DUMFLD10 = ' + str(row[12]) + ', DUMFLD11 = ' + str(row[13]) + ', DUMFLD12 = ' + str(row[14]) + ', DUMFLD13 = ' + str(row[15]) + ', DUMFLD14 = ' + str(row[16]) + ', DUMFLD15 = ' + str(row[17]) + ', DUMFLD16 = ' + str(row[18]) + ', DUMFLD17 = ' + str(row[19]) + ', DUMFLD18 = ' + str(row[20]) + ', DUMFLD19 = ' + str(row[21]) + ', DUMFLD20 = ' + str(row[22]) +  ', ACCTNO = ' + str(row[23])  + ', DE_STATUS = ' + str(row[24])  + ', DECOMMFLAG = ' + str(row[25]) + ', PARENTID = ' + str(row[26]) + ', PARENTREC = ' + str(row[27])  + ', COPYNO = ' + str(row[28])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromIcu(myCursor):
	print('Testing ICU!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.ICU')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[41])
			task = 'ICU'
			timestamp = str(row[0])
			otherAttributes = 'ENT_TIME = ' + str(row[1]) + ', EXIT_DATE = ' + str(row[2]) + ', EXIT_TIME = ' + str(row[3]) + ', ENT_FROM = ' + str(row[4]) + ', EXIT_TO = ' + str(row[5]) + ', DOCTOR = ' + str(row[6]) + ', SERVICE = ' + str(row[7]) + ', SUB_CT = ' + str(row[8]) + ', UNPLAN_RTN = ' + str(row[9]) + ', LOS = ' + str(row[10]) + ', BLOODPRO = ' + str(row[11]) + ', AUTOTRANS = ' + str(row[12]) + ', TOTBLDPROD = ' + str(row[13]) + ', ICUTXCOMM = ' + str(row[14]) + ', DUMFLD1 = ' + str(row[15]) + ', DUMFLD2 = ' + str(row[16]) + ', DUMFLD3 = ' + str(row[17]) + ', DUMFLD4 = ' + str(row[18]) + ', DUMFLD5 = ' + str(row[19]) + ', DUMFLD6 = ' + str(row[20]) + ', DUMFLD7 = ' + str(row[21]) + ', DUMFLD8 = ' + str(row[22]) + ', DUMFLD9 = ' + str(row[23]) + ', DUMFLD10 = ' + str(row[24]) + ', DUMFLD11 = ' + str(row[25]) + ', DUMFLD12 = ' + str(row[26]) + ', DUMFLD13 = ' + str(row[27]) + ', DUMFLD14 = ' + str(row[28]) + ', DUMFLD15 = ' + str(row[29]) + ', DUMFLD16 = ' + str(row[30]) + ', DUMFLD17 = ' + str(row[31]) + ', DUMFLD18 = ' + str(row[32]) + ', DUMFLD19 = ' + str(row[33]) + ', DUMFLD20 = ' + str(row[34]) + ', ACCTNO = ' + str(row[35]) + ', DE_STATUS = ' + str(row[36]) + ', DECOMMFLAG = ' + str(row[37]) + ', PARENTID = ' + str(row[38]) + ', PARENTREC = ' + str(row[39]) + ', COPYNO = ' + str(row[40])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromInjdets(myCursor):
	print('Testing INJDETS!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.INJDETS')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[60])
			task = 'INJDETS'
			timestamp = 'None'
			otherAttributes = 'INITIALCARE = ' + str(row[0]) + ', SEVR_DIST = ' + str(row[1]) + ', ALERT_BY = ' + str(row[2]) + ', EMS_AIDER = ' + str(row[3]) + ', FIRST_AID = ' + str(row[4]) + ', EXTR_DONE = ' + str(row[5]) + ', EXTR_TIME = ' + str(row[6]) + ', INJ_BLDG = ' + str(row[7]) + ', INJ_STR1 = ' + str(row[8]) + ', INJ_STR2 = ' + str(row[9]) + ', INJ_ST_TYP = ' + str(row[10]) + ', QUADRANT = ' + str(row[11]) + ', INJ_CITY = ' + str(row[12]) + ', INJ_STATE = ' + str(row[13]) + ', INJ_ZIP = ' + str(row[14]) + ', INJ_ZIPPLS = ' + str(row[15]) + ', INJ_CNTY = ' + str(row[16]) + ', DESCRIPTIO = ' + str(row[17]) + ', SITE_CLASS = ' + str(row[18]) + ', MAP_PAGE = ' + str(row[19]) + ', MAP_X = ' + str(row[20]) + ', MAP_Y = ' + str(row[21]) + ', IN_CEN_TRT = ' + str(row[22]) + ', JOB_RELTD = ' + str(row[23]) + ', JOB_INDTRY = ' + str(row[24]) + ', JOB_TITLE = ' + str(row[25]) + ', JOB_EMP = ' + str(row[26]) + ', FALL_HT = ' + str(row[27]) + ', ETOH_PRES = ' + str(row[28]) + ', INJ_CLASS = ' + str(row[29]) + ', VEH_SPEED = ' + str(row[30]) + ', LOC = ' + str(row[31]) + ', LOC_LEN = ' + str(row[32]) + ', LOC_UNITS = ' + str(row[33]) + ', DUMFLD1 = ' + str(row[34]) + ', DUMFLD2 = ' + str(row[35]) + ', DUMFLD3 = ' + str(row[36]) + ', DUMFLD4 = ' + str(row[37]) + ', DUMFLD5 = ' + str(row[38]) + ', DUMFLD6 = ' + str(row[39]) + ', DUMFLD7 = ' + str(row[40]) + ', DUMFLD8 = ' + str(row[41]) + ', DUMFLD9 = ' + str(row[42]) + ', DUMFLD10 = ' + str(row[43]) + ', DUMFLD11 = ' + str(row[44]) + ', DUMFLD12 = ' + str(row[45]) + ', DUMFLD13 = ' + str(row[46]) + ', DUMFLD14 = ' + str(row[47]) + ', DUMFLD15 = ' + str(row[48]) + ', DUMFLD16 = ' + str(row[49]) + ', DUMFLD17 = ' + str(row[50]) + ', DUMFLD18 = ' + str(row[51]) + ', DUMFLD19 = ' + str(row[52]) + ', DUMFLD20 = ' + str(row[53]) + ', ACCTNO = ' + str(row[54]) + ', DE_STATUS = ' + str(row[55]) + ', DECOMMFLAG = ' + str(row[56]) + ', PARENTID = ' + str(row[57]) + ', PARENTREC = ' + str(row[58]) + ', COPYNO = ' + str(row[59])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromInjdiag(myCursor):
	print('Testing INJDIAG!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.INJDIAG')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[41])
			task = 'INJDIAG'
			timestamp = str(row[6])
			otherAttributes = 'CAREPHASE = ' + str(row[0]) + ', INJ_CLASS = ' + str(row[1]) + ', INJ_COMP = ' + str(row[2]) + ', AIS = ' + str(row[3]) + ', BODY_PART = ' + str(row[4]) + ', AIS_CODE = ' + str(row[5]) + ', TIME = ' + str(row[7]) + ', SOURCE = ' + str(row[8]) + ', SERVICE = ' + str(row[9]) + ', DESCRIPTOR = ' + str(row[10]) + ', DIAG_NOTE = ' + str(row[11]) + ', DX_TEXT = ' + str(row[12]) + ', PHASE_COPY = ' + str(row[13]) + ', DUMFLD1 = ' + str(row[14]) + ', DUMFLD2 = ' + str(row[15]) + ', DUMFLD3 = ' + str(row[16]) + ', DUMFLD4 = ' + str(row[17]) + ', DUMFLD5 = ' + str(row[18]) + ', DUMFLD6 = ' + str(row[19]) + ', DUMFLD7 = ' + str(row[20]) + ', DUMFLD8 = ' + str(row[21]) + ', DUMFLD9 = ' + str(row[22]) + ', DUMFLD10 = ' + str(row[23]) + ', DUMFLD11 = ' + str(row[24]) + ', DUMFLD12 = ' + str(row[25]) + ', DUMFLD13 = ' + str(row[26]) + ', DUMFLD14 = ' + str(row[27]) + ', DUMFLD15 = ' + str(row[28]) + ', DUMFLD16 = ' + str(row[29]) + ', DUMFLD17 = ' + str(row[30]) + ', DUMFLD18 = ' + str(row[31]) + ', DUMFLD19 = ' + str(row[32]) + ', DUMFLD20 = ' + str(row[33]) + ', FX_FREE_TX' + str(row[34]) + ', ACCTNO = ' + str(row[35]) + ', DE_STATUS = ' + str(row[36]) + ', DECOMMFLAG = ' + str(row[37]) + ', PARENTID = ' + str(row[38]) + ', PARENTREC = ' + str(row[39]) + ', COPYNO = ' + str(row[40])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromInjmech(myCursor):
	print('Testing INJMECH!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.INJMECH')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[28])
			task = 'INJMECH'
			timestamp = 'None'
			otherAttributes = 'INJ_WHERE = ' + str(row[0]) + ', INJ_CAUSES = ' + str(row[1]) + ', DUMFLD1 = ' + str(row[2]) + ', DUMFLD2 = ' + str(row[3]) + ', DUMFLD3 = ' + str(row[4]) + ', DUMFLD4 = ' + str(row[5]) + ', DUMFLD5 = ' + str(row[6]) + ', DUMFLD6 = ' + str(row[7]) + ', DUMFLD7 = ' + str(row[8]) + ', DUMFLD8 = ' + str(row[9]) + ', DUMFLD9 = ' + str(row[10]) + ', DUMFLD10 = ' + str(row[11]) + ', DUMFLD11 = ' + str(row[12]) + ', DUMFLD12 = ' + str(row[13]) + ', DUMFLD13 = ' + str(row[14]) + ', DUMFLD14 = ' + str(row[15]) + ', DUMFLD15 = ' + str(row[16]) + ', DUMFLD16 = ' + str(row[17]) + ', DUMFLD17 = ' + str(row[18]) + ', DUMFLD18 = ' + str(row[19]) + ', DUMFLD19 = ' + str(row[20]) + ', DUMFLD20 = ' + str(row[21]) +  ', ACCTNO = ' + str(row[22])  + ', DE_STATUS = ' + str(row[23])  + ', DECOMMFLAG = ' + str(row[24]) + ', PARENTID = ' + str(row[25]) + ', PARENTREC = ' + str(row[26])  + ', COPYNO = ' + str(row[27])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromLab(myCursor):
	print('Testing LAB!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.LAB')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[51])
			task = 'LAB'
			timestamp = str(row[0])
			otherAttributes = 'ORD_TIME = ' + str(row[1]) + ', RESLT_DATE = ' + str(row[2]) + ', RESLT_TIME = ' + str(row[3]) + ', DRAW_DATE = ' + str(row[4]) + ', DRAW_TIME = ' + str(row[5]) + ', DESCRIPT = ' + str(row[6]) + ', ORD_BY = ' + str(row[7]) + ', LABGROUP = ' + str(row[8]) + ', CAREPHASE = ' + str(row[9]) + ', PHASE_COPY = ' + str(row[10]) + ', LABRES = ' + str(row[11]) + ', DUMFLD1 = ' + str(row[12]) + ', DUMFLD2 = ' + str(row[13]) + ', DUMFLD3 = ' + str(row[14]) + ', DUMFLD4 = ' + str(row[15]) + ', DUMFLD5 = ' + str(row[16]) + ', DUMFLD6 = ' + str(row[17]) + ', DUMFLD7 = ' + str(row[18]) + ', DUMFLD8 = ' + str(row[19]) + ', DUMFLD9 = ' + str(row[20]) + ', DUMFLD10 = ' + str(row[21]) + ', DUMFLD11 = ' + str(row[22]) + ', DUMFLD12 = ' + str(row[23]) + ', DUMFLD13 = ' + str(row[24]) + ', DUMFLD14 = ' + str(row[25]) + ', DUMFLD15 = ' + str(row[26]) + ', DUMFLD16 = ' + str(row[27]) + ', DUMFLD17 = ' + str(row[28]) + ', DUMFLD18 = ' + str(row[29]) + ', DUMFLD19 = ' + str(row[30]) + ', DUMFLD20 = ' + str(row[31]) + ', ETOH = ' + str(row[32]) + ', ETOH_TEST = ' + str(row[33]) + ', L_HGB = ' + str(row[34]) + ', L_HCT = ' + str(row[35]) + ', L_LACTATE = ' + str(row[36]) + ', L_WBC = ' + str(row[37]) + ', L_GLUCOSE = ' + str(row[38]) + ', L_BUN = ' + str(row[39]) + ', L_CREAT = ' + str(row[40]) + ', L_INR = ' + str(row[41]) + ', L_PT = ' + str(row[42]) + ', L_PTT = ' + str(row[43]) + ', L_INTR = ' + str(row[44]) + ', ACCTNO = ' + str(row[45]) + ', DE_STATUS = ' + str(row[46]) + ', DECOMMFLAG = ' + str(row[47]) + ', PARENTID = ' + str(row[48]) + ', PARENTREC = ' + str(row[49]) + ', COPYNO = ' + str(row[50])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromMaindata(myCursor):
	print('Testing MAINDATA!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.MAINDATA')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[82])
			task = 'MAINDATA'
			timestamp = str(row[6])
			otherAttributes = 'ACCTNO = ' + str(row[0]) + ', ENT_FROM = ' + str(row[1]) + ', MEDRECNUM = ' + str(row[2]) + ', EMRNUM = ' + str(row[3]) + ', REG1_NUM = ' + str(row[4]) + ', REG2_NUM = ' + str(row[5]) + ', ADMTIME = ' + str(row[7]) + ', LASTNAME = ' + str(row[8]) + ', FIRSTNAME = ' + str(row[9]) + ', MIDINIT = ' + str(row[10]) + ', ALIASNAME = ' + str(row[11]) + ', ALIASF = ' + str(row[12]) + ', ALIASM = ' + str(row[13]) + ', LOS = ' + str(row[14]) + ', ISS = ' + str(row[15]) + ', PROB_SURV = ' + str(row[16]) + ', DE_PERSON = ' + str(row[17]) + ', ABSTRACTOR = ' + str(row[18]) + ', FULLNAME = ' + str(row[19]) + ', SYS_ACCES = ' + str(row[20]) + ', BEFORE = ' + str(row[21]) + ', COMPLETE = ' + str(row[22]) + ', DHS_PAT = ' + str(row[23]) + ', ENTRYMODE = ' + str(row[24]) + ', TCCODE = ' + str(row[25]) + ', SEQNO = ' + str(row[26]) + ', RESERVE1 = ' + str(row[27]) + ', RESERVE2 = ' + str(row[28]) + ', DUMFLD1 = ' + str(row[29]) + ', DUMFLD2 = ' + str(row[30]) + ', DUMFLD3 = ' + str(row[31]) + ', DUMFLD4 = ' + str(row[32]) + ', DUMFLD5 = ' + str(row[33]) + ', DUMFLD6 = ' + str(row[34]) + ', DUMFLD7 = ' + str(row[35]) + ', DUMFLD8 = ' + str(row[36]) + ', DUMFLD9 = ' + str(row[37]) + ', DUMFLD10 = ' + str(row[38]) + ', DUMFLD11 = ' + str(row[39]) + ', DUMFLD12 = ' + str(row[40]) + ', DUMFLD13 = ' + str(row[41]) + ', DUMFLD14 = ' + str(row[42]) + ', DUMFLD15 = ' + str(row[43]) + ', DUMFLD16 = ' + str(row[44]) + ', DUMFLD17 = ' + str(row[45]) + ', DUMFLD18 = ' + str(row[46]) + ', DUMFLD19 = ' + str(row[47]) + ', DUMFLD20 = ' + str(row[48]) + ', SKETCH = ' + str(row[50]) + ', NISS = ' + str(row[51]) + ', LOCKED = ' + str(row[52]) + ', DBNO = ' + str(row[53]) + ', RECDATE = ' + str(row[54]) + ', CREATETIME = ' + str(row[55]) + ', CREATEUIID = ' + str(row[56]) + ', COMPLTDATE = ' + str(row[57]) + ', COMPLTTIME = ' + str(row[58]) + ', COMPLTUID = ' + str(row[59]) + ', MODIFYDATE = ' + str(row[60]) + ', MODIFYTIME = ' + str(row[61]) + ', MODIFYUID = ' + str(row[62]) + ', ACCESSDATE = ' + str(row[63]) + ', ACCESSTIME = ' + str(row[64]) + ', ACCESSUID = ' + str(row[65]) + ', LOCKDATE = ' + str(row[66]) + ', LOCKTIME = ' + str(row[67]) + ', LOCKUID = ' + str(row[68]) + ', CREATORID = ' + str(row[69]) + ', XFER_ID = ' + str(row[70]) + ', EXPORTED = ' + str(row[71]) + ', EXPT_CONF = ' + str(row[72]) + ', IMPORTED = ' + str(row[73]) + ', IMPT_CONF = ' + str(row[74]) + ', RECSTATFLA = ' + str(row[75]) + 'SKELETON = ' + str(row[76]) + ', DE_STATUS = ' + str(row[77]) + ', DECOMMFLAG = ' + str(row[78]) + ', PARENTID = ' + str(row[79]) + ', PARENTREC = ' + str(row[80]) + ', COPYNO = ' + str(row[81])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromMortdets(myCursor):
	print('Testing MORTDETS!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.MORTDETS')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[36])
			task = 'MORTDETS'
			timestamp = str(row[0])
			otherAttributes = 'MM_EVAL = ' + str(row[1]) + ', LOCATION = ' + str(row[2]) + ', EXTENT = ' + str(row[3]) + ', AUTOP_IDNO = ' + str(row[4]) + ', MEO = ' + str(row[5]) + ', MEO_NAME = ' + str(row[6]) + ', CORNER_NO = ' + str(row[7]) + ', ORG_REQST = ' + str(row[8]) + ', TOXICDONE = ' + str(row[9]) + ', DUMFLD1 = ' + str(row[10]) + ', DUMFLD2 = ' + str(row[11]) + ', DUMFLD3 = ' + str(row[12]) + ', DUMFLD4 = ' + str(row[13]) + ', DUMFLD5 = ' + str(row[14]) + ', DUMFLD6 = ' + str(row[15]) + ', DUMFLD7 = ' + str(row[16]) + ', DUMFLD8 = ' + str(row[17]) + ', DUMFLD9 = ' + str(row[18]) + ', DUMFLD10 = ' + str(row[19]) + ', DUMFLD11 = ' + str(row[20]) + ', DUMFLD12 = ' + str(row[21]) + ', DUMFLD13 = ' + str(row[22]) + ', DUMFLD14 = ' + str(row[23]) + ', DUMFLD15 = ' + str(row[24]) + ', DUMFLD16 = ' + str(row[25]) + ', DUMFLD17 = ' + str(row[26]) + ', DUMFLD18 = ' + str(row[27]) + ', DUMFLD19 = ' + str(row[28]) + ', DUMFLD20 = ' + str(row[29]) + ', ACCTNO = ' + str(row[30]) + ', DE_STATUS = ' + str(row[31]) + ', DECOMMFLAG = ' + str(row[32]) + ', PARENTID = ' + str(row[33]) + ', PARENTREC = ' + str(row[34]) + ', COPYNO = ' + str(row[35])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromMtos(myCursor):
	print('Testing Mtos!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.MTOS')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[39])
			task = 'MTOS'
			timestamp = str(row[1])
			otherAttributes = 'CAREPHASE = ' + str(row[0]) + ', SELFFEED = ' + str(row[2]) + ', LOCOMO = ' + str(row[3]) + ', EXPRESS = ' + str(row[4]) + ', MOBILITY = ' + str(row[5]) + ', SOCIAL = ' + str(row[6]) + ', DISB_STAT = ' + str(row[7]) + ', DUMFLD1 = ' + str(row[8]) + ', DUMFLD2 = ' + str(row[9]) + ', DUMFLD3 = ' + str(row[10]) + ', DUMFLD4 = ' + str(row[11]) + ', DUMFLD5 = ' + str(row[12]) + ', DUMFLD6 = ' + str(row[13]) + ', DUMFLD7 = ' + str(row[14]) + ', DUMFLD8 = ' + str(row[15]) + ', DUMFLD9 = ' + str(row[16]) + ', DUMFLD10 = ' + str(row[17]) + ', DUMFLD11 = ' + str(row[18]) + ', DUMFLD12 = ' + str(row[19]) + ', DUMFLD13 = ' + str(row[20]) + ', DUMFLD14 = ' + str(row[21]) + ', DUMFLD15 = ' + str(row[22]) + ', DUMFLD16 = ' + str(row[23]) + ', DUMFLD17 = ' + str(row[24]) + ', DUMFLD18 = ' + str(row[25]) + ', DUMFLD19 = ' + str(row[26]) + ', DUMFLD20 = ' + str(row[27]) + ', F_PHASE = ' + str(row[28]) + ', F_L_STAT = ' + str(row[29]) + ', F_E_STAT = ' + str(row[30]) + ', F_M_STAT = ' + str(row[31]) + ', FIM_TOTAL = ' + str(row[32]) + ', ACCTNO = ' + str(row[33]) + ', DE_STATUS = ' + str(row[34]) + ', DECOMMFLAG = ' + str(row[35]) + ', PARENTID = ' + str(row[36]) + ', PARENTREC = ' + str(row[37]) + ', COPYNO = ' + str(row[38])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromNarrativ(myCursor): # PROBLEM WITH CHARACTER
	print('Testing NARRATIV!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.NARRATIV')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[38])
			task = 'NARRATIV'
			timestamp = 'None'
			otherAttributes = 'ETIOLOGY = ' + str(row[0]) + ', MEDHISTY = ' + str(row[1]) + ', PREHOSP = ' + str(row[2]) + ', REFHOSP = ' + str(row[3]) + ', ED_MEMO = ' + str(row[4]) + ', TRA_MEMO = ' + str(row[5]) + ', QA_MEMO = ' + str(row[6]) + ', DX_MEMO = ' + str(row[7]) + ', INP_MEMO = ' + str(row[8]) + ', DC_MEMO = ' + str(row[9]) + ', FLU_MEMO = ' + str(row[10]) + ', DTH_MEMO = ' + str(row[11]) + ', DUMFLD1 = ' + str(row[12]) + ', DUMFLD2 = ' + str(row[13]) + ', DUMFLD3 = ' + str(row[14]) + ', DUMFLD4 = ' + str(row[15]) + ', DUMFLD5 = ' + str(row[16]) + ', DUMFLD6 = ' + str(row[17]) + ', DUMFLD7 = ' + str(row[18]) + ', DUMFLD8 = ' + str(row[19]) + ', DUMFLD9 = ' + str(row[20]) + ', DUMFLD10 = ' + str(row[21]) + ', DUMFLD11 = ' + str(row[22]) + ', DUMFLD12 = ' + str(row[23]) + ', DUMFLD13 = ' + str(row[24]) + ', DUMFLD14 = ' + str(row[25]) + ', DUMFLD15 = ' + str(row[26]) + ', DUMFLD16 = ' + str(row[27]) + ', DUMFLD17 = ' + str(row[28]) + ', DUMFLD18 = ' + str(row[29]) + ', DUMFLD19 = ' + str(row[30]) + ', DUMFLD20 = ' + str(row[31]) +  ', ACCTNO = ' + str(row[32]) + ', DE_STATUS = ' + str(row[33]) + ', DECOMMFLAG = ' + str(row[34]) + ', PARENTID = ' + str(row[35]) + ', PARENTREC = ' + str(row[36]) + ', COPYNO = ' + str(row[37])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromOprm(myCursor):
	print('Testing OPRM!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.OPRM')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[37])
			task = 'OPRM'
			timestamp = str(row[0])
			otherAttributes = 'ENT_TIME = ' + str(row[1]) + ', EXIT_DATE = ' + str(row[2]) + ', EXIT_TIME = ' + str(row[3]) + ', ENT_FROM = ' + str(row[4]) + ', EXIT_TO = ' + str(row[5]) + ', DOCTOR = ' + str(row[6]) + ', SERVICE = ' + str(row[7]) + ', SUB_CT = ' + str(row[8]) + ', UNPLAN_RTN = ' + str(row[9]) + ', LOS = ' + str(row[10]) + ', DUMFLD1 = ' + str(row[11]) + ', DUMFLD2 = ' + str(row[12]) + ', DUMFLD3 = ' + str(row[13]) + ', DUMFLD4 = ' + str(row[14]) + ', DUMFLD5 = ' + str(row[15]) + ', DUMFLD6 = ' + str(row[16]) + ', DUMFLD7 = ' + str(row[17]) + ', DUMFLD8 = ' + str(row[18]) + ', DUMFLD9 = ' + str(row[19]) + ', DUMFLD10 = ' + str(row[20]) + ', DUMFLD11 = ' + str(row[21]) + ', DUMFLD12 = ' + str(row[22]) + ', DUMFLD13 = ' + str(row[23]) + ', DUMFLD14 = ' + str(row[24]) + ', DUMFLD15 = ' + str(row[25]) + ', DUMFLD16 = ' + str(row[26]) + ', DUMFLD17 = ' + str(row[27]) + ', DUMFLD18 = ' + str(row[28]) + ', DUMFLD19 = ' + str(row[29]) + ', DUMFLD20 = ' + str(row[30]) + ', ACCTNO = ' + str(row[31]) + ', DE_STATUS = ' + str(row[32]) + ', DECOMMFLAG = ' + str(row[33]) + ', PARENTID = ' + str(row[34]) + ', PARENTREC = ' + str(row[35]) + ', COPYNO = ' + str(row[36])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromOrgans(myCursor):
	print('Testing ORGANS!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.ORGANS')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[27])
			task = 'ORGANS'
			timestamp = 'None'
			otherAttributes = 'ORG_DONATE = ' + str(row[0]) + ', DUMFLD1 = ' + str(row[1]) + ', DUMFLD2 = ' + str(row[2]) + ', DUMFLD3 = ' + str(row[3]) + ', DUMFLD4 = ' + str(row[4]) + ', DUMFLD5 = ' + str(row[5]) + ', DUMFLD6 = ' + str(row[6]) + ', DUMFLD7 = ' + str(row[7]) + ', DUMFLD8 = ' + str(row[8]) + ', DUMFLD9 = ' + str(row[9]) + ', DUMFLD10 = ' + str(row[10]) + ', DUMFLD11 = ' + str(row[11]) + ', DUMFLD12 = ' + str(row[12]) + ', DUMFLD13 = ' + str(row[13]) + ', DUMFLD14 = ' + str(row[14]) + ', DUMFLD15 = ' + str(row[15]) + ', DUMFLD16 = ' + str(row[16]) + ', DUMFLD17 = ' + str(row[17]) + ', DUMFLD18 = ' + str(row[18]) + ', DUMFLD19 = ' + str(row[19]) + ', DUMFLD20 = ' + str(row[20]) +  ', ACCTNO = ' + str(row[21])  + ', DE_STATUS = ' + str(row[22])  + ', DECOMMFLAG = ' + str(row[23]) + ', PARENTID = ' + str(row[24]) + ', PARENTREC = ' + str(row[25])  + ', COPYNO = ' + str(row[26])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromPerhist(myCursor):
	print('Testing PERHIST!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.PERHIST')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[68])
			task = 'PERHIST'
			timestamp = str(row[4])
			otherAttributes = 'PT_SSN = ' + str(row[0]) + ', SEX = ' + str(row[1]) + ', RACE = ' + str(row[2]) + ', MARG_STAT = ' + str(row[3]) + ', AGE = ' + str(row[5]) + ', AGE_UNIT = ' + str(row[6]) + ', BORN_CITY = ' + str(row[7]) + ', BORN_CNTY = ' + str(row[8]) + ', BORN_STATE = ' + str(row[9]) + ', BORN_CNTRY = ' + str(row[10]) + ', BLDG_NO = ' + str(row[11]) + ', PT_STREET = ' + str(row[12]) + ', PER_ST_TYP = ' + str(row[13]) + ', QUAD = ' + str(row[14]) + ', APT_NO = ' + str(row[15]) + ', PT_CITY = ' + str(row[16]) + ', PT_STATE = ' + str(row[17]) + ', PT_ZIP = ' + str(row[18]) + ', PER_ZIPPLS = ' + str(row[19]) + ', PT_CNTY = ' + str(row[20]) + ', PT_CNTRY = ' + str(row[21]) + ', PR_CEN_TRT = ' + str(row[22]) + ', PT_PHONE = ' + str(row[23]) + ', NEXT_KIN_L = ' + str(row[24]) + ', NEXT_KIN_F = ' + str(row[25]) + ', RELATION = ' + str(row[26]) + ', ELGBL_ALIN = ' + str(row[27]) + ', EMPLY_TYPE = ' + str(row[28]) + ', MONTH_INC = ' + str(row[29]) + ', INCME_SRCE = ' + str(row[30]) + ', FAMILY_SIZ = ' + str(row[31]) + ', MOM_NAME = ' + str(row[32]) + ', SIGN_OTHER = ' + str(row[33]) + ', SIGN_ADDRE = ' + str(row[34]) + ', SIGN_CITY = ' + str(row[35]) + ', SIGN_STATE = ' + str(row[36]) + ', SIGN_ZIP = ' + str(row[37]) + ', SIGN_PHONE = ' + str(row[38]) + ', PREGNANT = ' + str(row[39]) + ', DUMFLD1' + str(row[40]) + ', DUMFLD2 = ' + str(row[41]) + ', DUMFLD3 = ' + str(row[42]) + ', DUMFLD4 = ' + str(row[43]) + ', DUMFLD5 = ' + str(row[44]) + ', DUMFLD6 = ' + str(row[45]) + ', DUMFLD7 = ' + str(row[46]) + ', DUMFLD8 = ' + str(row[47]) + ', DUMFLD9 = ' + str(row[48]) + ', DUMFLD10 = ' + str(row[49]) + ', DUMFLD11 = ' + str(row[50]) + ', DUMFLD12 = ' + str(row[51]) + ', DUMFLD13 = ' + str(row[52]) + ', DUMFLD14 = ' + str(row[53]) + ', DUMFLD15 = ' + str(row[54]) + ', DUMFLD16 = ' + str(row[55]) + ', DUMFLD17 = ' + str(row[56]) + ', DUMFLD18 = ' + str(row[57]) + ', DUMFLD19 = ' + str(row[58]) + ', DUMFLD20 = ' + str(row[59]) + ', ALT_ADDRES = ' + str(row[60]) + ', ETHNICITY = ' + str(row[61]) + ', ACCTNO = ' + str(row[62]) + ', DE_STATUS = ' + str(row[63]) + ', DECOMMFLAG = ' + str(row[64]) + ', PARENTID = ' + str(row[65]) + ', PARENTREC = ' + str(row[66]) + ', COPYNO = ' + str(row[67])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromPosthosp(myCursor):
	print('Testing POSTHOSP!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.POSTHOSP') # ND PRONTO
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[])
			task = 'POSTHOSP'
			timestamp = str(row[0])
			otherAttributes = ' = ' + str(row[0]) + ', CAREPHASE = ' + str(row[1]) + ', TIME = ' + str(row[3]) + ', AIS_FACE = ' + str(row[4]) + ', AIS_HEAD = ' + str(row[5]) + ', AIS_ABD = ' + str(row[6]) + ', AIS_EXTRMY = ' + str(row[7]) + ', AIS_CHEST = ' + str(row[8]) + ', AIS_EXTRNL = ' + str(row[9]) + ', DRG_DX = ' + str(row[10]) + ', PHASE_COPY = ' + str(row[11]) + ', DUMFLD1 = ' + str(row[12]) + ', DUMFLD2 = ' + str(row[13]) + ', DUMFLD3 = ' + str(row[14]) + ', DUMFLD4 = ' + str(row[15]) + ', DUMFLD5 = ' + str(row[16]) + ', DUMFLD6 = ' + str(row[17]) + ', DUMFLD7 = ' + str(row[18]) + ', DUMFLD8 = ' + str(row[19]) + ', DUMFLD9 = ' + str(row[20]) + ', DUMFLD10 = ' + str(row[21]) + ', DUMFLD11 = ' + str(row[22]) + ', DUMFLD12 = ' + str(row[23]) + ', DUMFLD13 = ' + str(row[24]) + ', DUMFLD14 = ' + str(row[25]) + ', DUMFLD15 = ' + str(row[26]) + ', DUMFLD16 = ' + str(row[27]) + ', DUMFLD17 = ' + str(row[28]) + ', DUMFLD18 = ' + str(row[29]) + ', DUMFLD19 = ' + str(row[30]) + ', DUMFLD20 = ' + str(row[31]) + ', NISS = ' + str(row[32]) + ', ACCTNO = ' + str(row[33]) + ', DE_STATUS = ' + str(row[34]) + ', DECOMMFLAG = ' + str(row[35]) + ', PARENTID = ' + str(row[36]) + ', PARENTREC = ' + str(row[37]) + ', COPYNO = ' + str(row[38])
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