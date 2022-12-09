def plot_clustercategory_bar(df):
    from matplotlib import pyplot as plt
    import seaborn as sns
    sns.set_theme()

    category = df.groupby('category').count()['cluster'].sort_values(ascending=False)
    category.plot(kind='bar', color=['darkslateblue', 'midnightblue', 'royalblue', 'deepskyblue', 'lightskyblue',
                                        'mediumturquoise', 'paleturquoise'])

def plot_category_bar(df,column,formula):
    from matplotlib import pyplot as plt
    import seaborn as sns
    sns.set_theme()

    # To view the number of deaths according to Category in a pivot table
    pivot = df.pivot_table(index = 'category', values =column, aggfunc = formula)
    pivot = pivot.sort_values(column)  # ----To sort the values in ascending order
    pivot.plot(kind='bar', xlabel='Category', ylabel=column, color='green', legend=False)

def plot_clustertrend_heatmap(df):
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.set_theme()
    import warnings
    warnings.filterwarnings('ignore')

    #Dataframe Transformation
    cluster_casedist = df[['cluster','date_announced','category','cases_total']]
    cluster_casedist['date_announced'] = pd.to_datetime(cluster_casedist['date_announced'],yearfirst=True)

    #Pivot
    cluster_pivot = cluster_casedist.pivot_table(index=pd.Grouper(freq = 'W',key='date_announced'),columns='category',values='cases_total',aggfunc=np.sum,fill_value=0)
    cluster_pivot_week = cluster_pivot.resample('7D').sum().tail(25)

    #Heatmap Visualization
    f,ax = plt.subplots(figsize=(19, 25))
    y_axis_label = ['24 weeks ago','23 weeks ago','22 weeks ago','21 weeks ago','20 weeks ago','19 weeks ago','18 weeks ago','17 weeks ago','16 weeks ago','15 weeks ago','14 weeks ago','13 weeks ago','12 weeks ago','11 weeks ago','10 weeks ago','9 weeks ago','8 weeks ago','7 weeks ago','6 weeks ago','5 weeks ago','4 weeks ago','3 weeks ago','2 weeks ago','1 weeks ago','This week']
    plt.tick_params(axis='both', which='major', labelsize='large', labelbottom = False, bottom=False, top = False, labeltop=True)
    f.suptitle('Distribution of Cases in Clusters by Clusters Category',fontsize = 20,y=0.92)

    sns.heatmap(
        cluster_pivot_week,
        annot=True,
        annot_kws = {'size':15},
        fmt=".0f",
        linewidths=.5,
        ax=ax,
        linecolor ='black',
        cmap='Reds',
        cbar = False,
        yticklabels=y_axis_label
    ).invert_yaxis()

    ax.set_ylabel(ylabel = '')
    ax.set_xlabel(xlabel ='Cases in Clusters Distribution',loc = 'center')

def plot_correlation_heatmap(df):
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set_theme()

    # Correlation Coefficient(Pearson-Test) for multivariate features
    sns.set_theme(style="white")
    corr = df.corr()
    mask = np.triu(df.corr())
    f, ax = plt.subplots(figsize=(10, 5))
    cmap = sns.color_palette("Blues")

    vis3 = sns.heatmap(corr,
                       mask=mask,
                       cmap=cmap,
                       vmax=.3,
                       center=0,
                       square=True,
                       linewidths=3,
                       cbar_kws={"shrink": .5},
                       annot=True
                       )

    plt.title('''Correlation Coefficient (Pearson-Test) for Multivariate Features
    of Covid19 Clusters
    ''')