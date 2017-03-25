function p = predictOneVsAll(all_theta, X)
%PREDICT Predict the label for a trained one-vs-all classifier. The labels 
%are in the range 1..K, where K = size(all_theta, 1). 
%  p = PREDICTONEVSALL(all_theta, X) will return a vector of predictions
%  for each example in the matrix X. Note that X contains the examples in
%  rows. all_theta is a matrix where the i-th row is a trained logistic
%  regression theta vector for the i-th class. You should set p to a vector
%  of values from 1..K (e.g., p = [1; 3; 1; 2] predicts classes 1, 3, 1, 2
%  for 4 examples) 

m = size(X, 1);
num_labels = size(all_theta, 1);

% You need to return the following variables correctly 
p = zeros(size(X, 1), 1);

% Add ones to the X data matrix
X = [ones(m, 1) X];

% ====================== YOUR CODE HERE ======================
% Instructions: Complete the following code to make predictions using
%               your learned logistic regression parameters (one-vs-all).
%               You should set p to a vector of predictions (from 1 to
%               num_labels).
%
% Hint: This code can be done all vectorized using the max function.
%       In particular, the max function can also return the index of the 
%       max element, for more information see 'help max'. If your examples 
%       are in rows, then, you can use max(A, [], 2) to obtain the max 
%       for each row.
%       

% 棣栧厛鐢ㄦ墍鏈夌殑theta璁＄畻鍑烘瘡涓涓垎绫诲櫒鐨勯娴嬬粨鏋
result = sigmoid(X*all_theta');
% 鐒跺悗鎵惧嚭鎵鏈夊垎绫诲櫒棰勬祴缁撴灉鏈澶у肩殑绱㈠紩
[~,I] = max(result,[],2);
% 绱㈠紩鍑1,寰楀埌鐨勬槸0�?
% I = I-1;
% zeroIndex = I==0;
% 鎷垮埌缁撴灉�?鐨勭储寮曪紝骞跺皢杩欎簺鍏冪礌鏇挎崲�?0锛坹涓殑缁撴灉�?0�?zeroIndex = find(I==0)
% I(zeroIndex) = 10;

p = I;





% =========================================================================


end
