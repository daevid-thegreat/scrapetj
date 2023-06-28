from bs4 import BeautifulSoup


with open("index.html", 'r') as html_file:
    soup = BeautifulSoup(html_file, "lxml")
    course_cards = soup.find_all('div', class_="card")
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f"{course_name} costs {course_price}")
