"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # ----- Write your code below this line ----- #
        text = soup.find_all('div', {'class': 'fw6 m-pt2 fs3 ta-c'})
        tex2 = soup.find_all('table', {'class': 't-stripe'})
        list8 = []
        # list : 5 digits as a rank => to fetch top 200 ranks, should get 5*200 = 1000 digits
        for tag in tex2:
            # print(tag.text)
            list8 += tag.text.strip().split()
        # use n to find the start one of the info(rank) that we need.
        n = 0
        for i in range(len(list8)):
            word = list8[i]
            if word.isdigit():
                # find the start one of the info(rank).
                n = i
                break
        # list8 index from n to 999+n is about top rank 200.
        catch_main_content = list8[n:999+n+1]
        # print(catch_main_content)
        # catch_main_content list : The count of male starts from index, 2. // The count of female starts from index,4
        # The next count of female or male  will at the new index(Previous index plus 5)
        female_num = 0
        male_num = 0
        # male
        for j in range(2, len(catch_main_content), 5):
            # str// count
            count = catch_main_content[j]
            count2 = ''
            # remove the ',' among the count
            for k in range(len(count)):
                if count[k].isdigit() is True:
                    count2 += count[k]
            male_num += int(count2)
        # Female
        for f in range(4, len(catch_main_content), 5):
            # str// count
            count = catch_main_content[f]
            count2 = ''
            # remove the ',' among the count
            for k in range(len(count)):
                if count[k].isdigit() is True:
                    count2 += count[k]
            female_num += int(count2)
        print('Male Number: ' + str(male_num))
        print('Female Number: ' + str(female_num))



if __name__ == '__main__':
    main()
