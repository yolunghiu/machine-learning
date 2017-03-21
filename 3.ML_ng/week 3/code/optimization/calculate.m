options = optimset('GradObj', 'on', 'MaxIter', 100);
initTheta = zeros(2,1);
[optTheta, functionVal, exitFlag] = fminunc(@costFunction, initTheta, options);