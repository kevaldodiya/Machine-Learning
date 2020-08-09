function [a] = findA(data,in,w,y)   
sum =0;
for i=1:size(data,1)
     t = data(i,:) * w;
     t = t - (data(i,in) * w(in,1));
     t = t - y(i,1);
     t = t * data(i,in);
     sum = sum + t;
end
a = 2 .* sum;
            