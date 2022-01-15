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

    name, profile, email,birthdate, phone, homepage, facebook, linkedin, github, image = tuple("" for i in range(10))

    # if data["image"]["status"] == "on":
    #     decodeIMG(data["image"]["avatar"], path)
    #     image += "\n\\photo[64pt][0.4pt]{avatar.png}"
    Arr = []
    for _key, _val in data["profile"].items():
        if _key == "fullname" and _val != "":
            name += "\n\n\\familyname{ " + str(_val) + "}\\\\\n\\title{CV}"
        if _key == "birth" and _val != "":
            birthdate += "\\faCalendar{ "+str(_val)+"}"
            Arr.append(birthdate)
        if _key == "phone" and _val != "":
            phone += "\\faPhone{ "+str(_val)+"}"
            Arr.append(phone)
        if _key == "email" and _val != "":
            email += "\\faEnvelope{ "+str(_val)+"}"
            Arr.append(email)
        if _key == "homepage" and _val != "":
            homepage += "\\faGlobe{ "+str(_val)+"}"
            Arr.append(homepage)
        if _key == "facebook" and _val != "":
            facebook += "\\faFacebook{ "+str(_val)+"}"
            Arr.append(facebook)
        if _key == "linked" and _val != "":
            linkedin += "\\faLinkedin{ "+str(_val)+"}"
            Arr.append(linkedin)
        if _key == "github" and _val != "":
            github += "\\faGithub{ " + str(_val) + "}"
            Arr.append(github)

    contact = ""
    for index, val in enumerate(Arr):
        if index % 2 == 0:
            contact += "\\item[]" + str(val) +"\n"
        else:
            contact += "\\item[]" + str(val)+"\n"

    # if len(Arr) % 2 == 0 and len(Arr) != 0:
    #     contact += "\\\\\n"
    if contact != "":
        contact = "\\section{PERSONAL INFO}\n\n\\vspace{6pt}\n\\begin{itemize}\n" + contact + "\n\\end{itemize}"

    print(contact)
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
                desc1 += "\\section{ABOUT ME}\n\n\\vspace{6pt}\n\\begin{itemize}\n"
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
                education += "\\section{EDUCATION}\n\n\\vspace{6pt}\n\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["degree"] == "":
                        item["degree"] = " "
                    if item["time"] == "":
                        item["time"] = " "
                    if item["org"] == "":
                        item["org"] = " "
                    if item["gpa"] == "":
                        item["gpa"] = " "
                    education += "\t\\item{\\cventry {" + str(item["time"]) + "}{" + str(item["degree"]) + \
                                     "}{" + str(item["title"]) + "}{" + str(item["org"]) + "}{"+str(item["gpa"])+ "}{\\vspace{3pt}}}\n"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            education += "\n\\begin{itemize}"
                            for sub_item in desc:
                                education += "\n\t\t\t\\item{" + str(sub_item) + "}"
                            education += "\n\\end{itemize}{\\vspace{7pt}}\n"
                education += "\n\\end{itemize}\n"

        elif _item["name"] == "experience" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["company"] != "":
                experience += "%===============================EXPERIENCE========================\n"
                experience += "\\section{EXPERIENCE}\n\n\\vspace{5pt}\n\n\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["pos"] == "":
                        item["pos"] = " "
                    if item["time"] == "":
                        item["time"] = " "
                    if item["loc"] == "":
                        item["loc"] = " "
                    experience += "\t\\item{\\cventry {"+str(item["time"])+"}{"+str(item["loc"])+\
                                      "}{"+str(item["company"])+"}{"+str(item["pos"])+"}{ }{\\vspace{3pt}}}\n"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            experience += "\n\\begin{itemize}"
                            for sub_item in desc:
                                experience += "\n\t\t\t\\item{" + str(sub_item) + "}"
                            experience += "\n\\end{itemize}{\\vspace{7pt}}"
                experience += "\n\\end{itemize}"

        elif _item["name"] == "project"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                project += "%===============================PROJECT========================\n"
                project += "\\section{PROJECT}\n\n\\vspace{5pt}\n\n\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["time"] == "":
                        item["time"] = " "
                    if item["desc"] == "":
                        item["desc"] = " "
                    project += "\t\\item{\\textbf{"+str(item["title"])+"}\\hfill{"+str(item["time"])+"}\\\\}\n"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            project += "\n\\begin{itemize}"
                            for sub_item in desc:
                                project += "\n\t\t\t\\item{" + str(sub_item) + "}\n"
                            project += "\n\\end{itemize}\n{\\vspace{7pt}}"
                project += "\n\\end{itemize}\n"

        elif _item["name"] == "skill"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                skill += "%===============================SKILL========================\n"
                skill += "\\section{SKILL}\n\n\\vspace{6pt}\n\n\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["desc"] == "":
                        item["desc"] = " "
                    skill += "\t\\item\\textbf{"+str(item["title"])+"}\n"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            skill += "\n\t\t\\begin{itemize}\n"
                            for sub_item in desc:
                                skill += "\n\t\t\t\\item{" + str(sub_item) + "}\n"
                            skill += "\t\t\t\\vspace{6pt}\n\t\t\\end{itemize}\n "
                skill += "\n\\end{itemize}"

        elif _item["name"] == "award" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                award += "%===============================AWARD========================\n"
                award += "\\section{AWARD}\n\n\\vspace{6pt}\n\n\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["time"] == "":
                        item["time"] = " "
                    if item["org"] == "":
                        item["org"] = " "
                    award += "\t\\item\\textbf{" + str(item["title"]) + "}{\\hfill"+str(item["time"])+"}{\\\\"+str(item["org"])+"}\n"
                award += "\n\\end{itemize}"

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
        f.write(contact)
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
