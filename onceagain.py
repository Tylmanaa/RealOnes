services = [
    "nginx:OK",
    "postgres:ERROR",
    "redis:OK",
    "backend:ERROR",
    "grafana:OK"
]
slovar={}
clear_service=[]
for i in services:
    s = i.split(":")
    clear_service.append(s)

for t in clear_service:
    slovar[t[0]]=t[1]
    #print(slovar)

print(slovar)

schetka=0
bad_service=[]

for h in slovar:
    if slovar[h] == 'ERROR':
        schetka+=1
        bad_service.append([h,slovar[h]])
print('Плохо себя чувствуют ==',bad_service, 'таких серверов ща ==',schetka)