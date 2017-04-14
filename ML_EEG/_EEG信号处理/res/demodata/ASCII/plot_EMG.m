%% Author: Lu, Chia-Feng 2013.10.11
close all

%% open new figure, and plot an axis with one signal (單一視窗單一圖軸單一訊號)
figure,plot(MAX80_TEST(:,3))  % only plot ch.3 signal

title('Ch3 EMG')
xlabel('Data points')
ylabel('Magnitude (\muV)')   % please check the string property of "text" function for the TeX character sequence table
grid on

%% open new figure, and plot an axis with mutiple signals (單一視窗單一圖軸多訊號)
figure,
plot(MAX80_TEST(:,1),'color','r'), hold on
plot(MAX80_TEST(:,2),'color','g')
plot(MAX80_TEST(:,3),'color','b')

title('EMG')
xlabel('Data points')
ylabel('Magnitude (\muV)')   % please check the string property of "text" function for the TeX character sequence table
legend('Ch1','Ch2','Ch3')    % add figure legend

%% open new figure, and plot multiple axis with one signal (單一視窗多圖軸單一訊號)
figure,
subplot(3,1,1),plot(MAX80_TEST(:,1))
ylabel('Ｃh1 (\muV)')   % please check the string property of "text" function for the TeX character sequence table

subplot(3,1,2),plot(MAX80_TEST(:,2))
ylabel('Ch2 (\muV)')   % please check the string property of "text" function for the TeX character sequence table

subplot(3,1,3),plot(MAX80_TEST(:,3))
xlabel('Data points')
ylabel('Ch3 (\muV)')   % please check the string property of "text" function for the TeX character sequence table



