function g = sigmoid(z)
%SIGMOID Compute sigmoid function
%   g = SIGMOID(z) computes the sigmoid of z.

% You need to return the following variables correctly 
g = zeros(size(z));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the sigmoid of each value of z (z can be a matrix,
%               vector or scalar).
rows = size(g,1);   % >0
cols = size(g,2);   % >=0

for row=1:rows
    if cols==0
        g(row)=(1+exp(-z(row)))^-1;
    else
        for col=1:cols
            g(row,col)=(1+exp(-z(row,col)))^-1;
        end
    end
end




% =============================================================

end
