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

	function = input('Type 1 to filter by attributes or 2 to sort by timestamp: ')

	if tableName == 'AcctHist':
		objectList = getTuplesFromAcctHist(myCursor)
	elif tableName == 'ADM_INPT':
		objectList = getTuplesFromAdm_inpt(myCursor)
	elif tableName == 'BURNS': 
		objectList = getTuplesFromBurns(myCursor)
	elif tableName == 'comments': 
		objectList = getTuplesFromComments(myCursor) 
	elif tableName == 'CONSULT': 
		objectList = getTuplesFromConsult(myCursor)
	elif tableName == 'CULTURE': 
		objectList = getTuplesFromCulture(myCursor)
	elif tableName == 'dellog': 
		objectList = getTuplesFromDellog(myCursor)
	elif tableName == 'DIAGS': 
		objectList = getTuplesFromDiags(myCursor)
	elif tableName == 'EMERG':
	    objectList = getTuplesFromEmerg(myCursor)
	elif tableName == 'FINANCE': 
		objectList = getTuplesFromFinance(myCursor)
	elif tableName == 'FLDDETAI': 
		objectList = getTuplesFromFlddetai(myCursor)
	elif tableName == 'GENMECH': 
		objectList = getTuplesFromGenmech(myCursor)
	elif tableName == 'HEMO': 
		objectList = getTuplesFromHemo(myCursor)
	elif tableName == 'HOSPREV':
		objectList = getTuplesFromHosprev(myCursor)
	elif tableName == 'ICU':
		objectList = getTuplesFromIcu(myCursor)
	elif tableName == 'INJDETS':
		objectList = getTuplesFromInjdets(myCursor)
	elif tableName == 'INJDIAG':
		objectList = getTuplesFromInjdiag(myCursor)
	elif tableName == 'INJMECH':
		objectList = getTuplesFromInjmech(myCursor)
	elif tableName == 'LAB':
		objectList = getTuplesFromLab(myCursor)
	elif tableName == 'MAINDATA':
		objectList = getTuplesFromMaindata(myCursor)
	elif tableName == 'MORTDETS':
		objectList = getTuplesFromMortdets(myCursor)
	elif tableName == 'MTOS':
		objectList = getTuplesFromMtos(myCursor)
	elif tableName == 'NARRATIV':
		objectList = getTuplesFromNarrativ(myCursor)
	elif tableName == 'OPRM':
		objectList = getTuplesFromOprm(myCursor)
	elif tableName == 'ORGANS':
		objectList = getTuplesFromOrgans(myCursor)
	elif tableName == 'PERHIST':
		objectList = getTuplesFromPerhist(myCursor)
	elif tableName == 'POSTHOSP':
		objectList = getTuplesFromPosthosp(myCursor)
	elif tableName == 'PRECONDS':
		objectList = getTuplesFromPreconds(myCursor)
	elif tableName == 'PROTECT':
		objectList = getTuplesFromProtect(myCursor)
	elif tableName == 'QAISSUE':
		objectList = getTuplesFromQaissue(myCursor)
	elif tableName == 'RADIOLOG':
		objectList = getTuplesFromRadiolog(myCursor)
	elif tableName == 'READMIT':
		objectList = getTuplesFromReadmit(myCursor)
	elif tableName == 'STEP':
		objectList = getTuplesFromStep(myCursor)
	elif tableName == 'SURG':
		objectList = getTuplesFromSurg(myCursor)
	elif tableName == 'sysdefs':
		objectList = getTuplesFromSysdefs(myCursor)
	elif tableName == 'TLogComm':
		objectList = getTuplesFromTLogComm(myCursor)
	elif tableName == 'TOXIANAL':
		objectList = getTuplesFromToxianal(myCursor)
	elif tableName == 'TRA':
		objectList = getTuplesFromTra(myCursor)
	elif tableName == 'tranlog':
		objectList = getTuplesFromTranlog(myCursor, function)
	elif tableName == 'TRANSFER':
		objectList = getTuplesFromTransfer(myCursor)
	elif tableName == 'TRANSPRT':
		objectList = getTuplesFromTransprt(myCursor)
	elif tableName == 'TREATMEN':
		objectList = getTuplesFromTreatmen(myCursor)
	elif tableName == 'TRICRIT':
		objectList = getTuplesFromTricrit(myCursor)
	elif tableName == 'TRMTEAM':
		objectList = getTuplesFromTrmteam(myCursor)
	elif tableName == 'TTDETLS':
		objectList = getTuplesFromTtdetls(myCursor)
	elif tableName == 'VITALS':
		objectList = getTuplesFromVitals(myCursor)
	elif tableName == 'WARD':
		objectList = getTuplesFromWard(myCursor)
	else: 
		print ('Type a valid table name.\n')
		sys.exit(0)

	if function == '1' :
		filter(objectList)
	elif function == '2' :
		output2File(objectList)
	else :
		print('Not a valid number!')
		sys.exit(0)

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

		return patientList
			
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
			patientList.append(patient)

		return patientList

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
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromComments(myCursor): 
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
			otherAttributes = 'fileid = ' + str(row[0]) + ', fieldname = ' + str(row[2]) + ', ccomment = ' + str(row[3]).replace(u"\u2019", "'") + ', cimage = ' + str(results[4]) + ', copyno = ' + str(results[5]) + ', acctno = ' + str(results[6])
			#otherAttributes = 'Teste'
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

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

		return patientList

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

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromDellog(myCursor): 
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
			otherAttributes = 'acctno = ' + str(row[1]) + ', acc_path = ' + str(row[2]) + ', copyid = ' + str(row[3]) + ', action = ' + str(row[4]) + ', fieldname = ' + str(row[5]) + ', fieldtype = ' + str(row[6]) + ', fieldval = ' + str(row[7]) + ', fieldstat = ' + str(row[8]) + ', memofldval = ' + str(row[9]).replace(u"\u2019", "'").replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2026", '...') + ', genfldval = ' + str(row[10]) + ', trantime = ' + str(row[12]) + ', tranuser = ' + str(row[13]) + ', transtn = ' + str(row[14])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

			return patientList

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

		return patientList

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

		return patientList

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

		return patientList

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

		return patientList

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

		return patientList

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

		return patientList

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

		return patientList

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

		return patientList

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

		return patientList

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

		return patientList

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

		return patientList

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

		return patientList

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

		return patientList

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

		return patientList

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

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromNarrativ(myCursor): 
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
			otherAttributes = 'ETIOLOGY = ' + str(row[0]).replace(u"\u2019", "'").replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2014", '-').replace(u"\u2026", '...') + ', MEDHISTY = ' + str(row[1]) + ', PREHOSP = ' + str(row[2]) + ', REFHOSP = ' + str(row[3]) + ', ED_MEMO = ' + str(row[4]) + ', TRA_MEMO = ' + str(row[5]) + ', QA_MEMO = ' + str(row[6]) + ', DX_MEMO = ' + str(row[7]) + ', INP_MEMO = ' + str(row[8]) + ', DC_MEMO = ' + str(row[9]) + ', FLU_MEMO = ' + str(row[10]) + ', DTH_MEMO = ' + str(row[11]) + ', DUMFLD1 = ' + str(row[12]) + ', DUMFLD2 = ' + str(row[13]) + ', DUMFLD3 = ' + str(row[14]) + ', DUMFLD4 = ' + str(row[15]) + ', DUMFLD5 = ' + str(row[16]) + ', DUMFLD6 = ' + str(row[17]) + ', DUMFLD7 = ' + str(row[18]) + ', DUMFLD8 = ' + str(row[19]) + ', DUMFLD9 = ' + str(row[20]) + ', DUMFLD10 = ' + str(row[21]) + ', DUMFLD11 = ' + str(row[22]) + ', DUMFLD12 = ' + str(row[23]) + ', DUMFLD13 = ' + str(row[24]) + ', DUMFLD14 = ' + str(row[25]) + ', DUMFLD15 = ' + str(row[26]) + ', DUMFLD16 = ' + str(row[27]) + ', DUMFLD17 = ' + str(row[28]) + ', DUMFLD18 = ' + str(row[29]) + ', DUMFLD19 = ' + str(row[30]) + ', DUMFLD20 = ' + str(row[31]) +  ', ACCTNO = ' + str(row[32]) + ', DE_STATUS = ' + str(row[33]) + ', DECOMMFLAG = ' + str(row[34]) + ', PARENTID = ' + str(row[35]) + ', PARENTREC = ' + str(row[36]) + ', COPYNO = ' + str(row[37])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

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

		return patientList

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

		return patientList

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

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromPosthosp(myCursor):
	print('Testing POSTHOSP!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.POSTHOSP')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[38])
			task = 'POSTHOSP'
			timestamp = str(row[0])
			otherAttributes = 'PH_ENT_TM = ' + str(row[1]) + ', PH_ENT_FRM = ' + str(row[2]) + ', FNL_OUTCM = ' + str(row[3]) + ', DSCHG_TO = ' + str(row[4]) + ', PH_LFT_VIA = ' + str(row[5]) + ', DEST_FACTY = ' + str(row[6]) + ', REASON_CH = ' + str(row[7]) + ', FOLL_DOC = ' + str(row[8]) + ', FOLL_SVC = ' + str(row[9]) + ', TR_OUTHOSP = ' + str(row[10]) + ', DC_PHYS = ' + str(row[11]) + ', DUMFLD1 = ' + str(row[12]) + ', DUMFLD2 = ' + str(row[13]) + ', DUMFLD3 = ' + str(row[14]) + ', DUMFLD4 = ' + str(row[15]) + ', DUMFLD5 = ' + str(row[16]) + ', DUMFLD6 = ' + str(row[17]) + ', DUMFLD7 = ' + str(row[18]) + ', DUMFLD8 = ' + str(row[19]) + ', DUMFLD9 = ' + str(row[20]) + ', DUMFLD10 = ' + str(row[21]) + ', DUMFLD11 = ' + str(row[22]) + ', DUMFLD12 = ' + str(row[23]) + ', DUMFLD13 = ' + str(row[24]) + ', DUMFLD14 = ' + str(row[25]) + ', DUMFLD15 = ' + str(row[26]) + ', DUMFLD16 = ' + str(row[27]) + ', DUMFLD17 = ' + str(row[28]) + ', DUMFLD18 = ' + str(row[29]) + ', DUMFLD19 = ' + str(row[30]) + ', DUMFLD20 = ' + str(row[31]) + ', ACCTNO = ' + str(row[32]) + ', DE_STATUS = ' + str(row[33]) + ', DECOMMFLAG = ' + str(row[34]) + ', PARENTID = ' + str(row[35]) + ', PARENTREC = ' + str(row[36]) + ', COPYNO = ' + str(row[37])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromPreconds(myCursor):
	print('Testing PRECONDS!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.PRECONDS')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[30])
			task = 'PRECONDS'
			timestamp = 'None'
			otherAttributes = 'PRE_HIST = ' + str(row[0]) + ', PRE_APACHE = ' + str(row[1]) + ', COMP_ICD9 = ' + str(row[2]) + ', PRE_TEXT = ' + str(row[3]) + ', DUMFLD1 = ' + str(row[4]) + ', DUMFLD2 = ' + str(row[5]) + ', DUMFLD3 = ' + str(row[6]) + ', DUMFLD4 = ' + str(row[7]) + ', DUMFLD5 = ' + str(row[8]) + ', DUMFLD6 = ' + str(row[9]) + ', DUMFLD7 = ' + str(row[10]) + ', DUMFLD8 = ' + str(row[11]) + ', DUMFLD9 = ' + str(row[12]) + ', DUMFLD10 = ' + str(row[13]) + ', DUMFLD11 = ' + str(row[14]) + ', DUMFLD12 = ' + str(row[15]) + ', DUMFLD13 = ' + str(row[16]) + ', DUMFLD14 = ' + str(row[17]) + ', DUMFLD15 = ' + str(row[18]) + ', DUMFLD16 = ' + str(row[19]) + ', DUMFLD17 = ' + str(row[20]) + ', DUMFLD18 = ' + str(row[21]) + ', DUMFLD19 = ' + str(row[22]) + ', DUMFLD20 = ' + str(row[23]) + ', ACCTNO = ' + str(row[24])  + ', DE_STATUS = ' + str(row[25])  + ', DECOMMFLAG = ' + str(row[26]) + ', PARENTID = ' + str(row[27]) + ', PARENTREC = ' + str(row[28])  + ', COPYNO = ' + str(row[29])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromProtect(myCursor):
	print('Testing PROTECT!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.PROTECT')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[29])
			task = 'PROTECT'
			timestamp = 'None'
			otherAttributes = 'PROTECTIVE = ' + str(row[0]) + ', DUMFLD1 = ' + str(row[1]) + ', DUMFLD2 = ' + str(row[2]) + ', DUMFLD3 = ' + str(row[3]) + ', DUMFLD4 = ' + str(row[4]) + ', DUMFLD5 = ' + str(row[5]) + ', DUMFLD6 = ' + str(row[6]) + ', DUMFLD7 = ' + str(row[7]) + ', DUMFLD8 = ' + str(row[8]) + ', DUMFLD9 = ' + str(row[9]) + ', DUMFLD10 = ' + str(row[10]) + ', DUMFLD11 = ' + str(row[11]) + ', DUMFLD12 = ' + str(row[12]) + ', DUMFLD13 = ' + str(row[13]) + ', DUMFLD14 = ' + str(row[14]) + ', DUMFLD15 = ' + str(row[15]) + ', DUMFLD16 = ' + str(row[16]) + ', DUMFLD17 = ' + str(row[17]) + ', DUMFLD18 = ' + str(row[18]) + ', DUMFLD19 = ' + str(row[19]) + ', DUMFLD20 = ' + str(row[20]) + ', AIRBAG = ' + str(row[21]) + ', CHILDSEAT = ' + str(row[22]) + ', ACCTNO = ' + str(row[23])  + ', DE_STATUS = ' + str(row[24])  + ', DECOMMFLAG = ' + str(row[25]) + ', PARENTID = ' + str(row[26]) + ', PARENTREC = ' + str(row[27])  + ', COPYNO = ' + str(row[28])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromQaissue(myCursor):
	print('Testing QAISSUE!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.QAISSUE')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[54])
			task = 'QAISSUE'
			timestamp = str(row[8])
			problematicString = 'None'
			otherAttributes = 'CAREPHASE = ' + str(row[0]) + ', ORG_DATE = ' + str(row[1]) + ', QA_ISSUE = ' + str(row[2]) + ', PRIM_CAUSE = ' + str(row[3]) + ', REVIEW_BY = ' + str(row[4]) + ', REVIEW_DAT = ' + str(row[5]) + ', RECOMD = ' + str(row[6]) + ', RESOLUTE = ' + str(row[7]) + ', IS_DESCRIP = ' + str(row[9]) + ', DOC_NAME = ' + str(row[10]).replace(u"\u2019", "'").replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2014", '-').replace(u"\u2026", '...').replace(u"\u2013", '-').replace(u"\u2018", "'") + ', FACTOR = ' + str(row[11]) + ', MORBIDITY = ' + str(row[12]) + ', MORTABILITY = ' + str(row[13]) + ', QI_MEMO = ' + str(row[14]).replace(u"\u2019", "'").replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2014", '-').replace(u"\u2026", '...').replace(u"\u2013", '-').replace(u"\u2018", "'") + ', DUMFLD1 = ' + str(row[15]) + ', DUMFLD2 = ' + str(row[16]) + ', DUMFLD3 = ' + str(row[17]) + ', DUMFLD4 = ' + str(row[18]) + ', DUMFLD5 = ' + str(row[19]) + ', DUMFLD6 = ' + str(row[20]) + ', DUMFLD7 = ' + str(row[21]) + ', DUMFLD8 = ' + str(row[22]) + ', DUMFLD9 = ' + str(row[23]) + ', DUMFLD10 = ' + str(row[24]) + ', DUMFLD11 = ' + str(row[25]) + ', DUMFLD12 = ' + str(row[26]) + ', DUMFLD13 = ' + str(row[27]) + ', DUMFLD14 = ' + str(row[28]) + ', DUMFLD15 = ' + str(row[29]) + ', DUMFLD16 = ' + str(row[30]) + ', DUMFLD17 = ' + str(row[31]) + ', DUMFLD18 = ' + str(row[32]) + ', DUMFLD19 = ' + str(row[33]) + ', DUMFLD20 = ' + str(row[34]) + ', QA_PDA = ' + str(row[35]) + ', QA_PDA2 = ' + str(row[36]).replace(u"\u2019", "'").replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2014", '-').replace(u"\u2026", '...').replace(u"\u2013", '-').replace(u"\u2018", "'") + ', ACTION = ' + str(row[37]).replace(u"\u2019", "'").replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2014", '-').replace(u"\u2026", '...').replace(u"\u2013", '-').replace(u"\u2018", "'") + ', REFERTO = ' + str(row[38]).replace(u"\u2019", "'").replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2014", '-').replace(u"\u2026", '...').replace(u"\u2013", '-').replace(u"\u2018", "'") + ', LOCATION = ' + str(row[39]) + ', TPM_R_DATE = ' + str(row[40]) + ', TMD_R_DATE = ' + str(row[41]) + ', HX_FLU = ' + problematicString + ', QA_EVENT = ' + str(row[43]) + ', SYSREL = ' + str(row[44]) + ', DISREL = ' + str(row[45]) + ', PROVEL = ' + str(row[46]) + ', STATUS = ' + str(row[47]) + ', ACCTNO = ' + str(row[48]) + ', DE_STATUS = ' + str(row[49]) + ', DECOMMFLAG = ' + str(row[50]) + ', PARENTID = ' + str(row[51]) + ', PARENTREC = ' + str(row[52]) + ', COPYNO = ' + str(row[53])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromRadiolog(myCursor):
	print('Testing RADIOLOG!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.RADIOLOG')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[38])
			task = 'RADIOLOG'
			timestamp = str(row[1])
			otherAttributes = 'CAREPHASE = ' + str(row[0]) + ', ORD_TIME = ' + str(row[2]) + ', STUDY = ' + str(row[3]) + ', BODY = ' + str(row[4]) + ', RESULT = ' + str(row[5]) + ', RESLT_DATE = ' + str(row[6]) + ', RESLT_TIME = ' + str(row[7]) + ', EXT_SRRC = ' + str(row[8]) + ', HEADCT_FN = ' + str(row[9]) + ', TIMETO = ' + str(row[10]) + ', PHASE_COPY = ' + str(row[11]) + ', DUMFLD1 = ' + str(row[12]) + ', DUMFLD2 = ' + str(row[13]) + ', DUMFLD3 = ' + str(row[14]) + ', DUMFLD4 = ' + str(row[15]) + ', DUMFLD5 = ' + str(row[16]) + ', DUMFLD6 = ' + str(row[17]) + ', DUMFLD7 = ' + str(row[18]) + ', DUMFLD8 = ' + str(row[19]) + ', DUMFLD9 = ' + str(row[20]) + ', DUMFLD10 = ' + str(row[21]) + ', DUMFLD11 = ' + str(row[22]) + ', DUMFLD12 = ' + str(row[23]) + ', DUMFLD13 = ' + str(row[24]) + ', DUMFLD14 = ' + str(row[25]) + ', DUMFLD15 = ' + str(row[26]) + ', DUMFLD16 = ' + str(row[27]) + ', DUMFLD17 = ' + str(row[28]) + ', DUMFLD18 = ' + str(row[29]) + ', DUMFLD19 = ' + str(row[30]) + ', DUMFLD20 = ' + str(row[31]) + ', ACCTNO = ' + str(row[32]) + ', DE_STATUS = ' + str(row[33]) + ', DECOMMFLAG = ' + str(row[34]) + ', PARENTID = ' + str(row[35]) + ', PARENTREC = ' + str(row[36]) + ', COPYNO = ' + str(row[37])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromReadmit(myCursor):
	print('Testing READMIT!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.READMIT')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[37])
			task = 'READMIT'
			timestamp = str(row[0])
			otherAttributes = 'ENT_TIME = ' + str(row[1]) + ', EXIT_DATE = ' + str(row[2]) + ', EXIT_TIME = ' + str(row[3]) + ', ENT_FROM = ' + str(row[4]) + ', EXIT_TO = ' + str(row[5]) + ', DOCTOR = ' + str(row[6]) + ', SERVICE = ' + str(row[7]) + ', SUB_CT = ' + str(row[8]) + ', UNPLAN_RTN = ' + str(row[9]) + ', LOS = ' + str(row[10]) + ', DUMFLD1 = ' + str(row[11]) + ', DUMFLD2 = ' + str(row[12]) + ', DUMFLD3 = ' + str(row[13]) + ', DUMFLD4 = ' + str(row[14]) + ', DUMFLD5 = ' + str(row[15]) + ', DUMFLD6 = ' + str(row[16]) + ', DUMFLD7 = ' + str(row[17]) + ', DUMFLD8 = ' + str(row[18]) + ', DUMFLD9 = ' + str(row[19]) + ', DUMFLD10 = ' + str(row[20]) + ', DUMFLD11 = ' + str(row[21]) + ', DUMFLD12 = ' + str(row[22]) + ', DUMFLD13 = ' + str(row[23]) + ', DUMFLD14 = ' + str(row[24]) + ', DUMFLD15 = ' + str(row[25]) + ', DUMFLD16 = ' + str(row[26]) + ', DUMFLD17 = ' + str(row[27]) + ', DUMFLD18 = ' + str(row[28]) + ', DUMFLD19 = ' + str(row[29]) + ', DUMFLD20 = ' + str(row[30]) + ', ACCTNO = ' + str(row[31]) + ', DE_STATUS = ' + str(row[32]) + ', DECOMMFLAG = ' + str(row[33]) + ', PARENTID = ' + str(row[34]) + ', PARENTREC = ' + str(row[35]) + ', COPYNO = ' + str(row[36])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromStep(myCursor):
	print('Testing STEP!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.STEP')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[37])
			task = 'STEP'
			timestamp = str(row[0])
			otherAttributes = 'ENT_TIME = ' + str(row[1]) + ', EXIT_DATE = ' + str(row[2]) + ', EXIT_TIME = ' + str(row[3]) + ', ENT_FROM = ' + str(row[4]) + ', EXIT_TO = ' + str(row[5]) + ', DOCTOR = ' + str(row[6]) + ', SERVICE = ' + str(row[7]) + ', SUB_CT = ' + str(row[8]) + ', UNPLAN_RTN = ' + str(row[9]) + ', LOS = ' + str(row[10]) + ', DUMFLD1 = ' + str(row[11]) + ', DUMFLD2 = ' + str(row[12]) + ', DUMFLD3 = ' + str(row[13]) + ', DUMFLD4 = ' + str(row[14]) + ', DUMFLD5 = ' + str(row[15]) + ', DUMFLD6 = ' + str(row[16]) + ', DUMFLD7 = ' + str(row[17]) + ', DUMFLD8 = ' + str(row[18]) + ', DUMFLD9 = ' + str(row[19]) + ', DUMFLD10 = ' + str(row[20]) + ', DUMFLD11 = ' + str(row[21]) + ', DUMFLD12 = ' + str(row[22]) + ', DUMFLD13 = ' + str(row[23]) + ', DUMFLD14 = ' + str(row[24]) + ', DUMFLD15 = ' + str(row[25]) + ', DUMFLD16 = ' + str(row[26]) + ', DUMFLD17 = ' + str(row[27]) + ', DUMFLD18 = ' + str(row[28]) + ', DUMFLD19 = ' + str(row[29]) + ', DUMFLD20 = ' + str(row[30]) + ', ACCTNO = ' + str(row[31]) + ', DE_STATUS = ' + str(row[32]) + ', DECOMMFLAG = ' + str(row[33]) + ', PARENTID = ' + str(row[34]) + ', PARENTREC = ' + str(row[35]) + ', COPYNO = ' + str(row[36])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromSurg(myCursor): 
	print('Testing SURG!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.SURG')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[51])
			task = 'SURG'
			timestamp = str(row[1])
			otherAttributes = 'CAREPHASE = ' + str(row[0]) + ', AN_ST_TME = ' + str(row[2]) + ', AN_END_TIME = ' + str(row[3]) + ', PROC_ICD9 = ' + str(row[4]) + ', CPT = ' + str(row[5]) + ', PROC_TYPE = ' + str(row[6]) + ', PRIM_SURG = ' + str(row[7]).replace(u"\u0178", 'Y') + ', PROBLEM = ' + str(row[8]) + ', ANEST_MODE = ' + str(row[9]) + ', PHARM_AGNT = ' + str(row[10]) + ', BLD_LOSS = ' + str(row[11]) + ', DESCRIPT = ' + str(row[12]) + ', H_SBP = ' + str(row[13]) + ', L_SBP = ' + str(row[14]) + ', L_TEMP = ' + str(row[15]) + ', TOTAL_FLDS = ' + str(row[16]) + ', TOT_TIME = ' + str(row[17]) + ', TIME_INJY = ' + str(row[18]) + ', PR_TEXT = ' + str(row[19]) + ', OTH_SURGN = ' + str(row[20]) + ', PHASE_COPY = ' + str(row[21]) + ', DUMFLD1 = ' + str(row[22]) + ', DUMFLD2 = ' + str(row[23]) + ', DUMFLD3 = ' + str(row[24]) + ', DUMFLD4 = ' + str(row[25]) + ', DUMFLD5 = ' + str(row[26]) + ', DUMFLD6 = ' + str(row[27]) + ', DUMFLD7 = ' + str(row[28]) + ', DUMFLD8 = ' + str(row[29]) + ', DUMFLD9 = ' + str(row[30]) + ', DUMFLD10 = ' + str(row[31]) + ', DUMFLD11 = ' + str(row[32]) + ', DUMFLD12 = ' + str(row[33]) + ', DUMFLD13 = ' + str(row[34]) + ', DUMFLD14 = ' + str(row[35]) + ', DUMFLD15 = ' + str(row[36]) + ', DUMFLD16 = ' + str(row[37]) + ', DUMFLD17 = ' + str(row[38]) + ', DUMFLD18 = ' + str(row[39]) + ', DUMFLD19 = ' + str(row[40]) + ', DUMFLD20 = ' + str(row[41]) + ', DATE_OUT = ' + str(row[42]) + ', PRO_STRT = ' + str(row[43]) + ', PROC_END = ' + str(row[44]) + 'ACTNO = ' + str(row[45]) + ', DE_STATUS = ' + str(row[46]) + ', DECOMMFLAG = ' + str(row[47]) + ', PARENTID = ' + str(row[48]) + ', PARENTREC = ' + str(row[49]) + ', COPYNO = ' + str(row[50])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromSysdefs(myCursor): 
	print('Testing sysdefs!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_SYS.sysdefs')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = 'None'
			task = 'sysdefs'
			timestamp = str(row[48])
			otherAttributes = 'SHIFT1STAR = ' + str(row[0]) + ', SHIFT1END = ' + str(row[1]) + ', SHIFT2STAR = ' + str(row[2]) + ', SHIFT2END = ' + str(row[3]) + ', SHIFT3STAR = ' + str(row[4]) + ', SHIFT3END = ' + str(row[5]) + ', DT_SEPRATR = ' + str(row[6]) + ', DT_ORDER = ' + str(row[7]) + ', DT_CENTURY = ' + str(row[8]) + ', TM_SEPRATR = ' + str(row[9]) + ', TM_SECONDS = ' + str(row[10]) + ', SECURITY = ' + str(row[11]) + ', AUTOLOCK = ' + str(row[12]) + ', CROSS_CHEC = ' + str(row[13]) + ', SHOWSTAT = ' + str(row[14]) + ', CRYPTION = ' + str(row[15]) + ', ONCLOSEPOP = ' + str(row[16]) + ', LOCKDELAY = ' + str(row[17]) + ', RTT_ACTIVE = ' + str(row[18]) + ', RTT_UNIV = ' + str(row[19]) + ', RTT_INTVAL = ' + str(row[20]) + ', SYSLOGDETS = ' + str(row[21]) + ', SLPURGE_EX = ' + str(row[22]) + ', SLPURGE_NM = ' + str(row[23]) + ', SLPURGE_VB = ' + str(row[24]) + ', DETIMEOUT = ' + str(row[25]) + ', DETOQLOGIN = ' + str(row[26]) + ', ONLOCKRT = ' + str(row[27]) + ', WARNONSEL = ' + str(row[28]) + ', INSTADD = ' + str(row[29]) + ', INSTPHONE = ' + str(row[30]) + ', INSTFAX = ' + str(row[31]) + ', INSTMODEM = ' + str(row[32]) + ', INST_EMAIL = ' + str(row[33]) + ', CB_REFRMIN = ' + str(row[34]) + ', TIMEOUT_CB = ' + str(row[35]) + ', THAUTOREST = ' + str(row[36]) + ', DFLTREPCPY = ' + str(row[37]) + ', SHOWIGNERR = ' + str(row[38]) + ', CHRTFORMAT = ' + str(row[39]) + ', CHRTSORT = ' + str(row[40]) + ', TMCB_PRIOR = ' + str(row[41]) + ', DEF_SERVER = ' + str(row[42]) + ', EASYDECTLS = ' + str(row[43]) + 'FORCERBOOT = ' + str(row[44]) + ', MAXRBOOTTM = ' + str(row[45]) + ', WSOG_INTVL = ' + str(row[46]) + ', MEM_TMSTMP = ' + str(row[47]) + ', MAX_APP_DT = ' + str(row[49]) + ', OPSTATUS = ' + str(row[50]) + ', EXBLTEXT = ' + str(row[51]) + ', EXNATEXT = ' + str(row[52]) + ', EXNDTEXT = ' + str(row[53]) + ', INTELLPICL = ' + str(row[54]) + ', MINPWDLEN = ' + str(row[55]) + ', PWDSTYLE = ' + str(row[56]) + ', PWDEQUSR = ' + str(row[57]) + ', PWDEXPRFLG = ' + str(row[58]) + ', PWDEXPRVAL = ' + str(row[59]) + ', MAXINACTVE = ' + str(row[60]) + ', MAXATTMPT = ' + str(row[61]) + ', LANCLOGIN = ' + str(row[62]) + ', DISPDISCLM = ' + str(row[63]) + ', DISCLAIMER = ' + str(row[64]) + ', TAB_EASYDE = ' + str(row[65]) + ', RESERVE1 = ' + str(row[66]) + ', RESERVE2 = ' + str(row[67]) + ', RESERVE3 = ' + str(row[68]) + ', RESERVE4 = ' + str(row[69]) + ', RESERVE5 = ' + str(row[70]) + ', RESERVE6 = ' + str(row[71]) + ', RESERVE7 = ' + str(row[72]) + ', RESERVE8 = ' + str(row[73]) + ', RESERVE9 = ' + str(row[74]) + ', RESERVE10 = ' + str(row[75])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromTLogComm(myCursor):
	print('Testing TLogComm!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TRAUMA2.TLogComm')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[0]) + ' and ' + str(row[3])
			task = 'TLogComm'
			timestamp = 'None'
			otherAttributes = 'tcomment = ' + str(row[1]).replace(u"\u2019", "'").replace(u"\u201c", '"').replace(u"\u201d", '"').replace(u"\u2014", '-').replace(u"\u2026", '...').replace(u"\u2013", '-').replace(u"\u2018", "'") + ', timage = ' + str(row[2]) 
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromToxianal(myCursor): 
	print('Testing TOXIANAL!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.TOXIANAL')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[40])
			task = 'TOXIANAL'
			timestamp = str(row[1])
			otherAttributes = 'CAREPHASE = ' + str(row[0]) + ', ORD_TIME = ' + str(row[2]) + ', DRAW_DATE = ' + str(row[3]) + ', DRAW_TIME = ' + str(row[4]) + ', ORD_TIME = ' + str(row[5]) + ', RESLT_DATE = ' + str(row[6]) + ', RESLT_TIME = ' + str(row[7]) + ', DESCRIPT = ' + str(row[8]) + ', SUBSTANCE = ' + str(row[9]) + ', CT = ' + str(row[10]) + ', RESULT_VAL = ' + str(row[11]) + ', STATUS = ' + str(row[12]) + ', PHASE_COPY = ' + str(row[13]) + ', DUMFLD1 = ' + str(row[14]) + ', DUMFLD2 = ' + str(row[15]) + ', DUMFLD3 = ' + str(row[16]) + ', DUMFLD4 = ' + str(row[17]) + ', DUMFLD5 = ' + str(row[18]) + ', DUMFLD6 = ' + str(row[19]) + ', DUMFLD7 = ' + str(row[20]) + ', DUMFLD8 = ' + str(row[21]) + ', DUMFLD9 = ' + str(row[22]) + ', DUMFLD10 = ' + str(row[23]) + ', DUMFLD11 = ' + str(row[24]) + ', DUMFLD12 = ' + str(row[25]) + ', DUMFLD13 = ' + str(row[26]) + ', DUMFLD14 = ' + str(row[27]) + ', DUMFLD15 = ' + str(row[28]) + ', DUMFLD16 = ' + str(row[29]) + ', DUMFLD17 = ' + str(row[30]) + ', DUMFLD18 = ' + str(row[31]) + ', DUMFLD19 = ' + str(row[32]) + ', DUMFLD20 = ' + str(row[33]) + ', ACCTNO = ' + str(row[34]) + ', DE_STATUS = ' + str(row[35]) + ', DECOMMFLAG = ' + str(row[36]) + ', PARENTID = ' + str(row[37]) + ', PARENTREC = ' + str(row[38]) + ', COPYNO = ' + str(row[39])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromTra(myCursor):
	print('Testing TRA!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.TRA')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[51])
			task = 'TRA'
			timestamp = str(row[1])
			otherAttributes = 'TR_NOTIFID = ' + str(row[0]) + ', TR_NOTF_TM = ' + str(row[2]) + ', TR_DOA = ' + str(row[3]) + ', TR_MJR_TRM = ' + str(row[4]) + ', TR_ENT_DT = ' + str(row[5]) + ', TR_ENT_TM = ' + str(row[6]) + ', TR_EXIT_DT = ' + str(row[7]) + ', TR_EXIT_TM = ' + str(row[8]) + ', TR_ENT_FRM = ' + str(row[9]) + ', TR_EXIT_TO = ' + str(row[10]) + ', TR_ADM_TYP = ' + str(row[11]) + ', TR_ADM_SRC = ' + str(row[12]) + ', TR_DISPO = ' + str(row[13]) + ', TR_LFT_VIA = ' + str(row[14]) + ', TR_REBG_TM = ' + str(row[15]) + ', TR_REEN_TM = ' + str(row[16]) + ', TR_DOCTOR = ' + str(row[17]) + ', TR_SERVICE = ' + str(row[18]) + ', TR_UNCPROB = ' + str(row[19]) + ', TR_LOS = ' + str(row[20]) + ', TR_SUB_CT = ' + str(row[21]) + ', TR_SEV_HD = ' + str(row[22]) + ', TME_CT = ' + str(row[23]) + ', RD_TOT_TME = ' + str(row[24]) + ', DUMFLD1 = ' + str(row[25]) + ', DUMFLD2 = ' + str(row[26]) + ', DUMFLD3 = ' + str(row[27]) + ', DUMFLD4 = ' + str(row[28]) + ', DUMFLD5 = ' + str(row[29]) + ', DUMFLD6 = ' + str(row[30]) + ', DUMFLD7 = ' + str(row[31]) + ', DUMFLD8 = ' + str(row[32]) + ', DUMFLD9 = ' + str(row[33]) + ', DUMFLD10 = ' + str(row[34]) + ', DUMFLD11 = ' + str(row[35]) + ', DUMFLD12 = ' + str(row[36]) + ', DUMFLD13 = ' + str(row[37]) + ', DUMFLD14 = ' + str(row[38]) + ', DUMFLD15 = ' + str(row[39]) + ', DUMFLD16 = ' + str(row[40]) + ', DUMFLD17 = ' + str(row[41]) + ', DUMFLD18 = ' + str(row[42]) + ', DUMFLD19 = ' + str(row[43]) + ', DUMFLD20 = ' + str(row[44]) + 'ACCTNO = ' + str(row[45]) + ', DE_STATUS = ' + str(row[46]) + ', DECOMMFLAG = ' + str(row[47]) + ', PARENTID = ' + str(row[48]) + ', PARENTREC = ' + str(row[49]) + ', COPYNO = ' + str(row[50])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromTranlog(myCursor): # IT WON'T RUN!!
	print('Testing tranlog!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ("SELECT DISTINCT acctno \
							FROM TRAUMA2.tranlog")
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []
		for row in results:
			print(row[0])
			fetchTuplesFromTranlog(row[0], patientList, myCursor)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def fetchTuplesFromTranlog(acctno, patientList, myCursor):
	# be careful about the list
	try:
		SQLSelectCommand = ("SELECT * \
							FROM TRAUMA2.tranlog \
							WHERE acctno = %d" % (acctno) )
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()
		
		for row in results:
			patientId = str(row[0])
			task = 'tranlog'
			timestamp = str(row[11])
			problematicString = 'None'
			otherAttributes = 'acctno = ' + str(row[1]) + ', acc_path = ' + str(row[2]) + ', copyid = ' + str(row[3]) + ', action = ' + str(row[4]) + ', fieldname = ' + str(row[5]) + ', fieldtype = ' + str(row[6]) + ', fieldval = ' + str(row[7]).replace(u"\u0178", "Y") + ', fieldstat = ' + str(row[8]) + ', memofldval = ' +  problematicString + ', genfldval = ' + str(row[10]) + ', trantime = ' + str(row[12]) + ', tranuser = ' + str(row[13]) + ', transtn = ' + str(row[14])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return 0

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromTransfer(myCursor): 
	print('Testing TRANSFER!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.TRANSFER')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[43])
			task = 'TRANSFER'
			timestamp = str(row[0])
			otherAttributes = 'ENT_TIME = ' + str(row[1]) + ', EXIT_DATE = ' + str(row[2]) + ', EXIT_TIME = ' + str(row[3]) + ', ENT_FROM = ' + str(row[4]) + ', EXIT_TO = ' + str(row[5]) + ', REF_HOSP = ' + str(row[6]) + ', REF_DOC = ' + str(row[7]) + ', REF_STAT = ' + str(row[8]) + ', TRANS_TIME = ' + str(row[9]) + ', NAT_TRFR = ' + str(row[10]) + ', RATIO_TRFR = ' + str(row[11]) + ', REAS_SEL = ' + str(row[12]) + ', OTH_REGNUM = ' + str(row[13]) + ', LOS = ' + str(row[14]) + ', PRE_FORM = ' + str(row[15]) + ', TRAN_HOSP = ' + str(row[16]) + ', DUMFLD1 = ' + str(row[17]) + ', DUMFLD2 = ' + str(row[18]) + ', DUMFLD3 = ' + str(row[19]) + ', DUMFLD4 = ' + str(row[20]) + ', DUMFLD5 = ' + str(row[21]) + ', DUMFLD6 = ' + str(row[22]) + ', DUMFLD7 = ' + str(row[23]) + ', DUMFLD8 = ' + str(row[24]) + ', DUMFLD9 = ' + str(row[25]) + ', DUMFLD10 = ' + str(row[26]) + ', DUMFLD11 = ' + str(row[27]) + ', DUMFLD12 = ' + str(row[28]) + ', DUMFLD13 = ' + str(row[29]) + ', DUMFLD14 = ' + str(row[30]) + ', DUMFLD15 = ' + str(row[31]) + ', DUMFLD16 = ' + str(row[32]) + ', DUMFLD17 = ' + str(row[33]) + ', DUMFLD18 = ' + str(row[34]) + ', DUMFLD19 = ' + str(row[35]) + ', DUMFLD20 = ' + str(row[36]) + ', ACCTNO = ' + str(row[37]) + ', DE_STATUS = ' + str(row[38]) + ', DECOMMFLAG = ' + str(row[39]) + ', PARENTID = ' + str(row[40]) + ', PARENTREC = ' + str(row[41]) + ', COPYNO = ' + str(row[42])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromTransprt(myCursor):
	print('Testing TRANSPRT!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.TRANSPRT')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[58])
			task = 'TRANSPRT'
			timestamp = str(row[1])
			otherAttributes = 'CAREPHASE = ' + str(row[0]) + ', CALL_TIME = ' + str(row[2]) + ', DISP_ID = ' + str(row[3]) + ', DISP_TIME = ' + str(row[4]) + ', DEPRT_TIME = ' + str(row[5]) + ', ARRIV_TIME = ' + str(row[6]) + ', BSCNT_TIME = ' + str(row[7]) + ', EXIT_TIME = ' + str(row[8]) + ', RENDEZ_TIME = ' + str(row[9]) + ', ETA = ' + str(row[10]) + ', DEST_TIME = ' + str(row[11]) + ', ACT_DEST = ' + str(row[12]) + ', BSCNT_ID = ' + str(row[13]) + ', BYP_HOSP = ' + str(row[14]) + ', CARRY_PT = ' + str(row[15]) + ', RS_NUM = ' + str(row[16]) + ', TRANS_TYPE = ' + str(row[17]) + ', TRANS_AGNT = ' + str(row[18]) + ', TRANS_ID = ' + str(row[19]) + ', TRANS_MODE = ' + str(row[20]) + ', PRPSE_LVL = ' + str(row[21]) + ', TRANS_DIST = ' + str(row[22]) + ', TRANS_UNIT = ' + str(row[23]) + ', TRAN_AGNCY = ' + str(row[24]) + ', RESP_TM = ' + str(row[25]) + ', SCENE_TM = ' + str(row[26]) + ', TRANSP_TM = ' + str(row[27]) + ', TOTAL_TM = ' + str(row[28]) + ', DUMFLD1' + str(row[29]) + ', DUMFLD2 = ' + str(row[30]) + ', DUMFLD3 = ' + str(row[31]) + ', DUMFLD4 = ' + str(row[32]) + ', DUMFLD5 = ' + str(row[33]) + ', DUMFLD6 = ' + str(row[34]) + ', DUMFLD7 = ' + str(row[35]) + ', DUMFLD8 = ' + str(row[36]) + ', DUMFLD9 = ' + str(row[37]) + ', DUMFLD10 = ' + str(row[38]) + ', DUMFLD11 = ' + str(row[39]) + ', DUMFLD12 = ' + str(row[40]) + ', DUMFLD13 = ' + str(row[41]) + ', DUMFLD14 = ' + str(row[42]) + ', DUMFLD15 = ' + str(row[43]) + ', DUMFLD16 = ' + str(row[44]) + ', DUMFLD17 = ' + str(row[45]) + ', DUMFLD18 = ' + str(row[46]) + ', DUMFLD19 = ' + str(row[47]) + ', DUMFLD20 = ' + str(row[48]) + ', ARR_DATE = ' + str(row[49]) + ', DEP_DATE = ' + str(row[50]) + ', DEST_DATE = ' + str(row[51]) + ', ACCTNO = ' + str(row[52]) + ', DE_STATUS = ' + str(row[53]) + ', DECOMMFLAG = ' + str(row[54]) + ', PARENTID = ' + str(row[55]) + ', PARENTREC = ' + str(row[56]) + ', COPYNO = ' + str(row[57])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromTreatmen(myCursor): 
	print('Testing TREATMEN!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.TREATMEN')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[43])
			task = 'TREATMEN'
			timestamp = str(row[1])
			otherAttributes = 'CAREPHASE = ' + str(row[0]) + ', TIME = ' + str(row[2]) + ', END_TIME = ' + str(row[3]) + ', TREATMENT = ' + str(row[4]) + ', QUANTITY = ' + str(row[5]) + ', TX_SITE = ' + str(row[6]) + ', ROUTE = ' + str(row[7]) + ', PROBLEM = ' + str(row[8]) + ', RESULTS = ' + str(row[9]) + ', TX_BY = ' + str(row[10]) + ', TX_CPT = ' + str(row[11]) + ', INT_TREAT = ' + str(row[12]) + ', INT_PFI = ' + str(row[13]) + ', IV_FLUIDS = ' + str(row[14]) + ', BLD_PROD = ' + str(row[15]) + ', PHASE_COPY = ' + str(row[16]) + ', DUMFLD1 = ' + str(row[17]) + ', DUMFLD2 = ' + str(row[18]) + ', DUMFLD3 = ' + str(row[19]) + ', DUMFLD4 = ' + str(row[20]) + ', DUMFLD5 = ' + str(row[21]) + ', DUMFLD6 = ' + str(row[22]) + ', DUMFLD7 = ' + str(row[23]) + ', DUMFLD8 = ' + str(row[24]) + ', DUMFLD9 = ' + str(row[25]) + ', DUMFLD10 = ' + str(row[26]) + ', DUMFLD11 = ' + str(row[27]) + ', DUMFLD12 = ' + str(row[28]) + ', DUMFLD13 = ' + str(row[29]) + ', DUMFLD14 = ' + str(row[30]) + ', DUMFLD15 = ' + str(row[31]) + ', DUMFLD16 = ' + str(row[32]) + ', DUMFLD17 = ' + str(row[33]) + ', DUMFLD18 = ' + str(row[34]) + ', DUMFLD19 = ' + str(row[35]) + ', DUMFLD20 = ' + str(row[36]) + ', ACCTNO = ' + str(row[37]) + ', DE_STATUS = ' + str(row[38]) + ', DECOMMFLAG = ' + str(row[39]) + ', PARENTID = ' + str(row[40]) + ', PARENTREC = ' + str(row[41]) + ', COPYNO = ' + str(row[42])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromTricrit(myCursor):
	print('Testing TRICRIT!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.TRICRIT')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[27])
			task = 'TRICRIT'
			timestamp = 'None'
			otherAttributes = 'TRIAGE_CRT = ' + str(row[0]) + ', DUMFLD1 = ' + str(row[1]) + ', DUMFLD2 = ' + str(row[2]) + ', DUMFLD3 = ' + str(row[3]) + ', DUMFLD4 = ' + str(row[4]) + ', DUMFLD5 = ' + str(row[5]) + ', DUMFLD6 = ' + str(row[6]) + ', DUMFLD7 = ' + str(row[7]) + ', DUMFLD8 = ' + str(row[8]) + ', DUMFLD9 = ' + str(row[9]) + ', DUMFLD10 = ' + str(row[10]) + ', DUMFLD11 = ' + str(row[11]) + ', DUMFLD12 = ' + str(row[12]) + ', DUMFLD13 = ' + str(row[13]) + ', DUMFLD14 = ' + str(row[14]) + ', DUMFLD15 = ' + str(row[15]) + ', DUMFLD16 = ' + str(row[16]) + ', DUMFLD17 = ' + str(row[17]) + ', DUMFLD18 = ' + str(row[18]) + ', DUMFLD19 = ' + str(row[19]) + ', DUMFLD20 = ' + str(row[20]) + ', ACCTNO = ' + str(row[21])  + ', DE_STATUS = ' + str(row[22])  + ', DECOMMFLAG = ' + str(row[23]) + ', PARENTID = ' + str(row[24]) + ', PARENTREC = ' + str(row[25])  + ', COPYNO = ' + str(row[26])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromTrmteam(myCursor):
	print('Testing TRMTEAM!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.TRMTEAM')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[35])
			task = 'TRMTEAM'
			timestamp = str(row[1])
			otherAttributes = 'CAREPHASE = ' + str(row[0]) + ', CODE_TIME = ' + str(row[2]) + ', CALL_TIME = ' + str(row[3]) + ', ACT_TIME = ' + str(row[4]) + ', ACT_LEVEL = ' + str(row[5]) + ', WORKING = ' + str(row[6]) + ', ACTIVATED = ' + str(row[7]) + ', PHASE_COPY = ' + str(row[8]) + ', DUMFLD1 = ' + str(row[9]) + ', DUMFLD2 = ' + str(row[10]) + ', DUMFLD3 = ' + str(row[11]) + ', DUMFLD4 = ' + str(row[12]) + ', DUMFLD5 = ' + str(row[13]) + ', DUMFLD6 = ' + str(row[14]) + ', DUMFLD7 = ' + str(row[15]) + ', DUMFLD8 = ' + str(row[16]) + ', DUMFLD9 = ' + str(row[17]) + ', DUMFLD10 = ' + str(row[18]) + ', DUMFLD11 = ' + str(row[19]) + ', DUMFLD12 = ' + str(row[20]) + ', DUMFLD13 = ' + str(row[21]) + ', DUMFLD14 = ' + str(row[22]) + ', DUMFLD15 = ' + str(row[23]) + ', DUMFLD16 = ' + str(row[24]) + ', DUMFLD17 = ' + str(row[25]) + ', DUMFLD18 = ' + str(row[26]) + ', DUMFLD19 = ' + str(row[27]) + ', DUMFLD20 = ' + str(row[28]) + ', ACCTNO = ' + str(row[29]) + ', DE_STATUS = ' + str(row[30]) + ', DECOMMFLAG = ' + str(row[31]) + ', PARENTID = ' + str(row[32]) + ', PARENTREC = ' + str(row[33]) + ', COPYNO = ' + str(row[34])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromTtdetls(myCursor): 
	print('Testing TTDETLS!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.TTDETLS')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[38])
			task = 'TTDETLS'
			timestamp = str(row[31])
			otherAttributes = 'CAREPHASE = ' + str(row[0]) + ', SPECIALITY = ' + str(row[1]).replace(u"\u0178", "Y") + ', MEM_CODE = ' + str(row[2]) + ', MEM_CALL = ' + str(row[3]) + ', PHNE_RESP = ' + str(row[4]) + ', MEM_ARRIV = ' + str(row[5]) + ', DEPRT_TIME = ' + str(row[6]) + ', TT_OTHER = ' + str(row[7]) + ', RESP_TIME = ' + str(row[8]) + ', PHASE_COPY = ' + str(row[9]) + ', DUMFLD1 = ' + str(row[10]) + ', DUMFLD2 = ' + str(row[11]) + ', DUMFLD3 = ' + str(row[12]) + ', DUMFLD4 = ' + str(row[13]) + ', DUMFLD5 = ' + str(row[14]) + ', DUMFLD6 = ' + str(row[15]) + ', DUMFLD7 = ' + str(row[16]) + ', DUMFLD8 = ' + str(row[17]) + ', DUMFLD9 = ' + str(row[18]) + ', DUMFLD10 = ' + str(row[19]) + ', DUMFLD11 = ' + str(row[20]) + ', DUMFLD12 = ' + str(row[21]) + ', DUMFLD13 = ' + str(row[22]) + ', DUMFLD14 = ' + str(row[23]) + ', DUMFLD15 = ' + str(row[24]) + ', DUMFLD16 = ' + str(row[25]) + ', DUMFLD17 = ' + str(row[26]) + ', DUMFLD18 = ' + str(row[27]) + ', DUMFLD19 = ' + str(row[28]) + ', DUMFLD20 = ' + str(row[29]) + ', TT_LONGNAM = ' + str(row[30]) +  ', ACCTNO = ' + str(row[32]) + ', DE_STATUS = ' + str(row[33]) + ', DECOMMFLAG = ' + str(row[34]) + ', PARENTID = ' + str(row[35]) + ', PARENTREC = ' + str(row[36]) + ', COPYNO = ' + str(row[37])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromVitals(myCursor):
	print('Testing VITALS!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.VITALS')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[110])
			task = 'VITALS'
			timestamp = str(row[53])
			otherAttributes = 'HR = ' + str(row[0]) + ', PULSE_OX = ' + str(row[1]) + ', HRT_RYTHM = ' + str(row[2]) + ', SKIN_COND = ' + str(row[3]) + ', BREAT_STAT = ' + str(row[4]) + ', PED_AIR = ' + str(row[5]) + ', PED_OPEN = ' + str(row[6]) + ', PED_CNS = ' + str(row[7]) + ', PED_PULSE = ' + str(row[8]) + ', PED_SKEL = ' + str(row[9]) + ', PED_WGTH = ' + str(row[10]) + ', PED_PTS = ' + str(row[11]) + ', CRAMS_C = ' + str(row[12]) + ', CRAMS_R = ' + str(row[13]) + ', CRAMS_A = ' + str(row[14]) + ', CRAMS_M = ' + str(row[15]) + ', CRAMS_S = ' + str(row[16]) + ', CRAMS = ' + str(row[17]) + ', TEMP = ' + str(row[18]) + ', TEMP_UNITS = ' + str(row[19]) + ', TEMP_LOC = ' + str(row[20]) + ', HEIGHT = ' + str(row[21]) + ', HT_UNITS = ' + str(row[22]) + ', WEIGHT = ' + str(row[23]) + ', WT_UNITS = ' + str(row[24]) + ', ETOH_STAT = ' + str(row[25]) + ', ETOH_LEVEL = ' + str(row[26]) + ', PUP_REAC_L = ' + str(row[27]) + ', PUP_REAC_R = ' + str(row[28]) + ', PUP_SIZE_L = ' + str(row[29]) + ', PUP_SIZE_R = ' + str(row[30]) + ', PA_SYS = ' + str(row[31]) + ', PA_DIA = ' + str(row[32]) + ', PA_MEAN = ' + str(row[33]) + ', ICP = ' + str(row[34]) + ', PWP = ' + str(row[35]) + ', CARD_OUT = ' + str(row[36]) + ', CV_PRESSURE = ' + str(row[37]) + ', URINE_OUT = ' + str(row[38]) + ', CHEST_OUT = ' + str(row[39]) + ', NG_OUT = ' + str(row[40]) + ', FIST_OUT = ' + str(row[41]) + ', MONT_TYPE = ' + str(row[42]) + ', OPEN_ICP = ' + str(row[43]) + ', HIGH_ICP = ' + str(row[44]) + ', INS_CPP = ' + str(row[45]) + ', LOW_CPP = ' + str(row[46]) + ', LOW_SBP = ' + str(row[47]) + ', LOW_SAO2 = ' + str(row[48]) + ', FIRST_PCO2 = ' + str(row[49]) + ', REP_ABG = ' + str(row[50]) + ', REP_PCO2 = ' + str(row[51]) + ', CAREPHASE = ' + str(row[52]) + ', TIME = ' + str(row[54]) + ', VS_DESIGN = ' + str(row[55]) + ', PAR_AGENT = ' + str(row[56]) + ', INTUBATED = ' + str(row[57]) + ', RESP_RATE = ' + str(row[58]) + ', RR_CONTRL = ' + str(row[59]) + ', RESP_ASST = ' + str(row[60]) + ', RESP_EXPS = ' + str(row[61]) + ', CAP_REFIL = ' + str(row[62]) + ', BP_MEASURE = ' + str(row[63]) + ', SBP = ' + str(row[64]) + ', DBP = ' + str(row[65]) + ', MBP = ' + str(row[66]) + ', EO = ' + str(row[67]) + ', VR = ' + str(row[68]) + ', MR = ' + str(row[69]) + ', GCS = ' + str(row[70]) + ', TS = ' + str(row[71]) + ', RTS_RAW = ' + str(row[72]) + ', RTS = ' + str(row[73]) + ', VENT_DAYS = ' + str(row[74]) + ', PRBCS = ' + str(row[75]) + ', FFP = ' + str(row[76]) + ', PLATELET = ' + str(row[77]) + ', CRYO = ' + str(row[78]) + ', TOT_BLOOD = ' + str(row[79]) + ', VIT_MEMO = ' + str(row[80]) + ', SWANGANZ = ' + str(row[81]) + ', ICP_DONE = ' + str(row[82]) + ', PHASE_COPY = ' + str(row[83]) + ', DUMFLD1 = ' + str(row[84]) + ', DUMFLD2 = ' + str(row[85]) + ', DUMFLD3 = ' + str(row[86]) + ', DUMFLD4 = ' + str(row[87]) + ', DUMFLD5 = ' + str(row[88]) + ', DUMFLD6 = ' + str(row[89]) + ', DUMFLD7 = ' + str(row[90]) + ', DUMFLD8 = ' + str(row[91]) + ', DUMFLD9 = ' + str(row[92]) + ', DUMFLD10 = ' + str(row[93]) + ', DUMFLD11 = ' + str(row[94]) + ', DUMFLD12 = ' + str(row[95]) + ', DUMFLD13 = ' + str(row[96]) + ', DUMFLD14 = ' + str(row[97]) + ', DUMFLD15 = ' + str(row[98]) + ', DUMFLD16 = ' + str(row[99]) + ', DUMFLD17 = ' + str(row[100]) + ', DUMFLD18 = ' + str(row[101]) + ', DUMFLD19 = ' + str(row[102]) + ', DUMFLD20 = ' + str(row[103]) + 'ACCTNO = ' + str(row[104]) + ', DE_STATUS = ' + str(row[105]) + ', DECOMMFLAG = ' + str(row[106]) + ', PARENTID = ' + str(row[107]) + ', PARENTREC = ' + str(row[108]) + ', COPYNO = ' + str(row[109])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def getTuplesFromWard(myCursor):
	print('Testing WARD!') 
	
    # Getting tuples
	try:
		SQLSelectCommand = ('SELECT *'
							'FROM TR02_TRANS.WARD')
		myCursor.execute(SQLSelectCommand)
		results = myCursor.fetchall()

		patientList = []

		for row in results:
			patientId = str(row[37])
			task = 'WARD'
			timestamp = str(row[0])
			otherAttributes = 'ENT_TIME = ' + str(row[1]) + ', EXIT_DATE = ' + str(row[2]) + ', EXIT_TIME = ' + str(row[3]) + ', ENT_FROM = ' + str(row[4]) + ', EXIT_TO = ' + str(row[5]) + ', DOCTOR = ' + str(row[6]) + ', SERVICE = ' + str(row[7]) + ', SUB_CT = ' + str(row[8]) + ', UNPLAN_RTN = ' + str(row[9]) + ', LOS = ' + str(row[10]) + ', DUMFLD1 = ' + str(row[11]) + ', DUMFLD2 = ' + str(row[12]) + ', DUMFLD3 = ' + str(row[13]) + ', DUMFLD4 = ' + str(row[14]) + ', DUMFLD5 = ' + str(row[15]) + ', DUMFLD6 = ' + str(row[16]) + ', DUMFLD7 = ' + str(row[17]) + ', DUMFLD8 = ' + str(row[18]) + ', DUMFLD9 = ' + str(row[19]) + ', DUMFLD10 = ' + str(row[20]) + ', DUMFLD11 = ' + str(row[21]) + ', DUMFLD12 = ' + str(row[22]) + ', DUMFLD13 = ' + str(row[23]) + ', DUMFLD14 = ' + str(row[24]) + ', DUMFLD15 = ' + str(row[25]) + ', DUMFLD16 = ' + str(row[26]) + ', DUMFLD17 = ' + str(row[27]) + ', DUMFLD18 = ' + str(row[28]) + ', DUMFLD19 = ' + str(row[29]) + ', DUMFLD20 = ' + str(row[30]) + ', ACCTNO = ' + str(row[31]) + ', DE_STATUS = ' + str(row[32]) + ', DECOMMFLAG = ' + str(row[33]) + ', PARENTID = ' + str(row[34]) + ', PARENTREC = ' + str(row[35]) + ', COPYNO = ' + str(row[36])
			patient = Tuples(patientId, task, timestamp, otherAttributes)
			print(patient.patientId, patient.task, patient.timestamp, patient.otherAttributes)
			patientList.append(patient)

		return patientList

	except:
		print ("ERROR: unable to fetch data")
		raise

