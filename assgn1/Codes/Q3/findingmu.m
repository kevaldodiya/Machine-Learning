function [x1,x2] = findingmu(c1,c2)
x1 =0;
x2 =0;
for i = 1:size(c1,1)
    x1 = x1 + c1(i);
    x2 = x2 + c2(i);
end
x1 = x1/size(c1,1);
x2 = x2/size(c1,1);
end
