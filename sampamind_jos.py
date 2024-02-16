
import  requests
from bs4 import  BeautifulSoup
job_list = []

responce = requests.get('https://www.sampamind.com/jobs')
soup = BeautifulSoup(responce.text,'html.parser')

# print (responce.status_code)

jobs  =  soup.find_all('a', class_='text-decoration-none')

for job in jobs:
    title = job.find('h3',class_="text-secondary mt0 mb4").text.strip()
    link = 'https://www.sampamind.com'+job.get('href')
    city = 'Bucuresti'
    job_type  = 'On_site'
    job_list.append({
            "job_title": title,
            "job_link": link,
            "company": "Sampamind",
            "country": "Romania",
            "city": city,
            "remote": job_type
        })

print(job_list)





