function [mu] = findingMu(data,index,k)
    mu =zeros(size(data,2),k);
    count = zeros(1,k);
    for i=1:size(index,2)
        k = index(i);
        count(k) = count(k) + 1;
        temp = data(i,:);
        temp = temp';
        mu(:,k) = mu(:,k) + temp;
    end
    for i=1:size(mu,2)
        mu(:,i) = (1/count(i)) * mu(:,i);
    end
end
        