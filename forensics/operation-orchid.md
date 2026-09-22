## Operation Orchid

I was given a .img.gz disk image.

I gunzipped it, then ran mmls to see the partitions. One was labeled "Linux Swap / Solaris x86" lowkey just meant that partition type ID is shared by both, so mmls just can't tell. I checked with fls on each offset, and the one that errored out with "cannot determine file system type" was swap.

The root partition had the real files. I tried mounting it normally but /root was permission denied even on a read-only mount. I used fls/icat instead since they read the disk directly and don't care about permissions.

/root had 3 files: .ash_history, a deleted flag.txt, and flag.txt.enc. The deleted one was shredded so it's just garbage now. The history file had the whole thing though, someone made the flag, encrypted it with openssl aes256 -k password, then shredded the original. The password was just sitting there in plaintext.

I pulled the .enc file with icat, then decrypted it. It took a few tries to get the openssl flags right (-d goes after the cipher name, -out needs a filename or it eats the next arg). I got a "bad decrypt" warning at the end but the flag printed fine anyway, seems to just be a padding check complaining, not an actual failure.

The password was left in shell history the whole time so you should like check that first.

# the command openssl aes256 -d -in flag.txt.enc -out decryptedflag.txt -k gofindthepasswordyourselfbuddy
