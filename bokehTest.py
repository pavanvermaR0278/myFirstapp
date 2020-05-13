#importing bokeh
from bokeh.plotting import figure
from bokeh.io import output_file,show
import pandas
#prepare some datax

df=pandas.read_csv("data.csv")
print(df)
x=df["x"]
y=df["y"]
#x=[1,2,3,4,5]
#y=[6,7,8,9,10]

#prepre the output file
#output_file("Line.html")
output_file("Line_from_cdv.html")

#create  a  figure object
f=figure()

#create line plot
f.circle_x(x,y)

#write the plot in the figure object
show(f)