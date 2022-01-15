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

    name, profile, person, link, homepage, phone,cityname = tuple("" for i in range(7))

    for _key, _val in data["profile"].items():
        if _key == "fullname"and _val != "":
            name += "\\MyName{"+str(_val)+"}\n"
        if _key == "email" or _key == "linked"  or _key == "homepage" or _key == "github" or _key == "facebook":
            if _val != "":
                link += "\\PersonalEntry{" + str(_key).capitalize() + "}{\\url{ " + str(_val) + "}}\n"
        if _key == "phone" or _key == "birth" :
            if _val != "" :
                person += "\\PersonalEntry{" +str(_key).capitalize()  + "}{" +  str(_val) + "}\n"
        profile +=  person + link

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
                desc1 += "\\NewPart{About Me}{}\n\\begin{itemize}\n\n"
                for item in _item["data"]:
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            for sub_item in desc:
                                desc1 += "\t\\item{" + str(sub_item) + "}\n"
                desc1 += "\\end{itemize}\n"

        if _item["name"] == "skill" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                skill += "\\NewPart{Skills}{}\n"
                for item in _item["data"]:
                    if item["desc"] == "":
                        item["desc"] = " "
                    skill += "\\SkillsEntry{\\bf{" + str(item["title"]) + "}}{"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            skill += "\n\t\\begin{itemize}"
                            for sub_item in desc:
                                skill += "\n\t\t\\item{" + str(sub_item) + "}"
                            skill += "\n\t\\end{itemize}"
                            skill += "\\sepspace\n"
                    skill += "}\n"

        elif _item["name"] == "education" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                education += "\\NewPart{" +str(_item["name"]).capitalize() + "}{}\n"
                for item in _item["data"]:
                    if item["degree"] == "":
                        item["degree"] = " "
                    if item["time"] == "":
                        item["time"] = " "
                    if item["org"] == "":
                        item["org"] = " "
                    if item["gpa"] == "":
                        item["gpa"] = " "
                    education += "\\sepspace\n\\EducationEntry{" + str(item["title"]) + "}{" + str(
                            item["time"]) + "}\n\t\t\t{" + \
                                     str(item["degree"]) + "}{GPA: " + str(item["gpa"]) + "}{" + str(item["org"]) + "}\n" "{"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            education += "\n\t\\begin{itemize}"
                            for sub_item in desc:
                                education += "\n\t\t\\item{" + str(sub_item) + "}"
                            education += "\n\t\\end{itemize}"
                    education += "}\\sepspace\n"

        elif _item["name"] == "experience" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["company"] != "":
                experience += "\\NewPart{" +str(_item["name"]).capitalize() + "}{}\n"
                for item in _item["data"]:
                    if item["pos"] == "":
                        item["pos"] = " "
                    if item["time"] == "":
                        item["time"] = " "
                    if item["loc"] == "":
                        item["loc"] = " "
                    experience += "\\sepspace\n\\WorkEntry{" + str(item["pos"]) + "}{" + str(item["time"]) +"}{" + str(item["company"]) + "\\\\"+str(item["loc"])+"}{"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            experience += "\n\t\\begin{itemize}"
                            for sub_item in desc:
                                experience += "\n\t\t\\item{" + str(sub_item) + "}"
                            experience += "\n\t\\end{itemize}"
                    experience += "}\\sepspace\n"
                experience += "\n\\divider\n"

        if _item["name"] == "project" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                project += "\\NewPart{Projects}{}\n"
                for item in _item["data"]:
                    if item["time"] == "":
                        item["time"] = " "
                    if item["desc"] == "":
                        item["desc"] = " "
                    project += "\\sepspace\n\\WorkEntry{"  + str(item["title"]) + "}{" + str(item["time"]) + "}{}\n{"
                    if len(item["desc"]) > 0:
                        if item["desc"][0] != "":
                            desc = item["desc"][0].strip("\n").split("\n")
                            project += "\n\t\\begin{itemize}"
                            for sub_item in desc:
                                project += "\n\t\t\\item{" + str(sub_item) + "}"
                            project += "\n\t\\end{itemize}"
                    project += "}\\sepspace\n"
                    project += "{}\n"


        if _item["name"] == "award" and _item["data"] != "" and _item["status"] == "on":
            if _item["data"][0]["title"] != "":
                award += "\\NewPart{Awards}{}\n"
                for item in _item["data"]:
                    if item["time"] == "":
                        item["time"] = " "
                    if item["org"] == "":
                        item["org"] = " "
                    award += "\\sepspace\n\\EducationEntry{" + str(item["title"]) + "}{" + str(
                        item["time"]) + "}\n\t\t\t{" + \
                                     str(item["org"]) + "}{}\n"
                    award += "\\sepspace\n"

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

    personal_info = person + link

    with open(media_path + "/person_info.tex" , "w", encoding="utf-8") as f:
        f.write(personal_info)
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
