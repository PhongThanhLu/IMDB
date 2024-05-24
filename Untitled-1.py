import requests_with_caching
import json
def get_movies_from_tastedive(string):
    new_dict = {}
    new_dict['q'] = string
    new_dict['type'] = 'movies'
    new_dict['limit'] = 5

    new_url = requests_with_caching.get('https://tastedive.com/api', params = new_dict)
    dic= json.loads(new_url.text)
    return dic

def get_movies_from_tastedive(string):
    new_dict = {}
    new_dict['q'] = string
    new_dict['type'] = 'movies'
    new_dict['limit'] = 5

    new_url = requests_with_caching.get('https://tastedive.com/api', params = new_dict)
    dic= json.loads(new_url.text)
    return dic

def extract_movie_titles(dic):
    new_list = []
    for num1 in dic:
        for num2 in dic[num1]:
            for num3 in dic[num1][num2]:
                new_list.append((num3['Name']))                       
    off_list = new_list[1:]
    return list(off_list)

def get_related_titles(list_movie):
    new_list1=[]
    for i in list_movie:
        new_titles = extract_movie_titles(get_movies_from_tastedive(i))
        new_list1 = new_list1 + new_titles
        new_one = set(new_list1)
        new_list1 = list(new_one)
    return new_list1
    
    
def get_movie_data(one):
    baseurl = 'http://www.omdbapi.com/'
    dic = {}
    dic['t'] = one
    dic['r'] = 'json'
    new_one = requests_with_caching.get(baseurl, params = dic)
    new_new =json.loads(new_one.text)
    return new_new
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages

# get_movie_rating(get_movie_data("Deadpool 2"))
def get_movie_rating(new_new):
    if 'Ratings' in new_new and len(new_new['Ratings']) > 1:
        if new_new['Ratings'][1]['Source'] == 'Rotten Tomatoes':
            return int(new_new['Ratings'][1]['Value'][0:2])
    else:
        return 0
    
    
def get_sorted_recommendations(list_movies):
    phong = get_related_titles(list_movies)
    new_dict3 = {}
    phong1 = []
    for i in phong:
        van = get_movie_rating(get_movie_data(i))
        phong1.append(van)
    for i in range(10):
        new_dict3[phong[i]] = phong1[i]

    cop = sorted(new_dict3.keys(), key=lambda k: (new_dict3[k], k[::-1]), reverse=True)

    return cop
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

