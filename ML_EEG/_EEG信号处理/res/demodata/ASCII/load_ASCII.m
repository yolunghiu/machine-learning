%% Author: Lu, Chia-Feng 2013.10.11
clear,
%% define the full_filepath
%%% option 1: keyin the full file path
% full_filepath='MAX80_TEST.txt';

%%% option 2: assign the full file path using "file open" dialog
[filename filepath]=uigetfile('*.*');
full_filepath=[filepath filename];

%% load ASCII file with regular matrix/vector arrangement
load(full_filepath)
