from scipy import stats
import math
import pandas as pd
import numpy as np

## Graphs
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

################################################################################
##############  READABLE NUMBER ################################################
    
def readableNumbers(x):
    """
    Takes a large number and formats it into K,M to make it more readable
    Args:
        x: a number.
    Returns:
        A string easy to read information.
    Usage:
        # Use the readable_numbers() function to create a new column 
        df['readable'] = df['big_num'].apply(readable_numbers)

    """
    if x >= 1e6:
        s = '{:1.1f}M'.format(x*1e-6)
    else:
        s = '{:1.0f}K'.format(x*1e-3)
    return s

################################################################################
############## FEATURE OBSERVE  ################################################

def feature_observe(dataframe: pd.DataFrame):
    
    """
    Recieve a dataframe and check for null elements, 
    it returns a dictionary with keys: message, feature
    over 5% and features between 0 and 5%, and its values.
    
    Args:
        df(pd.DataFrame): a pandas DataFrame
    """
    
    # Running validation on the argument recieved
    assert type(dataframe) == pd.DataFrame, f'{dataframe}, is not a pandas df.'
    
    # assing and reset values
    df = dataframe
    feat_look = []
    feat_kill = []
    for i in df.columns:
        pct_miss = (df.isnull().sum() / df.isnull().count())
        if (df[i].isnull().sum() / df[i].isnull().count()) > 0.05:
            feat_kill.append(i) 
        elif (df[i].isnull().sum() / df[i].isnull().count()) > 0:
            feat_look.append(i)
        else: pass
    lenghts = [len(feat_look), len(feat_kill)]
    elementos = [feat_look, feat_kill]
    results = {
        "message" : f"{lenghts[0]} features are missing less than 5%. And \
        {lenghts[1]} features are missing more than 5%.",
        "features over 5%" : elementos[1], 
        "features less 5%" : elementos[0]
    }
    return results

################################################################################
######################### MISSING INFORMATION  #################################

def miss_df(dataframe: pd.DataFrame):
    """
    Take a pandas df as argument, returns another one
    with  basic information about missing data
    Args:
        df(pd.DataFrame): a pdDataFrame.
    """
    # Running validation on the argument recieved
    assert type(dataframe) == pd.DataFrame, f'{dataframe}, is not a pandas df.'
    df = dataframe
    total_missing = df.isnull().sum().sort_values(ascending=False)
    percent_missing = (df.isnull().sum()/df.isnull().count())\
    .sort_values(ascending=False)
    missing_data = pd.concat([total_missing, percent_missing], axis=1, \
                             keys=['Total', 'Percent'])
    return(missing_data.head(len(df.columns)))

################################################################################
#################   INVALID STRINGS   ##########################################

def invalid_df(dataframe: pd.DataFrame):
    """
    Take a pandas df as argument, looks for the items 
    in an invalid list. returns a pd df with
    the columns: column, nulls, invalids, 
    and the unique values.
    
    Args:
        df(pd.DataFrame): a pdDataFrame.
    """
    # Running validation on the argument recieved
    assert type(dataframe) == pd.DataFrame, f'{dataframe}, is not a pandas df.'
    df = dataframe
    
    invalid_list =\
    [np.nan, None, [], {}, 'NaN', 'Null','NULL'\
     ,'None','NA','?','-', '--','.','', ' ', '   ']
    
    columnas_con_invalidos = []
    nan_or_nones = []
    invalids = []
    uniques = []
    invalid_dict = {
        'column': columnas_con_invalidos,
        'nulls': nan_or_nones,
        'invalids': invalids, 
        'unique_item': []
    }
    for c in df.columns:
        string_null = np.array([x in invalid_list[2:] for x in df[c]])
        columnas_con_invalidos.append(c)
        nan_or_nones.append((df[c].isnull().sum()))
        invalids.append(string_null.sum())
        uniques.append(df[c].unique())
        invalid_dict = {
        'columns': columnas_con_invalidos,
        'nulls': nan_or_nones,
        'invalids': invalids,
        'unique_item': uniques
        }
        
    result = pd.DataFrame(invalid_dict)
    return(result.head(len(df.columns)))
 
################################################################################
###############  SIFT DATA BY THE PD.TYPES #####################################
    
