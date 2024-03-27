import pwn
import pyshark

cap = pyshark.FileCapture('plates.pcapng', display_filter="not arp")


n1, n2, key = 0, 0, 0

for i, pkt in enumerate(cap):
	data = bytes.fromhex(pkt.data.data)

	if i == 0:
		n1 = data[3:]
	elif i == 1:
		n2 = data[3:]
		key = pwn.xor(n1, n2)
	else:
		for i in range(0, len(data[3:]), 16):
			plate_index = i + 4
			plate = pwn.xor(data[3+plate_index:3+plate_index+16], key)
			print(plate)


# MetaCTF{dr1ver_t3st}
