# Matplotlib Cheatsheet

Matplotlib is a library which provides building blocks to create rich data visualisation for different datasets

> Most of the Matplotlib utilities lies under the pyplot submodule

> *Sample Code can be found **[here](notebooks/Matplotlib.ipynb)***
<br>

## Installing Matplotlib library
`pip install matplotlib`

<br>

## Import Matplotlib subpackage Pyplot 
 `import matplotlib.pyplot as plt  `

<br>

## Functions

### Plotting x and y
`plt.plot(x_points, y_points)`
> ***x_points*** is an array containing the points on the x-axis

> ***y_points*** is array containing the points on the y-axis

> `plt.plot(x_points, y_points, 'o')` plots the points without a line

<br>


### Plotting default-x points
`plt.plot(y_points)`
> ***y_points*** is array containing the points on the y-axis

<br>

### Markers
`plt.plot(x_points, y_points, '*')`
> **`*`**  is a marker; the library offers different markers that can specify size, color etc.

<br>

### LineStyle
`plt.plot(x_points, y_points, linestyle = 'dotted')`
> ***linestyle*** can be written as ls<br>
> Different lineStyles are: *solid*(default), *dotted*, *dashed*, *dashdot*, *None*

> *lines can also have colors and width specifications*

<br>

### Labels for a Plot
`plt.xlabel("X-Axis")`

`plt.ylabel("Y-Axis")`

<br>

### Title for a Plot
`plt.title("Title of Plot")`

<br>

### Font Properties for Title and Labels
> We can use ***fontdict*** parameter in xlabel( ), ylabel( ), and title( ) to set font properties for the title and labels.

> ***Example*** <br>
`plt.title("Sports Watch Data", fontdict = {'family':'serif', 'color':'blue', 'size':20} )`

<br>

### To display the plot 
`plt.show()`
> An explicit command required to display the plot 

<br>

## Barplots 
*A bar graph is helpful when you have to visualise a numeric feature (fact) across multiple categories.*

To draw a bar graph: <br>
`plt.bar(x_component, y_component)`

<br>

 ### Horizontal Bar Graphs 
`plt.barh(x_component, y_component)`

<br>

 ### Bar Color, Width 
> To specify color<br>
`plt.bar(x_component, y_component, color="red")`

> To specify width<br>
`plt.bar(x_component, y_component, width=0.6)`

<br>

 ### Tick values and label :
`plt.yticks(tick_values, tick_labels)`
 
## Scatterplots
*Scatterplots display the scatter of data.* 

It can be helpful in checking for any relationship pattern between two quantitative variables and detecting the presence of outliers within them.

### To draw a scatterplot
`plt.scatter(x_axis, y_axis)`

`plt.scatter(x_axis, y_axis, c = color, label = labels)`
> *all the parameters (x_axis, y_axis, colour, labels) need to be provided in the form of a list or array*

<br>

### To add a note (to annotate) in the scatterplot
`plt.annotate(text, xy = points_to_annotate_xy)`<br>

### Setting the transparency of points in a scatterplot
`plt.scatter(x_axis, y_axis, alpha=0.5)`

<br>

## Line Graphs
*A line graph is used to present continuous time-dependent data.*

It accurately depicts the trend of a variable over a specified time period.

### Plotting a line Graph
`plt.plot(x_axis, y_axis)`

<br>

###  Line plot with the points marked
`plt.plot(y, 'red', marker = 'o')`

<br>

###  To rotate the labels on the axes
`plt.yticks(rotation = number)`
> *can be done for xticks as well*

<br>

 ## Histogram
 *A histogram is a frequency chart that records the occurrence of an entry or an element in a data set.*

It is useful when you want to understand the distribution of a given series.

### Plotting a Histogram
`plt.hist(input, bins = number_of_bins, edgecolor = "color", color = "color")`
 
 <br>

 ## Box Plots
*Box plots are very effective in summarising the spread of large data into a visual representation.*

They take the help of percentiles to divide the data range. 

### Creating a Box Plot
`plt.boxplot([ list_1, list_2])`
<br>

### Box plots divide the data range into three important categories:
  > **Median value**<br>
   > This is the value that divides the data range into two equal halves, that is, the 50th percentile.

  > **Interquartile range (IQR)**<br>
   > These are data points between the 25th and 75th percentile values.

  > **Outliers:**<br>
   > These are data points that differ significantly from other observations and lie beyond the whiskers.
  
