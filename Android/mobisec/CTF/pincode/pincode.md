# pincode

* part 1
checkPin 需要看smali代码

apktool d -f xx.apk -o xx

有没有办法去爆破 

jeb2 没有编译成功，人工翻译 smali代码（208行）

pin 的长度为 6

checkPin(pin){
	if !len(pin) == 6:
		return 0
	v0 = getBytes(pin)
	for v2 in range(0,0x0019):
		for v3 in range(0,0x190):
			MessageDigest v4 = MessageDigest.getInstance(md5)
			md.update(getBytes(pin))
			byte v5[] = md.digest();
			v6 = v5.clone(); 
			v6 = byte[](v6)
	v2 = PinChecker.toHexString(v0)
	v3 = "d04988522ddfed3133cc24fb6924eae9"
	v3 = v2.equals(v3)
	if v3 != 0:
		return 1
	else:
		return 0
}

整个题目的解题思路如下
1.逆smali代码，得到pin
2.从“https://challs.reyammer.io/pincode/pin”中得到flag
