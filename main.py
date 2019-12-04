from bs4 import BeautifulSoup
import ast 
import requests
url = "https://kingcounty.gov/depts/elections/results/2019/201911.aspx"
text = requests.get (url).text
soup = BeautifulSoup(text)
row = soup.find("div", id={"by-the-numbers"}).div.table.tbody
rv1 = row.tr.td.find_next("td")
br1= row.tr.find_next("tr").td.find_next("td")
bmail = br1.parent.find_next("tr").td.find_next("td")
drpbx = bmail.parent.find_next("tr").td.find_next("td")
emlfx = drpbx.parent.find_next("tr").td.find_next("td")
vpct1 = emlfx. parent.find_next("tr").td.find_next("tr").td.find_next("td")

url = "https://results.vote.wa.gov/results/20191105/turnout.html"
text = requests.get(url).text
soup = BeautifulSoup(text)
row = soup.find("div", id = "ResultsContent").find("table").find("a", href = "king").parent
rv2 = row.find_next("td")
br2= rv2.find_next("td")
vpct2 = br2.find_next("td")

print("KC -  Registered: ", rv1.string)
print("St(kc)Registered: ", rv2.string)
print("KC -  Ballots:", br1.string)
print("St(kc)Ballots:", br2.string)
print("KC - Participation", vpct1.string)
print("St(c)Participation", vpct2.string)

print("Registered difference:", int (rv1.string..replace(',','')) - int (rv2.string.replace(',','')))
print("Ballots difference:", int (br1.string..replace(',','')) - int (br2.string.replace(',','')))
print("Participation difference:", float (vpct1.string..replace('%', '')) - float(vpct2.string.replace('%','')))

#x = soup.find(id="total-mileage")
#print(x.span.contents[0])

