import os
import base64


def decodeIMG(base, path):
    imgdata = base64.b64decode(base)
    filename = path + "/avatar.png"
    with open(filename, "wb") as f:
        f.write(imgdata)


def fill(data, media_path=None):
    if media_path == None:
        full_path = os.path.realpath(__file__)
        path, filename = os.path.split(full_path)
        media_path = path

    name,birthdate,phone,homepage,facebook,linkedin,github,email,image  = tuple("" for i in range(9))
    Arr = []
    if data["image"]["status"] == "on" and data["image"]["avatar"] != None:
        decodeIMG(data["image"]["avatar"], media_path)
        image += " \\vspace{0.5cm}\n\\begin{wrapfigure}{R}{0.25\\textwidth}" \
                 "\n\\vspace{-1.7cm}\n\\begin{center}\n" \
                 "\\includegraphics[height=4cm,width=3.5cm]{avatar.png}\n" \
                 "\\end{center}" \
                 "\n\\vspace{-1.5cm}" \
                 "\n\\end{wrapfigure}"


    for _key, _val in data["profile"].items():
        if _key == "fullname" and _val != "":
            name += "\t{" + str(_val) + "}\n"
        if _key == "birth" and _val != "":
            birthdate += "\t\\faBirthdayCake \\space {" + str(_val) + "}\\\\\n"
            Arr.append(birthdate)
        if _key == "phone" and _val != "":
            phone += "\t\\faPhone \\space {" + str(_val) + "}\\\\\n"
            Arr.append(phone)
        if _key == "homepage" and _val != "":
            homepage += "\t\\faTv \\space \\href{" + str(_val) + "}{" + str(_val) + "} \\\\\n"
            Arr.append(homepage)
        if _key == "facebook" and _val != "":
            facebook += "\t\\faFacebook \\space \\href{" + str(_val) + "}{" + str(_val) + "} \\\\\n"
            Arr.append(facebook)
        if _key == "linked" and _val != "":
            linkedin += "\t\\faLinkedin \\space \\href{" + str(_val) + "}{" + str(_val) + "} \\\\\n"
            Arr.append(linkedin)
        if _key == "github" and _val != "":
            github += "\t\\faGithub \\space \\href{" + str(_val) + "}{" + str(_val) + "} \\\\\n"
            Arr.append(github)
        if _key == "email" and _val != "":
            email += "\t\\faEnvelope \\space \\href{" + str(_val) + "}{" + str(_val) + "}\\\\\n"
            Arr.append(email)

    contact = ""
    print(Arr)

    for index, val in enumerate(Arr):
        if index % 2 == 0:
            contact +=  str(val)
        else:
            contact +=  str(val)

    contact = "\\section{\\mysidestyle{Personal Information}}\n"+contact+"\n"

    body = ""
    education = ""
    experience = ""
    project = ""
    skill = ""
    award = ""
    desc1 =""

    for _item in data["list_section"]:
        if _item["name"] == "desc" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["desc"] != [""]:
                desc1 += "%===============================DESC========================\n"
                desc1 += "\\section{\\mysidestyle {About Me}}\n\\begin{itemize}\n\n"
                for item in _item["data"]:
                    if item["desc"][0] != "":
                        desc = item["desc"][0].strip("\n").split("\n")
                        if len(item["desc"]) > 0:
                            for sub_item in desc:
                                desc1 += "\t\\item{" + str(sub_item) + "}\n"
                desc1 += "\\end{itemize}\n"

        if _item["name"] == "education"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                education += "\\section{\\mysidestyle {Education}}\n\\vspace{2mm}"
                for item in _item["data"]:
                    if item["degree"] == "":
                        item["degree"] = " "
                    if item["time"] == "":
                        item["time"] = " "
                    if item["org"] == "":
                        item["org"] = " "
                    if item["gpa"] == "":
                        item["gpa"] = " "
                    education += "\n\t{\\textbf{"+str(item["title"]) + "}}\\\\\n \\small{\\faCertificate \\space{" + str(
                            item["degree"]) + "}} \\\\\n {\\faGraduationCap \\space{"+str(item["org"])+\
                                 "}}\\\\\n {\\faCalendar \\space" + str(item["time"]) +\
                                 "}\\\\\n \\textsl{GPA: " + str(item["gpa"]) + "}\n"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            education += "\n\t\\begin{itemize}"
                            for sub_item in desc:
                                education += "\n\t\t\\item{" + str(sub_item) + "}\\\\"
                            education += "\n\t\\end{itemize}"


        elif _item["name"] == "experience"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["company"] != "":
                experience += "\\section{\\mysidestyle {Experience}}\n\\vspace{2mm}"
                for item in _item["data"]:
                    if item["pos"] == "":
                        item["pos"] = " "
                    if item["time"] == "":
                        item["time"] = " "
                    if item["loc"] == "":
                        item["loc"] = " "
                    experience += "\n\t\\textbf{" + str(item["pos"]) + "}\\\\\\textsl{\\faCalendar \\space{" + str(item["time"]) + "}}\n" \
                                "\\\\\n\t{\\faBuilding \\space {" + str(item["company"]) + \
                                  "}}\\\\ \n\t\\small{\\faMapMarker \\space {" + str(item["loc"]) + "}}\n\t\n"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            experience += "\n\t\\begin{itemize}"
                            for sub_item in desc:
                                experience += "\n\t\t\\item{" + str(sub_item) + "}\\\\"
                            experience += "\n\t\\end{itemize}\n"

        elif _item["name"] == "project"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                project += "\\section{\\mysidestyle {Projects}}\n\\vspace{2mm}"
                for item in _item["data"]:
                    if item["time"] == "":
                        item["time"] = " "
                    if item["desc"] == "":
                        item["desc"] = " "
                    project += "\\textbf{" + str(item["title"]) + "}\\\\\n{\\faCalendar \\space {"+str(item["time"])+"}}\n"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            project += "\t\\begin{itemize}"
                            for sub_item in desc:
                                project += "\n\t\t\\item{" + str(sub_item) + "}\\\\"
                            project += "\n\t\\end{itemize}"

        elif _item["name"] == "skill"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                skill += "\\section{\\mysidestyle {Skills}}\n \\vspace{2mm}"
                for item in _item["data"]:
                    if item["desc"] == "":
                        item["desc"] = " "
                    skill += "\n\t\\textbf{" + str(item["title"]) + "}\n"
                    skill += "\\begin{description}\n"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            skill += "\t\\begin{itemize}"
                            for sub_item in desc:
                                skill += "\n\t\t\\item{" + str(sub_item) + "}\\\\"
                            skill += "\n\t\\end{itemize}"
                    skill += "\n\\end{description}\n"

        elif _item["name"] == "award"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                award += "\\section{\\mysidestyle {Awards}}\n \\vspace{2mm}"
                for item in _item["data"]:
                    if item["time"] == "":
                        item["time"] = " "
                    if item["org"] == "":
                        item["org"] = " "
                    award += "\n\t\\textbf{" + str(item["title"]) + "}\\\\\n{\\faCalendar \\space {"+str(item["time"])+"}}\\\\\n{\\faMapMarker \\space {"+str(item["org"])+"}}\n"
                # award += "\\begin{description}\n"
                # if len(item["desc"]) > 0:
                #     award += "\t\\begin{itemize}"
                #     for sub_item in item["desc"]:
                #         award += "\n\t\t\\item[]{" + str(sub_item) + "}"
                #     award += "\n\t\\end{itemize}"
                # award += "\n\\end{description}\n"

    body1 = ""
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

    if data["image"]["avatar"] != None:
        body1 += "\\input{image.tex}"
    else:
        body1 += "\n"

    with open(media_path + "/person_info.tex" , "w", encoding="utf-8") as f:
        f.write(contact)
    with open(media_path + "/name_info.tex" , "w", encoding="utf-8") as f:
        f.write(name)
    with open(media_path + "/meta_cv.tex" , "w", encoding="utf-8") as f:
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
    with open(media_path + "/image.tex", "w", encoding="utf-8") as f:
        f.write(image)
    with open(media_path + "/Header.tex", "w", encoding="utf-8") as f:
        f.write(body1)



