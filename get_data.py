def read_csv(folder, filename):
    import pandas as pd

    filepath = f'{folder}/{filename}.csv'
    df = pd.read_csv(filepath)

    return df
def convert_state_code(df):

    state_param = read_csv('epidemic/linelist','param_geo')
    state_param = state_param[159:][['state','idxs']].set_index('idxs')
    state_param.state = state_param.state.str.upper()
    state_param.index = state_param.index.astype('str')

    df2 = df.assign(state=df.state.str.split(","))[['state','cluster']].explode('state')
    df2.state = df2.state.map(state_param['state']).fillna('not stated')
    df2 = df2.groupby('cluster').agg({'state': lambda x: ",".join(x)})
    df2.rename(columns={'state':'state_join'},inplace=True)

    df.set_index('cluster',inplace=True)
    df3 = df.join(df2,how = 'inner')
    df3 = df3.reset_index()[['cluster','state_join','district','date_announced','date_last_onset','category','status','cases_new','cases_total','cases_active','tests','icu','deaths','recovered','summary_bm','summary_en']]
    df3.rename(columns={'state_join':'state'},inplace=True)

    return df3