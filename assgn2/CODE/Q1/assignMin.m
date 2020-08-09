function [index] = assignMin(data,mu)
    index =[];
    for i=1:size(data,1)
        min = findingDist(data(i,:)',mu(:,1));
        temp = 1;
        for j =2:size(mu,2)
            t1 = findingDist(data(i,:)',mu(:,j));
            if(t1<min)
                min = t1;
                temp = j;
            end
        end
        index = [index ,temp];
    end
end