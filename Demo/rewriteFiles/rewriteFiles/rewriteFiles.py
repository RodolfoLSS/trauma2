def main(): 

	try:
		oldFile07 = open('tranlog_07.txt', 'r')
		newFile07 = open('newTranlog_07.txt', 'w')
		"""oldFile08 = open('tranlog_08.txt', 'r')
		newFile08 = open('newTranlog_08.txt', 'w')
		oldFile09 = open('tranlog_09.txt', 'r')
		newFile09 = open('newTranlog_09.txt', 'w')
		oldFile10 = open('tranlog_10.txt', 'r')
		newFile10 = open('newTranlog_10.txt', 'w')
		oldFile11 = open('tranlog_11.txt', 'r')
		newFile11 = open('newTranlog_11.txt', 'w')"""

	except:
		print("Unable to open files.")
		raise

	try:
		file07 = oldFile07.read()
		tuples07 = file07.split('\n\n')
		writeFile(tuples07, newFile07)
		tuples07.clear()
		file07 = []
		oldFile07.close()
		newFile07.close()
		"""
		file08 = oldFile08.read()
		tuples08 = file08.split('\n\n')
		writeFile(tuples08, newFile08)
		tuples08.clear()
		file08 = []
		oldFile08.close()
		newFile08.close()

		file09 = oldFile09.read()
		tuples09 = file09.split('\n\n')
		writeFile(tuples09, newFile09)
		tuples09.clear()
		file09 = []
		oldFile09.close()
		newFile09.close()

		file10 = oldFile10.read()
		tuples10 = file10.split('\n\n')
		writeFile(tuples10, newFile10)
		tuples10.clear()
		file10 = []
		oldFile10.close()
		newFile10.close()

		file11 = oldFile11.read()
		tuples11 = file11.split('\n\n')
		writeFile(tuples11, newFile11)
		tuples11.clear()
		file11 = []
		oldFile11.close()
		newFile11.close()"""

	except:
		print("Error reading files")
		raise

def writeFile(tuples, file):
	import pypyodbc
	import sys

	# Database connection
	print('Trying to connect to the database...')

	try:
		myConnection = pypyodbc.connect('Driver={SQL Server};'
									'Server=localhost;'
									'Database=Trauma2;'
									'uid=Rodolfo;pwd=trauma2')
		myCursor = myConnection.cursor()
		print('Connected.')
	except:
		print('Could not connect:', sys.exc_info()[0])

	try:
		lineNumber = 1
		counter = 0
		currentTime = 0
		currentDate = 0
		currentComplement = 0
		oldTime = 0 
		oldDate = 0
		oldComplement = 0
		dicAcctNo = {}
		dicTableName = {}

		while counter < (len(tuples)-1) :
			lines = tuples[counter]
			print(lines)

			cutFieldName = lines.split('fieldname = ') # trimming fieldname out the whole line of attributes
			tempFieldName = cutFieldName[1].split('fieldtype')
			fieldName = tempFieldName[0].replace(', ','').replace(' ','_').lower()

			cutFieldValue = lines.split('fieldval = ') # trimming fieldvalue out the whole line of attributes
			tempFieldValue = cutFieldValue[1].split('fieldstat')
			fieldValue = tempFieldValue[0].replace(', ','').replace(' ','_').lower()

			cutAcc_Path = lines.split('acc_path = ') # trimming acc_path out the whole line of attributes
			tempAcc_Path = cutAcc_Path[1].split('copyid')
			acc_path = tempAcc_Path[0].replace(', ','').replace(' ','_').lower()
			print('\n acc_path = ' + acc_path+'\n')
			
			if fieldName != 'none':

				try:
					print('##')
					SQLSelectCommand = ("SELECT DISTINCT c.name AS ColName, t.name AS TableName \
										FROM sys.columns c \
										JOIN sys.tables t ON c.object_id = t .object_id\
										WHERE  c.name LIKE '%s'" % (fieldName))
					myCursor.execute(SQLSelectCommand)

					if acc_path in dicTableName:
						tableName = dicTableName[acc_path]
					else:
						tableName = myCursor.fetchone()
						dicTableName[acc_path] = tableName[1]

					print('\n tableName = ' + dicTableName[acc_path]+'\n')
				except:
					print ("ERROR: unable to fetch data")
					raise

			else:
				tableName = 'none'

			attributes = lines.split(' ')
			acctNo = attributes[10].replace(',','')

			time = attributes[7].replace(',','')

			if(attributes[6] == '00:00:00'): # adjusting timestamps
				h = time[0] + time[1]
				m = time[2] + time[3]
				s = time[4] + time[5]
				timestamp = attributes[5] + ' ' + h + ':' + m + ':' + s
			else:
				timestamp = attributes[5] + ' ' + attributes[6] 

			currentTime = attributes[6]
			currentDate = attributes[5]
			currentComplement = time

			if currentTime == oldTime and currentDate == oldDate and currentComplement == oldComplement:
				counter += 1 # merging repeated lines by skiping them and writing the complement on the past line
				file.write('  ' + fieldName + '=' + fieldValue)
			else:
				# conditions for the file writing
				if acctNo in dicAcctNo:
					dicAcctNo[acctNo] += 1
				else:
					dicAcctNo[acctNo] = 1
				lineNumberForEachAcctNo = dicAcctNo[acctNo]

				if counter != 0:
					file.write('\n\n')

				file.write(str(lineNumber) + ' ' + str(acctNo) + ' ' + str(lineNumberForEachAcctNo) + ' ' + str(tableName) + ' ' + str(timestamp) + ' # ' + fieldName + '=' + fieldValue)
				oldTime = currentTime
				oldDate = currentDate
				oldComplement = currentComplement
				lineNumber += 1 
				counter += 1

	except:
		print('Error writting the files.')
		raise

if __name__ == '__main__':

	main()