def filter(objectList): # Outputs the objects filtered by attributes
	try:
		counter = 0
		chosenAttribute = input('Filter by: \n 1 = patientId \n 2 = task \n 3 = timestamp \n 4 = otherAttributes \n')
		chosenValue = input('Type the value: ')

		if chosenAttribute == '1' :
			while counter < len(objectList) :
				if chosenValue == objectList[counter].patientId :
					print('patientId: ' + objectList[counter].patientId + ' task: ' + objectList[counter].task + ' timestamp: ' + objectList[counter].timestamp + ' otherAttribute: ' + objectList[counter].otherAttributes + '\n\n')
				counter += 1

		elif chosenAttribute == '2' :
			while counter < len(objectList) :
				if chosenValue == objectList[counter].task :
					print('patientId: ' + objectList[counter].patientId + ' task: ' + objectList[counter].task + ' timestamp: ' + objectList[counter].timestamp + ' otherAttribute: ' + objectList[counter].otherAttributes + '\n\n')
				counter += 1

		elif chosenAttribute == '3' :
			while counter < len(objectList) :
				if chosenValue == objectList[counter].timestamp :
					print('patientId: ' + objectList[counter].patientId + ' task: ' + objectList[counter].task + ' timestamp: ' + objectList[counter].timestamp + ' otherAttribute: ' + objectList[counter].otherAttributes + '\n\n')
				counter += 1

		elif chosenAttribute == '4' :
			while counter < len(objectList) :
				if chosenValue == objectList[counter].otherAttributes :
					print('patientId: ' + objectList[counter].patientId + ' task: ' + objectList[counter].task + ' timestamp: ' + objectList[counter].timestamp + ' otherAttribute: ' + objectList[counter].otherAttributes + '\n\n')
				counter += 1

		else :
			print('Not a valid number!')
			sys.exit(0)
		
	except:
		print ("ERROR: unable to filter")
		raise

