# ============================================================

# Example Makefile for blog post about research replication

#
# @author James Brusey
# @date 1/7/2020

# ============================================================


paper.pdf: paper.tex table1.tex
	latexmk paper

table1.tex: table1.csv
	python make_latex_table.py <$< >$@

table1.csv:
	python generate_some_data.py >$@
