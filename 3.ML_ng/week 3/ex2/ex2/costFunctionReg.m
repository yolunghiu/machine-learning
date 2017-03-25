function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta


% compute Cost(h(x),y)
cost=0;
for iter=1:m
    if y(iter)==1
        cost = cost - log(sigmoid(X(iter,:)*theta));
    elseif y(iter)==0
        cost = cost - log(1-sigmoid(X(iter,:)*theta));
    end
end
cost = cost/m;

% compute the regularizing part,exclude theta(1)
regular = (lambda/(2*m)) * (theta'*theta - theta(1)^2);

% function J(theta)
J = cost + regular;

% compute gradient
for j=1:size(grad,1)
    sum = 0;
    for i=1:m
        sum = sum + ...
              (sigmoid(X(i,:)*theta) - y(i)) * X(i,j);
    end
    
    % theta(1) should not be regularized     
    if j==1
        grad(j)= sum/m;
    else
        grad(j) = sum/m + lambda/m*theta(j);
    end
end



% =============================================================

end
