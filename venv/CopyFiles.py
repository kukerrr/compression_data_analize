    # Python program to demonstrate
    # shutil.copytree()
    # importing modules

import datetime as dt



if(False):
    import shutil
# Source path
    src = 'C:/TSAGI/Docs/from'
# Destination path
    dest = 'C:/TSAGI/Docs/test'
# Copying the contents from Source
# to Destination without some
# specified files or directories
    shutil.copytree(src, dest, ignore=shutil.ignore_patterns('*.html', '*.jpeg' ,'test10*' ))



#print ( mcolors.CSS4_COLORS )
#print ( len(mcolors.CSS4_COLORS) )

def arr_to_floats(list_strings):
    result = []
    for i in list_strings:
        try:
            e = float(i)
            result.append(e)
        except:
            result.append(0)

    #print(result)
    return  result;

def removeFirstWhereNull( arrayx , arrayy):
    while( len(arrayx)>0 ):
        if( abs(arrayy[0])<0.1 ):
            del(arrayy[0])
            del(arrayx[0])
        else:
            return ;




def array_normolize(arrayY):
    for xt in arrayY:
        xt=xt -arrayY[0]

def delete_last(arrayX , arrayY):
    ind=0;
    #print( len(arrayX) )

    i =int( len(arrayX)/2 ) ;

    while( i< len(arrayX)-2):
        i+=1;
        if(  arrayX[i+1] < 0.9*arrayX[i] ):
            ind = i;
            break;

    if(ind!=0):
        del arrayX[ind:]
        del arrayY[ind:]


import os
from glob import glob

dest = 'C:/TSAGI/Docs/test'
#result = [y for x in os.walk(dest) for y in glob(os.path.join(x[0], '*.csv'))]
result = [y for x in os.walk(dest) for y in glob(os.path.join(x[0], '*dspH.csv'))]
#print( result );
#s= result[0];
#print( s );


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

norm_x_to_1 = lambda x,mx :[xs/mx  for xs in x];

len_max = len( mcolors.CSS4_COLORS )

#i =0;
#s= result[0]
#if(True):
#for s in result[1:2]:


print( "result len, count of experiments = " , len(result) )

#кол-во точек в данных
count_points = []

max_y =0;
#x_all=[]
#y_all=[]
all_pairs=[]


for s in result:
    df = pd.read_csv(s , sep=';',  encoding='latin-1')
    #print (df.columns)

    x = df.iloc[:, 1] #[-10:-1]
    y = df.iloc[:, 2] #[-10:-1]

    #x = df.iloc[:, 0] #[-10:-1]
    #print(x)

    count_points.append(  len(x) )
    #print( "x len = " , len(x), " y len =" , len(y) )

    #delete kH from strings
    remove_last = lambda x: [xs[:-2] for xs in x];

    x_f     = remove_last(x);
    x_tmp   = arr_to_floats(x_f);
    #print( 'x_f =' ,x_f)

    y_tmp=arr_to_floats(y);
    removeFirstWhereNull(x_tmp, y_tmp)

    #array_normolize(y_tmp)
    array_normolizeY = lambda y: [xs  - y[0] for xs in y];
    y_tmp =array_normolizeY(y_tmp)


    if(False):
        #print( "x_temp before = " , x_tmp)
        max_x = max(x_tmp)
        #print("xt before = ", x_tmp)
        x_tmp = norm_x_to_1(x_tmp, max_x)
        #print("x_temp after = ",x_tmp)

    delete_last(x_tmp, y_tmp)

    if( len(x_tmp) < 10 ):
        print("error")

    #int_max_count = max( len(x_tmp), int_max_count )
    max_y = max( max(y_tmp) , max_y )

    #print("x_tmp len = ", len(x_tmp), " y_tmp len =", len(y_tmp))
    #print('x_tmp =', x_tmp)
    #print('y_tmp =',y_tmp )
    #print('x_tmp =', x_tmp[-5:-1])
    #print('y_tmp =', y_tmp[-5:-1])

   #f1 = interp1d(x_tmp, y_tmp, kind='linear')

    all_pairs.append( [x_tmp,y_tmp] )
    #x_all.append(x_tmp )
    #y_all.append( y_tmp)

    if(False):
        plt.plot( y_tmp  , x_tmp  );

    plt.plot( x_tmp  , y_tmp  )

    plt.show();

    #color = mcolors.CSS4_COLORS[i]
plt.show();

import scipy
import scipy.interpolate as  sci
import scipy.stats
import numpy as np
#x_new = np.linspace(0.1, int_max_count, num=300)

y_new =np.arange(0.1, max_y, 0.1)

y_temp =np.arange(0.1, 7.3, 0.1)


all_to_teach=[]


####ITS FOR INTERPOLATE!!!
for pair in all_pairs:
    x=pair[0]
    y=pair[1]
   #print( max(y) )
   #y_dop = np.arange(0.1, max(y), 0.1)
    y_add = np.arange(max(y), max_y, 0.1)

    for t in y_add:
        y.append(t);
        x.append(0);

    f1 = sci.interp1d(y, x, kind='linear')

    x_new = f1(y_temp);
    plt.plot( y_temp, x_new)

    all_to_teach.append([x_tmp, y_tmp])

#descrepency


if (False):
    import scipy.stats
    import numpy as np
    print("count points = ",count_points)
    n_bins = len(count_points)
    plt.hist(count_points, bins=n_bins)
    #plt.set_title('hist of points len')
    plt.show()


# naming the x axis
plt.ylabel('sila')
# naming the y axis
plt.xlabel('datchik')
# giving a title to my graph
plt.title(s)
# function to show the plot
plt.show();



# for x in df.columns:
#     #print('x:', x)
#     #print ( df[x]  )
#
#     # x axis values
#     x = df[x]
#
#     # plotting the points
#     plt.plot(x, y)
#
#     # naming the x axis
#     plt.xlabel('x - axis')
#     # naming the y axis
#     plt.ylabel('y - axis')
#
#     # giving a title to my graph
#     plt.title('My first graph!')
#
#     # function to show the plot
#     plt.show()
