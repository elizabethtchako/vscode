#Elizabeth Tchako
#07/03/2024
#Learn how to remove prefixes and suffixes from code 

url = 'https://nostarch.com'
print (url.removeprefix('https://')) # print = nostarch.com

print(url) # print = https://nostarch.com
url = url.removeprefix('https://') #make permanent 
print(url) # print = nostarch.com

url='https://google.com'
print(f"{url.removeprefix('https://')}")
print(url)


#you can also make the suffix of something removed
file_name = 'python_notes.txt'
print (file_name) #print = python_notes.txt
file_name = file_name.removesuffix('.txt')
print(file_name) #print = python_notes