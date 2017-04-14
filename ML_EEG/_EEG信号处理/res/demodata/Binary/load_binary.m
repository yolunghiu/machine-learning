%% Author: Lu, Chia-Feng 2013.10.11
clear,
%% initialize parameters
channelno=34;     % record in the *.vhdr file

%% define the full_filepath
%%% option 1: keyin the full file path
full_filepath='fl0014.eeg';

%%% option 2: assign the full file path using "file open" dialog
% [filename filepath]=uigetfile('*.*');
% full_filepath=[filepath filename];

%% load ASCII file with regular matrix/vector arrangement
fid=fopen(full_filepath,'r');
data=fread(fid,inf,'float32');   % read binary data with given precision
data=reshape(data,channelno,[])';            % re-shape data size
fclose(fid);

