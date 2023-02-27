from scipy.stats import norm
import seaborn as sns
import numpy as np

data=np.arange(1,21,1)
pdf=norm.pdf(loc=10,scale=2)

cdfn=norm(loc=10,scale=2).cdf(5)
print(cdfn)


from scipy.stats import poisson
cdfp=poisson.cdf(15,mu=10)
prob=1-cdfp
print(prob)

cdfp1=poisson.cdf(200,mu=100)
prob1=1-cdfp1
print(prob1)