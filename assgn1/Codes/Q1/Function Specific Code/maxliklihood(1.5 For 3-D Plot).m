load Dataset1.csv
c1 = Dataset1(:,1);
c2 = Dataset1(:,2);
mu1 = [];
for i = -10:10
    for j = i:10
        mu1 = [mu1;i,j];
    end
end      
jem = [];
for i =1:size(mu1,1)
    [covari,k1] = findingcovariance(mu1(i,:),c1,c2);
    covari = [1,0;0,1];
    in = inv(covari);
    temp = log(2*pi);
    temp = (-2000)*temp;
    B = findingLle(k1,in);
    temp = temp + B;
    jem = [jem,temp];
end
k = mu1;
for i =1:size(mu1,1)
    k(i,3) = jem(i);
end
scatter3(k(:,1),k(:,2),k(:,3));
xlabel("xaxis");
ylabel("y-axis");