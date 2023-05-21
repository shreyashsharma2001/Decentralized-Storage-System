# Module Imports
import mariadb
from cryptography.fernet import Fernet

import sys

key = Fernet.generate_key()
print(key)
print(type(key))


# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="yash",
        password="yash123",
        host="127.0.0.1",
        port=3306,
        database="Guardian1"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
cur.execute("select ClientKey from Authentication where Username='yash' and Password='yash123';")                                                  
output = cur.fetchone()

if(output=="4i1T75tFPXXG-acx2ZX3vRWt-vvCQETPzNyDxexicLE="):
	print("yes")
else:
	print("no")
print(output[0])