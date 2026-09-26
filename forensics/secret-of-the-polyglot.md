# Secret of the Polyglot

September 25, 2026

This is my second ctf today.

I open the alleged pdf file and see `1n_pn9_&_pdf_96385309}`
Seems like one part of the flag

```
tesseract flag2of2-final.pdf -
acadermy{f1u3n7_
```

oh... is that it?

```
acadermy{f1u3n7_1n_pn9_&_pdf_96385309}
```

Nope, let me try:

```
academy{f1u3n7_1n_pn9_&_pdf_96385309}
```

Wow that was it. But I'm not satisfied, lets investigate further.

```
file flag2of2-final.pdf
flag2of2-final.pdf: PNG image data, 200 x 40, 4-bit colormap, non-interlaced
```

hah, it was a png, makes sense why tesseract worked

```
pdftotext flag2of2-final.pdf -
1n_pn9_&_pdf_96385309}
```

hm yeah okay that could've also worked but kind of useless,

since it's a png, lets go to xxd

```
xxd flag2of2-final.pdf | grep "{"
00000100: b4e0 0756 2e23 0fef 104d 887b c353 140e  ...V.#...M.{.S..
00000180: 0b32 9dd9 2657 215e 8268 617b b085 1f40  .2..&W!^.ha{...@

xxd flag2of2-final.pdf | grep "}"
000000e0: 1da2 8715 f17d 42b7 7c04 32c3 ca0a 0e84  .....}B.|.2.....
00000110: ce80 c5c0 b0fc e75b 7da2 2607 669c 391d  .......[}.&.f.9.
```

Yeah I'm not seeing anything here....

So what's going on here?
I'm assuming from the title, this file has 2 formats, pdf and png, thats why tesseract and pdftotext gave me different results, nice.

```
xxd flag2of2-final.pdf | grep -i pdf
000001c0: 44ae 4260 8225 5044 462d 312e 340a 25c7  D.B`.%PDF-1.4.%.
00000230: 3d70 6466 7772 6974 6520 2d73 7374 646f  =pdfwrite -sstdo
00000380: 5072 6f63 5365 745b 2f50 4446 202f 5465  ProcSet[/PDF /Te
00000600: 786d 6c6e 733a 7064 663d 2768 7474 703a  xmlns:pdf='http:
00000620: 6466 2f31 2e33 2f27 2070 6466 3a50 726f  df/1.3/' pdf:Pro
00000830: 6c69 6361 7469 6f6e 2f70 6466 273e 3c64  lication/pdf'><d

xxd flag2of2-final.pdf | grep -i png
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
```
