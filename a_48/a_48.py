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

    Arr = []
    for _key, _val in data["profile"].items():
        if _key == "fullname"and _val != "":
            name = "\\firstname{"+  str(_val) + "}\n"
        if _key == "birth" and _val != "":
            birthdate += "\\birthday{ " + str(_val) + "}"
            Arr.append(birthdate)
        if _key == "phone" and _val != "":
            phone += "\\phone{ " + str(_val) + "}"
            Arr.append(phone)
        if _key == "email" and _val != "":
            email += "\\email{ " + str(_val) + "}"
            Arr.append(email)
        if _key == "homepage" and _val != "":
            homepage += "\\homepage{ " + str(_val) + "}"
            Arr.append(homepage)
        if _key == "facebook" and _val != "":
            facebook += "\\facebook{ " + str(_val) + "}"
            Arr.append(facebook)
        if _key == "linked" and _val != "":
            linkedin += "\\linkedin{ " + str(_val) + "}"
            Arr.append(linkedin)
        if _key == "github" and _val != "":
            github += "\\github{ " + str(_val) + "}"
            Arr.append(github)

    contact = ""
    for index, val in enumerate(Arr):
        if index % 2 == 0:
            contact +=  str(val) +"\n"
        else:
            contact +=  str(val) +"\n"

        # if len(Arr) % 2 == 0 and len(Arr) != 0:
        #     contact += "\\\\\n"

    contact = "\\personalinfo{\n" + contact + "}"

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
                desc1 += "\\cvsection{ABOUT ME}\n\\medskip\n\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["desc"][0] != "":
                        desc = item["desc"][0].strip("\n").split("\n")
                        if len(item["desc"]) > 0:
                            for sub_item in desc:
                                desc1 += "\t\\item{" + str(sub_item) + "}\n"
                desc1 += "\n\\end{itemize}\n\\medskip"

        if _item["name"] == "education" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                education += "%===============================EDUCATION========================\n"
                education += "\\cvsection{EDUCATION}\n\\medskip\n"
                for item in _item["data"]:
                    if item["degree"] == "":
                        item["degree"] = " "
                    if item["time"] == "":
                        item["time"] = " "
                    if item["org"] == "":
                        item["org"] = " "
                    if item["gpa"] == "":
                        item["gpa"] = " "
                    education += "\t\\cvuniversity {" + str(item["title"]) + "}{" + str(item["degree"]) + \
                                 "}{" + str(item["time"]) + "}{" + str(item["org"]) + "}{" + str(
                        item["gpa"]) + "}\n"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            education += "\n\\begin{itemize}"
                            for sub_item in desc:
                                education += "\n\t\t\t\\item{" + str(sub_item) + "}"
                            education += "\n\\end{itemize}\n\\divider"
                education += "\n\\medskip"

        elif _item["name"] == "experience" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["company"] != "":
                experience += "%===============================EXPERIENCE========================\n"
                experience += "\\cvsection{EXPERIENCE}\n\\medskip\n"
                for item in _item["data"]:
                    if item["pos"] == "":
                        item["pos"] = " "
                    if item["time"] == "":
                        item["time"] = " "
                    if item["loc"] == "":
                        item["loc"] = " "
                    experience += "\t\\cvexperience {" + str(item["pos"]) + "}{" + str(item["company"]) + \
                                  "}{" + str(item["time"]) + "}{" + str(item["loc"]) + "}\n"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            experience += "\n\\begin{itemize}"
                            for sub_item in desc:
                                experience += "\n\t\t\t\\item{" + str(sub_item) + "}"
                            experience += "\n\\end{itemize}\n\\divider"
                experience += "\n\\medskip"

        elif _item["name"] == "project" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                project += "%===============================PROJECT========================\n"
                project += "\\cvsection{PROJECTS}\n\\medskip\n"
                for item in _item["data"]:
                    if item["time"] == "":
                        item["time"] = " "
                    if item["desc"] == "":
                        item["desc"] = " "
                    project += "\t\\cvproject {"+str(item["title"])+"}{"+str(item["time"])+"} \n"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            project += "\n\\begin{itemize}"
                            for sub_item in desc:
                                project += "\n\t\t\t\\item{" + str(sub_item) + "}\n"
                            project += "\n\\end{itemize}\n\\divider"
                project += "\n\\medskip"

        elif _item["name"] == "skill"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                skill += "%===============================SKILL========================\n"
                skill += "\\cvsection{SKILLS}\n\\medskip\n"
                for item in _item["data"]:
                    if item["desc"] == "":
                        item["desc"] = " "
                    skill += "\t\\textbf{"+str(item["title"])+"}"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            skill += "\n\t\t\\begin{itemize}\n"
                            for sub_item in desc:
                                skill += "\n\t\t\t\\item{" + str(sub_item) + "}\n"
                            skill += "\t\t\\end{itemize}\n\\divider "
                skill += "\n\\medskip"

        elif _item["name"] == "award"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                award += "%===============================AWARD========================\n"
                award += "\\cvsection{AWARDS}\n\\medskip\n"
                for item in _item["data"]:
                    if item["time"] == "":
                        item["time"] = " "
                    if item["org"] == "":
                        item["org"] = " "
                    award += "\t\\cvevent{" + str(item["title"]) + "}{"+str(item["time"])+"}{"+str(item["org"])+"}\n"
                award +="\n\\medskip"

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



    with open(media_path + "/name.tex", "w", encoding="utf-8") as f:
        f.write(name)
    with open(media_path + "/PROFILE.tex", "w", encoding="utf-8") as f:
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