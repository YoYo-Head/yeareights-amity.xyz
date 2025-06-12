from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']


def scrapeTimetable():
    driver = webdriver.Chrome()
    driver.get('https://sb.amity.nsw.edu.au/login/')

    # time.sleep(2)

    # driver.find_element(By.CSS_SELECTOR, "div.samlbutton").click()

    time.sleep(15)

    driver.get('https://sb.amity.nsw.edu.au/timetable')

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    cells = soup.find_all('table', class_="timetable no-hover")

     # Find all timetable rows (periods)
    periods = soup.select('table.timetable tbody tr')
    
    print(f"\nFound {len(periods)} periods in timetable\n")

    with open('timetable.txt', 'w', encoding='utf-8') as t:
        t.write('New timetable upload!')
        for i in range(2):
            t.write('\n')

    
    for period in periods:
        # Get period name and time
        period_header = period.select_one('th')
        if not period_header:
            continue
            
        period_name = period_header.contents[0].strip()
        period_time_tag = period_header.select_one('time.meta')
        period_time = period_time_tag.get_text(strip=True) if period_time_tag else "No time specified"


        title = f"\n=== {period_name} ({period_time}) ==="
        
        print(title)
        
        # Get all cells for this period (days of week)
        day_cells = period.select('td')


        with open('timetable.txt', 'a', encoding='utf-8') as t:
            t.write(title)
            t.write('\n')
        
        for i, cell in enumerate(day_cells):
            days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
            # Find subject information
            subject_div = cell.select_one('div.timetable-subject')

            if i <= 4:
               Week = 'A'
               Day = days[i]
            elif i >= 5:
                Week = 'B'
                Day = days[i - 5]
            else:
                Week = 'Unknown'
                Day = f'Day {i + 1}'

        
                
            # Extract subject details
            subject_name = subject_div.a.get_text(strip=True) if subject_div.a else "No subject name"
            div = subject_div.div.get_text(strip=True).split('\n')[0]
            class_nameHANDLE = re.search(r'\((.*?)\)', div)
            class_name = class_nameHANDLE.group(1) if class_nameHANDLE else "No code"
            room_numANDteacher_info = re.sub(r'\(.*?\)', '', div).strip()
            room_num = room_numANDteacher_info[:4]
            teacher_info = room_numANDteacher_info[5:]

            peHead = f"Week {Week} - {Day}: {subject_name} ({class_name}) - {room_num} {teacher_info}"
            
            print(peHead)

            with open('timetable.txt', 'a', encoding='utf-8') as t:
                t.write(peHead)
                t.write('\n')

if __name__ == '__main__':
    print('Now scraping the Timetable!')
    scrapeTimetable()




