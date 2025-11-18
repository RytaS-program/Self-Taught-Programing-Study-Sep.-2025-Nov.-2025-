#問1
with open("st.txt","r")as f:
    print(f.read())

#問2
answer=input("What is your favorite music?: ")
with open("favorite_music","w") as f:
    f.write(answer)

#問3
import csv

with open("movie.csv","w") as f:
    w=csv.writer(f,delimiter=",")
    w.writerow(["Top Gun","Risky Bussiness","Minority Report"])
    w.writerow(["Titanic","The Revenant","Inception"])
    w.writerow(["Training Day","Man on Fire","Flight"])

import csv

movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)

#問4
import csv

movies = [["トップガン", "リスキービジネス", "マイノリティーレポート"], ["タイタニック", "レベナント", "インセプション"], ["研修時", "火男", "とべ"]]
with open("translated_movies.csv", "w",encoding="utf-8") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)
