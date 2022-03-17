'''methods prog'''
def shoose(com,com1,com2,com3,com4,command,txt_m,n_p):
    import com_q1
    b=0
    if command in com:
                if (command in com1) and k>=1:
                    b=1
                elif (command in com2) and k>=2:
                    print(txt_m[5])
                    log_info=(str(input()))
                    if log_info in info:
                        inf=info[log_info].split('*/n*')
                    for o in inf:
                        print(o)
                    else:
                        print(txt_m[6])
                elif (command in com3) and k>=3:
                    x=0
                    while x!=(len(l_p)):
                        print(txt_m[0])
                        l1=(str(input()))
                        p1=(str(input()))
                        if '*' in l1 or '*' in p1:
                            print(txt_m[8])
                            break
                        for h in l_p:
                            l_and_p=h.split('/*/')
                            if l_and_p[0]==l1:
                            print(txt_m[7])
                        else:
                            x+=1
                    new_lp=l1+'/*/'+p1
                    l_p[new_lp]=1
                    print(l_p)
                elif (command in com4) and k==4:
                    print(txt_m[9],n_p)
                else:
                    print(txt_m[4])
    else:
        print(txt_m[3])

