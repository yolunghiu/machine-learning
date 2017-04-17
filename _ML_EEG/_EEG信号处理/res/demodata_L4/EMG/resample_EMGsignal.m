%% Author: Lu, Chia-Feng 2013.10.18
clear, close all

%% initialize parameters
org_SR=2000;  % in Hz

new_SR1=1000;
new_SR2=500;
new_SR3=300;
new_SR4=100;
new_SR5=50;

%% load EMG data with ICA noise elimination
load('EMG_ICA.mat')  % the EMG data are saved as "fdata" matrix
org_signal=fdata(:,1);  % in this demo, we only use the first channel
org_taxis=[1:length(fdata)]/org_SR;  % define time axis

%% resample signal in different sampling rates
[p,q]=rat(new_SR1/org_SR);
new_signal1=resample(org_signal,p,q);
new_taxis1=[1:length(new_signal1)]'/new_SR1;

[p,q]=rat(new_SR2/org_SR);
new_signal2=resample(org_signal,p,q);
new_taxis2=[1:length(new_signal2)]'/new_SR2;

[p,q]=rat(new_SR3/org_SR);
new_signal3=resample(org_signal,p,q);
new_taxis3=[1:length(new_signal3)]'/new_SR3;

[p,q]=rat(new_SR4/org_SR);
new_signal4=resample(org_signal,p,q);
new_taxis4=[1:length(new_signal4)]'/new_SR4;

[p,q]=rat(new_SR5/org_SR);
new_signal5=resample(org_signal,p,q);
new_taxis5=[1:length(new_signal5)]'/new_SR5;

%% plot original signal and resampled signals
figure, 
subplot(6,1,1),plot(org_taxis,org_signal),axis([14 15.4 -1 1]),ylabel([num2str(org_SR) 'Hz'])
subplot(6,1,2),plot(new_taxis1,new_signal1),axis([14 15.4 -1 1]),ylabel([num2str(new_SR1) 'Hz'])
subplot(6,1,3),plot(new_taxis2,new_signal2),axis([14 15.4 -1 1]),ylabel([num2str(new_SR2) 'Hz'])
subplot(6,1,4),plot(new_taxis3,new_signal3),axis([14 15.4 -1 1]),ylabel([num2str(new_SR3) 'Hz'])
subplot(6,1,5),plot(new_taxis4,new_signal4),axis([14 15.4 -1 1]),ylabel([num2str(new_SR4) 'Hz'])
subplot(6,1,6),plot(new_taxis5,new_signal5),axis([14 15.4 -1 1]),ylabel([num2str(new_SR5) 'Hz']),xlabel('time(s)')

