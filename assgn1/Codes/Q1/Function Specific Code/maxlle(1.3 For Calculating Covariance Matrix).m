load Dataset1.csv
c1 = Dataset1(:,1);
c2 = Dataset1(:,2);
[x1,x2] = findingmu(c1,c2);
mu = [x1 x2];
[A,k1] = findingcovariance(mu,c1,c2);
disp(A);
in = inv(A);
d = det(A);
mle = (-2000)*log(2*pi);
mle  = mle + (-1000)*log(d);
B = findingLle(k1,in);
mle = mle + B;
disp(mle);