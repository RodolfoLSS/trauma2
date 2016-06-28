import pypyodbc
import sys
# Database connection
print('Trying to connect')
try:
    myConnection = pypyodbc.connect('Driver={SQL Server};'
                                    'Server=localhost;'
				    'Database=Trauma2;'
				    'uid=Rodolfo;pwd=Trauma2')
    print('Connected')

except:
    print('Could not connect:', sys.exc_info()[0])
    raise
