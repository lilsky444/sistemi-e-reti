import math

IP_SBM = "11111111111111111111111111111111"
BIT = 8
SBM = 32


class IPadress():
    def __init__(self, ip_adress, sm, nr):
        self.ip_decimal = ip_adress
        if (sm[1:] == "/"):
            self.subnet_mask = sm
        else:
            self.subnet_mask = sm
            self.ip_binary = self.convertBin()
            self.ip_subnet_mask = self.ip_sbm()
            self.n_host_collegabili = self.hostCanConect()
            self.ip_rete_binary = self.ipReteBrodcast("0")
            self.ip_brodcast_binary = self.ipReteBrodcast("1")
            self.ip_rete = self.ipConverter(self.ip_rete_binary)
            self.ip_brodcast = self.ipConverter(self.ip_brodcast_binary)
            self.nsottoreti = nr

    def toList(self, ip):
        list = ip.split(".")
        return [int(i) for i in list]

    def convertBin(self):
        list = self.toList(self.ip_decimal)
        ip = ""

        for i in list:
            tmp = bin(i)[2:]
            tmp = "0" * (BIT - len(tmp)) + tmp
            ip += tmp + "."

        return ip[:-1]

    def ip_sbm(self):
        tmp = IP_SBM[:len(IP_SBM) - (SBM - int(self.subnet_mask[1:]))]
        tmp += "0" * (len(IP_SBM) - len(tmp))

        ip = ""
        for i in range(len(tmp)):
            if (i == 7 or i == 15 or i == 23):
                ip += tmp[i] + "."
            else:
                ip += tmp[i]

        return ip

    def hostCanConect(self):
        return (2 ** (SBM - int(self.subnet_mask[1:])) - 2)

    def ipReteBrodcast(self, b):
        s = self.convert_ip_to_string(self.ip_binary)

        tmp = s[:len(s) - (SBM - int(self.subnet_mask[1:]))]
        tmp += b * (len(s) - len(tmp))

        ip = ""
        for i in range(len(tmp)):
            if (i == 7 or i == 15 or i == 23):
                ip += tmp[i] + "."
            else:
                ip += tmp[i]

        return ip

    def convert_ip_to_string(self, ip):
        l = ip.split(".")
        s = ""
        for i in l:
            s += i
        return s

    def binaryToDecimal(self, binary):
        decimal, i = 0, 0
        while (binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary // 10
            i += 1

        return decimal

    def ipConverter(self, ip):
        l = ip.split(".")
        s = ""

        for i in l:
            s += str(self.binaryToDecimal(int(i))) + "."
        return s[:-1]

def calcoloSottoReti(ipRete, sm, nsottoreti):
    sm = int(sm[1:])
    host_utilizzabili = 2**(32-sm)-2
    sm += math.ceil(math.log2(nsottoreti))

    print(sm, host_utilizzabili)
    


def main():
    ip_adress = IPadress(input("inserire indirizzo ip: "), input("inserire subnetmask: "),
    input("inserire il numero di sottoreti: "))

    # print("ip iniziale: ", ip_adress.ip_decimal)
    # print("ip iniziale binario:", ip_adress.ip_binary)
    # print()
    # print(ip_adress.ip_subnet_mask)
    # print()

    print("n max host: ", ip_adress.n_host_collegabili)

    # print()
    # print("ip rete bin:", ip_adress.ip_rete_binary)
    # print("ip rete brodcast bin: ", ip_adress.ip_brodcast_binary)
    # print()

    print("ip rete:", ip_adress.ip_rete)
    print("ip brodcast:", ip_adress.ip_brodcast)
    calcoloSottoReti(ip_adress.ip_rete, input("inserire subnetmask: "), 4)


if __name__ == "__main__":
    main()