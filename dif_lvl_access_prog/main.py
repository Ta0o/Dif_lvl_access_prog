'''main prog'''
import commands_q1
while True:
    print(txt_m[0])
    login=(str(input()))
    password=(str(input()))
    #Введение логина и пароля
    lp=login+'/*/'+password
    #Поиск этих входных данных в списке с логинами и паролями пользователей
    if lp in l_p:
        k=l_p[lp]
        print(txt_m[1])
        print('Ваш уровень доступа:',k)
        #Пользователь уже зашёл в систему и знает свой уровень доступа
        while True:
            print(txt_m[10])
            command=(str(input()))
            commands_q1.shoose(com,com1,com2,com3,com4,command,txt_m,n_p)
            #Выполнение команд
            if b==1:
                break
    else:
        print(txt_m[2])
        n_p+=1
