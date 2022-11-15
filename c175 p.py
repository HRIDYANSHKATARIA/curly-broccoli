import matplotlib.pyplot as plt
import psutil as p

app_name_list = []
app_percentage_list = []
app_name_dict = []


keymax = max(app_name_dict,key=app_name_dict.get)
keymin = min(app_name_dict,key=app_name_dict.get)

name_list = [keymax,keymin]

app=app_name_dict.values()
max_app = max(app)
min_app = min(app)

count = 0

for process in p.process_iter():
    count=count+1
    if count <= 6:
        name=process.name()
        cpu_usage=p.cpu_percent()
        print("Name: ",name,"--  CPU_usage",cpu_usage)
        app_name_list.append(name)
        app_percentage_list.append(name)
        
app_name_dict.update({name:cpu_usage})
plt.figure(figsize=(15,7))
plt.xlabel("Application")
plt.ylabel("CPU Usage")

plt.bar(app_name_list,app_percentage_list,width=0.6,color=("yellow","blue","orange","green","purple","pink"))#bargraph

plt.show()