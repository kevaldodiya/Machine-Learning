function [x] = randominit(arr,k)
x =[];
j=1;
for i=1:k.*10
    x = [x,j];
    if(mod(i,10)== 0)
        j = j+1;
    end
end
for i = (k.*10)+1:size(arr,1)
        temp = randperm(k,1);
        x = [x,temp];
end
end