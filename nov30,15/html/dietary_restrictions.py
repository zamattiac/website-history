# Matthew Keitelman (mak2vr)
import urllib.request

stream = urllib.request.urlopen('https://docs.google.com/spreadsheets/d/1MlCKBfwv4-q8Oa-3sEa8jFSUqTzZG2Z5Z8CLhSx0t38/pub?gid=2129789108&single=true&output=tsv')

output = open('dietary_output.html','w')

restrictions = {'vegan':0,'kosher':0,'halal':0,'lactose':0,'pescatarian':0,'allergy':0,'vegetarian':0}

allergies = {}
allergy_times = []
times = []
count = 0
lines = []

for line in stream:
    decoded = line.decode('UTF-8')
    lines.append(decoded)

for line in lines:
    if lines.index(line) > 0:
        count += 1

        restriction = line.lower().strip('"').split('\t')[1]
        times.append(line.lower().strip('"').split('\t')[0])

        for key in restrictions:
            if key in restriction:

                restrictions[key] += 1

        if 'allerg' in restriction:

            allergy_times.append(line.lower().strip('"').split('\t')[0])
            specific_allergy = ''
            words = restriction
            words = words.split()
            for word in words:

                if 'allerg' not in word:
                    specific_allergy += word.strip('"') + ' '


            if specific_allergy in allergies:
                allergies[specific_allergy] += 1
            else:
                allergies[specific_allergy] = 1

output.write("<title>Restrictions results</title><h2>Results</h2>")
output.write((str(count)+" responses counted out of 322 subscribers<br><br>\n\n"))
for key in restrictions:
    output.write((str(restrictions[key])+' w/ restriction: <font color=#0000FF>'+str(key)+'</font><br><br>\n'))
output.write('\n Allergies:<br><br>\n\n')
for key in allergies:
    output.write((str(allergies[key])+' ' + key+'allergies<br>\n'))

print("Recorded count, restrictions, and allergies")

cont = input('\nmore/done: ')
if cont == 'more':
    print("\nSubmission times recorded")
    output.write("\n<br>Submission times: <br>\n")
    for time in times:
        output.write((time + '<br>\n'))
    output.write("\n<br>Allergy submission times: <br>\n\n")
    for time in allergy_times:
        output.write((time+'<br>\n'))

elif cont == 'done':
    stream.close()
    output.close()