import chardet

sb = "11431 10638 31350 10550 20532 21252 20940 11438 20431 30937 " \
    "30449 11431 10638 21035 21941 " \
    "20429 10638 30532 30533 " \
    "11131 20936 20532 20532 20341 31433 31136 12034 20545 20546 " \
    "11431 21131 31633 20532".split()
sh = "0x2ca7 0x298e 0x7a76 0x2936 0x5034 0x5304 0x51cc 0x2cae 0x4fcf 0x78d9 0x76f1 0x2ca7 0x298e 0x522b 0x55b5 0x4fcd " \
     "0x298e 0x7744 0x7745 0x2b7b 0x51c8 0x5034 0x5034 0x4f75 0x7ac9 0x79a0 0x2f02 0x5041 0x5042 0x2ca7 0x528b 0x7b91 " \
     "0x5034".replace("0x", "\\u").split()

# print(b"87D6".decode("GBK"))
print(max(sb))
# 究倴匄凌俏磙盱
# for i in sb:
#     h_t = hex(int(i))
#     h_t = "\\u" + h_t[2:]
#     h_st = h_t.encode('utf-8')
#     h_st = h_st.decode("GBk")
#     print(h_st, end=" ")


# for i in sh:
#     print(i)
#     a = chardet.detect(b"0x2ca7")
#     print(a)
# print(chardet.detect(b"0x2ca7"))
# print(b"2ca7".decode("ISO-8859-1"))
# print(chardet.detect(b"\345"))
# print(b"\345".decode("ascii"))

# test = 11431
# h_t = hex(test)
# h_t = "\\u" + h_t[2:]
# h_st = h_t.encode('utf-8')
# h_st = h_st.decode("unicode_escape")
# print(h_st)

