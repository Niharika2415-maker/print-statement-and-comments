studentdata= {'id1':{'name':['Niharika'],'class':['V'],'subject':['math,AI,english']},'id2':{'name':['Nithvika'],'class':['I'],'subject':['hindi,computer science,evs']},'id3':{'name':['Niharika'],'class':['V'],'subject':['math,AI,english']},'id4':{'name':['Niharika'],'class':['V'],'subject':['math,AI,english']},}
result={}
for key, value in studentdata.items():
    if value not in result.values():
        result[key]=value
print(result)
