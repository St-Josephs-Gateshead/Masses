.PHONY: all
GTEX?=
MARIAN?=

all: missalette-booklet.pdf pew-sheet-booklet.pdf

%.pdf: %.tex
	env openout_any=a latexmk --pdflatex=lualatex --pdf $<

%.gtex: %.gabc
	openout_any=a gregorio $< -o $@

%-booklet.pdf: %.pdf
	pdfjam --landscape --suffix booklet --booklet true $<


amen.gtex: amen.gabc

GTEX += amen.gtex

dominus-vobiscum.gtex: dominus-vobiscum.gabc

GTEX += dominus-vobiscum.gtex

pax-domini.gtex: pax-domini.gabc

GTEX += pax-domini.gtex

preface.gtex: preface.gabc

GTEX += preface.gtex

sed-libera-nos.gtex: sed-libera-nos.gabc

GTEX += sed-libera-nos.gtex

sequenti.gtex: sequenti.gabc

GTEX += sequenti.gtex

introit.gtex: introit.gabc

GTEX += introit.gtex

offertory.gtex: offertory.gabc

GTEX += offertory.gtex

communion.gtex: communion.gabc

GTEX += communion.gtex



../Ordinaries/masses/8/kyrie.gtex: ../Ordinaries/masses/8/kyrie.gabc

GTEX += ../Ordinaries/masses/8/kyrie.gtex

../Ordinaries/masses/8/sanctus.gtex: ../Ordinaries/masses/8/sanctus.gabc

GTEX += ../Ordinaries/masses/8/sanctus.gtex

../Ordinaries/masses/8/agnus.gtex: ../Ordinaries/masses/8/agnus.gabc

GTEX += ../Ordinaries/masses/8/agnus.gtex

../Ordinaries/masses/8/ite.gtex: ../Ordinaries/masses/8/ite.gabc

GTEX += ../Ordinaries/masses/8/ite.gtex


../Ordinaries/credo/1/credo.gtex: ../Ordinaries/credo/1/credo.gabc

GTEX += ../Ordinaries/credo/1/credo.gtex



asperges.gtex: asperges.gabc

GTEX += asperges.gtex


../Ordinaries/masses/8/gloria.gtex: ../Ordinaries/masses/8/gloria.gabc

GTEX += ../Ordinaries/masses/8/gloria.gtex


gradual.gtex: gradual.gabc

GTEX += gradual.gtex


alleluia.gtex: alleluia.gabc

GTEX += alleluia.gtex



marian.gtex: marian.gabc

MARIAN_GTEX += marian.gtex


missalette.pdf: missalette.tex propers.tex styling.sty rubrics.sty titlepage.sty ${GTEX} ${MARIAN}

missalette-booklet.pdf: missalette.pdf

pew-sheet.pdf: pew-sheet.tex propers.tex styling.sty rubrics.sty ${MARIAN}

pew-sheet-booklet.pdf: pew-sheet.pdf


clean:
	find . -maxdepth 1 -name '*latexmk' -delete
	find . -maxdepth 1 -name '*.gtex' -delete
	find . -maxdepth 1 -name '*.fls' -delete
	find . -maxdepth 1 -name '*.log' -delete
	find . -maxdepth 1 -name '*.aux' -delete
	find . -maxdepth 1 -name '*.gaux' -delete
