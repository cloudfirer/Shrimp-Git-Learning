keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
# zip(keys, values) 会把 keys 和 values 这两个列表 “压缩” 到一起，形成由元组构成的迭代器。
# dict 接收可迭代对象，进而创建字典；取第一个元素为键，第二个元素为值
dictionary = dict(zip(keys, values))
print(dictionary)

print("Part 1")
print("Part 2")
print("Part 3")