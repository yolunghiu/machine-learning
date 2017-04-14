%% Author: Lu, Chia-Feng 2013.10.11
clear,

data=rand(100,3);

[filename filepath]=uiputfile('*.xls');
full_filepath=[filepath filename];

xlswrite(full_filepath,data,3,'B10');  % write the data into the 3rd sheet from B10

