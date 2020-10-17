# filename : hello.py

class Hello(object) :
	def __init__(self) :
		self.string = "Hello World!"

	def __str__(self) :
		return "{}: ({})".format(self.__class__.__name__, self.string)

	def show_string(self) :
		print(self.string)

def test() :
	tmp_list = list()
	for i in range(0, 16) :
		tmp_list.append((i, i * i))
	print(tmp_list)

def main() :
	print ("Hello World!")
	test()

	print("This is the test of class Hello: ")

	tmp = Hello()
	print(tmp)
	tmp.show_string()

if __name__ == "__main__" :
	main()
