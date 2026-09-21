import gmpy2
from Crypto.Util.number import long_to_bytes

# RSA: c = m^e mod N
# if m^e < N, no wraparound happens, so mod does nothing like 10^3 mod 10000 = 1000
# that means c = m^e 
# so: m = e-th root of c  (here, e=3, so m = cube root of c)
#
# gmpy2.iroot(c, e) finds the exact integer root, avoiding float precision loss on huge numbers
# exact=True confirms m^e = c exactly, proving the vulnerability applies here

N = 0
e = 3
c = 0

m, exact = gmpy2.iroot(c, e)

if exact:
    print(long_to_bytes(m))
else:
    print("not a perfect root, this attack doesn't apply here")

# PicoCTF Mini RSA