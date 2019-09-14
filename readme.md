# Alpha Decay Calc

Calculates the theoretical stability of nucleons to alpha decay using the semi-empirical formula of Bethe-Weizsacker

# Overview / How to use

Constants Used:
* Coeficiente de Volume              Av = 15.56 MeV
* Coeficiente de superficie          As = 17.23 MeV
* Coeficiente de Coulombian          Ac = 0.697 MeV
* Coeficiente de Simetria            Asim = 23.285 MeV
* Coeficiente de Paridade            Ab = 12.0 MeV

* Mass of Neutron                    Mn = 938.272 MeV*c^2
* Mass of Proton                     Mp = 939.566 MeV*c^2

This theory is based on calculating the actual mass of 2 nucleus e comparing if an alpha decay would put the resulting child nucleon (and alpha particle) in a lower energy state. if it does the
decay can (and will) spontaneous occurs (the time length it may take for it to happen is another history).

So, the steps involved in this are:
1. Calculate the Mass of a Nucleon (Z,A)
2. Calculate the Mass of the resulting child nucleon (Z-2,A-4) if an alpha decay would occur
3. Check if Q > 0 ,where Q =  M(Z,A) - (M(Z-2,A-4) + Maplha)

The main work this algorithm does is to calculate the masses using Z and A.

* It's Also possible to only use the algorithm to calculate Masses using the semi-empirical formula.

## Theory Overview

We know, experimentally, that the mass of a nucleus is not equal to the sum of the mass of the Z protons and N neutrons, the mass is always lower than this sum. So,

DeltaM = Z*Mp + N*Mn - M(Z,A)

where M(Z,A) is the actual measurable mass of the nucleus.
This Difference is called the binding energy and it's responsible to bind the nucleons to one another. We can call it,
B(Z,A) = DeltaM*c^2
So,

M(Z,A) = Z*Mp + N*Mn - B(Z,A)

So, the mass of a nucleus is equal to the sum of the mass of its constituents (protons and neutrons) minus the binding energy.
However, the masses we mostly work on are the atomic ones not the nuclear ones, mostly to simplify tables and reduce confusion. Either way, this same formula still holds 
if you change make M be the atomic mass, you just also must make Mp the hydrogen mass.

Know the work is to calculate the Binding Energy of the Nucleus. This is done by the semi-empirical formula of Bethe-Weizsacker.
This is also called the Liquid Drop Model, as it works as a parallel to a water drop.

This formula works by considering five effects divided in five different correction terms. The effects are:
1. Volume
2. Superficies
3. Coulomb energy
4. Symmetry
5. Coupling

The full Formula is:

B(Z,A) = Av*A - As*(A**2/3) - Ac*(Z**2/A**1/3) - Aa*((A - 2Z)**2 / A) + Delta_Coupling

A more appropriate explanation of the terms can be found in the reference.


## Referencies

* [1] "Introdução à Física Nuclear" de K.C. Chung, Editora da UERJ ( Universidade Estadual do Rio de Janeiro), 2001.
* [2] "Nuclear and Particle Physics" de W.S.C. Williams, Oxford Science Publications, 1992.
