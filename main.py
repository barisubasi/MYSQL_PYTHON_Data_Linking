import mysql.connector
import names
import random
from datetime import date,datetime,timedelta
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             password="1234",
                             )
ms=mydb.cursor()
ms.execute("DROP DATABASE instagram")
ms.execute("CREATE DATABASE instagram")
ms.execute("USE instagram")
ms.execute("CREATE TABLE insta (id int NOT NULL, isim VARCHAR(255), soyisim VARCHAR(255),dogumgunu DATE,PRIMARY KEY (id))")
kullanici_sayisi=200
def dates():
    year=random.randint(1970,2006)
    month=random.randint(1,12)

    if month==2:
        day=random.randint(1,28)
    elif month==4 or month==6 or month==9 or month==11:
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 31)

    return date(year,month,day)


ms.execute("CREATE TABLE takip (takip_edilen_id INT PRIMARY KEY,FOREIGN KEY(takip_edilen_id) REFERENCES insta(id) ON UPDATE CASCADE ON DELETE CASCADE,takip_eden1_id INT NOT NULL, takip_eden2_id INT NOT NULL, takip_eden3_id INT NOT NULL)")

for i in range(kullanici_sayisi):
    tuple1 = (i, names.get_first_name(), names.get_last_name(), dates())
    sql = "INSERT INTO insta VALUES (%s,%s,%s,%s)"
    ms.execute(sql, tuple1)

    cm1 = "INSERT INTO takip VALUES (%s,%s,%s,%s)"
    ms.execute(cm1,(i,random.randint(0,kullanici_sayisi),random.randint(0,kullanici_sayisi),random.randint(0,kullanici_sayisi)))

# ms.execute("select *from instagram.insta")
# myresult=ms.fetchall()
# for i in myresult:
#     print(i)


ms.execute("CREATE TABLE eski_kullanici(kullanici_id int NOT NULL, kullanici_isim VARCHAR(30), kullanici_soyisim VARCHAR(30), kullanici_dogumgunu DATE)")
ms.execute("CREATE TRIGGER eski_kullanici BEFORE DELETE ON insta FOR EACH ROW BEGIN INSERT INTO eski_kullanici SET kullanici_id = OLD.id,kullanici_isim = OLD.isim,kullanici_soyisim = OLD.soyisim,kullanici_dogumgunu = OLD.dogumgunu;END")

ms.execute("DELETE FROM insta WHERE id=1")
ms.execute("DELETE FROM insta WHERE id=3")
ms.execute("DELETE FROM insta WHERE id=7")
ms.execute("select * from insta")
myresult=ms.fetchall()
for i in myresult:
    print(i)

print("\n\n")
ms.execute("select * from instagram.takip")
myresult=ms.fetchall()
for i in myresult:
    print(i)

print("\n\n")
ms.execute("select * from instagram.eski_kullanici")
myresult = ms.fetchall()
for i in myresult:
    print(i)

# print("kullanıcılar:")
# ms.execute("select * from insta")
# myresult=ms.fetchall()
# for i in myresult:
#     print(i)
#
#
# print("\n\ntakip:")
# ms.execute("select * from instagram.takip")
# myresult=ms.fetchall()
# for i in myresult:
#     print(i)
#



# ms.execute("CREATE PROCEDURE kullanici_takipci() SELECT takip.takip_edilen_id,insta.id,insta.isim,insta.soyisim FROM takip,insta WHERE takip.takip_eden1_id=insta.id OR takip.takip_eden2_id=insta.id OR takip.takip_eden3_id=insta.id")
#
# ms.execute("CALL kullanici_takipci();")
# myresult = ms.fetchall()
# for x in myresult:
#  print(x)

#
# ms.execute("CREATE PROCEDURE kullanici_takip_edilmeyen() SELECT takip.takip_edilen_id,insta.id,insta.isim,insta.soyisim FROM takip,insta WHERE takip.takip_eden1_id!=insta.id OR takip.takip_eden2_id!=insta.id OR takip.takip_eden3_id!=insta.id")
# ms.execute("CALL kullanici_takip_edilmeyen();")
# myresult = ms.fetchall()
# for x in myresult:
#  print(x)


# print("\n\nSilinenler")
#
# ms.execute("select *from eski_kullanicilar")
# myresult = ms.fetchall()
# for x in myresult:
#  print(x)
