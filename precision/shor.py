import shor_func as shf
import math
import random
# m = 2^l, l es el entero menor para cumplir m >=n 
class ShorState:

    def __init__(self, N, y, r, l):
        """
        Inicializa el estado de un array de tuplas (amplitud, estado)
        Dado N = n_1 n_2
        q = 2 ^ L
        """
        self.N = N
        self.y = y
        self.r = r
        self.l = l
        self.L = math.ceil(math.log2(self.N)) 
        self.q = 2**self.L
        amplitud = 1/math.sqrt(self.q)
        self.State = [[amplitud,i,0,0,""] for i in range(self.q)]
        self.n1 = 0
        self.n2 = 0

    def modular_exp(self):
        exp = 0
        for row in self.State:
            row[2] = shf.bin_exp(self.y, exp, self.N)
            exp += 1

    def rand_l (self):
        self.l = random.randint(0,self.r)
    
    def QFTi (self):
        c = 0
        for row in self.State:
            row[0] = shf.func_c(c, self.r, self.q, self.l)
            c += 1

    def measure(self):
        for row in self.State:
            row[3] = shf.complex_prob(row[0])
            row[4] = '|' + str(row[1]) + '⟩' +  '|' + str(row[2]) + '⟩' 
    def get_labels(self):
        labels = []
        for row in self.State:
            labels.append(row[4])
        return labels

    def get_prob(self):
        prob = []
        for row in self.State:
            prob.append(row[3])
        return prob

    def getfactor(self):
        r_2 = math.floor(self.r/2)
        y_r_2 = self.y ** r_2
        f_1 = y_r_2 + 1
        f_2 = y_r_2 - 1
        self.n1 = shf.gcd(f_1, self.N)
        self.n2 = shf.gcd(f_2, self.N)

    def execute(self):
        self.modular_exp()
        self.QFTi()
        self.measure()
        self.getfactor()


    def set_params_recal(self, r, y, l):
        self.r = r
        self.y = y
        self.l = l
        self.n1 = 0
        self.n2 = 0
        self.modular_exp()
        self.QFTi()
        self.measure()
        self.getfactor()



    def print_factors(self):
        print("N:", self.N, "(",self.n1, "*", self.n2 , ") =", self.n1 * self.n2)

    def print_prob(self):    
        bin_length = '0' + str(self.L) + 'b'        
        for row in self.State:
            base = "|" + format(row[1], bin_length) + '>'
            print("prob:",row[3], "  base:", base , "  mod:", row[2])

    def print_state(self):
        bin_length = '0' + str(self.L) + 'b'        
        for row in self.State:
            base = "|" + format(row[1], bin_length) + '>'
            print("aplha:",row[0], "  base:", base , "  mod:", row[2])