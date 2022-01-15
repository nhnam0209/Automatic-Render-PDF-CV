import os
import base64
def decodeIMG(base,path):
    imgdata = base64.b64decode(base)
    filename = path + "/avatar.png"
    with open(filename, "wb") as f:
        f.write(imgdata)

def fill(data, media_path=None):
    if media_path == None:
        full_path = os.path.realpath(__file__)
        path, filename = os.path.split(full_path)
        media_path = path

    name, email, linkedin, github, phone, image, facebook, birthdate, cityname = tuple(
        "" for i in range(9))
    Arr =[]
    # if data["image"]["status"] == "on":
    #     decodeIMG(data["image"]["avatar"], media_path)
    #     image += " \n\n\t\t{\\color{LinkedInBlue} \\ovalbox{\\includegraphics[scale=.25]{avatar.png}}}\n\t\t\\vspace{0.2in}"

    for _key, _val in data["profile"].items():
        if _key == "fullname"and _val != "":
            name += "\t\\begin{tcolorbox}\n\t\t[width=0.5\\textwidth ,colframe=WhiteSmoke,colback=LinkedInBlue,arc=1mm,]\n\t\t\\color{WhiteSmoke}"
            name += "\n\t\t\\centerline{\\Large{" + str(_val) + "}}"
            name += " \n\t\\end{tcolorbox}\n\t\\vspace{0.25in}"

    for _key, _val in data["profile"].items():
        if _key == "birth"and _val != "":
            birthdate += "{\\color{LinkedInBlue} \\ovalbox{Birthdate}}\n\t\t{\n\t\t{" + str(_val) + "}\n\t\t}\n\n"
            Arr.append(birthdate)
        if _key == "phone"and _val != "":
            phone += "{\\color{LinkedInBlue} \\ovalbox{Phone}}\n\t\t{\n\t\t{" + str(_val) + "}\n\t\t}\n\n"
            Arr.append(phone)
        if _key == "email"and _val != "":
            email += "{\\color{LinkedInBlue} \\ovalbox{Email}}\n\t\t{\\href{" + str(
                _val) + "}\n\t\t{\\color{OuterSpace}{" + str(_val) + "}}\n\t\t}\n\n"
            Arr.append(email)
        if _key == "github"and _val != "":
            github += "{\\color{LinkedInBlue} \\ovalbox{Github}}\n\t\t{\\href{" + str(
                _val) + "}\n\t\t{\\color{OuterSpace}{" + str(_val) + "}}\n\t\t}\n\n"
            Arr.append(github)
        if _key == "facebook"and _val != "":
            facebook += "{\\color{LinkedInBlue} \\ovalbox{Facebook}}\n\t\t{\\href{" + str(
                _val) + "}\n\t\t{\\color{OuterSpace} {" + str(_val) + "}}\n\t\t}\n\n"
            Arr.append(facebook)
        if _key == "linked"and _val != "":
            linkedin += "{\\color{LinkedInBlue} \\ovalbox{Linkedin}}\n\t\t{\\href{" + str(
                _val) + "}\n\t\t{\\color{OuterSpace} {" + str(_val) + "}}\n\t}"
            Arr.append(linkedin)

    print(Arr)
    profile = ""
    for index, val in enumerate(Arr):
        if index % 2 == 0:
            profile += "\\item" + str(val) +"\n"
        else:
            profile += "\\item" + str(val)+"\n"

    if profile != "":
        profile = "\\begin{tcolorbox}\n\t[width=\\textwidth, \n\t colframe=WhiteSmoke,\n\t colback=LinkedInBlue,\n\t arc=1mm,]\n\t\\color{WhiteSmoke}\n\t\\centerline{\\Large PERSONAL INFO}\n\\end{tcolorbox}\n\\begin{itemize}\n" +\
                  profile + "\n\\end{itemize}"


    education = ""
    experience = ""
    project = ""
    skill = ""
    award = ""
    body = ""
    desc1 = ""

    for _item in data["list_section"]:
        if _item["name"] == "desc" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["desc"] != [""]:
                desc1 += "%===============================DESC========================\n"
                desc1 += "\\begin{tcolorbox}\n\t[width=\\textwidth, \n\t colframe=WhiteSmoke,\n\t " \
                        "colback=LinkedInBlue,\n\t arc=1mm,]\n\t\\color{WhiteSmoke}\n\t\\centerline{\\Large ABOUT ME}\n\\end{tcolorbox}"
                desc1 += "\n\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["desc"][0] != "":
                        desc = item["desc"][0].strip("\n").split("\n")
                        if len(item["desc"]) > 0:
                            for sub_item in desc:
                                desc1 += "\t\\item \\mybullet{" + str(sub_item) + "}\n"
                desc1 += "\\end{itemize}\n"

        if _item["name"] == "education"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                education += "%===============================EDUCATION========================\n"
                education += "\\begin{tcolorbox}\n\t[width=\\textwidth, \n\t colframe=WhiteSmoke,\n\t" \
                             " colback=LinkedInBlue,\n\t arc=1mm,]\n\t\\color{WhiteSmoke}\n\t\\centerline{\\Large EDUCATION}\n\\end{tcolorbox}"
                education += "\n\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["degree"] == "":
                        item["degree"] = " "
                    if item["time"] == "":
                        item["time"] = " "
                    if item["org"] == "":
                        item["org"] = " "
                    if item["gpa"] == "":
                        item["gpa"] = " "
                    education += "\t\\item\n\t{\\color{LinkedInBlue} \\ovalbox{" + str(item["title"]) + "}}{\\hfill\n\t" \
                                     + str(item["time"]) + "\\\\}{\n\t" + str(
                        item["degree"]) + "}{\\\\GPA: "+str(item["gpa"])+"}{\\\\"+str(item["org"])+"}"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            education += "\n\\begin{itemize}"
                            for sub_item in desc:
                                education += "\n\t\t\t\\item \\mybullet{" + str(sub_item) + "}\n"
                            education += "\n\\end{itemize}\n\\divider"
                education += "\n\\end{itemize}\n"

        elif _item["name"] == "experience" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["company"] != "":
                experience += "%===============================EXPERIENCE========================\n"
                experience += "\\begin{tcolorbox}\n\t[width=\\textwidth, \n\t colframe=WhiteSmoke,\n\t" \
                                  " colback=LinkedInBlue,\n\t arc=1mm,]\n\t\\color{WhiteSmoke}\n\t\\centerline{\\Large EXPERIENCE}\n\\end{tcolorbox}"
                experience += "\n\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["pos"] == "":
                        item["pos"] = " "
                    if item["time"] == "":
                        item["time"] = " "
                    if item["loc"] == "":
                        item["loc"] = " "
                    experience += "\t\\item\n\t{\\color{LinkedInBlue} \\ovalbox{" + str(item["pos"]) + "}}{\\hfill\n\t" \
                                             + str(item["time"]) + "}{\\\\\n\t" + str(item["company"]) + \
                                          "}{\\hfill\n\t" + str(item["loc"]) + "}"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            experience += "\n\\begin{itemize}"
                            for sub_item in desc:
                                experience += "\n\t\t\t\\item \\mybullet{" + str(sub_item) + "}\n"
                            experience += "\n\\end{itemize}\n\\divider"
                experience += "\n\\end{itemize}\n"

        elif _item["name"] == "project" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                project += "%===============================PROJECT========================\n"
                project += "\\begin{tcolorbox}\n\t[width=\\textwidth, \n\t colframe=WhiteSmoke,\n\t colback=LinkedInBlue,\n\t arc=1mm,]" \
                           "\n\t\\color{WhiteSmoke}\n\t\\centerline{\\Large PROJECT}\n\\end{tcolorbox}"
                project += "\n\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["time"] == "":
                        item["time"] = " "
                    if item["desc"] == "":
                        item["desc"] = " "
                    project += "\t\\item {\\color{LinkedInBlue} \\ovalbox{" + str(item["title"]) + "}}{\\hfill"+str(item["time"])+"}"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            project += "\t\t\\begin{itemize}\n"
                            for sub_item in desc:
                                project += "\t\t\t\\item \\mybullet{" + str(sub_item) + "}\n"
                            project += "\t\t\\end{itemize}\n "
                project += "\n\\end{itemize}\n"

        elif _item["name"] == "skill"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                skill +="%===============================SKILL========================\n"
                skill +="\\begin{tcolorbox}\n\t[width=\\textwidth, \n\t colframe=WhiteSmoke,\n\t colback=LinkedInBlue," \
                        "\n\t arc=1mm,]\n\t\\color{WhiteSmoke}\n\t\\centerline{\\Large SKILLS}\n\\end{tcolorbox}"
                skill += "\n\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["desc"] == "":
                        item["desc"] = " "
                    skill += "\t\\item{\\color{LinkedInBlue} \\ovalbox{" + str(item["title"]) + "}}"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            skill += "\t\t\\begin{itemize}\n"
                            for sub_item in desc:
                                skill += "\t\t\t\\item \\mybullet{"+str(sub_item)+"}\n"
                            skill += "\t\t\\end{itemize}\n "
                skill += "\n\\end{itemize}\n"

        elif _item["name"] == "award"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                award +="%===============================AWARD========================\n"
                award +="\\begin{tcolorbox}\n\t[width=\\textwidth, \n\t colframe=WhiteSmoke,\n\t colback=LinkedInBlue," \
                        "\n\t arc=1mm,]\n\t\\color{WhiteSmoke}\n\t\\centerline{\\Large AWARD}\n\\end{tcolorbox}"
                award += "\n\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["time"] == "":
                        item["time"] = " "
                    if item["org"] == "":
                        item["org"] = " "
                    award += "\t\\item {\\color{LinkedInBlue} \\ovalbox{" + str(item["title"]) + "}}{\\hfill "+str(item["time"])+"}{\n\\\\"+str(item["org"])+"}\\\\"
                award += "\n\\end{itemize}\n"

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
