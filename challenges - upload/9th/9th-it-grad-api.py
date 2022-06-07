import requests
import json

parameters = {
    "q": 'information'
}
r_uni = requests.get("https://data.gov.sg/api/action/datastore_search?resource_id=115bf8a7-46df-466c-b7fc-375ef3c1b425&", params=parameters)
r_poly = requests.get("https://data.gov.sg/api/action/datastore_search?resource_id=f358cf0d-61fa-4eeb-93a2-1eca971cf1a4&", params=parameters)

# University
r_uni = r_uni.json()
uni_cohorts = r_uni['result']['total']
uni_grad = []
x = 0

for x in range(uni_cohorts): # loop through all the cohorts of IT
    if (r_uni['result']['records'][x]['sex'] == 'MF'): # set condition that the sex is MF
        uni_grad.append(r_uni['result']['records'][x]['graduates']) # append the value to a list 
uni_grad = map(int, uni_grad) # convert list to integer

# polytechnic
r_poly = r_poly.json()
poly_cohorts = r_poly['result']['total']
poly_grad = []
y = 0

for y in range(poly_cohorts):
    if (r_poly['result']['records'][y]['sex'] == 'MF'):
        poly_grad.append(r_poly['result']['records'][y]['graduates'])
poly_grad = map(int, poly_grad)

x = sum(uni_grad)
y = sum(poly_grad)
# print("University Graduates: ", x)
# print("Poly Graduates: ", y)
print("Total Graduates: ", x + y)