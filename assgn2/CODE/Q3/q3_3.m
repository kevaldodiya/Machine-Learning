load Dataset_train.csv;
load Dataset_test.csv
data =Dataset_train;
y = data(:,101);
data(:,101) = [];
w = rand(size(data,2),1);
lam_ar =[];
er = [];
ratio=input("ratio");

for lam=0.01:0.01:0.2
   k = cross_validation(data,ratio,y,lam);
   er =[er,k];
   lam_ar = [lam_ar,lam];
end
er = er';
lam_ar = lam_ar';
plot(lam_ar,er);
xlabel("lamda value");
ylabel("validation error");
title("error Vs lamda");

e = testError(Dataset_test,0.06); %testing error