def output2File(objectList): # Writes a files with all objects ranked by timestamp
	counter = 0
	
	try:
		sortedList = []
		sortedList = sorted(objectList, key = lambda object : (object.timestamp, object.patientId))
		file = open('trauma2.txt', 'w')

		while counter < len(sortedList) :
			file.write('patientId: ' + sortedList[counter].patientId + ' task: ' + sortedList[counter].task + ' timestamp: ' + sortedList[counter].timestamp + ' otherAttribute: ' + sortedList[counter].otherAttributes + '\n\n')
			counter += 1
		print('File created successfully.')
		file.close()

	except:
		print ("ERROR")
		raise

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
		objectList = getTuplesFromAcctHist(myCursor)
	elif tableName == 'ADM_INPT':
		objectList = getTuplesFromAdm_inpt(myCursor)
	elif tableName == 'BURNS': 
		objectList = getTuplesFromBurns(myCursor)
	elif tableName == 'comments': 
		objectList = getTuplesFromComments(myCursor) 
	elif tableName == 'CONSULT': 
		objectList = getTuplesFromConsult(myCursor)
	elif tableName == 'CULTURE': 
		objectList = getTuplesFromCulture(myCursor)
	elif tableName == 'dellog': 
		objectList = getTuplesFromDellog(myCursor)
	elif tableName == 'DIAGS': 
		objectList = getTuplesFromDiags(myCursor)
	elif tableName == 'EMERG':
	    objectList = getTuplesFromEmerg(myCursor)
	elif tableName == 'FINANCE': 
		objectList = getTuplesFromFinance(myCursor)
	elif tableName == 'FLDDETAI': 
		objectList = getTuplesFromFlddetai(myCursor)
	elif tableName == 'GENMECH': 
		objectList = getTuplesFromGenmech(myCursor)
	elif tableName == 'HEMO': 
		objectList = getTuplesFromHemo(myCursor)
	elif tableName == 'HOSPREV':
		objectList = getTuplesFromHosprev(myCursor)
	elif tableName == 'ICU':
		objectList = getTuplesFromIcu(myCursor)
	elif tableName == 'INJDETS':
		objectList = getTuplesFromInjdets(myCursor)
	elif tableName == 'INJDIAG':
		objectList = getTuplesFromInjdiag(myCursor)
	elif tableName == 'INJMECH':
		objectList = getTuplesFromInjmech(myCursor)
	elif tableName == 'LAB':
		objectList = getTuplesFromLab(myCursor)
	elif tableName == 'MAINDATA':
		objectList = getTuplesFromMaindata(myCursor)
	elif tableName == 'MORTDETS':
		objectList = getTuplesFromMortdets(myCursor)
	elif tableName == 'MTOS':
		objectList = getTuplesFromMtos(myCursor)
	elif tableName == 'NARRATIV':
		objectList = getTuplesFromNarrativ(myCursor)
	elif tableName == 'OPRM':
		objectList = getTuplesFromOprm(myCursor)
	elif tableName == 'ORGANS':
		objectList = getTuplesFromOrgans(myCursor)
	elif tableName == 'PERHIST':
		objectList = getTuplesFromPerhist(myCursor)
	elif tableName == 'POSTHOSP':
		objectList = getTuplesFromPosthosp(myCursor)
	elif tableName == 'PRECONDS':
		objectList = getTuplesFromPreconds(myCursor)
	elif tableName == 'PROTECT':
		objectList = getTuplesFromProtect(myCursor)
	elif tableName == 'QAISSUE':
		objectList = getTuplesFromQaissue(myCursor)
	elif tableName == 'RADIOLOG':
		objectList = getTuplesFromRadiolog(myCursor)
	elif tableName == 'READMIT':
		objectList = getTuplesFromReadmit(myCursor)
	elif tableName == 'STEP':
		objectList = getTuplesFromStep(myCursor)
	elif tableName == 'SURG':
		objectList = getTuplesFromSurg(myCursor)
	elif tableName == 'sysdefs':
		objectList = getTuplesFromSysdefs(myCursor)
	elif tableName == 'TLogComm':
		objectList = getTuplesFromTLogComm(myCursor)
	elif tableName == 'TOXIANAL':
		objectList = getTuplesFromToxianal(myCursor)
	elif tableName == 'TRA':
		objectList = getTuplesFromTra(myCursor)
	elif tableName == 'tranlog':
		objectList = getTuplesFromTranlog(myCursor)
	elif tableName == 'TRANSFER':
		objectList = getTuplesFromTransfer(myCursor)
	elif tableName == 'TRANSPRT':
		objectList = getTuplesFromTransprt(myCursor)
	elif tableName == 'TREATMEN':
		objectList = getTuplesFromTreatmen(myCursor)
	elif tableName == 'TRICRIT':
		objectList = getTuplesFromTricrit(myCursor)
	elif tableName == 'TRMTEAM':
		objectList = getTuplesFromTrmteam(myCursor)
	elif tableName == 'TTDETLS':
		objectList = getTuplesFromTtdetls(myCursor)
	elif tableName == 'VITALS':
		objectList = getTuplesFromVitals(myCursor)
	elif tableName == 'WARD':
		objectList = getTuplesFromWard(myCursor)
	else: 
		print ('Type a valid table name.\n')
		sys.exit(0)

	myConnection.close()
	myCursor.close()

	function = input('Type 1 to filter by attributes or 2 to sort by timestamp: ')
	if function == '1' :
		filter(objectList)
	elif function == '2' :
		output2File(objectList)
	else :
		print('Not a valid number!')
		sys.exit(0)

if __name__ == '__main__':
	class Tuples:
		def __init__(self, patientId, task, timestamp, otherAttributes):
			self.patientId = patientId
			self.task = task
			self.timestamp = timestamp
			self.otherAttributes = otherAttributes

	main()