import requests, re


def get_raw_sequence(n):
    response = requests.get("https://oeis.org/A" + str(n))
    return str(response.content, response.apparent_encoding)


def get_description(n):
    contents = get_raw_sequence(n)
    return contents.split("<td valign=top align=left>")[1].split("<td width=2>")[0].strip()


def get_terms(n):
    contents = get_raw_sequence(n)
    a = contents.split("<tt>")[1].split("</tt>")[0].strip()
    return [int(i) for i in a.split(", ")]


def get_comments(n):
    contents = get_raw_sequence(n)
    a = contents.split("<tr>\n                         <td width=\"20\">\n                         <td valign=top "
                       "align=left width=100>\n                             <font size=-2>COMMENTS</font>\n           "
                       "              <td width=600>")[1].split("<tr>\n                         <td width=\"20\">\n   "
                                                                "                      <td valign=top align=left "
                                                                "width=100>\n                             <font "
                                                                "size=-2>REFERENCES</font>\n                         "
                                                                "<td width=600>")[0].strip().split("\n\n")
    b = [re.sub("<.*?>", "", i).strip() for i in a]
    return [i.replace("&quot;", "\"").replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&") for i in b]
