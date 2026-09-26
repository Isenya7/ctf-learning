# Verify

September 25, 2026

I am doing Verify on picoCTF

People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate.

```
ssh -p 37322 ctf-player@chatelaine.cylabacademy.net
```

Using the password `13792798`. Accept the fingerprint with yes, and `ls` once connected to begin. Remember, in a shell, passwords are hidden!

> Checksum: `bf7701262e3fce45531b13d9866fb0913847a669823064aec1f60be7c2591ba8`
>
> To decrypt the file once you've verified the hash, run `./decrypt.sh files/<file>`.

## Hints

1. Checksums let you tell if a file is complete and from the original distributor. If the hash doesn't match, it's a different file.
2. You can create a SHA checksum of a file with `sha256sum <file>` or all files in a directory with `sha256sum <directory>/*`.
3. Remember you can pipe the output of one command to another with `|`. Try practicing with the 'First Grep' challenge if you're stuck!

## Solve

```
ctf-player@academy-chall$ ls -la
total 20
drwxr-xr-x 3 ctf-player ctf-player   57 Sep 23 05:27 .
drwxr-xr-x 1 ctf-player ctf-player   51 Sep 25 17:02 ..
-rw-r--r-- 1 root       root         65 Sep 23 05:27 checksum.txt
-rwxr-xr-x 1 root       root        856 Sep 23 05:27 decrypt.sh
drwxr-xr-x 2 ctf-player ctf-player 8192 Sep 23 05:27 files
```

I see there is checksum.txt

```
bf7701262e3fce45531b13d9866fb0913847a669823064aec1f60be7c2591ba8
```

```
ctf-player@academy-chall$ cat decrypt.sh

        #!/bin/bash

        # Check if the user provided a file name as an argument
        if [ $# -eq 0 ]; then
            echo "Expected usage: decrypt.sh <filename>"
            exit 1
        fi

        # Store the provided filename in a variable
        file_name="$1"

        # Check if the provided argument is a file and not a folder
        if [ ! -f "/home/ctf-player/drop-in/$file_name" ]; then
            echo "Error: '$file_name' is not a valid file. Look inside the 'files' folder with 'ls -R'!"
            exit 1
        fi

        # If there's an error reading the file, print an error message
        if ! openssl enc -d -aes-256-cbc -pbkdf2 -iter 100000 -salt -in "/home/ctf-player/drop-in/$file_name" -k academy; then
            echo "Error: Failed to decrypt '$file_name'. This flag is fake! Keep looking!"
        fi
        ctf-player@academy-chall$
```

