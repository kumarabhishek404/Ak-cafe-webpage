import requests
from bs4 import BeautifulSoup
from pprint import pprint

link="https://www.imdb.com/india/top-rated-indian-movies/"
response=requests.get(link)
# print(response.text)

# my_file=open("Task_1.text", "w")
# my_file.write(response.text)
# my_file.close()

my_file1=open("Task_1.text", "r")
file_data=my_file1.read()
my_file1.close()
# print(file_data)

soup=BeautifulSoup(file_data, "html.parser")
# print(soup.prettify)
main_div=soup.find("div", class_="lister")
sub_div=main_div.find("tbody", class_="lister-list")

movie_name_list=[]
movie_year_list=[]
movie_position_list=[]
movie_rating_list=[]
movie_url_list=[]

for tag_tr in sub_div.find_all("tr"):
	tag_td=tag_tr.find("td", class_="titleColumn")
	tag_td1=tag_tr.find("td", class_="ratingColumn imdbRating")
	tag_td2=tag_tr.find("td", class_="posterColumn")
	url=tag_td.a

	#movie name
	movie_name_list.append(str(tag_td.a.text))
	#year of releasing
	movie_year_list.append(int(tag_td.span.text[1:5]))
	#position
	movie_position_list.append(int(tag_td2.span["data-value"]))
	#Rating
	movie_rating_list.append(float(tag_td1.text[1:4]))
	#Link
	half_link="https://www.imdb.com"
	full_link=half_link + url["href"]
	movie_url_list.append(full_link)

# print(movie_name_list)
# print(movie_year_list)
# print(movie_position_list)
# print(movie_rating_list)
# print(movie_url_list)

task_1=[]	
my_dict={'1_Name':'','2_Year':'','3_Position':'','4_Rating':'','5_Url':''}
for i in range(250):
	my_dict['1_Name']=movie_name_list[i]
	my_dict['2_Year']=movie_year_list[i]
	my_dict['3_Position']=movie_position_list[i]
	my_dict['4_Rating']=movie_rating_list[i]
	my_dict['5_Url']=movie_url_list[i]

	task_1.append(my_dict)
pprint(task_1)
