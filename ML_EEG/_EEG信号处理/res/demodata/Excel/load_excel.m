%% Author: Lu, Chia-Feng 2013.10.11
clear,

%% define the full_filepath
%%% option 1: keyin the full file path
full_filepath='Take06.csv';

%%% option 2: assign the full file path using "file open" dialog
% [filename filepath]=uigetfile('*.*');
% full_filepath=[filepath filename];

%% load ASCII file with regular matrix/vector arrangement
[NUMERIC,TXT,RAW]=xlsread(full_filepath,1,'H11887:J23746');

