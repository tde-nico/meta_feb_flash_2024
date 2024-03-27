from pwn import *

r = remote('host5.metaproblems.com', 7050)

g = 3
r.recvuntil(b'p = ')
p = int(r.recvline().strip())
r.recvuntil(b'secret = ')
secret = int(r.recvline().strip())

my_secret = (p - 1) + secret

r.sendlineafter(b'secret: ', str(my_secret).encode())
r.interactive()

# MetaCTF{well_d0n3_you_br0k3_sha256?!}
