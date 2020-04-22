# Plotter.py

The plotter uses the pandas and MatPlotLib Library

It takes a text file with two column of values separated with a whitespace and outputs a png files with the plotted file

How to use it:

**Exemple:**

python3.7 plotter.py -i mean_news.txt mean_test.txt -o test.png -l test news

The **-i** argument is the input data file(s) you want to use to produce a graph

The **-o** argument is the png file outputed by the script

The **-l** argument is legend name(s) you'll give with respect to the input arguments

Exemple of usages :

With 1 argument :
    python3.7 plotter.py -i mean_news.txt -o test.png -l test

With Three arguments :

python3.7 plotter.py -i mean_news.txt mean_test.txt mean_testofnews -o test.png -l test news testofnews

