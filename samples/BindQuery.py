#------------------------------------------------------------------------------
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# BindQuery.py
#
# Demonstrate how to perform a simple query limiting the rows retrieved using
# a bind variable. Since the query that is executed is identical, no additional
# parsing is required, thereby reducing overhead and increasing performance. It
# also permits data to be bound without having to be concerned about escaping
# special characters or SQL injection attacks.
#------------------------------------------------------------------------------

import cx_Oracle
import sample_env

connection = cx_Oracle.connect(sample_env.get_main_connect_string())

cursor = connection.cursor()
sql = 'select * from SampleQueryTab where id = :bvid'

print("Query results with id = 4")
for row in cursor.execute(sql, bvid = 4):
    print(row)
print()

print("Query results with id = 1")
for row in cursor.execute(sql, bvid = 1):
    print(row)
print()

