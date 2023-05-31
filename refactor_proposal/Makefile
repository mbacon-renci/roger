all: pdf readme html

sources = $(shell ls *.md | grep -v README)

OUTPUT_BASENAME ?= refactor

$(OUTPUT_BASENAME).pdf: $(sources)
	pandoc --to=pdf --output $(OUTPUT_BASENAME).pdf $(sources)
pdf: $(OUTPUT_BASENAME).pdf

README.md: $(sources)
	cat $(sources) > README.md
readme: README.md

$(OUTPUT_BASENAME).html: $(sources)
	pandoc --to=html --output $(OUTPUT_BASENAME).html $(sources)
html: $(OUTPUT_BASENAME).html
