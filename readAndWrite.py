text = '\tThis is my first test.\n\tThis is next line.\n\tThis is last line.'
print(text)

my_file = open('./Data/my file.txt', 'w')
my_file.write(text)
my_file.close()

append_text = '\nThis is appended file.'
my_file = open('./Data/my file.txt', 'a')   # 'a'=append 以增加内容的形式打开
my_file.write(append_text)
my_file.close()

file = open('./Data/my file.txt', 'r')
content = file.readlines()
print(content)

second_read_time = file.readline()
print(second_read_time)

for item in content:
    print(item)