from os import environ
from pathlib import Path

root = Path(__file__).parent.parent
masses = sorted(set(x.parent.name for x in root.glob("**/*.copier-answers.yml")))
repo = environ["GITHUB_REPOSITORY"]
assert repo
printout_types = {"missalette": "Missalette", "missalette-booklet": "Missalette [Booklet]", "pew-sheet": "Pew Sheet", "pew-sheet-booklet": "Pew Sheet [Booklet]"}

holy_days_of_obligation = [
    'Dominica I Adventus', 'Dominica II Adventus', 'Dominica III Adventus', 'Dominica IV Adventus',
    'In Vigilia Nativitatis Domini', 'In Nativitate Domini',
    'Dominica Infra Octavam Nativitatis', 'Sanctissimi Nominis Jesu',
    'In Circumcisione Domini', 'In Epiphania Domini',
    'Sanctae Familiae Jesu Mariae Joseph', 'Dominica II Post Epiphaniam', 'Dominica III Post Epiphaniam', 'Dominica IV Post Epiphaniam', 'Dominica V Post Epiphaniam', 'Dominica VI Post Epiphaniam',
    'Dominica in Septuagesima', 'Dominica in Sexagesima', 'Dominica in Quinquagesima', 'Feria IV Cinerum',
    'Dominica I in Quadragesima', 'Dominica II in Quadragesima', 'Dominica III in Quadragesima', 'Dominica IV in Quadragesima', 'Dominica de Passione', 'Dominica in Palmis', 'Feria Quinta in Coena Domini', 'Feria Sexta in Passione et Morte Domini', 'Sabbato Sancto',
    'Dominica Resurrectionis', 'Dominica in Albis', 'Dominica II Post Pascha', 'Dominica III Post Pascha', 'Dominica IV Post Pascha', 'Dominica V Post Pascha', 'In Ascensione Domini', 'Dominica infra Octavam Ascensionis', 'Dominica Pentecostes',
    'Dominica Sanctissimae Trinitatis', 'Festum Sanctissimi Corporis Christi', 'Sacratissimi Cordis DNJC', 'Dominica II Post Pentecosten', 'Dominica III Post Pentecosten', 'Dominica IV Post Pentecosten', 'Dominica V Post Pentecosten', 'Dominica VI Post Pentecosten', 'Dominica VII Post Pentecosten', 'Dominica VIII Post Pentecosten', 'Dominica IX Post Pentecosten', 'Dominica X Post Pentecosten', 'Dominica XI Post Pentecosten', 'Dominica XII Post Pentecosten', 'Dominica XIII Post Pentecosten', 'Dominica XIV Post Pentecosten', 'Dominica XV Post Pentecosten', 'Dominica XVI Post Pentecosten', 'Dominica XVII Post Pentecosten', 'Dominica XVIII Post Pentecosten', 'Dominica XIX Post Pentecosten', 'Dominica XX Post Pentecosten', 'Dominica XXI Post Pentecosten', 'Dominica XXII Post Pentecosten', 'Dominica XXIII Post Pentecosten', 'Dominica XXIV et ultima Post Pentecosten',
    'Dominica III quae superfuit Post Epiphaniam', 'Dominica IV quae superfuit Post Epiphaniam', 'Dominica V quae superfuit Post Epiphaniam', 'Dominica VI quae superfuit Post Epiphaniam',
    'In Conceptione Immaculata BMV',
    'In Purificatione BMV',
    'S Joseph Sponsi BMV Confessoris',
    'SS Apostolorum Petri et Pauli',
    'In Assumptione BMV',
    'Nativitate BMV',
    'In Exaltatione Sanctae Crucis',
    'In Dedicatione S Michaelis Archangelis',
    'In Festo Domino Nostro Jesu Christi Regis',
    'Omnium Sanctorum'
    ]
# derived from divinum officium. this is a terrible way of storing data, but just so I have the missing ones marked

if __name__ == "__main__":
    assert Path(root, "releases.md").exists()
    releases = ["# Latest Releases", "| | | | | |", "| --- | --- | --- | --- | --- |"]
    for day in holy_days_of_obligation:
        mass = '-'.join(day.split())
        if mass not in masses:
            releases.append(f"| {day} | ***#todo*** |")
        else:
            links = [day]
            for p_type, p_typeF in printout_types.items():
                if Path(root, "pdfs", f"{mass}_{p_type}.pdf").exists():
                    links.append(f"[{p_typeF}](https://github.com/{repo}/releases/download/latest/{mass}_{p_type}.pdf)")
                else:
                    links.append("_not available_")
            releases.append(f"| {'|'.join(links)} |")
            masses.remove(mass)

    with open(Path(root, "releases.md"), "w") as f:
        f.write("\n".join(releases))

    if masses:
        print("Mass not found:", masses)