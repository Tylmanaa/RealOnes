services = [
    "nginx:OK",
    "postgres:ERROR",
    "redis:OK",
    "backend:ERROR",
    "grafana:OK"
]


def slovar():
    services_dict={}
    errors_numb=0
    erorrs_names=[]
    for line in services:
        #print(line) Разбил на строки
        a=line.split(":") # Сделал дробление по :
        services_dict[a[0]]=a[1]
        
    #print('SLOVAR',services_dict) #сделал словарь где а[0]- ключ, а[1] - значение
    for schet in services_dict:
        if services_dict[schet] == 'ERROR':
            errors_numb+=1
            #print(errors_numb)
            
            
            erorrs_names.append(schet)
        #print(erorrs_names)
    if errors_numb > 0:

        print('Проблема с сервисом',erorrs_names, 'Всего ошибок:',errors_numb)

    else:
        print('Все сервисы работают')
    
    
slovar()
