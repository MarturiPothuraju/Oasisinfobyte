import requests
import tkinter as tk
def get_weather(area):  
    api_url = "http://api.weatherapi.com/v1/current.json"  
    params = {"key": "4be7f75c58ef49fe8ca152505241008",'q':area,  "days":1     }  
    response = requests.get(api_url, params)  
    data = response.json()  
    return data

def disp_weather():
    try:
        area=area_enter.get()
        data = get_weather(area)
        title="The weather report at "+area
        temp="Tempurature is : "+str(data['current']['temp_c'])
        him="Himidity is : "+str(data['current']['humidity'])
        cond="Weather condition is : "+str(data['current']['condition']['text'])
        str1=title+'\n'+temp+'\n'+him+'\n'+cond
    except:
        str1="location not found"
    message=tk.Message(window,text=str1,justify="left",padx=20,pady=40)
    message.grid(row=2,column=1,)
    

window=tk.Tk()
window.title('weather report')
window.geometry('400x400')
text=tk.Message(window, text='Enter the location:',justify="center",padx=20,pady=40)
area_enter=tk.Entry(window)
print(area_enter)
button=tk.Button(window,text='Get weather report',justify="center",command=disp_weather)
text.grid(row=0,column=0)
area_enter.grid(row=0,column=1)
button.grid(row=1,column=1)
window.mainloop()