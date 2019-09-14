

## Mass Constants
M_ELECTRON = float(0.511)
M_PROTON   = float(938.272)
M_NEUTRON  = float(939.566)
M_ALPHA    = float(3727.323) 

## Coeficients of of the Bethe-Weizsacker formula
A_VOLUME = float(15.56)
A_SURFACE = float(17.23)
A_COULOMB = float(0.697)
A_SYMMETRY = float(23.285)
A_BINDING = float(12.0)

class Nucleon():
    """
    Defines a Nucleon and if suffers alpha decay

    """
    def __init__(self,Z,A):
        # print("fiz um nucle")
        self.Z = Z
        self.A = A
        self.N = A - Z
        self.BindingE = 0
        self.Mass = 0
        self.AlphaStable = True

    def Calculate_Mass(self):
        if self.BindingE == 0:
            self.Calculate_BindingE()
        
        self.Mass = M_NEUTRON * self.N + M_PROTON * self.Z - self.BindingE
        return self.Mass
        # print("Massa: ",self.Mass)


    def Calculate_BindingE(self):
        Volume_term = A_VOLUME * self.A
        Surface_term = A_SURFACE * (self.A ** (2/3))
        Coulomb_term = A_COULOMB * ((self.Z **2) / (self.A ** (1/3)))
        Symmetry_term = A_SYMMETRY * (((self.A - (2 * self.Z)) ** 2) / (self.A))
        if self.A % 2 == 0:
            Binding_term = (A_BINDING / (self.A ** (1/2)))
            if self.Z % 2 == 0:
                Binding_term = - Binding_term
        else:
            Binding_term = 0

        self.BindingE = Volume_term - Surface_term - Coulomb_term - Symmetry_term - Binding_term
        # print("Binding energy: ",self.BindingE,"(",Volume_term,Surface_term,Coulomb_term,Symmetry_term,Binding_term,")")


    def Check_Stability(self):
        if self.Mass == 0:
            self.Calculate_Mass()

        decayed_nucleon = Nucleon(self.Z-2,self.A-4)
        decayed_nucleon.Calculate_Mass()
        Q = self.Mass - (decayed_nucleon.Mass + M_ALPHA)
        # print("Q value: ",Q)
        if Q > 0:
           self.AlphaStable = False
        
        return self.AlphaStable
         