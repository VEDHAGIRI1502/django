'''from pymysql import *

identifier=connect(host='localhost',user='root',password='',database='vedhaa')
funny=identifier.cursor()
'''
'''identifier.autocommit(True)
qry="""insert into list(sino,name,address,age)values(%d,'%s','%s','%s')""" %(3,'kisame','konoha',33)
funny.execute(qry)
identifier.commit()
print(funny.rowcount,'record inserted')'''


'''qry=""" update list set sino=2 WHERE name='kakashi' """
funny.execute(qry)
identifier.commit()'''


'''qry="""delete from list where sino=3"""
funny.execute(qry)
identifier.commit()'''


from pymysql import*

class ninja():
    icu=connect(host='localhost',user='root',password='',database='vedhagiri')
    sdf=icu.cursor()
    icu.autocommit(True)
    

    def first(self):
        
        
        qry="""insert into students(sino,name,standard,sec)values('%s','%s','%s','%s')"""% ('1','naruto','1st','a')
        self.sdf.execute(qry)
        self.icu.commit()
        print(self.sdf.rowcount,'record inserted')
    def second(self):
        
            
        qry="""insert into students(sino,name,standard,sec)values('%s','%s','%s','%s')"""% (2,'sasuke','1st','a')
        self.sdf.execute(qry)
        self.icu.commit()
        print(self.sdf.rowcount,'record inserted')

    def third(self):
        
        
        qry="""insert into students(sino,name,standard,sec)values('%s','%s','%s','%s')"""% (3,'sakura','1st','a')
        self.sdf.execute(qry)
        self.icu.commit()
        print(self.sdf.rowcount,'record inserted')
    def fourth(self):
         
        
        qry="""insert into students(sino,name,standard,sec)values('%s','%s','%s','%s')"""% (4,'rock lee','1st','b')
        self.sdf.execute(qry)
        self.icu.commit()
        print(self.sdf.rowcount,'record inserted')
    def fifth(self):

        qry="""delete from students where sino=4"""
        self.sdf.execute(qry)
        self.icu.commit()
        print(self.sdf.rowcount,'deleted')
    def sixth(self):

        qry='''update students set name='hinata', standard='1st' WHERE sino=3 '''
        self.sdf.execute(qry)
        self.icu.commit()
        print(self.sdf.rowcount,'updated')


shinobi=ninja()
shinobi.sixth()
