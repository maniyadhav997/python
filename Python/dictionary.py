a={
    "name":"mani",
    "no":"93203",
    "list":[1,3.4,],
}
print(a)
print(a.items())
print(a.keys())
a.update({
    "fruit":"appele",
    "scope":"37yy4923"
    })
print(a)
for i,j in a.items():
  print(i,":",j)
  for i in a.keys():
      print(i)
print(a.get("name"))
print(a.get("no"))
         