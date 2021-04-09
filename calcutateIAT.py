'''

This python script was used to calculate the IAT scores from data generated by PsychoPy script.

It is based on -

Greenwald, A. G., Nosek, B. A., & Banaji, M. R. (2003). Understanding and using the implicit association test: I. An improved scoring algorithm. Journal of personality and social psychology, 85(2), 1972-216.

'''

## -----------IMPORT LIBRARIES
import pandas as pd #for dealing with csv import
import os # for joining paths and filenames sensibly
import numpy as np #for the population std
import glob # for finding csv data files
import platform # paths use different dividers on linux vs windows, so we need to test for this
import csv

## -----------DEFINE FUNCTIONS


def adjustedmean(RTs,corrs,penalty):
    n=len(corrs) #trials
    n_errors=n-sum(corrs) #errors
    cor_RTs=np.array(corrs)*RTs #sum of correct RTs
    cor_mean=sum(cor_RTs)/sum(corrs)
    import csv
    #mean with errors replaced with penalty value
    return cor_mean+(n_errors*penalty)/n



def exclude_slows(RTs,corrs,slowRT_limit):
    new_rt=[] #holding variables
    new_cr=[]
    for i in range(len(RTs)): #iterate over every item
        if RTs[i] < slowRT_limit: #if it isn't too fast, include RT and corr values
            new_rt.append(RTs[i])
            new_cr.append(corrs[i])
    
    return (new_rt, new_cr)

## -----------DEFINE PARAMETERS
print "setting parameters"

penalty=0.600 #penalty - in seconds - for incorrect responses
slowRT_limit=10 #threshold at which slow RTs are discarded
fastRT_limit=0.300 #threshold which defines responses which are "too fast"
fast_prop_limit=0.1 # threshold proportion of "too fast" responses which defines exclusion of ppt

#where we expect the data files to be
search_string=os.path.join('..','data','*.csv') 
#we use os.path.join because the slashes go different ways on different operating systems
#ie path = '../IAT-1.1/data' #linux
#   path = '..\IAT-1.1\data' #windows

## -----------LOAD DATA
print "loading datafiles"

files = glob.glob(search_string) #list of data files in the named location

#the controls writing the results to a csvfile
with open('IATscores.csv', 'w') as csvfile:
    datwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #the first row of our output file is the headers
    datwriter.writerow(['file','IAT score', 'raw uncorrected', 'congruent mean RT','congruent RT sd', 'congruent error prop','incongruent mean RT','incongruent RT sd', 'incongruent error prop'])     
            
    #now iterate through all data files and calculate the IAT    
    for filename in files:
    
        #import into python using pandas
        df = pd.read_csv(filename)
        
        ## -----------EXTRACT DATA
        print "extracting data & calculating IAT"
        
        #extract the stuff we're interested in (n.b i am indexing using the column names defined in the csv)
        #dropna() drops nans
        #tolist() converts from series to list
        corrs=df['key_resp.corr'].dropna().tolist()
        rts=df['key_resp.rt'].dropna().tolist()
        block_length=int(len(corrs)/2)
        #find order 
        order=df['order'].tolist()[0]
        #1 congr then incong
        #2 incongr then congr

        if order==1:
            congr_corr=corrs[0:block_length]
            congr_rts=rts[0:block_length]
            incon_corr=corrs[block_length:]
            incon_rts=rts[block_length:]
        else:
            congr_corr=corrs[block_length:]
            congr_rts=rts[block_length:]
            incon_corr=corrs[0:block_length]
            incon_rts=rts[0:block_length]
                
        
        
