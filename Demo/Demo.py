import pypyodbc
# Database connection
print('Trying to connect')
try:
	myConnection = pypyodbc.connect('Driver={SQL Server};'
								    'Server=localhost;'
								    'Database=Trauma2;'
                                    'uid=sa;pwd=P@ssw0rd')
	print('Connceted')

except:
	print('Could not connect')


"""
def main():
	tableName = raw_input('Table name: ')
	createClass(tableName)

	
def createClass(tableName):
	# Creating classes
	class 'tableName':
				def __init__(self, patientId, task, timestamp, otherAttributes):
					self.patientId = patientId
					self.task = task
					self.timestamp = timestamp
					otherAttributes = otherAttributes

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

def output2File():


if __name__ == '__main__':
	main()
"""