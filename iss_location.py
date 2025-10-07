import requests

atbilde = requests.get(url="http://api.open-notify.org/iss-now.json")

# if atbilde.status_code != 200:
#     raise Exception("Nav derīgas atbildes no API.")

atbilde.raise_for_status()

dati = atbilde.json()["iss_position"]
platums = dati["latitude"]
garums = dati["longitude"]
print(platums,garums)