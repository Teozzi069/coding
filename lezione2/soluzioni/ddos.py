import requests
target=input()
while True:
    r=rquests.get(target)
    print(r.status_code)