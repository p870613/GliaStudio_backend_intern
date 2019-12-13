#input
urls = [
       "http://www.google.com/a.txt",
       "http://www.google.com.tw/a.txt",
       "http://www.google.com/download/c.jpg",
       "http://www.google.co.jp/a.txt",
       "http://www.google.com/b.txt",
       "https://facebook.com/movie/b.txt",
       "http://yahoo.com/123/000/c.jpg",
       "http://gliacloud.com/haha.png",
]

tmp_data = []
#get filenames
for item in urls:
       tmp = item.split('/')
       tmp_data.append(tmp[len(tmp)-1])

#去重  
data = list(set(tmp_data))
ans = []

#count
for item in data:
       ans.append(tmp_data.count(item))

#sort
for i in range(len(ans)):
       for j in range(len(ans)):
              if(ans[i] > ans[j]):
                     tmp_1 = ans[i]
                     ans[i] = ans[j]
                     ans[j] = tmp_1
                     tmp_2 = data[i]
                     data[i] = data[j]
                     data[j] = tmp_2


for i in range(3):
       print(data[i], ans[i])
