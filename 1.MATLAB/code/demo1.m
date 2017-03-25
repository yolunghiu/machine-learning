%% I. 常用命令

clear all   % 清除Workspace中的所有变量
clc         % 清除Command Window中的所有命令
doc         % 查看文档
who         % 查看所有变量
whos        % 查看所有变量的详细信息c
save hello.mat v    % 将变量v保存到文件中
save hello.txt v -ascii

%% II. MATLAB数据类型

%%
% 1. 数字

2 + 3

%%
% 2. 字符与字符串

s = 'a'
abs(s)
char(65)
num2str(65)

str = 'I Love MATLAB & Machine Learning.'

length(str)

doc num2str

%%
% 3. 矩阵

A = [1 2 3; 4 5 2; 3 2 7]
B = A'
C = A(:)		% 将A转化成一个列向量[1 2 3 4 5 2 3 2 7]'
D = inv(A)
A * D
%%
% 

E = zeros(10,5,3)
E(:,:,1) = rand(10,5)
E(:,:,2) = randi(5, 10,5)
E(:,:,3) = randn(10,5)

%%
% 4. 元胞数组

A = cell(1, 6)
A{2} = eye(3)
A{5} = magic(5)
B = A{5}

%% III. MATLAB矩阵操作

%%
% 1. 矩阵的定义与构造

A = [1 2 3 5 8 5 4 6]
B = 1:2:9
C = repmat(B, 3, 1)
D = ones(2, 4)

%%
% 2. 矩阵的四则运算

A = [1 2 3 4; 5 6 7 8]
B = [1 1 2 2; 2 2 1 1]
C = A + B
D = A - B
E = A * B'
F = A .* B
G = A / B     % B * G = A
H = A ./ B

%%
% 3. 矩阵的下标

A = magic(5)

B = A(2,3)
B([1 3], :)     % 取下标为1或3的行

C = A(3,:)
D = A(:,4)
D(:)            % 将D转换成一个列向量

[m, n] = find(A > 20)


%% VI. MATLAB基本绘图操作

%%
% 0. 绘图
x = (0:0.01:0.98)
y = sin(2*pi*x*8)
plot(x,y)

hold on;            % 在原图像上继续画

y2 = cos(2*pi*x*8)
plot(x,y2,'r')

axis([30, 100, 30, 100])	% 设置横纵坐标的量度

xlabel('time')          % x轴名称
ylabel('value')         % y轴名称
legend('sin','cos')     % 每条曲线的含义
title('my plot')
print -dpng 'myPlot.png'

close                   % 关闭窗口


%%
% 1. 二维平面绘图

x = 0:0.01:2*pi;
y = sin(x);
figure
plot(x, y)
title('y = sin(x)')
xlabel('x')
ylabel('sin(x)')
xlim([0 2*pi])

x = 0:0.01:20;
y1 = 200*exp(-0.05*x).*sin(x);
y2 = 0.8*exp(-0.5*x).*sin(10*x);
figure
[AX,H1,H2] = plotyy(x,y1,x,y2,'plot');
set(get(AX(1),'Ylabel'),'String','Slow Decay')
set(get(AX(2),'Ylabel'),'String','Fast Decay')
xlabel('Time (\musec)')
title('Multiple Decay Rates')
set(H1,'LineStyle','--')
set(H2,'LineStyle',':')

%%
% 2. 三维立体绘图

t = 0:pi/50:10*pi;
plot3(sin(t),cos(t),t)
xlabel('sin(t)')
ylabel('cos(t)')
zlabel('t')
grid on
axis square

%%
% 3. 图形的保存与导出

% (1) Edit → Copy Figure
% (2) Toolbar → Save
% (3) print('-depsc','-tiff','-r300','picture1')
% (4) File → Export Setup

%% VII. MATLAB文件导入

%%
% 1. mat格式

save data.mat x y1 y2
clear all
load data.mat

%%
% 2. txt格式

M = importdata('myfile.txt');

S = M.data;
save 'data.txt' S -ascii
T = load('data.txt');

isequal(S, T)

%%
% 3. xls格式

xlswrite('data.xls',S)
W = xlsread('data.xls');
isequal(S, W)

xlswrite('data.xlsx',S)
U = xlsread('data.xlsx');
isequal(S, U)

%%
% 4. csv格式

csvwrite('data.csv',S)
V = csvread('data.csv');
isequal(S, V)