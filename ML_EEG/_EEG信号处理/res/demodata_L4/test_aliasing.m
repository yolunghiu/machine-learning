%% Author: Lu, Chia-Feng 2013.10.18
clear close all

%% initialize parameters
wave1_freq=30;   % in Hz
wave2_freq=150;  % in Hz

rfactor=8;               % downsample factor
disp_trange=[0 0.15];    % define minimal and maximal time points to display (in second)

%% create two different-frequency sine waves and mix them
t = 0:0.001:1;     % 1000 datapoints within 1 second, namely 1000Hz
wave1 = sin(2*pi*wave1_freq*t);   % 30 Hz
wave2 = sin(2*pi*wave2_freq*t);  % 150 Hz
mixwave = wave1 + wave2;

figure,
subplot(4,1,1);
plot(t,wave1,'o-')  % plot wave 1
axis([disp_trange(1) disp_trange(end) -2 2]);
grid on

subplot(4,1,2);
plot(t,wave2,'o-')  % plot wave 2
axis([disp_trange(1) disp_trange(end) -2 2]);
grid on

subplot(4,1,3);
plot(t,mixwave,'o-'); hold on
axis([disp_trange(1) disp_trange(end) -2 2]);
y = decimate(mixwave,rfactor);      % downsample with lowpass filter
plot(t(1:rfactor:end),y,'ro-','linewidth',2)   
legend('Original Signal','Decimated Signal')
grid on

subplot(4,1,4);
plot(t,mixwave,'o-'); hold on
axis([disp_trange(1) disp_trange(end) -2 2]);
y = downsample(mixwave,rfactor);   % downsample without lowpass filter
plot(t(1:rfactor:end),y,'ro-','linewidth',2) 
legend('Original Signal','Decimated Signal (no filtering)')
grid on