

## Mass Constants
M_ELECTRON = float(0.511)
M_PROTON   = float(938.272)
M_NEUTRON  = float(939.566) 

## Coeficients of of the Bethe-Weizsacker formula
A_VOLUME = float(15.68)
A_SURFACE = float(18.56)
A_COULOMB = float(0.717)
A_SYMMETRY = float(28.1)

class Nucleon():
    """
    Defines a Nucleon and if suffers alpha decay

    """
    def __init__(self,Z,A):
        self.Z = Z
        self.A = A
        self.N = A - Z
        self.BindingE = 0
        self.Mass = 0
        self.AlphaStable = True

    def Calculate_Mass(self):
        if(self.BindingE == 0)
            self.Calculate_BindingE()
        
        self.Mass = M_NEUTRON * self.N + M_PROTON * self.Z - self.BindingE


    def Calculate_BindingE(self):
        Volume_term = A_VOLUME * self.A
        Surface_term = A_SURFACE * (self.A ** 2/3)
        Coulomb_term = A_COULOMB * ((self.Z * (self.Z - 1)) / (self.A ** 1/3))
        Symmetry_term = A_SYMMETRY * (((self.N - self.Z) ** 2) / (self.A))
        if self.A % 2 == 0:
            Binding_term = (34 * (self.A ** (-3/4)) )
            if self.Z % 2 == 0:
                Binding_term = - Binding_term
        else:
            Binding_term = 0
        
        self.BindingE = Volume_term - Surface_term - Coulomb_term - Symmetry_term - Binding_term


    def Check_Stability(self):






def main():
    print("Hello World")


if __name__ == "__main__":
    main()