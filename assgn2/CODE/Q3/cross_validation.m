function [e] = cross_validation(data,ratio,y,lam)
 w = rand(size(data,2),1);
 rat = round(ratio.* size(data,1));
 x = 1:1:rat;
 d_train = data(x,:);
 y_train = y(x,:);
for k=1:800
    for i=1:size(d_train,2)
        b=findB(d_train,i);
        a=findA(d_train,i,w,y_train);
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
for i = (rat+1):size(data,1)
    temp =  data(i,:) * w;
    e = e + ((temp - y(i,1)).^ 2);
end
e = e ./ (2.*(size(data,1)-rat+1));
end
    