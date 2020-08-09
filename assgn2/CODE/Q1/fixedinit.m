function [x] = fixedinit(arr,k)
x =[];
j=1;
q = 300;
for i=1:size(arr,1)
    x = [x,j];
    if(mod(i,q)== 0)
        j = j+1;
        if(j>k)
            j =1;
        end
    end
end
end