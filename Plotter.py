#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import chart_studio.plotly as pl
import plotly.offline as po
import cufflinks as cf


# In[2]:


po.init_notebook_mode(connected=True)
cf.go_offline()
#Use the plotly and cufflinks modules offline.

# In[3]:


def createdata(data):
    if data==1:
        x=np.random.rand(100,5)
        df1=pd.DataFrame(x,columns=['A','B','C','D','E'])
    elif data==2:
        x=[0,0,0,0,0]
        r1=[0,0,0,0,0]
        r2=[0,0,0,0,0]
        r3=[0,0,0,0,0]
        r4=[0,0,0,0,0]
        #Assume default values for rows and change using iteration.
        print('Enter the values for column')
        i=0
        for i in [0,1,2,3,4]:
            x[i]=input()
            i+=1
        print('Enter the values for first row')
        i=0
        for i in [0,1,2,3,4]:
            r1[i]=int(input())
            i+=1
        print('Enter the values for second row')
        i=0
        for i in [0,1,2,3,4]:
            r2[i]=int(input())
            i+=1
        print('Enter the values for third row')
        i=0
        for i in [0,1,2,3,4]:
            r3[i]=int(input())
            i+=1
        print('Enter the values for fourth row')
        i=0
        for i in [0,1,2,3,4]:
            r4[i]=int(input())
            i+=1
            
        df1=pd.DataFrame([r1,r2,r3,r4],columns=x)
    elif data==3:
        file=input('Enter the name of the file')
        x=pd.read_csv(file)
        df1=pd.DataFrame(x)
    else:
        print('Dataframe creation failed please enter a number between 1 to 3')
    return df1


# In[4]:


def plotter(plot):
    if plot==1:
        finalplot=df1.iplot(kind='scatter')
    elif plot==2:
        finalplot=df1.iplot(kind='scatter',mode='markers')
        #Convert mode to markers for scatter plot to disapper the line.
    elif plot==3:
        finalplot=df1.iplot(kind='bar')
    elif plot==4:
        finalplot=df1.iplot(kind='hist')
    elif plot==5:
        finalplot=df1.iplot(kind='box')
    elif plot==6:
        finalplot=df1.iplot(kind='surface')
    else:
        finalplot=print('Select from 1 to 7')
    return finalplot


# In[5]:


def plotter2(plot):
    col=int(input('Enter the number of columns you want to plot 1,2 or 3'))
    if col==1:
        colm=input('Enter the column from the dataframe above')
        if(plot==1):
            finalplot = df1[colm].iplot(kind='scatter')
        elif(plot==2):
            finalplot = df1[colm].iplot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')
        elif(plot==3):
            finalplot = df1[colm].iplot(kind='bar')
        elif(plot==4):
            finalplot = df1[colm].iplot(kind='hist')
        elif(plot==5):
            finalplot = df1[colm].iplot(kind='box')
        elif(plot==6 or plot==7):
            finalplot = print('Bubble plot and surface plot require more than one column arguments')
        else:
            finalplot = print('Select only between 1 to 7')
    #For 2 or 3 columns use indexing of dataframe using list.
    elif col==2:
        print('Enter the columns you want to plot')
        x=input('Enter the first column')
        y=input('Enter the second column')
        
        if(plot==1):
            finalplot = df1[[x,y]].iplot(kind='scatter')
        elif(plot==2):
            finalplot = df1[[x,y]].iplot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')
        elif(plot==3):
            finalplot = df1[[x,y]].iplot(kind='bar')
        elif(plot==4):
            finalplot = df1[[x,y]].iplot(kind='hist')
        elif(plot==5):
            finalplot = df1[[x,y]].iplot(kind='box')
        elif(plot==6):
            finalplot = df1[[x,y]].iplot(kind='surface')
        elif(plot==7):
            size = input('Please enter the size column for bubble plot')
            finalplot = df1.iplot(kind='bubble' , x=x,y=y,size=size)
        else:
            finalplot = print('Select only between 1 to 7')
    #Size should be taken for the bubble plot.
    elif(col==3):
        print('Enter the columns you want to plot')
        x=input('First column')
        y=input('Second column')
        z=input('Third column')
        if(plot==1):
            finalplot = df1[[x,y,z]].iplot(kind='scatter')
        elif(plot==2):
            finalplot = df1[[x,y,z]].iplot(kind='scatter' , mode='markers' , symbol='x' ,colorscale='paired')
        elif(plot==3):
            finalplot = df1[[x,y,z]].iplot(kind='bar')
        elif(plot==4):
            finalplot = df1[[x,y,z]].iplot(kind='hist')
        elif(plot==5):
            finalplot = df1[[x,y,z]].iplot(kind='box')
        elif(plot==6):
            finalplot = df1[[x,y,z]].iplot(kind='surface')
        elif(plot==7):
            size = input('Please enter the size column for bubble plot')
            finalplot = df1.iplot(kind='bubble' , x=x,y=y,z=z,size=size )
        else:
            finalplot = print('Select only between 1 to 7')
    else:
        finalplot = print('Please enter only 1 , 2 or 3')
    return finalplot


# In[7]:


def main(cat):
    if cat==1:
        print('1.Line plot')
        print('2.Scatter plot')
        print('3.Bar plot')
        print('4.Histogram')
        print('5.Box plot')
        print('6.Surface plot')
        plot = int(input())
        output = plotter(plot)
    elif(cat == 2):
        print('Select the type of plot you need to plot by writing 1 to 7')
        print('1.Line plot')
        print('2.Scatter plot')
        print('3.Bar plot')
        print('4.Histogram')
        print('5.Box plot')
        print('6.Surface plot')
        print('7.Bubble plot')
        plot = int(input())
        output = plotter2(plot)
    else:
        print('Please enter 1 or 2 and try again')
        


# In[8]:


print('Select the type of Data')
print('1.Random number between 0 and 100 with 5 columns')
print('2.Create a customised dataframe with 5 columns and 4 rows')
print('3.Upload a csv/json file')
data=int(input())
df1=createdata(data)


# In[9]:


print('The columns to be plotted are given below')
df1.head()


# In[10]:


print('What kind of plot do you need?, the complete plot or the specified columns plot')
cat=int(input('Enter 1 for complete plot and 2 for specific columns plot'))


# In[16]:


main(cat)


# In[ ]:





# In[ ]:




