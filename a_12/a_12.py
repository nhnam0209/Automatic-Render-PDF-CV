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

    name,birthdate,phone,homepage,facebook,linkedin,github,email  = tuple("" for i in range(8))
    Arr = []
    for _key, _val in data["profile"].items():
        if _key == "fullname" and _val != "":
            name = "\\textbf{\\LARGE " + str(_val) + "}\\\\\n"
        if _key == "email" and _val != "":
            Arr.append(_val)
        if _key == "birth" and _val != "":
            Arr.append(_val)
        if _key == "facebook" and _val != "":
            Arr.append(_val)
        if _key == "homepage" and _val != "":
            Arr.append(_val)
        if _key == "linked" and _val != "":
            Arr.append(_val)
        if _key == "phone" and _val != "":
            Arr.append(_val)
        if _key == "github" and _val != "":
            Arr.append(_val)

    contact = ""
    print(Arr)

    for index, val in enumerate(Arr):
        if index % 2 == 0:
            contact += "\\textbf{" + str(val) + "}"
        else:
            contact += "&\\hfill\\textbf{" + str(val) + "}\\\\\n"

    if len(Arr) % 2 == 0 and len(Arr) != 0:
        contact += "\\\\\n"

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
                desc1 += "\\section{About Me}\n\\begin{itemize}\n\n"
                for item in _item["data"]:
                    if item["desc"]!= "":
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            for sub_item in desc:
                                desc1 += "\t\\item{" + str(sub_item) + "}\n"
                desc1 += "\\end{itemize}\n"

        if _item["name"] == "education"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                education += "%===============================EDUCATION========================\n"
                education += "\\section{Education}\n"
                education += "\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["degree"] == "":
                        item["degree"] = " "
                    if item["time"] == "":
                        item["time"] = " "
                    if item["org"] == "":
                        item["org"] = " "
                    if item["gpa"] == "":
                        item["gpa"] = " "
                    education += "\\item{\\textbf{" + str(item["title"]) + "}}\\hfill{" + str(item["time"]) + \
                                     "}\\\\\\textbf{" + str(item["degree"]) + "}\\\\\\textitt{GPA: "+str(item["gpa"])+"}\\\\{" + str(item["org"]) + "}"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            education += "\\begin{itemize}"
                            for sub_item in desc:
                                education += "\n\\item{" + str(sub_item) + "}"
                            education += "\\end{itemize}"
                education += "\\end{itemize}\n"

        elif _item["name"] == "experience"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["company"] != "":
                experience += "%===============================EXPERIENCE========================\n"
                experience += "\\section{Experience}\n"
                experience += "\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["pos"] == "":
                        item["pos"] = " "
                    if item["time"] == "":
                        item["time"] = " "
                    if item["loc"] == "":
                        item["loc"] = " "
                    experience += "\\item {\\textbf{" + str(item["pos"]) + "}}\\hfill{" + str(item["time"]) + \
                                     "}\\\\\\textbf{" + str(item["company"]) + "}\\\\{" + str(item["loc"]) + "}"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            experience += "\\begin{itemize}"
                            for sub_item in desc:
                                experience += "\n\\item{" + str(sub_item) + "}\n"
                            experience += "\\end{itemize}"
                experience += "\\end{itemize}\n"

        elif _item["name"] == "project"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                project += "%===============================PROJECT========================\n"
                project += "\\section{Projects}\n"
                project += "\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["time"] == "":
                        item["time"] = " "
                    if item["desc"] == "":
                        item["desc"] = " "
                    project += "\t\\item {\\textbf{" + str(item["title"]) + "}}\\hfill{" + str(item["time"]) + "}"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            project += "\\begin{itemize}\n"
                            for sub_item in desc:
                                project += "\n\\item{" + str(sub_item) + "}\n"
                            project += "\\end{itemize}\n"
                project += "\\end{itemize}\n"

        elif _item["name"] == "skill"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                skill += "%===============================SKILL========================\n"
                skill += "\\section{Skills}\n\n\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["desc"] == "":
                        item["desc"] = " "
                    skill += "\t\\item\\textcolor{bgcol}{\\textbf{" + str(item["title"]) + "}}"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            skill += "\\begin{itemize}"
                            for sub_item in desc:
                                skill += "\\item{" + str(sub_item) + "}\n"
                            skill += "\\end{itemize}"
                skill += "\n\\end{itemize}"

        elif _item["name"] == "award"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                award += "%===============================AWARD========================\n"
                award += "\\section{Awards}\n\\begin{itemize}"
                for item in _item["data"]:
                    if item["time"] == "":
                        item["time"] = " "
                    if item["org"] == "":
                        item["org"] = " "
                    award += "\\item\\textbf{" + str(item["title"]) + "}\\hfill{" + str(item["time"]) + "}\\\\{"+str(item["org"])+"}\\\\"
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
