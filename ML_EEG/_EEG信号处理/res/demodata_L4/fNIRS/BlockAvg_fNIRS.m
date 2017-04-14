%% Author: Lu, Chia-Feng 2013.10.18
clear, close all

%% initialize parameters
select_Hbcomp=1; % 1 for HbO2, 2 for Hb, 3 for Hb total
select_channel=5;

SR=10.42; % sampling rate in Hz
segment_tplength=round(50*SR);  % segment in 50 s

%% load fNIRS data with block design
load('fNIRSdata.mat')
% the data signal was saved as "Hbdata" with size timepoints*Hb components(HbO2, Hb, Hbtotal)*channels
% the event markers were recorded in "stimarker" with size timepoints*numbers of event
% "taxis" records the time axis of whole series
signal=Hbdata(:,select_Hbcomp,select_channel);  % we take all timepoints data for HbO2 component at channel 5 as the example

%% locate the event timepoint
% the 1st column of stimarker records the start timepoints of right-arm lifting
% the 2nd column of stimarker records the start timepoints of left-arm lifting
right_time=find(stimarker(:,1)==1);
left_time=find(stimarker(:,2)==1);

%% plot the signal with event timepoints
figure, plot(taxis,signal), hold on
for i=1:length(right_time)
   plot([taxis(right_time(i)) taxis(right_time(i))],[min(signal) max(signal)],'r--','linewidth',2) % red for right
end
for i=1:length(left_time)
   plot([taxis(left_time(i)) taxis(left_time(i))],[min(signal) max(signal)],'k--','linewidth',2) % black for left
end
xlabel('time(s)')
ylabel('HbO2 concentration (a.u.)')

%% cut signal into segments and save as a new matrix with size    segment length* numbers of segment
right_Hbsegment=zeros(segment_tplength,length(right_time));
for i=1:length(right_time)
    right_Hbsegment(:,i)=signal(right_time(i):right_time(i)+segment_tplength-1);
end

left_Hbsegment=zeros(segment_tplength,length(left_time));
for i=1:length(left_time)
    left_Hbsegment(:,i)=signal(left_time(i):left_time(i)+segment_tplength-1);
end

%% plot the segment signals
figure,
cmap='brgbk';
for i=1:length(right_time)
    plot(taxis(1:segment_tplength),right_Hbsegment(:,i),'color',cmap(i)),hold on
end
xlabel('time(s)')
ylabel('HbO2 concentration (a.u.)')
title('Right-arm lifting')
legend('seg. 1','seg. 2','seg. 3','seg. 4','seg. 5')

figure,
for i=1:length(left_time)
    plot(taxis(1:segment_tplength),left_Hbsegment(:,i),'color',cmap(i)),hold on
end
xlabel('time(s)')
ylabel('HbO2 concentration (a.u.)')
title('Left-arm lifting')
legend('seg. 1','seg. 2','seg. 3','seg. 4','seg. 5')

%% plot the block average signals
right_BlockAvg=mean(right_Hbsegment,2);
left_BlockAvg=mean(left_Hbsegment,2);

figure,
plot(taxis(1:segment_tplength),right_BlockAvg,'b'),hold on
plot(taxis(1:segment_tplength),left_BlockAvg,'r'),hold on

xlabel('time(s)')
ylabel('HbO2 concentration (a.u.)')
title('Arm lifting')
legend('right-arm','left-arm')




