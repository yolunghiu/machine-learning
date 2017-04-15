%% Author: Lu, Chia-Feng 2013.10.11
clear,
%% initialize parameters
offset=178;       % use Binary Viewer to check how many bytes should be skipped
channelno=40;     % record in the *.vhdr file
datapoint=93040;  % record in the *.vhdr file

%% define the full_filepath
%%% option 1: keyin the full file path
full_filepath='data.dat';

%%% option 2: assign the full file path using "file open" dialog
% [filename filepath]=uigetfile('*.*');
% full_filepath=[filepath filename];

%% load ASCII file with regular matrix/vector arrangement
fid=fopen(full_filepath,'r');
fseek(fid,offset,'bof');                       % re-locate the position of indicator
data=fscanf(fid,'%f',[channelno datapoint])';  % fscanf scan the file line by line
fclose(fid);

