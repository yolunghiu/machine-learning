with open('name_age.txt', 'r') as f:
	lines = f.readlines()
	for line in lines:
		name, age = line.rstrip().split(',')
		print('{} is {} years old.'.format(name, age))