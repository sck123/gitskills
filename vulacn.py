print "Hello World !"
a 10,
b 5,
print a,
def text_create():
    path='j/data/learn/git/python/'
    for text_name in name(1,10):
        #1-10的范围需要用到range函数
        with open (path + str(text_name) + '.txt', 'w') as text:
            text.write(str(txtx_name))
            text.close()
            print('done')
            text_create()
