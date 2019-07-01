import hashlib
import pdb
v0 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
src = 'activity'

m2 = hashlib.md5()
m2.update(src)
src_md5 = m2.digest()


v1 = len(src_md5)
v2 = [None]*v1*2
v4 = 0
print(src_md5)
for i in range(0,len(src_md5)):
	v5 = ord(src_md5[i])
	v6 = v4 + 1
	print("[+] ",v5 >> 4 & 15)
	v2[v4] = v0[v5 >> 4 & 15]
	v4 = v6 +1
	print("[+1] ",v5&15)
	v2[v6]=v0[v5&15]

print(v2)