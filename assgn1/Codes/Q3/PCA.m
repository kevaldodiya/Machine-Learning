load Dataset3.csv
c1 = Dataset3(:,1);
c2 = Dataset3(:,2);
[x1,x2] = findingmu(c1,c2);
mu = [x1,x2];
[covari,k1] = findingcovariance(mu,c1,c2);
disp(covari);
[P,D] = eig(covari);
[P,D] = setEigen(P,D);
total =0;
for i = 1:size(D,1)
    total = total + D(i,i);
end
disp('variance captured by PC1 in %');
ans = (D(1,1)/total)*100;
disp(ans);
disp('variance captured by PC2 in %');
ans = (D(2,2)/total)*100;
disp(ans);
newDataset = transpose(P) * transpose(k1);
newDataset = newDataset';
scatterplot(newDataset); %new data sets
title("PCA");
legend("projected data points");
xlabel("x-comp");
ylabel("y-comp");