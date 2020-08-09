load Dataset1.csv;
k = input("give va1ue of k")
index = fixedinit(Dataset1,k);
disp(index);
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
  figure(1);
   temp =[];
    for j=1:size(index,2)
        if(index(j) == 1)
            temp = [temp;Dataset1(j,:)];
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
    
    temp =[];
    for j=1:size(index,2)
        if(index(j) == 5)
            temp = [temp;Dataset1(j,:)];
        end
    end
    if(isempty(temp) == 0)
        c1 = temp(:,1);
        c2 = temp(:,2);
        scatter(c1,c2,'k');
        hold on
    end
    xlabel("x-axis");
    ylabel("y-axis");
    title("dataset after k-means");
    c1 = Dataset1(:,1);
    c2 = Dataset1(:,2);
    c1 = c1';
    c2 = c2';
    xmin = c1(1)*10000;
    xmax = c1(1)*10000;
    ymin = c2(1)*10000;
    ymax = c2(1)*10000;
    for i=1:size(c1,2)
        if(c1(i).* 10000>xmax)
            xmax = c1(i).*10000;
        end
        if(c1(i).* 10000<xmin)
            xmin = c1(i).*10000;
        end
        if(c1(i).* 10000>ymax)
            ymax = c2(i).*10000;
        end
        if(c1(i).* 10000<ymin)
            ymin = c2(i).*10000;
        end
    end
    mat = voro(mu,xmin,xmax,ymin,ymax,k);
    for i=1:size(mat,1)
        for j=1:size(mat,2)
            if(mat(i,j) == 1)
                mat(i,j) = 200;
            elseif(mat(i,j) == 2)
                mat(i,j) = 100;
            elseif(mat(i,j) == 3)
                mat(i,j) = 25;
            elseif(mat(i,j) == 4)
                mat(i,j) = 175;
            else
                mat(i,j) = 50;
            end
        end
    end
    figure(2);
    imagesc(mat);
    title("voronoi regeion");