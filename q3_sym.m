syms p s;
P = [1-p,p,0;
     1-p,0,p;
     1-p,0,p];

I = eye(3);

det(s*I-P)