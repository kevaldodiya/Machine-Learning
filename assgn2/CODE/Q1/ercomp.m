function [e] = ercomp(Dataset1,k,sigma,i)
   [Dataset1,d3] = k2(Dataset1,sigma,k); 
   index = randominit(Dataset1,k);
    newmu = findingMu(Dataset1,index,k);
    mu = zeros(size(Dataset1,2),k);
    e = error1(Dataset1,newmu,index);
    index = assignMin(Dataset1,newmu);
    sum = comp(mu,newmu,k);
    while sum >0
        mu = newmu;
        newmu = findingMu(Dataset1,index,k);
        index = assignMin(Dataset1,newmu);
        e = error1(Dataset1,newmu,index);
        sum = comp(mu,newmu,k);
    end
    figure(i);
    temp =[];
    index =index';
    for j=1:size(index,2)
        if(index(j) == 1)
           temp = [temp;d3(j,:)];
        end
    end
        if(isempty(temp) == 0)
            c1 = temp(:,1);
            c2 = temp(:,2);
            scatter(c1,c2,'r');
            hold on
        end

        temp =[];
        for j=1:size(index,2)
            if(index(j) == 2)
                temp = [temp;d3(j,:)];
            end
        end
        if(isempty(temp) == 0)
            c1 = temp(:,1);
            c2 = temp(:,2);
            scatter(c1,c2,'b');
            hold on
        end

        temp =[];
        for j=1:size(index,2)
            if(index(j) == 3)
                temp = [temp;d3(j,:)];
            end
        end
       if(isempty(temp) == 0)
            c1 = temp(:,1);
            c2 = temp(:,2);
            scatter(c1,c2,'y');
            hold on
        end

        temp =[];
        for j=1:size(index,2)
            if(index(j) == 4)
                temp = [temp;d3(j,:)];
            end
        end
        if(isempty(temp) == 0)
            c1 = temp(:,1);
            c2 = temp(:,2);
            scatter(c1,c2,'g');
            hold on
        end
        xlabel("x-axis");
        ylabel("y-axis");
        title("dataset after kk-means");
end
    
    