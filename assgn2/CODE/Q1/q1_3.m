load Dataset1.csv
k = input("give va1ue of k");
temp =[];
t1 =[];
j =1;
   for i=1:1:5
       e = ercomp(Dataset1,k,i,j);
       j = j+1;
       temp =[temp,e];
       t1 =[t1,i];
   end
   figure(11);
   plot(t1,temp);
   xlabel("sigma value");
   ylabel("error");
   title("error Vs sigma");