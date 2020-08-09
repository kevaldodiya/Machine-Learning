function [A,k1]  = findingcovariance(mu,c1,c2)
x1 = mu(1,1);
x2 = mu(1,2);
k1 = [c1(1)-x1 c2(1)-x2];
for i = 2:size(c1,1)
    j = c1(i)-x1;
    k = c2(i)-x2;
    k1 = [k1;j,k];
end
transk1 = transpose(k1);
A = transk1 * k1;
A = (1/2000)*A;
end