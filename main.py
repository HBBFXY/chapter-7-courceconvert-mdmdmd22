# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字
reserved_words = set(keyword.kwlist)

# 以下内容自行完成
import keyword

# 读取Python保留字列表
python_keywords = keyword.kwlist

# 读取源文件
with open('random_int.py', 'r') as file:
    lines = file.readlines()

# 处理每一行，将非保留字的小写字母转为大写
processed_lines = []
for line in lines:
    words = line.split()
    new_words = []
    for word in words:
        if word in python_keywords:
            new_words.append(word)
        else:
            new_words.append(word.upper())
    processed_line = ' '.join(new_words) + '\n'
    processed_lines.append(processed_line)

# 将处理后的内容保存到新文件
with open('random_int_converted.py', 'w') as file:
    file.writelines(processed_lines)
