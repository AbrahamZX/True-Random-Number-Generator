
# simple code to implement Runs  
# test of randomnes 
  
import random 
import math
import time
import statistics 
import linecache 
import matplotlib.pyplot as plt

def runsTest(l, l_median): 
  
    runs, n1, n2 = 0, 0, 0
      
    # Checking for start of new run 
    for i in range(len(l)): 
          
        # no. of runs 
        if (l[i] >= l_median and l[i-1] < l_median) or (l[i] < l_median and l[i-1] >= l_median): 
            runs += 1  
          
        # no. of positive values 
        if(l[i]) >= l_median: 
            n1 += 1   
          
        # no. of negative values 
        else: 
            n2 += 1   
  
    runs_exp = ((2*n1*n2)/(n1+n2))+1
    stan_dev = math.sqrt((2*n1*n2*(2*n1*n2-n1-n2))/ (((n1+n2)**2)*(n1+n2-1))) 
  
    z = (runs-runs_exp)/stan_dev 
  
    return z 
    
def RunTestVarying (n,step):
    n_cum = range(10,n,step)
    n_cum_plt = []
    tic = time.perf_counter()
    Z_rm_cum = []
    for m in n_cum:
        
        n_cum_plt.append(m)
        l_rm = []
        for i in range(m): 
            l_rm.append(random.random()) 
              
        l_rm_median= statistics.median(l_rm) 
          
        Z_rm = abs(runsTest(l_rm, l_rm_median))
        
        Z_rm_cum.append(Z_rm)
        
    toc = time.perf_counter()
    #print(f"Z-Statistic for Random Module = {Z_rm:0.4f}")
    print(f"Random Module test of randomness took {toc - tic:0.4f} seconds.")

    tic = time.perf_counter()
    
    Z_trng_cum=[]
    tic = time.perf_counter()
    for p in n_cum:
        l_trng = []
        pt = 1
        image = 1
        file = 'TRNG txt data - Image {}.txt'.format(image)
        for i in range (p):
            rand = float(linecache.getline(file,pt))
            l_trng.append(rand)
            pt += 1
            if i == 5999999:
                image = 10
                file = 'TRNG txt data - Image {}.txt'.format(image)
                pt = 1
            if i == 5999999*2:
                image = 53
                file = 'TRNG txt data - Image {}.txt'.format(image)
                pt = 1
            if i == 5999999*3:
                image = 80
                file = 'TRNG txt data - Image {}.txt'.format(image)
                pt = 1

        l_trng_median= statistics.median(l_trng)

        Z_trng = abs(runsTest(l_trng, l_trng_median))

        Z_trng_cum.append(Z_trng)

        
    toc = time.perf_counter() 
    #print(f"Z-Statistic for TRNG = {Z_trng:0.4f}")
    print(f"TRNG test of randomness took {toc - tic:0.4f} seconds.")
    return Z_rm_cum, Z_trng_cum, n_cum_plt

def PlotIt (res):
    plt.title('Random Module - Runs Test of Randomness'), plt.xlabel('# numbers'), plt.ylabel('Z-Statistic')
    plt.plot (res[2],res[0])
    plt.axhline(y=1.96, color='r', linestyle='-')
    plt.show()
    plt.title('TRNG - Runs Test of Randomness'), plt.xlabel('# numbers'), plt.ylabel('Z-Statistic')
    plt.axhline(y=1.96, color='r', linestyle='-')
    plt.plot (res[2],res[1])
    plt.show()

# Running the code
n = 1000000
step = 1000
res = RunTestVarying(n,step)
PlotIt(res)
