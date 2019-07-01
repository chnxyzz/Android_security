
import hashlib,binascii
def toHexString(pin):
	v0 = ''
	for i in range(0,32):
		v2 = hex(ord(pin[i]) & 0xff)
		if len(v2) == 3: 
			v0+='0'
		v0+=v2
	return v0

sa = ['0','1','2','3','4','5','6','7','8','9']
flag = 0
for v0 in range(0,10):
	for v1 in range(0,10):
		for v2 in range(0,10):
			for v3 in range(0,10):
				for v4 in range(0,10):
					for v5 in range(0,10):
						#get pin
						pin = str(sa[v0])+str(sa[v1])+str(sa[v2])+str(sa[v3])+str(sa[v4])+str(sa[v5])
						print("[+] 1 " + pin)
						for j in range(0,0x20):
							for i in range(0,0x200):
								my_md5 = hashlib.md5()
								my_md5.update(pin.encode())
								my_md5_Digest = my_md5.hexdigest()
								pin = my_md5_Digest
								#print("[+] 2 " + pin)
						result = toHexString(pin)
						#print("[+] 3 " + pin)

						matchre = "d04988522ddfed3133cc24fb6924eae9"
						if matchre == result:
							flag = 1
							print('success')
						
						if flag:
							break
					if flag:
						break
				if flag:
					break
			if flag:
				break
		if flag:
			break
	if flag:
		break



