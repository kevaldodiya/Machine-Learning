function [dist] = findingDist(p1,p2)
dist =0;    
for i =1:size(p1,1)
    temp = p1(i,1)-p2(i,1);
    dist = dist +  temp .* temp;
end
end