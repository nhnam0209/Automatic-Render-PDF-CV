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

    name, name1, profile, person, link, profile1, image  = tuple("" for i in range(7))

    for _key, _val in data["profile"].items():
        if _key == "fullname" and _val != "":
            name1 += "\\vspace{-20pt}\n\\hspace{-0.25\\linewidth}\\colorbox{bgcol}" \
                     "{\n\\makebox[1.5\\linewidth][c]{\n\\HUGE{\\textcolor{white}{" + str(_val) \
                     + "}}\n\\textcolor{sectcol}{\\rule[-1mm]{1mm}{0.9cm}}\n\\HUGE{\\textcolor{white}{\\textsc{CV}}}}}\n\\vspace{10pt}"
        if _key == "birth" or _key == "phone" or _key == "email" or _key == "linked"  or _key == "homepage" or _key == "github" or _key == "facebook"  :
            if  _val != "":
                person += "\n\\metasection{"+str(_key).capitalize() +": }{"+str(_val)+"}"

        profile = person

    if data["image"]["status"] == "on" and data["image"]["avatar"] != None:
        decodeIMG(data["image"]["avatar"], media_path)
        image += "\n\\begin{figure}[H]\n\\begin{flushright}\n\\includegraphics[height=5cm,width=4cm]{avatar.png}\n\\end{flushright}\n\\end{figure}"


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
                desc1 += "\\cvsection{ABOUT ME}\n\\begin{itemize}\n\n"
                for item in _item["data"]:
                    if item["desc"][0] != "":
                        desc = item["desc"][0].strip("\n").split("\n")
                        if len(item["desc"]) > 0:
                            for sub_item in desc:
                                desc1 += "\t\\item{" + str(sub_item) + "}\n"
                desc1 += "\\end{itemize}\n"

        if _item["name"] == "education"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                education += "%===============================EDUCATION========================\n"
                education += "\\cvsection{EDUCATION}\n"
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
                    education += "\\item \\textcolor{bgcol}{\\textbf{" + str(item["title"]) + "}}\\hfill{" + str(item["time"]) + \
                                     "}\\\\\\textbf{" + str(item["degree"]) + "}  \\textitt{GPA: "+str(item["gpa"])+"}\\\\{" + str(item["org"]) + "}\\\\"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            education += "\\\\"
                            for sub_item in desc:
                                education += "\n\\cvdetail{" + str(sub_item) + "}"
                education += "\\end{itemize}\n"

        elif _item["name"] == "experience"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["company"] != "":
                experience += "%===============================EXPERIENCE========================\n"
                experience += "\\cvsection{EXPERIENCE}\n"
                experience += "\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["pos"] == "":
                        item["pos"] = " "
                    if item["time"] == "":
                        item["time"] = " "
                    if item["loc"] == "":
                        item["loc"] = " "
                    experience += "\\item \\textcolor{bgcol}{\\textbf{" + str(item["pos"]) + "}}\\hfill{" + str(item["time"]) + \
                                     "}\\\\\\textbf{" + str(item["company"]) + "}\\\\{" + str(item["loc"]) + "}\\\\"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            experience += "\\\\"
                            for sub_item in desc:
                                experience += "\n\\cvdetail{" + str(sub_item) + "}\\\\\n"
                experience += "\\end{itemize}\n"

        elif _item["name"] == "project"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                project += "%===============================PROJECT========================\n"
                project += "\\cvsection{PROJECTS}\n"
                project += "\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["time"] == "":
                        item["time"] = " "
                    if item["desc"] == "":
                        item["desc"] = " "
                    project += "\t\\item \\textcolor{bgcol}{\\textbf{" + str(item["title"]) + "}}\\hfill{" + str(item["time"]) + "}{}\\\\"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            project += "\\\\"
                            for sub_item in desc:
                                project += "\n\\cvdetail{" + str(sub_item) + "}\n"
                project += "\\end{itemize}\n"

        elif _item["name"] == "skill"and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                skill += "%===============================SKILL========================\n"
                skill += "\\cvsection{SKILLS}\n\n\\begin{itemize}\n"
                for item in _item["data"]:
                    if item["desc"] == "":
                        item["desc"] = " "
                    skill += "\t\\item\\textcolor{bgcol}{\\textbf{" + str(item["title"]) + "}}\\\\"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            skill += "\\\\"
                            for sub_item in desc:
                                skill += "\\cvdetail{" + str(sub_item) + "}\n"
                skill += "\n\\end{itemize}"

        elif _item["name"] == "award" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                award += "%===============================AWARD========================\n"
                award += "\\cvsection{AWARDS}\n"
                for item in _item["data"]:
                    if item["time"] == "":
                        item["time"] = " "
                    if item["org"] == "":
                        item["org"] = " "
                    award += "\t\\cvevent{" + str(item["time"]) + "}{" + str(item["title"]) + "}{"+str(item["org"])+"}\\\\"
    body1 =""
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
        body1 += "\\input{image.tex}\n\\vspace{-150pt}\n\\input{PROFILE.tex}"
    else:
        body1 += "\n\\vspace{20pt}\n\\input{PROFILE.tex}"

    with open(media_path + "/name.tex", "w", encoding="utf-8") as f:
        f.write(name1)
    with open(media_path + "/image.tex", "w", encoding="utf-8") as f:
        f.write(image)
    with open(media_path + "/PROFILE.tex", "w", encoding="utf-8") as f:
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
    with open(media_path + "/Header.tex", "w", encoding="utf-8") as f:
        f.write(body1)