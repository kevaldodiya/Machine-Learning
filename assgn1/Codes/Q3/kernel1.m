load Dataset3.csv;
data = Dataset3;
temp = data*transpose(data);
temp1 = ones(1000);
temp = temp1 + temp;
k2 = temp;
y = "value of d";
d = input(y);
for i =2:d
    k2 = k2 .* temp;
end
onebyn = (1/1000) *ones(1000);
k2 = k2 - (onebyn * k2) - (k2 * onebyn) + (onebyn*k2*onebyn);
[P,D] = eig(k2);
[P1, D1] = setEigen(P,D);   
x1 = P1(:,1);
x2 = P1(:,2);
eigspace = [x1,x2];
eigspace = transpose(eigspace);
result = eigspace * k2;
result = transpose(result);
j1 = result(:,1);
j2 = result(:,2);
scatter(j1,j2);
legend("projected data points");
title("kernel1 with d=3");
xlabel("x-comp");
ylabel("y-comp");