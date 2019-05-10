import requests, json, os.path
from os import path
exists = path.exists("/home/yogendra/Desktop/RequestsAPI/file.json")
if exists:
    with open("file.json") as f:
        k = json.load(f)
else:
    a = requests.get("http://saral.navgurukul.org/api/courses")
    b = a.text # json format
    with open("file.json", "w") as f:
        f.write(b)
    k = json.loads(b)
l = k["availableCourses"]
def headings():
    for i in range(len(l)):
        print (str(i)+". "+l[i]["name"]) #course-headings
    print ""
    exercises()

def exercises():
    user = input("enter an input: ")
    for i in range(len(l)):
        if user == i:
            value_store = l[i]["name"] # full list
            print (str(l[i]["id"]) +" your heading is " + value_store + "\n") #particular id with course-heading
            # print ("The website is " + "http://saral.navgurukul.org/api/courses/" + str(l[i]["id"]) + "/exercises")
            var = requests.get("http://saral.navgurukul.org/api/courses/" + str(l[i]["id"]) + "/exercises")
            x = var.text
            y = json.loads(x) # iske andar data hai saara `dict`
            z = y["data"]
    for j in range(len(z)):
        print ("          "+str(j)+". "+z[j]["name"] + "\n")
    #here outside-loop, the value of `j` is maximum
    user2 = input("enter another input: ")
    print ""
    for i in range(len(z)):
        if user2 <= j: # to check if input given is wrong. Here `j` has its maximum value
            if user2 == i:
                new_var = requests.get("http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug="+str(z[i]["slug"]))
                # print "http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug="+str(z[i]["slug"])
                access = new_var.text
                print access + "\n"
                while True:
                    agla_input = raw_input("enter an input(`p` for previous slug or `n` for next slug or `up` for main-menu or `e` to exit): ")
                    if agla_input == "p":
                        i = i-1
                        if i < 0:
                            print "your index was out of range:(\n"
                            headings()
                        new_var = requests.get("http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug="+str(z[i]["slug"]))
                        print new_var.text
                        continue
                    elif agla_input == "n":
                        i = i+1
                        if i > j:
                            print "your index was out of range:(\n"
                            headings()
                        new_var = requests.get("http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug="+str(z[i]["slug"]))
                        print new_var.text
                        continue
                    elif agla_input == "up":
                        headings()
                    elif agla_input == "e":
                        print "thanks for playing :D"
                        break
                    else:
                        print "you entered a wrong input"
                        break
        else:
            print "you've given an invalid input\nPlease try again:)\n"
            headings()
headings() # calling the headings function
