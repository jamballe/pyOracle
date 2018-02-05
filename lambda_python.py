import sys
import logging
import cx_Oracle

logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = cx_Oracle.connect('foobar/foobar123@saastest.cf0bahyobu7w.us-west-2.rds.amazonaws.com:1521/ORCL')

except:
    logger.error("ERROR: Unexpected error: Could not connect to Oracle instance.")
    sys.exit()

logger.info("SUCCESS: Connection to RDS Oracle instance succeeded")
print(conn.version)

def lambda_handler(event, context):
    """
    This function fetches content from Oracle RDS instance
    """

    item_count = 0

    with conn.cursor() as cur:
        cur.execute("create table Employee3 ( EmpID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))")
        cur.execute('insert into Employee3 (EmpID, Name) values(1, "Joe")')
        cur.execute('insert into Employee3 (EmpID, Name) values(2, "Bob")')
        cur.execute('insert into Employee3 (EmpID, Name) values(3, "Mary")')
        conn.commit()
        cur.execute("select * from Employee3")
        for row in cur:
            item_count += 1
            logger.info(row)
            #print(row)


    return "Added %d items from RDS Oracle table" %(item_count)
