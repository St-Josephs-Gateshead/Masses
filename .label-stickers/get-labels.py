"""
A little script to make qr-code label stickers with links to the completed pdf files.

(- Update `labels` and `web_link`, if necessary)
- Run this file
- Make label-make.tex
"""

labels = ["Dominica I Adventus",
"Dominica II Adventus",
"Dominica III Adventus",
"Dominica IV Adventus",
"In Vigilia Nativitatis Domini",
"In Nativitate Domini in nocte",
"In Nativitate Domini in aurora",
"In die Nativitatis Domini",
"Dominica infra Octavam Nativitatis",
"Sanctissimi Nominis Jesu",
"In Circumcisione Domini",
"In Epiphania Domini",
"Sanctae Familiae Jesu Mariae Joseph",
"Dominica II Post Epiphaniam",
"Dominica III Post Epiphaniam",
"Dominica IV Post Epiphaniam",
"Dominica V Post Epiphaniam",
"Dominica VI Post Epiphaniam",
"Dominica in Septuagesima",
"Dominica in Sexagesima",
"Dominica in Quinquagesima",
"Feria IV Cinerum",
"Dominica I in Quadragesima",
"Dominica II in Quadragesima",
"Dominica III in Quadragesima",
"Dominica IV in Quadragesima",
"Dominica de Passione",
"Dominica in Palmis",
"Feria Quinta in Coena Domini",
"Feria Sexta in Passione et Morte Domini",
"Sabbato Sancto",
"Dominica Resurrectionis",
"Dominica in Albis",
"Dominica II Post Pascha",
"Dominica III Post Pascha",
"Dominica IV Post Pascha",
"Dominica V Post Pascha",
"In Ascensione Domini",
"Dominica infra Octavam Ascensionis",
"Dominica Pentecostes",
"Dominica Sanctissimae Trinitatis",
"Festum Sanctissimi Corporis Christi",
"Sacratissimi Cordis DNJC",
"Dominica II Post Pentecosten",
"Dominica III Post Pentecosten",
"Dominica IV Post Pentecosten",
"Dominica V Post Pentecosten",
"Dominica VI Post Pentecosten",
"Dominica VII Post Pentecosten",
"Dominica VIII Post Pentecosten",
"Dominica IX Post Pentecosten",
"Dominica X Post Pentecosten",
"Dominica XI Post Pentecosten",
"Dominica XII Post Pentecosten",
"Dominica XIII Post Pentecosten",
"Dominica XIV Post Pentecosten",
"Dominica XV Post Pentecosten",
"Dominica XVI Post Pentecosten",
"Dominica XVII Post Pentecosten",
"Dominica XVIII Post Pentecosten",
"Dominica XIX Post Pentecosten",
"Dominica XX Post Pentecosten",
"Dominica XXI Post Pentecosten",
"Dominica XXII Post Pentecosten",
"Dominica XXIII Post Pentecosten",
"Dominica XXIV et ultima Post Pentecosten",
"Dominica III quae superfuit Post Epiphaniam",
"Dominica IV quae superfuit Post Epiphaniam",
"Dominica V quae superfuit Post Epiphaniam",
"Dominica VI quae superfuit Post Epiphaniam",
"In Conceptione Immaculata BMV",
"In Purificatione BMV",
"S Joseph Sponsi BMV Confessoris",
"SS Apostolorum Petri et Pauli",
"In Assumptione BMV",
"Nativitate BMV",
"In Exaltatione Sanctae Crucis",
"In Dedicatione S Michaelis Archangelis",
"In Festo Domino Nostro Jesu Christi Regis",
"Omnium Sanctorum",
"In Commemoratione Omnium Fidelium Defunctorum"]
web_link = "https://st-josephs-gateshead.github.io/"

output = []
for l in labels:
    l_ = '-'.join(l.split())
    b = f"{web_link}\\#{l_}_missalette-booklet"
    m = f"{web_link}\\#{l_}_missalette"
    output.append(rf"\addresslabel{{\qrcode{{{m}}} \rotatebox[origin=c]{{90}}{{\small\textsc{{Missalette}}}}\hspace*{{\fill}}\rotatebox[origin=c]{{90}}{{\small\textsc{{Booklet}}}} \qrcode{{{b}}}\\\centering{{\texttt{{{l}}}}}}}")

with open("labels.tex", "w") as f:
    f.write('\n'.join(output))