
flag = "Lcq]>N?s]bV[R[_OaScQ]]NGPYDKDNG]"

for i in range(len(flag)):
	char = chr(ord(flag[i]) + i + 1)
	print(char, end="")
print()

# MetaCTF{flag_in_reverse_is_galf}