```
ctf-player@academy-chall$ ls
060ffMbj  5SXUHB2c  EARBrLdS  KSj2pigL	RVdMeXW4  a2NI5R5A  gMHhRgV5  lyZrXer6	t6GLzYnX
0D1KJd6i  5gOsZApH  ECPeQZTn  KUiH8DdI	RZsUIbAt  aFYv1ERJ  ghzlVvLK  mHcA15MX	t8SN7kjU
0hwYJwMB  5mEgCdB2  Ey94l7MC  KckoJ52A	Rg07ouRn  aNiT4nE0  gli67npg  mMlNHF0l	ta83FVpr
0kf7pr6A  5tnt67q5  FI5lI7qZ  KiNS9Ug1	RytZ7wIN  aXtps30R  gq3v0qxF  mT8pWKOm	tfeBMSx1
11yfN562  64GTpJI4  FfWO1gw2  KrzLldsV	SBYMTnkz  agTRfder  hFX8d6pW  mZuJSNVB	uE8kRn1f
17NCzzP6  65DfQ7Se  FhYeTYmj  L211sh6M	SPZMaXGa  b37jzqDk  hQA2s1yQ  nZnRR7jL	uEvO8eN7
1DBOZaMq  7IeWFniN  G55NST1b  LFMFj2bW	SwSfuZwo  b6225255  hRpwnr91  no5KYE82	uILDzijI
1NzFJFKE  7KAQ6NGm  GNdf8QKr  LJW5eWbO	TO77GxLg  bQ8141tj  hbRcu66N  nx1RpaCg	uVLljMa0
1RO1Sgh4  7RZvuUz8  GT98VNgj  LP4pDJwJ	TSYTDrv7  bfhiyRUo  hcyS8Oni  o3uYVWWa	undm91eH
1WnScxJh  7j9IotSL  GaIb6dgi  Lveggx0G	TXMXvWqK  bkjNiu3h  hftIBykZ  o4dbax1u	uq9gy3M6
1eEZZ2eq  835ZOG0A  Gd9Ov6jI  Lw5ErRhO	Tos83DOx  bmR4vDqU  hgGA0841  o88Y8sP4	uwVBhEUY
1okl0HMi  8Er90u2n  GmU7rOwq  M3XLHHZq	UvB9prJv  bngVrc6q  hwGmCpnC  oC8NA4tI	v4aOmWPt
1t60znz2  8TlgrB3I  Goww2qUs  MXmSHikv	VFRDdyoY  btK7Z8rs  hxUXbWED  oHRIa07n	vkNrYzts
2UJlPeud  8TzQFl66  GxnkAImG  Me8YQxXc	VMUAV7ml  cIJOVGFx  iHjn7fzR  oPICRsyX	vkiEy6cT
2WHOIRlt  8Ve9bZ7t  Gy4nQlC1  Mn44m2Al	VMjGka0d  cZ8JZ4Rf  iIGWy0Go  ojc7mh7f	wGiZzjam
2xyuM01Z  8nJPtqYL  HNJfaPrA  N1mINrca	VUp5KmlF  cj31a6S7  inbdiuVS  ov7mGzVC	wTx2RiDQ
2y4KwtrQ  8v9ctK5y  HXjCD116  NEEeBBUS	VWtPbU5j  cxNsmnYC  j02x7MZM  pAmFiI2p	wZUIOmat
3BHHcilS  93opDnw6  HgxFGJdF  NSXr7tL9	Vlx6m8lR  ebPzGtz1  jIxZK3h3  pCHxf0GW	wcH9yCXT
3CAC99Li  98wxucLq  Hkj24bnK  Nnus5Sd9	Vn2eRiRP  ecGUaApd  jPwrcoNu  pLYTwa9D	whYFzF7y
3GorFWVA  9XR5cYDn  I0rgUjiO  No459Qfz	W12FXirO  elOyFqIJ  jqaIDxNE  peTCFvdw	xVwq0tBf
3a7OXCbU  9qcKds16  I3s4FN8t  NyTwAkZw	W3CMRX9E  ew3Ggerq  jyJ3MQbB  q5HFGcrQ	xvGdf3XK
3kVkl5yR  9sGrtewh  IFhgNMiw  OLyzYiWe	WbAecWve  f3oA9DaL  k0kEsOiL  qHxOMP6Q	y6pvi0sT
3qU3pHys  AY1ETZz8  IKifu1w1  OQVLHczE	WtmtQ4re  fL81ISX6  k6vAKJ78  qMyp7W9Q	yQtB1dMY
3xM9vnXW  AhDJmECO  IaEPThAF  Oppc8MrQ	WyMRAUX6  fNCbGCv6  kHxHNuL3  qjvvmz8g	yfyUNMFU
42Iusbhn  AiOIq9xD  Im4l0XCr  OwLyvU0w	X3xJty7i  fZPUxigz  kKVyWDPN  ql0KGYFx	ypy8FThM
4B42vwLS  B1uEUQ4a  Iwh3DvKR  PPfs34D2	Xd33b2lB  fZf5Nb8u  kTiMHpCN  qpIIyOdh	yxjc7syn
4FBXWirC  B5OaH06Q  J0KNVw81  PTRdimuH	XeGPZEY7  fazv7kQn  lEW2w5jq  r5P8pUuf	zIIF1F6N
4Rx3gDAZ  B6E8V1pc  J3fdxtX9  PTdPUCoO	YEgshWVz  fgoG8JP2  lHtCjgPa  rCLg0FRY	zZefSr1P
4c3wWeqC  Bh4CMcd0  J5NTxBBn  Pf9Upbte	YPuzKzZa  ftO1bzBE  lIvisjNV  rTJTlZxb	zvwovaPn
4nEPLPj2  CX868LC6  JNCRiv1E  PudYMvvW	YtdY68DsE  g0JrocPW  lOov55v6  rYTS2nL9
4nq3Rf2J  CaFZd0l9  JNLhbLAH  Q5kAoGMR	Z3wPIYIy  g3hIfim9  lcBtLlGe  rZHGY8yN
4pcKz1ph  CbA1J13J  JTWJ5DXz  QN84gEtv	Z4cWrSTS  gDfZBHfT  ll8jr2Us  rmQDH7HM
4r1dU75m  CkrOv8Wh  JkdWSdYM  RGUSdvYW	ZANp8ifx  gFhBWdej  lmuLsFuX  rtKXP3rZ
5NLdsJx4  CxrMd0T3  KSeDsAyf  ROuTRVsH	Zbjm8waV  gLz6UIRt  loBobTSi  s0JjGwDT
ctf-player@academy-chall$
```

Jeez that is so much files

Well time to sha256 all of them eh?
Let me hash everything like the hints said and push it into a text file:

```
ctf-player@challenge:~/drop-in/files$ sha256sum ~/drop-in/files/* > output.txt

ctf-player@challenge:~/drop-in/files$ cat output.txt | grep bf7701262e3fce45531b13d9866fb0913847a669823064aec1f60be7c2591ba8
bf7701262e3fce45531b13d9866fb0913847a669823064aec1f60be7c2591ba8  /home/ctf-player/drop-in/files/b6225255
ctf-player@challenge:~/drop-in/files$
```

whoohoo we got the file

```
ctf-player@challenge:~/drop-in/files$ cat b6225255
Salted__�4�22�J�ø����I`��$�%�p�КHZE�aO�3���$���M܊�|��ߞu�ctf-player@challenge:~/drop-in/files$
```

right... we have to decrypt it

```
ctf-player@challenge:~/drop-in$ ls
checksum.txt  decrypt.sh  files
ctf-player@challenge:~/drop-in$
```

`./decrypt.sh files/<file>` is what we have to do

```
./decrypt.sh files/home/ctf-player/drop-in/files/b6225255

ctf-player@challenge:~/drop-in/files$ ./decrypt.sh ~/drop-in/files/b6225255
bash: ./decrypt.sh: No such file or directory
ctf-player@challenge:~/drop-in/files$ cd ..
ctf-player@challenge:~/drop-in$ ./decrypt.sh ~/drop-in/files/b6225255
Error: '/home/ctf-player/drop-in/files/b6225255' is not a valid file. Look inside the 'files' folder with 'ls -R'!
ctf-player@challenge:~/drop-in$ ./decrypt.sh /drop-in/files/b6225255
Error: '/drop-in/files/b6225255' is not a valid file. Look inside the 'files' folder with 'ls -R'!
ctf-player@challenge:~/drop-in$ ./decrypt.sh files/b6225255
academy{trust_but_verify_b6225255}
```

I got it... ngl, I used the big gpt for that last one because my brain couldn't work for some reason

## What I learned today

- You can literally just sha256 a whole directory
- Nothing else except that my terminal needs some colouring because its all black and white and hard to navigate
