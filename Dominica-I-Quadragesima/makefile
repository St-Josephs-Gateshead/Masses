.PHONY: all gabc

all: missalette-booklet.pdf pew-sheet-booklet.pdf

%.pdf: %.tex
	env openout_any=a latexmk --pdflatex=lualatex --pdf $<

%-booklet.pdf: %.pdf
	pdfjam --landscape --suffix booklet --booklet true $<

missalette.pdf: missalette.tex propers.tex styling.sty rubrics.sty titlepage.sty

missalette-booklet.pdf: missalette.pdf

pew-sheet.pdf: pew-sheet.tex propers.tex styling.sty rubrics.sty

pew-sheet-booklet.pdf: pew-sheet.pdf


clean:
	find . -maxdepth 1 -name '*latexmk' -delete
	find . -maxdepth 1 -name '*.gtex' -delete
	find . -maxdepth 1 -name '*.fls' -delete
	find . -maxdepth 1 -name '*.log' -delete
	find . -maxdepth 1 -name '*.aux' -delete
	find . -maxdepth 1 -name '*.gaux' -delete
