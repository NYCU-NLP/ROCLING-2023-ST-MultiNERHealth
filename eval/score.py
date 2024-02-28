from os import listdir
from os import path
def score_sep(data_path):
    data=open(data_path,'r',encoding='utf-8')
    n=1
    for i in data.readlines():
        i=i.strip()
        
        if n == 3:
            ori_sore=i
            i=i.replace('  ',' ')
            score=i.split(' ')
            
            print(score)
        n+=1
    data.close()
    return score,ori_sore


for file in listdir('Score/'):
    if 'WA' in file:
        file_path=path.join('Score/',file)
        wiki,ori_wiki=score_sep(file_path)
    elif 'SM' in file:
        file_path=path.join('Score/',file)
        social,ori_social=score_sep(file_path)
    elif 'FT' in file:
        file_path=path.join('Score/',file)
        formal,ori_formal=score_sep(file_path)

score_list=[]
for k in range(1,8,2):
    a=float(social[k].replace('%;',''))+float(formal[k].replace('%;',''))+float(wiki[k].replace('%;',''))
    score=a/3
    score_list.append(score)

f=open('Score/Overall_Score.txt','a',encoding='utf-8')
print('FT:  ',ori_formal,file=f)
print('SM:  ',ori_social,file=f)
print('WA:  ',ori_wiki,file=f)
print('macro-F1:    accuracy:  {:.2f}%; precision:  {:.2f}%; recall:  {:.2f}%; FB1:  {:.2f}'.format(float(score_list[0]),float(score_list[1]),float(score_list[2]),float(score_list[3])),file=f)
print('\n',file=f)
f.close()    
