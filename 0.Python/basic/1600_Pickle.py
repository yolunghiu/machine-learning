import pickle

lines = {
	"hello, world",
	"how are you?",
	"haha"
}
print(lines)

# 将对象序列化
with open('lines.pkl', 'wb') as f:
	pickle.dump(lines, f)

# 读取序列化的对象
# with open('lines.pkl', 'rb') as f:
# 	lines_back = pickle.load(f)
# print(lines_back)