def siftdatatype(dataframe: pd.DataFrame):
    """
    Recive a pandas data frame as an argument
    returns a dictionary with a message and 
    keys categorical and numerical, the values
    are two list each corresponding to the keys.
    
    Args:
        df(pd.DataFrame): a pdDataFrame.
    """
    # Running validation on the argument recieved
    assert type(dataframe) == pd.DataFrame, f'{dataframe}, is not a pandas df.'
    df = dataframe
    # groupping columns with numbers, dtypes can increase in types len.
    num_features = df.select_dtypes(['int64', 'float64']).columns.to_list()
    # groupping object columns
    cat_features = df.select_dtypes(['object']).columns.to_list()
    lenghts = [len(num_features), len(cat_features)]
    elementos = [num_features, cat_features]
    results = {
        "message" : f"{lenghts[0]} features are numerical and {lenghts[1]} \
        features are categorical.",
        "nums" : elementos[0], 
        "objs" : elementos[1]
    }
    return results

################################################################################
#######################   FILL IN MISSINGA VALUES      #########################

def filler_of_the_nans(technique, df, list_to_fill):
    """
    Fill in nans of a fill_list from a pandas df,
    the fill list should be defined by the technique to use. 
    The options are mean, median, mode or interpolation.
    Returns a copy of the original dataframe, but filled.

    Args:
        technique (list): a technique to use, from the list
        df(pd.DataFrame): a pdDataFrame.
        fill_list (pd.Series): pd.Series or list of Series with
        missing values. 
        
    """
    #Running validation on the argument recieved
    tecnicas = ('mean', 'median', 'interpolation', 'mode', 'None')
    assert type(df) == pd.DataFrame, f'{df} is not a pandas df.'
    assert technique in tecnicas, f'{technique} not in options:\
        [mean|median|interpolation|mode|None]'
    technique = technique
    # Deffining and populating a dataframe
    dff = pd.DataFrame()
    dff = df.copy()

    if technique == 'mean':
        for i in list_to_fill:
            dff.loc[:, i] =  dff.loc[:, i].fillna(dff.loc[:, i].mean())
        return dff
    elif technique == 'median':
        for i in list_to_fill:
            dff.loc[:, i] =  dff.loc[:, i].fillna(dff.loc[:, i].median())
        return dff
    elif technique == 'interpolation':
        for i in list_to_fill:
            dff.loc[:, i] =  dff.loc[:, i].fillna(dff.loc[:, i].interpolate())
        return dff
    elif technique == 'mode':
        for i in list_to_fill:
            dff.loc[:, i] =  dff.loc[:, i].fillna(dff.loc[:, i].mode()[0])
        return dff
    elif technique == 'None':
        for i in list_to_fill:
            dff.loc[:, i] =  dff.loc[:, i].fillna('None')
        return dff
   
    else: return dff

################################################################################
######################  HISTOGRAM OF DESIRED  FEATURES #########################

def histogramas(df, features):
    """
    Show histograma.
    Take a pandas dataframe and a list
    of columns

    Args:
        df: a pdDataFrame.
        features: pd.Series or list of Series with
        desire values. 
    """
    plt.figure(figsize = (10, 35))
    for i, feature in enumerate(features):
        ax = plt.subplot(10, 3, i + 1)
        ax.hist(df[feature], bins=25, color='Orange', edgecolor='black',\
               label=feature, alpha=0.2)
        ax.set_title(feature + 'histograma')
        plt.xticks(rotation=45)
        plt.tight_layout(pad=5.0)
        

################################################################################
####################  KURTOSIS AND SKEWNESS ####################################

def kurt_skew(df, features):
    """
    Kurtosis and Skewness report.
    Take a pandas dataframe and a list
    of columns
    Args:
        df: a pdDataFrame.
        features: pd.Series or list of Series with
            desire values. 
    Returns a package with 3 objects to unpack.
    (info, list of columns, 
    """
    kurt = stats.describe(df[features]).kurtosis
    skew = stats.describe(df[features]).skewness
    # if the column is gretter than 0.5 is skew
    info = pd.DataFrame({'column': df[features].columns, 'kurtosis': abs(kurt), \
                         'skewness': abs(skew)})
    info['need_transformation'] = info['kurtosis'].\
    apply(lambda x: True if x >= 0.5 else False)
    
    # numerical columns that are skew and need attention.
    skewColumns = info.query('need_transformation == True')['column'].values
    
    return(histogramas(df, skewColumns), skewColumns, info)
    

################################################################################
################################################################################
## mario.hevia@gmail.com #######################################################