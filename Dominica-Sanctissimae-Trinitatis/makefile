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


introit.gtex: introit.gabc
GTEX += introit.gtex

gradual.gtex: gradual.gabc
GTEX += gradual.gtex

alleluia.gtex: alleluia.gabc
GTEX += alleluia.gtex

offertory.gtex: offertory.gabc
GTEX += offertory.gtex

communion.gtex: communion.gabc
GTEX += communion.gtex



../Ordinaries/masses/1/kyrie.gtex: ../Ordinaries/masses/1/kyrie.gabc
GTEX += ../Ordinaries/masses/1/kyrie.gtex

../Ordinaries/masses/1/gloria.gtex: ../Ordinaries/masses/1/gloria.gabc
GTEX += ../Ordinaries/masses/1/gloria.gtex

../Ordinaries/masses/1/sanctus.gtex: ../Ordinaries/masses/1/sanctus.gabc
GTEX += ../Ordinaries/masses/1/sanctus.gtex

../Ordinaries/masses/1/agnus.gtex: ../Ordinaries/masses/1/agnus.gabc
GTEX += ../Ordinaries/masses/1/agnus.gtex

../Ordinaries/masses/1/ite.gtex: ../Ordinaries/masses/1/ite.gabc
GTEX += ../Ordinaries/masses/1/ite.gtex



../Ordinaries/credo/1/credo.gtex: ../Ordinaries/credo/1/credo.gabc
GTEX += ../Ordinaries/credo/1/credo.gtex



../ToniCommunes/roman/amen.gtex: ../ToniCommunes/roman/amen.gabc
GTEX += ../ToniCommunes/roman/amen.gtex

../ToniCommunes/roman/asperges.gtex: ../ToniCommunes/roman/asperges.gabc
GTEX += ../ToniCommunes/roman/asperges.gtex

../ToniCommunes/roman/dominus-vobiscum.gtex: ../ToniCommunes/roman/dominus-vobiscum.gabc
GTEX += ../ToniCommunes/roman/dominus-vobiscum.gtex

../ToniCommunes/roman/pax-domini.gtex: ../ToniCommunes/roman/pax-domini.gabc
GTEX += ../ToniCommunes/roman/pax-domini.gtex

../ToniCommunes/roman/preface_standard.gtex: ../ToniCommunes/roman/preface_standard.gabc
GTEX += ../ToniCommunes/roman/preface_standard.gtex

../ToniCommunes/roman/sed-libera-nos.gtex: ../ToniCommunes/roman/sed-libera-nos.gabc
GTEX += ../ToniCommunes/roman/sed-libera-nos.gtex

../ToniCommunes/roman/sequenti.gtex: ../ToniCommunes/roman/sequenti.gabc
GTEX += ../ToniCommunes/roman/sequenti.gtex



../MarianAntiphons/roman/salve-regina.gtex: ../MarianAntiphons/roman/salve-regina.gabc
MARIAN += ../MarianAntiphons/roman/salve-regina.gtex
MARIAN += ../MarianAntiphons/salve-regina_resp.tex


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
