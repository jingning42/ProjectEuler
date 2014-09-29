# global constant
STRING = '''73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450'''
STR_LEN = 13

# 预处理
string1 = STRING.replace('\n','')
list1 = string1.split('0')   #用0把字符串分段，转为列表
list2 = list(list1)  #复制一份list1



#把list2中，长度小于13的元素删掉
for i in list1:
    if len(i)<13:
        list2.remove(i)


# global variable
mul_list = []


# help function
def help_function(string):
    for i in range(len(string)-STR_LEN+1):
        mul_result = 1
        for j in range(13):
            mul_result *= int(string[i+j])
        mul_list.append(mul_result)       
    return mul_list
#
for string in list2:
    help_function(string)

print (max(mul_list))