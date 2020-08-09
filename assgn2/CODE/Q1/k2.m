function [eigspace,d3] = k2(Dataset3,sigma,num)
    temp = Dataset3;
    d3 = Dataset3;
    k2 = zeros(1000);
    for i = 1:size(Dataset3,1)
        t = temp(i,:);
        for j = 1:size(Dataset3,1)
            k = t - temp(j,:);
            k = -(k * k');
            k = k/(2*sigma*sigma);
            k = exp(k);
            k2(i,j) = k;
        end
    end
    onebyn = (1/1000) *ones(1000);
    k2 = k2 - (onebyn * k2) - (k2 * onebyn) + (onebyn*k2*onebyn);
    [P,D] = eig(k2);
    [P1, D1] = setEigen(P,D);
    x =1:1:num-3;
    eigspace =P1(:,x);
end