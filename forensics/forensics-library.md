## file
checks the target file type
* file <filename>

## exiftool
checks image metadata
* exiftool <filename>
* use when the image looks normal, pixels and everything, so metadata is the next thing to check

## binwalk
scans for other files hidden inside this one, like a zip stuffed inside a jpg
* binwalk <filename>
* use right after file and exiftool come back clean

## strings
pulls human readable text out of a file, needs a run of several printable characters in a row to count
* strings <filename>
* cheap first step on pngs and disks, might as well check, sometimes just hands you the answer

## xxd
* xxd <filename>, hex viewer for a file
* xxd -r -p <filename>, hex back to raw binary
* hexedit <filename>, separate tool, for actually editing the raw bytes

## steghide
extracts data hidden in the actual pixel or audio content itself, steganography, not metadata
* steghide extract -sf <image.jpg>
* -sf means stego file, the file you're extracting from
* usually needs a password, common guess or one found elsewhere in the challenge
* run after exiftool, since its a different hiding method

## zsteg
same idea as steghide but for png/bmp specifically, checks pixel data for hidden bit patterns
* zsteg <image.png>
* no password needed unlike steghide
* found a base64 line in an image once that exiftool never showed, since exiftool only reads metadata not pixel data

## mmls
looks at the partition table on a disk image, shows where each partition starts and ends
* mmls <disk.img>

## fls
ls, but for a disk image
* fls -o <offset> <disk.img>
* lists files with their inode numbers, using the offset from mmls

## icat
cat, but for a disk image
* icat -o <offset> <disk.img> <inode> > output_file
* pulls a file's contents using its inode number, not filename, using whatever fls gave you

## foremost
scans raw bytes for known file signatures and carves out matching files
* foremost -i <disk.img> -o <output_folder>
* use when fls/icat cant find something, deleted file or broken filesystem

## mount
attaches a disk image to a folder so you can browse it normally
* sudo mount -o loop,ro,offset=$((2048*512)) <disk.img> /mnt/mydisk
* always mount read only, ro flag, so you dont modify the original evidence

## md5sum / sha256sum
hashes a file
* md5sum <filename>
* sha256sum <filename>
* use to check file integrity, or match a hash against a known one, like checking malware on virustotal

## volatility
analyzes memory dumps, ram captures
* volatility -f <memory.dmp> imageinfo
* pulls running processes, network connections, passwords in memory
* use when given a .raw/.mem/.dmp file instead of a disk image

## John the Ripper / hashcat
crack password hashes you already have, dictionary or brute force
* john <hashfile>
* hashcat -m <hash_type> <hashfile> <wordlist>
* hashcat is gpu accelerated, faster for big jobs
* john is cpu based, simpler for quick jobs

## Hydra
brute forces live logins instead of hashes and passwords
* hydra -l <user> -P <wordlist> <target> <service>
* tries username/password combos directly against a running service, ssh, ftp, a web login form

## nmap
scans a network for devices, and for open ports on a target
* nmap -sV <target>
* -sV adds service/version detection, tells you whats actually running on each port

## tcpdump
captures live network traffic from the command line
* sudo tcpdump -i eth0 -w capture.pcap
* use on a remote/headless box where wireshark's gui isnt available

## tshark
wireshark but cli
* tshark -r capture.pcap -Y "http"
* -Y is a display filter, same syntax as wireshark's filter bar
