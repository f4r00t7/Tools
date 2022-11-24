from urllib.request import urlopen
import sys

try:
    #Pegando ip 
    ip = sys.argv[1]

    if ip:
        url = f"http://ip-api.com/json/{ip}"

        #iniciando o request
        request = urlopen(url)
        data = request.read().decode()

        #convertendo string api, para DICT (dicionário)
        data = eval(data)

        for i in data:
            print(f"{i} == {data[i]}")

except Exception as ex:
    print(f"error: {ex}")
