from django.shortcuts import render,redirect
import bs4
import requests
import re
from googlesearch import search


def index(request):
	if request.method == "GET":
		return render(request,"index.html")
	else:
		try:
			query = request.POST.get("query")
			final = []
			links = []
			for j in search(query, tld="co.in", num=10, stop=10, pause=2):
				links.append(j)
			ls = image_src(links[:4])
			for i in range(4):
				final.append((links[i],ls[i]))

			return render(request,"result.html",{
				"final":final,
				"query":query,
				})
		except:
			msg = "SOME ERROR OCCURED 404"
			return render(request,"error.html",{"msg":msg})


def image_src(link_list):
	ls = []
	for i in link_list:
		url = requests.get(i)
		soup = bs4.BeautifulSoup(url.text,"html.parser")
		try:
			srcs = [img['src'] for img in soup.find_all('img')][0]
		except:
			srcs = "static/results/img/protect.png"
		ls.append(srcs)
	return ls


