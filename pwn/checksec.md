# Checksec

shows what protections are active, first thing you check

## Relro
locks the GOT (table of addresses for outside functions like printf)
* partial = some locked, rest still writable
* full = whole thing locked after startup, cant touch it
* ex: unlocked GOT means attacker overwrites printf's entry, program calls printf later and runs attacker's code instead

## Canary
a random value sitting right before the return address
* activates if theres overflow, shutting down the program before anything bad can happen
* checked right before function returns, if its different the overflow got caught in time like a tripwire

## NX
stack can be read/written but not run as code
* without NX, attacker overflows a buffer, writes their own malicious instructions into the stack, then redirects execution to jump there and run it
* with NX, that same stack memory is marked non executable, so the cpu refuses to run whatever code got written there, even if execution gets redirected to it
* this pushes attackers toward ROP instead, chaining together small pieces of code that already legitimately exist in the program, since that stays executable, rather than injecting anything new

## PIE
whole binary loads at a random address each run, house teleports to a random street every day
* rooms inside (functions) stay the same distance apart tho, thats why offset math still works
* need a leak first, like main's address, before calculating anything else, so you can calculate everything else (it's like a moving house, but even if the house moves, the rooms within it don't)
* addresses get written in reverse byte order, little endian, when building a payload, so account for that