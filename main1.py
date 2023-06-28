from bs4 import BeautifulSoup
import requests

start = True


def find_jobs():
    html_text = requests.get(
        'https://m.timesjobs.com/mobile/jobs-search-result.html?txtKeywords=python&txtLocation=&cboWorkExp1=-1').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_="srp-job-bx")
    for job in jobs:
        company_name = job.find('h4').text
        skills = job.find('div', class_="srp-keyskills").text.replace(' ', '')
        more_info = job.find('h3').a['href']
        with open('posts.txt', 'a') as f:
            f.write(f'company name: {company_name.strip()}\n')
            f.write(f'required skills: {skills.strip()}\n')
            f.write(f'more info: {more_info}\n')
            f.write("\n")
        print(f'File saved: {company_name.strip()}')
    global start
    start = False


if __name__ == "__main__":
    while start:
        find_jobs()
