    # Python program to demonstrate
    # shutil.copytree()
    # importing modules





if(False):
    import shutil
# Source path
    src = 'C:/TSAGI/Docs/from'
# Destination path
    dest = 'C:/TSAGI/Docs/test'
# Copying the contents from Source
# to Destination without some
# specified files or directories
    shutil.copytree(src, dest, ignore=shutil.ignore_patterns('*.html', '*.jpeg'))



import os
from glob import glob

dest = 'C:/TSAGI/Docs/test'
#result = [y for x in os.walk(dest) for y in glob(os.path.join(x[0], '*.csv'))]
result = [y for x in os.walk(dest) for y in glob(os.path.join(x[0], '*dspH.csv'))]

print( result );

s= result[0];
print( s );


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

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



len_max = len( mcolors.CSS4_COLORS )

#i =0;
#s= result[0]
#if(True):
for s in result[1:2]:
    df = pd.read_csv(s , sep=';',  encoding='latin-1')
    #print (df)

    print (df.columns)

    x = df.iloc[:, 1]
    print(x)

    #delete kH from strings
    remove_last = lambda x: [xs[:-2] for xs in x];

    x_f= remove_last(x);
    x_tmp= arr_to_floats(x_f);

    #ar_to_float =  lambda x: [ float( xt) for xt in  x];
    #x_f= ar_to_float( remove_last(x) );
    print( 'x_f =' ,x_f)
    print('x_tmp =', x_tmp)
    # for ( xs in  x ):
    #     Remove_last = xs[:-1];
    #     x_f.append( Remove_last );


    y = df.iloc[:, 2]
    #y_tmp=arr_to_floats(y)[14:-10];
    y_tmp=arr_to_floats(y);
    print('y_tmp =',y_tmp)
    #print ( y )
    #plt.plot(x, y   )
    plt.plot(x_tmp, y_tmp   )
    #color = mcolors.CSS4_COLORS[i]

# naming the x axis
plt.xlabel('sila')
# naming the y axis
plt.ylabel('datchik')

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
