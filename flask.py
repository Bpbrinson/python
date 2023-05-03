import pymysql

conn = pymysql.connect(
    host='finance.c2kupgap5up8.us-east-1.rds.amazonaws.com',
    user='Brandon',
    password='PfjRn7jk7598',
    db='finance',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with conn.cursor() as cursor:
    # Execute the SQL query
    cursor.execute('SELECT date FROM financial_data')

    # Fetch all rows of the query result
    rows = cursor.fetchall()

