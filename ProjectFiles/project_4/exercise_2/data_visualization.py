import pandas as pd
from ggplot import *
import pandasql
import datetime

def plot_weather_data(turnstile_weather):
    ''' 
    Use ggplot to make another data visualization focused on the MTA and weather
    data we used in assignment #3. You should make a type of visualization different
    than you did in exercise #1, and try to use the data in a different way (e.g., if you
    made a lineplot concerning ridership and time of day in exercise #1, maybe look at weather
    and try to make a histogram in exercise #2). 
    
    You should feel free to implement something that we discussed in class
    (e.g., scatterplots, line plots, or histograms) or attempt to implement 
    something more advanced if you'd like.  Here are some suggestions for things
    to investigate and illustrate:
    * Ridership by time of day or day of week
    * How ridership varies based on Subway station
    * Which stations have more exits or entries at different times of day

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
    
    You can check out: 
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
    
    However, due to the limitation of our Amazon EC2 server, we are giving you about 1/3
    of the actual data in the turnstile_weather dataframe
    '''

    #plot = ggplot(turnstile_weather, aes('EXITSn_hourly', 'ENTRIESn_hourly')) + stat_smooth(span=.15, color='black', se=True)+ geom_point(color='lightblue') + ggtitle("MTA Entries By The Hour!") + xlab('Exits') + ylab('Entries')
    df=turnstile_weather
    df.is_copy = False
    df['DOW']=df['DATEn'].apply(lambda x: datetime.datetime.strptime(x,'%Y-%m-%d').weekday())
    df.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)

    q = """
    select dow, hour, sum(entriesn_hourly) as entries
    from df
    Group By dow, hour order by entries desc;
    """
    dr = pandasql.sqldf(q, locals())

    plot = ggplot(dr,aes(x='hour',y='entries', fill='dow'))+geom_histogram(stat='bar')
    return plot

if __name__ == "__main__":
    image = "plot.png"
    input_filename = r'D:\Users\johnbaker\Desktop\NanoDegree\P1-AnalyzingTheNYCSubwayDataset\intro_to_ds_programming_files\project_4\exercise_1\turnstile_data_master_with_weather.csv'
    with open(image, "wb") as f:
        turnstile_weather = pd.read_csv(input_filename)
        turnstile_weather['datetime'] = turnstile_weather['DATEn'] + ' ' + turnstile_weather['TIMEn']
        gg =  plot_weather_data(turnstile_weather)
        ggsave(f, gg, format='png')