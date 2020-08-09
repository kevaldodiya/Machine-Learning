function [e] = testError(data,lam)
y = data(:,101);
data(:,101) = [];
w = rand(size(data,2),1);
for k=1:10000
    for i=1:size(data,2)
        b=findB(data,i);
        a=findA(data,i,w,y);
        if(a< (-lam))
            w(i,1) = (-lam - a)/b;
        elseif(a>lam)
            w(i,1) = (lam-a)/b;
        else
            w(i,1) = 0;
        end
    end
end
e =0;
temp =0;
for i = 1:size(data,1)
    temp =  data(i,:) * w;
    e = e + ((temp - y(i,1)).^ 2);
end
e = e ./ (2.*size(data,1));
end
