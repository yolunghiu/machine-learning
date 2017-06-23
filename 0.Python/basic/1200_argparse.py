import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	parser.add_argument(
      '--learning_rate',
      type=float,
      default=0.01,
      help='Initial learning rate.'
    )

	parser.add_argument(
      '--batch_size',
      type=int,
      default=100,
      help='Batch size.  Must divide evenly into the dataset sizes.'
    )

	args = parser.parse_args()
	# args = parser.parse_known_args()

	print(args)