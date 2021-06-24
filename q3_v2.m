
p = 0.25;
q = p;
n = 0;

num_n = q*(1-p)*p^n;
num_5 = p^5*(1-p);
den = q*(1-p^5)+(1-p)*p^5;

pi_n = num_n/den
pi_5 = num_5/den