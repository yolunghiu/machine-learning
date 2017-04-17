%% Author: Lu, Chia-Feng 2013.10.11
clear,
%% wirte a binary format
fid=fopen('test_binary.abc','w');    % overwrite the file from the beginning of file
% fid=fopen('test_binary.abc','a');   % append new information to the end of file

data=[23.456 19.664 -14.123 27.548 -10.168];
fwrite(fid,data,'double');                   % wirte variable "data" in double format
fclose(fid)

%% read a binary format
% fid=fopen('test_binary.abc','r');    
% data=fread(fid,5,'double');
% fclose(fid)

