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

    name, homepage, email, github, phone, birthdate,facebook,linkedin = tuple("" for i in range(8))

    Arr = []
    for _key, _val in data["profile"].items():
        if _key == "fullname" and _val != "":
            name += "\n\\name{" + str(_val) + "}"
        if _key == "birth"and _val != "":
            birthdate += "\\faCalendar{  " + str(_val) + "}"
            Arr.append(birthdate)
        if _key == "phone"and _val != "":
            phone += "\\faPhone{  " + str(_val) + "}"
            Arr.append(phone)
        if _key == "homepage"and _val != "":
            homepage += "\\faGlobe{  " + str(_val) + "}"
            Arr.append(homepage)
        if _key == "email"and _val != "":
            email += "\\faEnvelope{  " + str(_val) + "}"
            Arr.append(email)
        if _key == "github"and _val != "":
            github += "\\faGithub{  " + str(_val) + "}"
            Arr.append(github)
        if _key == "facebook"and _val != "":
            facebook += "\\faFacebook{  " + str(_val) + "}"
            Arr.append(facebook)
        if _key == "linked"and _val != "":
            linkedin += "\\faLinkedin{  " + str(_val) + "}"
            Arr.append(linkedin)

    profile=""

    for index, val in enumerate(Arr):
        if index % 2 == 0:
            profile += "\\item{" + str(val) +"}"
        else:
            profile += "\\hfill{" + str(val)+"}"
    print(profile)

    if profile != None and profile != "":
        profile = "\\begin{rSection}{PERSONAL INFO}\n\\begin{itemize}\n"+profile+"\n\\end{itemize}\n\\end{rSection}"

    education = ""
    experience = ""
    project = ""
    skill = ""
    award = ""
    body = ""
    desc1 =""

    for _item in data["list_section"]:
        if _item["name"] == "desc" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["desc"] != [""]:
                desc1 += "%===============================DESC========================\n"
                desc1 += "\\begin{rSection}{ABOUT ME}"
                desc1 += "\n\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["desc"][0] != "":
                        desc = item["desc"][0].strip("\n").split("\n")
                        if len(item["desc"]) > 0:
                            for sub_item in desc:
                                desc1 += "\t\\item {" + str(sub_item) + "}\n"
                desc1 += "\\end{itemize}\n"
                desc1 += "\\end{rSection}"

        if _item["name"] == "education"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                education += "\\begin{rSection}{Education}"
                for item in _item["data"]:
                    if item["degree"] == "":
                        item["degree"] = " "
                    if item["time"] == "":
                        item["time"] = " "
                    if item["org"] == "":
                        item["org"] = " "
                    if item["gpa"] == "":
                        item["gpa"] = " "
                    education += "\n{\\bf {" + str(item["title"]) + \
                                     "}}\\hfill{\\em{" + str(item["time"]) + \
                                     "}}\\\\\n{\\textit{" + str(item["degree"]) + "}} {GPA: " +str(item["gpa"])+"}\\\\{\\em{" + str(item["org"]) + "}}\n"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            education += "\n\\begin{itemize}"
                            for sub_item in desc:
                                education += "\n\t\t\t\\item{" + str(sub_item) + "}\n"
                            education += "\n\\end{itemize}\n"
                education += "\\end{rSection}"

        elif _item["name"] == "experience"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["company"] != "":
                experience += "\\begin{rSection}{Experience}"
                for item in _item["data"]:
                    if item["pos"] == "":
                        item["pos"] = " "
                    if item["time"] == "":
                        item["time"] = " "
                    if item["loc"] == "":
                        item["loc"] = " "
                    experience += "\n{\\bf {"+str(item["pos"])+\
                                     "}}\\hfill{\\em{"+str(item["time"])+\
                                     "}}\\\\\n{\\textit{"+str(item["company"])+"}}{\\\\{\\em{"+str(item["loc"])+"}}}\n"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            experience += "\n\t\\begin{itemize}"
                            for sub_item in desc:
                                experience += "\n\t\t\\item{" + str(sub_item) + "}"
                            experience += "\n\t\\end{itemize}"
                experience += "\\end{rSection}"

        elif _item["name"] == "project"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                project += "\\begin{rSection}{Projects}"
                for item in _item["data"]:
                    if item["time"] == "":
                        item["time"] = " "
                    if item["desc"] == "":
                        item["desc"] = " "
                    project += "\n{\\bf {"+str(item["title"])+"}}\\hfill{"+str(item["time"])+"}"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            project += "\n\t\\begin{itemize}"
                            for sub_item in desc:
                                project += "\n\t\t\\item{" + str(sub_item) + "}"
                            project += "\n\t\\end{itemize}"
                project += "\\end{rSection}"

        elif _item["name"] == "skill"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                skill += "\\begin{rSection}{Skills}"
                for item in _item["data"]:
                    if item["desc"] == "":
                        item["desc"] = " "
                    skill += "\n{\\bf {" + str(item["title"]) + "}}"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            skill += "\n\t\\begin{itemize}"
                            for sub_item in desc:
                                skill += "\n\t\t\\item{" + str(sub_item) + "}"
                            skill += "\n\t\\end{itemize}"
                skill += "\\end{rSection}"

        elif _item["name"] == "award"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                award += "\\begin{rSection}{Awards}"
                for item in _item["data"]:
                    if item["time"] == "":
                        item["time"] = " "
                    if item["org"] == "":
                        item["org"] = " "
                    award += "\n{\\bf {" + str(item["title"]) + "}}\\hfill{"+str(item["time"])+"}\\\\{"+str(item["org"])+"}"
                award += "\\end{rSection}"

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

    with open(media_path + "/person_info.tex", "w", encoding="utf-8") as f:
        f.write(profile)
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
    with open(media_path + "/NAME.tex", "w", encoding="utf-8") as f:
        f.write(name)
