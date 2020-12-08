#------------------------------------------------------------------------------
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# BindInsert.py
#
# Demonstrate how to insert a row into a table using bind variables.
#------------------------------------------------------------------------------

import cx_Oracle
import sample_env

connection = cx_Oracle.connect(sample_env.get_main_connect_string())

rows = [ (1, "First" ),
         (2, "Second" ),
         (3, "Third" ),
         (4, "Fourth" ),
         (5, "Fifth" ),
         (6, "Sixth" ),
         (7, "Seventh" ) ]

cursor = connection.cursor()
cursor.executemany("insert into mytab(id, data) values (:1, :2)", rows)

# Don't commit - this lets us run the demo multiple times
#connection.commit()

# Now query the results back

for row in cursor.execute('select * from mytab'):
    print(row)

