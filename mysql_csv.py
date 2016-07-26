#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import csv

try:
	con = mdb.connect('localhost', 'teste', 'teste123', 'pythondb')

	arqCSV = csv.writer(open("tblPessoas.csv", "wb"))

	arqCSV.writerow(["id","nome"])

#    cur = con.cursor()
#    cur.execute("SELECT VERSION()")

#    ver = cur.fetchone()
    
#    print "Database version : %s " % ver

	with con:
    
	    #cur = con.cursor()
	    cur = con.cursor(mdb.cursors.DictCursor)

	    #cur.execute("DROP TABLE IF EXISTS Pessoas")
	    #cur.execute("CREATE TABLE Pessoas(id INT PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(25))")
	    #cur.execute("INSERT INTO Pessoas(nome) VALUES('Juquinha da Silva')")
	    #cur.execute("INSERT INTO Pessoas(nome) VALUES('Pedro Luiz')")
	    #cur.execute("INSERT INTO Pessoas(nome) VALUES('Emilio Espiga')")
	    #cur.execute("INSERT INTO Pessoas(nome) VALUES('Pedro Pedroca')")
	    #cur.execute("INSERT INTO Pessoas(nome) VALUES('Pequeno Polegar')")
	    
	    cur.execute("SELECT * FROM Pessoas")

	    #rows = cur.fetchall()

	    #for row in rows:
            #	print row
	   
            #for i in range(cur.rowcount):
    
	    #	row = cur.fetchone()
	    #	print row[0], row[1]
	    
	    rows = cur.fetchall()

	    for row in rows:
		arqCSV.writerow([row["id"],row["nome"]])
		#print row["id"], row["nome"]
    
except mdb.Error, e:
  
    print "Error %d: %s" % (e.args[0],e.args[1])
    sys.exit(1)
    
finally:    
        
    if con:    
        con.close()


