%% Author: Lu, Chia-Feng 2013.10.11

clear,

fid=fopen('test_ASCII.txt','w');    % overwrite the file from the beginning of file
% fid=fopen('test_ASCII.txt','a');   % append new information to the end of file

fprintf(fid,'%15s','This is a test.')             % print a 15-character string
fprintf(fid,'\r\n')                               % change line
fprintf(fid,'%11s %8d','The date is',20131011)    % print an 11-character string and an 8-digit integer 
fprintf(fid,'\r\n')                               % change line
fprintf(fid,'%5.4f',12345.1234)                   % print a floating number

fclose(fid)