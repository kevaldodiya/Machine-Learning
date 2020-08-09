function [e] = error1(data,mu,index)
e = 0;   
for i=1:size(data,1)
        temp = data(i,:);
        temp = temp';
        k = index(i);
       t1 = temp - mu(:,k);
       for j=1:size(t1,1)
           e = e + t1(j,1) .* t1(j,1);
       end
end