import os
import base64
def decodeIMG(base,path):
    imgdata = base64.b64decode(base)
    filename = path + "/avatar.png"
    with open(filename, "wb") as f:
        f.write(imgdata)

def fill(data,media_path=None):
    if media_path == None:
        full_path = os.path.realpath(__file__)
        path, filename = os.path.split(full_path)
        media_path = path

    name, profile, email,birthdate, phone, homepage, facebook, linkedin, github, image = tuple("" for i in range(10))
    email1, birthdate1, phone1, homepage1, facebook1, linkedin1, github1, image1 = tuple("" for i in range(8))

    Arr = []
    Brr = []
    for _key, _val in data["profile"].items():
        if _key == "fullname"and _val != "":
            name = "\\nametag{}{"+  str(_val) + "}\n"
        if _key == "birth" and _val != "":
            birthdate += "{ " + str(_val) + "}&\\faCalendar"
            birthdate1 += "\\faCalendar & { " + str(_val) + "}"
            Arr.append(birthdate)
            Brr.append(birthdate1)
        if _key == "phone" and _val != "":
            phone += "{ " + str(_val) + "}&\\faPhone"
            phone1 += "\\faPhone & { " + str(_val) + "}"
            Arr.append(phone)
            Brr.append(phone1)
        if _key == "email" and _val != "":
            email += "{ " + str(_val) + "}&\\faEnvelope"
            email1 += "\\faEnvelope & {" + str(_val) + "}"
            Arr.append(email)
            Brr.append(email1)
        if _key == "homepage" and _val != "":
            homepage += "{ " + str(_val) + "}&\\faGlobe"
            homepage1 += "\\faGlobe & { " + str(_val) + "}"
            Arr.append(homepage)
            Brr.append(homepage1)
        if _key == "facebook" and _val != "":
            facebook += "{ " + str(_val) + "}&\\faFacebook"
            facebook1 += "\\faFacebook & { " + str(_val) + "}"
            Arr.append(facebook)
            Brr.append(facebook1)
        if _key == "linked" and _val != "":
            linkedin += "{ " + str(_val) + "}&\\faLinkedin"
            linkedin1 += "\\faLinkedin & { " + str(_val) + "}"
            Arr.append(linkedin)
            Brr.append(linkedin1)
        if _key == "github" and _val != "":
            github += "{ " + str(_val) + "}&\\faGithub"
            github1 += "\\faGithub & { " + str(_val) + "}"
            Arr.append(github)
            Brr.append(github1)

    contact = ""
    contact1 = ""
    contact2 = ""
    contact3 = ""
    for index, val in enumerate(Arr):
        if index % 2 == 0:
            contact +=  str(val) +"\\\\\n"
        else:
            contact +=  str(val) +"\\\\\n"

    for index, val in enumerate(Brr):
        if index % 2 == 0:
            contact3 += str(val) + "\\\\\n"
        else:
            contact3 += str(val) + "\\\\\n"
        # if len(Arr) % 2 == 0 and len(Arr) != 0:
        #     contact += "\\\\\n"

    contact1 = "\\begin{minipage}[t]{0.7\\textwidth}\n" \
              "\\vspace{2em}\n" \
              "\\flushright\n" \
              "\\begin{tabular}[t]{r|c}\n" + contact + "\\end{tabular}\n" \
                                                       "\\end{minipage}"
    contact2 = "\\begin{minipage}[t]{1.0\\textwidth}\n" \
               "\\vspace{2em}\n" \
               "\\flushleft\n" \
               "\\begin{tabular}[t]{c|l}\n" + contact3 + "\\end{tabular}\n" \
                                                        "\\end{minipage}"

    if data["image"]["status"] == "on" and data["image"]["avatar"] != None:
        decodeIMG(data["image"]["avatar"], media_path)
        image += "\\begin{minipage}[t]{0.22\\textwidth}\n" \
                 "\\includegraphics[valign=t,width=\\textwidth]{avatar.png}\n" \
                 "\\end{minipage}\\hspace{1em}\\hfill"

    education = ""
    experience = ""
    project = ""
    skill = ""
    award = ""
    body = ""
    desc1 =""
    body1 = ""

    for _item in data["list_section"]:
        if _item["name"] == "desc" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["desc"] != [""]:
                desc1 += "%===============================DESC========================\n"
                desc1 += "\\cvrule{black}{2pt}\n\\subsection{ABOUT ME}\n\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["desc"][0] != "":
                        desc = item["desc"][0].strip("\n").split("\n")
                        if len(item["desc"]) > 0:
                            for sub_item in desc:
                                desc1 += "\t\\item{" + str(sub_item) + "}\n"
                desc1 += "\\end{itemize}\n"

        if _item["name"] == "education" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                education += "%===============================EDUCATION========================\n"
                education += "\\cvrule{black}{2pt}\n\\subsection{EDUCATION}\n\\begin{itemize}"
                for item in _item["data"]:
                    if item["degree"] == "":
                        item["degree"] = " "
                    if item["time"] == "":
                        item["time"] = " "
                    if item["org"] == "":
                        item["org"] = " "
                    if item["gpa"] == "":
                        item["gpa"] = " "
                    education += "\t\\item \\textbf{" + str(item["title"]) + "}\\hfill{" + str(item["time"]) + \
                                 "}\\\\{" + str(item["degree"]) + "}\\\\{" + str(item["org"]) + "}\\\\{" + str(
                        item["gpa"]) + "}\n"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            education += "\n\\begin{itemize}"
                            for sub_item in desc:
                                education += "\n\t\t\t\\item{" + str(sub_item) + "}"
                            education += "\n\\end{itemize}\n\\divider"
                education += "\\end{itemize}\n"

        elif _item["name"] == "experience" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["company"] != "":
                experience += "%===============================EXPERIENCE========================\n"
                experience += "\\cvrule{black}{2pt}\n\\subsection{EXPERIENCE}\\begin{itemize}"
                for item in _item["data"]:
                    if item["pos"] == "":
                        item["pos"] = " "
                    if item["time"] == "":
                        item["time"] = " "
                    if item["loc"] == "":
                        item["loc"] = " "
                    experience += "\t\\item \\textbf{" + str(item["pos"]) + "}\\hfill{" + str(item["time"]) + \
                                  "}\\\\{" + str(item["company"]) + "}\\\\{" + str(item["loc"]) + "}\n"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            experience += "\n\\begin{itemize}"
                            for sub_item in desc:
                                experience += "\n\t\t\t\\item{" + str(sub_item) + "}"
                            experience += "\n\\end{itemize}\n\\divider"
                experience += "\n\\end{itemize}"

        elif _item["name"] == "project" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                project += "%===============================PROJECT========================\n"
                project += "\\cvrule{black}{2pt}\n\\subsection{PROJECTS}\n\\begin{itemize}"
                for item in _item["data"]:
                    if item["time"] == "":
                        item["time"] = " "
                    if item["desc"] == "":
                        item["desc"] = " "
                    project += "\t\\item \\textbf{"+str(item["title"])+"}\\hfill{"+str(item["time"])+"}\n"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            project += "\n\\begin{itemize}"
                            for sub_item in desc:
                                project += "\n\t\t\t\\item{" + str(sub_item) + "}\n"
                            project += "\n\\end{itemize}\n\\divider\n"
                project += "\\end{itemize}"

        elif _item["name"] == "skill"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                skill += "%===============================SKILL========================\n"
                skill += "\\cvrule{black}{2pt}\n\\subsection{SKILLS}\n\\begin{itemize}"
                for item in _item["data"]:
                    if item["desc"] == "":
                        item["desc"] = " "
                    skill += "\t\\item\\textbf{"+str(item["title"])+"}"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            skill += "\n\t\t\\begin{itemize}\n"
                            for sub_item in desc:
                                skill += "\n\t\t\t\\item{" + str(sub_item) + "}\n"
                            skill += "\\divider\n\t\t\\end{itemize}\n "
                skill += "\\end{itemzie}"

        elif _item["name"] == "award"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                award += "%===============================AWARD========================\n"
                award += "\\cvrule{black}{2pt}\n\\subsection{AWARDS}\n\\begin{itemize}"
                for item in _item["data"]:
                    if item["time"] == "":
                        item["time"] = " "
                    if item["org"] == "":
                        item["org"] = " "
                    award += "\t\\item {" + str(item["title"]) + "}\\hfill{"+str(item["time"])+"}\\\\{"+str(item["org"])+"}\n"
                award += "\\end{itemize}"

    for _item in data["list_section"]:
        if _item["name"] == "project":
            if _item["data"][0]["title"] != "":
                body += "\n\\input{PROJECT.tex}\n"
        if _item["name"] == "experience":
            if _item["data"][0]["company"] != "":
                body += "\\input{EXPERIENCE.tex}\n"
        if _item["name"] == "education":
            if _item["data"][0]["title"] != "":
                body += "\\input{EDUCATION.tex}\n"
        if _item["name"] == "skill":
            if _item["data"][0]["title"] != "":
                body += "\\input{SKILL.tex}\n"
        if _item["name"] == "award":
            if _item["data"][0]["title"] != "":
                body += "\\input{AWARD.tex}\n"
        if _item["name"] == "desc":
            if _item["data"][0]["desc"] != [""]:
                body += "\\input{DESC.tex}\n"
            body += ""

    if  data["image"]["avatar"] != None :
        body1 += "\\input{image.tex}\n\\input{PROFILE.tex}"
    else:
        body1 += "\n\\input{PROFILE1.tex}"


    with open(media_path + "/name.tex", "w", encoding="utf-8") as f:
        f.write(name)
    with open(media_path + "/image.tex", "w", encoding="utf-8") as f:
        f.write(image)
    with open(media_path + "/PROFILE.tex", "w", encoding="utf-8") as f:
        f.write(contact1)
    with open(media_path + "/meta_cv.tex", "w", encoding="utf-8") as f:
        f.write(body)
    with open(media_path + "/EDUCATION.tex", "w", encoding="utf-8") as f:
        f.write(education)
    with open(media_path + "/EXPERIENCE.tex", "w", encoding="utf-8") as f:
        f.write(experience)
    with open(media_path + "/PROJECT.tex", "w", encoding="utf-8") as f:
        f.write(project)
    with open(media_path + "/SKILL.tex", "w", encoding="utf-8") as f:
        f.write(skill)
    with open(media_path + "/AWARD.tex", "w", encoding="utf-8") as f:
        f.write(award)
    with open(media_path + "/DESC.tex", "w", encoding="utf-8") as f:
        f.write(desc1)
    with open(media_path + "/Header.tex", "w", encoding="utf-8") as f:
        f.write(body1)
    with open(media_path + "/PROFILE1.tex", "w", encoding="utf-8") as f:
        f.write(contact2)