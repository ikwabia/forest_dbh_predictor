#Determining thinning intensity using the available data
#Data of Pure pine stand trees, before  thinning.
#average diameter of trees removed adapted from provided data = 11.07cm

#import excel file of tree_stand
import pandas as pd

tree_stand = pd.read_excel(r'C:\Users\Windows10\Desktop\Data\tree stand.xls', sheet_name='tree stand')
tree_stand
tree_stand[['PRE THINNED']].mean()

#a(average diameter of trees removed) = 11.07cm)
#b(tree_stand[['PRE THINNED']].mean())=37.065)
#thinning intensity(TI)
a, b = 11.07, 37.065
TI = a/b
print(format(TI,".2f"))

#Determining growth ehancement factor
µ=0.534   #constants, µ & ß are determined by non linear regression,
ß=0.0465       ##and they show the response of growth to thinning intensity
def g_f(µ,ß,TI):
    return µ*(TI+1)**ß
growth_enhancement_factor=g_f(µ,ß,TI)
print(growth_enhancement_factor)

#age(2018)
age=87
#AGE(2020)
AGE=89
dbh=43.7
def DBH_n(dbh,AGE,age,growth_enhancement_factor):
    return dbh*((AGE/age)**growth_enhancement_factor)
DBH_PROJECTION=DBH_n(dbh,AGE,age,growth_enhancement_factor)
print(DBH_PROJECTION)

T=[item*10  for item in range(5)]
print(T)

g=[item*float(0.2) for item in range(5)]
print(g)

%matplotlib inline
import matplotlib.pyplot as plt
plt.ioff();
def makegraph():
    fig, ax = plt.subplots( nrows=1, ncols=1, figsize=(10,5) )

    ax.plot( T, g, linewidth=3, marker='o', markersize=10, color='black', label='y=0.534(x+1)**0.047' )
    ax.set_ylabel( 'Growth enhancement factor', fontsize=14 )
    ax.set_xlabel( 'Thinning intensity [%] ', fontsize=14 )

    ax.legend()
    
    plt.show()
makegraph()

data_compare = pd.read_excel(r'C:\Users\Windows10\Desktop\Data\thinning intensity.xls', sheet_name='thinning intensity.xls')
data_compare

data_compare.describe()
import pandas as pd
import matplotlib.pyplot as plt
data_compare = pd.read_excel(r'C:\Users\Windows10\Desktop\Data\thinning intensity.xls', sheet_name='thinning intensity.xls')
data_compare
x = list(data_compare['ID'])
y = list(data_compare['FIELD COLLECTED DBH'])
z=list(data_compare['DBH PROJECTION'])

plt.figure(figsize=(10,10))
plt.style.use('seaborn')
plt.scatter(x,y,marker="*",s=100,edgecolors="black",c="red", label='DBH FROM FIELD DATA')
plt.scatter(x,z,marker="o",s=100,edgecolors="black",c="blue",label='DBH PREDICTOR')
plt.title("COMPARING OUTCOME OF  DBH PREDICTOR USING THINNING INTENSITY")
plt.xlabel("ID")
plt.ylabel("TREE DBH")


plt.legend()
plt.show()
