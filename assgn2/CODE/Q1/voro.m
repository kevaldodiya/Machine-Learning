function [mat] = voro(mu,xmin,xmax,ymin,ymax,k)
  xmax = xmax + 10000;
  xmin = xmin -10000;
  ymax = ymax + 10000;
  ymin = ymin - 10000;
  range1 = (xmax - xmin +1)./2000;
  range2 = (ymax-ymin + 1)./2000;
  x = [];
  y =[];
  i = xmin;
  while(xmax>=i)
      x = [x,i./10000];
      i = i + range1;
  end
  i = ymin;
  while(ymax>=i)
      y = [y,i./10000];
      i = i + range2;
  end
  mat = zeros(size(y,2),size(x,2));
  for i =1:size(y,2)
      for j=1:size(x,2)
        temp = [x(j);y(i)];
        t =[];
        for q=1:k 
           t1 = findingDist(mu(:,q),temp);
           t =[t,t1];
        end
        min = t(1);
        kem = 1;
        for q =1:size(t,2)
            if(min>t(q))
                min = t(q);
                kem =q;
            end
        end
        mat(i,j) = kem;
      end
  end