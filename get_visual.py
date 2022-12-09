def plot_clustercategory_bar(df):
    category = df.groupby('category').count()['cluster'].sort_values(ascending=False)
    category.plot(kind='bar', color=['darkslateblue', 'midnightblue', 'royalblue', 'deepskyblue', 'lightskyblue',
                                        'mediumturquoise', 'paleturquoise'])