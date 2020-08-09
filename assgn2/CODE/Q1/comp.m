function [sum] = comp(mu,newmu,k)
    compare = [];
for i =1:k
    temp = findingDist(mu(:,i),newmu(:,i));
    temp = sqrt(temp);
    compare = [compare,temp];
end
j = compare > 0.001;
sum=0;
for i=1:k
    sum = sum + j(i);
end
