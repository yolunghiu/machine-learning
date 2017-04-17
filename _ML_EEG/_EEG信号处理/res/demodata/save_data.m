%% Author: Lu, Chia-Feng 2013.10.11
%% option 1
save('Data.mat')   % save all variables in workspace

%% option 2
A=[1:10];
B=[2:20];
save('Data.mat','A','B')   % save A and B variables

%% option 3
save('Data.txt','A','B','-ascii')   % save A and B variables in ASCII format
