import pandas as pd
import googletrans
from googletrans import Translator

translator = Translator()
crickerter_data = pd.read_csv("E:\Flask_Apps\web app\corpus\crickerters.csv" , encoding = 'unicode_escape')

print(crickerter_data.head())
age_list = crickerter_data.Age.tolist()
translated_age_list = []
for age in age_list:
    single_age_list = age.strip().split(" ")
    print(single_age_list)
    year = single_age_list[0]
    days = single_age_list[1]
    year = "අවු. "+ year[0:2]
    d_index = days.index('d')
    days = "දවස්. " + days[0:d_index]
    translated_age = year+" "+ days
    translated_age_list.append(translated_age)

#crickerter_data["Age"] = translated_age_list
#print(crickerter_data["Age"])

#translated = translator.translate("Dandeniyage", dest='sinhala').text
#print(translated)
cols_to_trans = ['Full Name','Born','Batting Style', 'Bowling Style','Carrer']
df = pd.DataFrame(columns = cols_to_trans)
for col in cols_to_trans:
    temp = []
    print(col)
    for i in crickerter_data[col]:
        #print(i)
        translated = translator.translate(i, dest='sinhala').text
        while(1):
            if(i == translated):
                print(i, translated)
                translated = translator.translate(i, dest='sinhala').text
                print("translated again")
                print(i, translated)
            else:
                break
        temp.append(translated)
    df[col] = temp
df['Age'] = translated_age_list
print(df.head())
file_name = 'crickerters_sinhala_2.csv'
df.to_csv(file_name, encoding='utf-8' , index=False)

sinhala_data = pd.read_csv("crickerters_sinhala_2.csv")
print(sinhala_data.head())


