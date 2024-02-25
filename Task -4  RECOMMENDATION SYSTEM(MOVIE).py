#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


data = {
    'title': ['Dilwale Dulhania Le Jayenge', 'Sholay', '3 Idiots', 'Lagaan', 'Queen',
              'The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump'],
    'genre': ['Romance', 'Action', 'Comedy', 'Drama', 'Drama',
              'Drama', 'Crime', 'Action', 'Crime', 'Drama'],
    'description': ['Raj and Simran meet during a trip across Europe and the two fall in love. However, Raj must win over Simran\'s family before they can be together.',
                    'A retired police officer enlists the help of two criminals to bring down a notorious bandit.',
                    'Three engineering students deal with societal pressure and the shortcomings of the Indian education system.',
                    'In 1890s India, a village is oppressed by high taxes and drought. A young farmer accepts the challenge to go up against the British.',
                    'A Delhi girl from a traditional family sets out on a solo honeymoon after her marriage is called off.',
                    'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
                    'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
                    'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
                    'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
                    'The presidencies of Kennedy and Johnson, the events of Vietnam, Watergate and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart.']
}

df = pd.DataFrame(data)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])


cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)


def get_recommendations(title, cosine_sim=cosine_sim):
    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices]


title = 'Sholay'
recommendations = get_recommendations(title)
print("Recommended movies for '{}':".format(title))
print(recommendations)


# In[ ]:




