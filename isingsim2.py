from random import random,choice
from math import exp
Temp=2.3              # Temperature
n=20                  # Sites per edge for n x n system
n2=n*n                # Precalculate n*n
nlist=list(range(n))  # List of sites
ntrials=200000        # Number Trials
nequil=100000         # Equilibration steps
Tmax=4.0
Temp=0.0
dT=0.1
while Temp<Tmax:
    Temp+=dT

    # Initialize sums for averages
    E_sum=0
    E2_sum=0
    ## Insert lines from lecture notes here

    # Create initial matrix of spins all spin up
    spins=[[1 for i in range(n)] for j in range(n)]

    # Run simulation
    for trials in range(1, (ntrials+nequil+1)):
        i=choice(nlist)
        j=choice(nlist)
    ## Insert lines from lecture notes here
        
        #Calculate the change in energy if we flip this spin
        deltaE=2.*(spins[i][j]*\
           (spins[i][(j+1)%n]+spins[i][(j-1+n)%n]+\
             spins[(i+1)%n][j]+spins[(i+-1+n)%n][j]))

        #Flip the spin using Metropolis MC
        if exp(-deltaE/Temp) > random():
            spins[i][j]=-spins[i][j]
        else:
            deltaE=0.0
        ## Insert lines from lecture notes here

        # Calculate system energy ONCE
        if trials==nequil:
            energy=0.0  
            for i in range(n):
                for j in range(n):
                    energy-=(spins[i][j]*
                             (spins[i][(j+1)%n]+spins[i][(j-1+n)%n]+\
                              spins[(i+1)%n][j]+spins[(i+-1+n)%n][j]))
            energy/=n2
        if trials > nequil:
            energy+=deltaE/n2
            E_sum+=energy
            E2_sum+=energy*energy
    E_ave=E_sum/ntrials
    E2_ave=E2_sum/ntrials
    Cv=1/(Temp*Temp)*(E2_ave-E_ave*E_ave)
    print('%8.4f %10.6f %10.6f'%(Temp, E_ave, Cv))
