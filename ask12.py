import datetime
from datetime import date
from calendar import monthrange
d = input("Enter a date in HH/MM/EEEE format: ")
da , m, y = map(int, d.split('/'))
dn = datetime.datetime.now()
y1 = int(dn.strftime("%Y"))
m1 = int(dn.strftime("%m"))
d1 = int(dn.strftime("%d"))
dat1 = date( y, m, da)
dat2 = date( y1, m1, d1)
fdat = (dat1 - dat2)
mr = monthrange(y,m)[1]
ndh = 24 - dn.hour - 1
nds= ((60 - dn.minute - 1 ) * 60) + (60 - dn.second)
print ("Aπομένουν ",(int(fdat.days)-1),"μέρες ",ndh,"ώρες και ",nds,"δευτερόλεπτα απο τώρα")
print ("Ο μήνας έχει ",mr,"μέρες")




