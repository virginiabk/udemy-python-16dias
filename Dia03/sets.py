tex="[]){}"
dias = {'Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sàbado'}
print(type(dias))
print(dias)

print(len(dias))
otro_set =  {1, 2, 3}
print(2 in otro_set)

s1 =  {1, 2, 3}
s2 =  {4, 5, 6, 2}
s3 =  s1.union(s2)
print(s3)

s1.add(4)
s3 =  s1.union(s2)
print(s3)

print(s1)
s1.remove(2)
s3 =  s1.union(s2)
print(s3)

s3.pop()
print(s3)

s3.clear()
print(s3)