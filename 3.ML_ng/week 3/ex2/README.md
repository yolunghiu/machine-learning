# ex2

## 将作业中以后可能有用的信息记录于此

- Before starting to implement any learning algorithm, it is always good to
visualize the data if possible
- plotData.m
画出数据
- sigmoid.m
实现sigmoid函数
- costFunction.m
实现计算Logistic Regression代价函数和梯度的方法；这里的计算用的是for循环的方式，在这里也只能用这种方式，但是在ex1的costFunction计算中，既可以用for循环，又可以将表达式转换成矩阵运算的形式并行计算来加快速度。
- Notice that by using fminunc, you did not have to write any loops
yourself, or set a learning rate like you did for gradient descent. This is all
done by fminunc: you only needed to provide a function calculating the cost
and the gradient.
- plotDecisionBoundary.m
画出DecisionBoundary
- mapFeature.m
根据一维特征生成更复杂的特征
- costFunctionReg.m
计算标准化的J(theta)、gradient