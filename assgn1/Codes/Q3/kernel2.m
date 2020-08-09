load Dataset3.csv;
temp = Dataset3;
k2 = zeros(1000);
x = "value of sigma";
sigma = input(x);
for i = 1:size(Dataset3,1)
    t = temp(i,:);
    for j = 1:size(Dataset3,1)
        k = t - temp(j,:);
        k = -(k * k');
        k = k/(2*sigma);
        k = exp(k);
        k2(i,j) = k;
    end
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
title("kernel2 with sigma is 1");
xlabel("x-comp");
ylabel("y-comp");