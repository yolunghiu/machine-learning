# Assignment2 notes

## Python broadcasting

- 这个机制是按行进行广播的

## 模型初始化的问题

	```
		self.params['b1'] = np.zeros((1, hidden_dim))
		self.params['b2'] = np.zeros((1, num_classes))
		self.params['W1'] = weight_scale * np.random.randn(input_dim, hidden_dim)
		self.params['W2'] = weight_scale * np.random.randn(hidden_dim, num_classes)
	```
- 这里的bias被初始化成1行c列的行向量原因如下：
	1. `score = [X(m*n) * W(n*c)] + b`,这里的b是指每一个分类器c都有一个bias，所以是将b加到每个样本的c个分类器上去
	2. `db = np.sum(dscore, axis=0, keepdims=True)`,score是`m*c`的矩阵，求和之后，db是`1*c`的矩阵

## layers.py -> softmax_loss、svm_loss的说明

- 这里的返回值除了loss之外，还有个dx，这里的dx不同于之前softmax分类器或svm分类器的dx，那里直接去的是dloss/dw,而这里的dx指的是dloss/dscore，为的是进行反向传播，下一步计算的是dscore/(dw,dx,db)
