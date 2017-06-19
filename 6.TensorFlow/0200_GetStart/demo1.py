import tensorflow as tf

# define two constants(tensors)
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
print(node1, node2)
print('\n')

# create a session
session = tf.Session()
print(session.run([node1, node2]))
print('\n')

# combine tensors
node3 = tf.add(node1, node2)
print("node3: ", node3)
print("sess.run(node3): ",session.run(node3))
print('\n')

# use placeholder
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b  # + provides a shortcut for tf.add(a, b)
print(session.run(adder_node, {a: 3, b:4.5}))
print(session.run(adder_node, {a: [1,3], b: [2, 4]}))
print('\n')

# more complex computation
add_and_triple = adder_node * 3.
print(session.run(add_and_triple, {a: 3, b:4.5}))