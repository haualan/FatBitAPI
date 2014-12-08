from tinydb import TinyDB, where    

db = TinyDB('db.json')

for i in db.all():
  print i

if db.search(where('UID') == 'myUID'):
  print "something there"


# db.purge()

db.close()

db = TinyDB('score.json')

r = []
for i in db.all():
  print i
  r.append([i['UID'],i['score']])

db.close()


r = sorted(r, key = lambda x: x[1], reverse = True)

print r