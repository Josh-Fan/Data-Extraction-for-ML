def comp_find(stringf1, stringf2):
    return stringf1.find(stringf2)


def comp_line_feature(stringx, featurex):
    '''print(stringx, end='')'''
    comp_line_output = ''
    lenall = len(featurex)
    for i in range(0, lenall):
        '''if len(featurex[i]) == 1:'''
        if type(featurex[i]) is str:
            '''print("@@@@")'''
            if comp_find(stringx, featurex[i]) == -1:
                '''print("0", end=',')'''
                comp_line_output += "0,"
            else:
                '''print("1", end=',')'''
                comp_line_output += "1,"
        else:
            '''print(type(featurex[i]))'''
            setvalue = 1
            for j in range(0, len(featurex[i])):
                if comp_find(stringx, featurex[i][j]) != -1:
                    '''print("1", end=',')'''
                    setvalue *= 0
                    break
                else:
                    '''print("0", end=',')'''
                    setvalue *= 1
            if setvalue == 1:
                comp_line_output += "0,"
            else:
                comp_line_output += "1,"
    return comp_line_output


'''data1 = open('SMSSpamCollection')'''
with open('SMSSpamCollection') as data1:
    data2 = open('output1.txt', 'w')
    data2.truncate(0)
    feature1 = ['free', 'urgent', 'congrat', 'win', 'won', 'offer','award','prize','call',\
                'reply','send','stop','click','sex','girl','cash',\
                ['0p','1p','2p','3p','4p','5p','6p','7p','8p','9p'], 'half price',\
                ['euro','gbp','pound','$'],['text','txt'],'spam']
    while True:
        line = data1.readline()
        if len(line) != 0:
            '''print(line, end='')'''
            data2.write(str(comp_line_feature(line.lower(), feature1)+'\n'))
            '''print('\n')'''
        else:
            break
    data2.close()
'''data1.close'''


'''# 功能：1处理line,初始化line小写，搜索字符，字符对比20个，有就在相应位置返回'''





