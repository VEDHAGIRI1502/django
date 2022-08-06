
'''from pymysql import *

con=connect(host='localhost',user='root',password='',database='vedhaa')
cur=con.cursor()
con.autocommit(True)

qry="""insert into red(name,age)values('%s',%d)""" %("sasi",23)
cur.execute(qry)
con.commit()'''

"""from pymysql import*

ghi=connect(host='localhost',user='root',password='',database='vedhagiri')
jkl=ghi.cursor()

ghi.autocommit(True)
qry='''insert into gifting(name,std,sec)values('%s','%s','%s')'''%('space05','four',7)
jkl.execute(qry)
ghi.commit()"""

#update

"""jkl=ghi.cursor()


qry='''update gifting set name='space05',sec=6 where std='four' '''
jkl.execute(qry)
ghi.commit()"""

#delete

"""qry='''DELETE FROM gifting WHERE name='space02' '''
jkl.execute(qry)
ghi.commit()
print(jkl.rowcount,'records deleted')"""

from pymysql import*

ident=connect(host='localhost',user='root',password='',database='tbl')
svk=ident.cursor()

'''ident.autocommit(True)
qry="""insert into retrica(sino,name,address)values('%d','%s','%s')"""%(5,'hashi','nkl')
svk.execute(qry)
ident.commit()
print(svk.rowcount,'records added')'''

"""qry='''delete from retrica WHERE sino=5 '''
svk.execute(qry)
ident.commit()"""

svk=ident.cursor()

qry="""update retrica set name='kisame',address='mist' WHERE sino=1"""
svk.execute(qry)
ident.commit()
print(svk.rowcount,'record updated')

