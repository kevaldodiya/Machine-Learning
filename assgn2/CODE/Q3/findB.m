function [a] = findB(data,in)
temp = 0;    
for i=1:size(data,1)
    temp = temp + data(i,in).* data(i,in);
end
a = 2.*temp;
end