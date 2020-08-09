load Dataset1.csv;
k = input("give va1ue of k")
index = randominit(Dataset1,k);
newmu = findingMu(Dataset1,index,k);
mu = zeros(size(Dataset1,2),k);
e = error1(Dataset1,newmu,index);
index = assignMin(Dataset1,newmu);
sum = comp(mu,newmu,k);
err = [];
while sum >0
    mu = newmu;
    newmu = findingMu(Dataset1,index,k);
    index = assignMin(Dataset1,newmu);
    e = error1(Dataset1,newmu,index);
    err = [err;e];
    sum = comp(mu,newmu,k);
end
  
   temp =[];
    for j=1:size(index,2)
        if(index(j) == 1)
            temp = [temp;Dataset1(j,:)];
        end
    end
    figure(1);
    if(isempty(temp) == 0)
        c1 = temp(:,1);
        c2 = temp(:,2);
        scatter(c1,c2,'r');
        hold on
    end
    
    temp =[];
    for j=1:size(index,2)
        if(index(j) == 2)
            temp = [temp;Dataset1(j,:)];
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
            temp = [temp;Dataset1(j,:)];
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
            temp = [temp;Dataset1(j,:)];
        end
    end
    if(isempty(temp) == 0)
        c1 = temp(:,1);
        c2 = temp(:,2);
        scatter(c1,c2,'g');
        hold on
    end
    figure(2);
    kv = [];
    for i =1:size(err,1)
        kv = [kv;i];
    end
    plot(kv,err);
    xlabel("no of iterations");
    ylabel("error");
    title("error Vs iterations");