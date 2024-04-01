from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji

def words_count(df):

    words = []
    for message in df['message']:
        words.extend(message.split())
    return len(words)

def link_count(df):

    links = []
    extractor = URLExtract()
    for message in df['message']:
        links.extend(extractor.find_urls(message))
    return len(links)


def fetch_stats(selected_user, df):

    
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    num_media = df[df['message'] == '<Media omitted>\n'].shape[0]
    num_messages = df.shape[0]
    return num_messages, words_count(df), num_media, link_count(df)
    
def most_active_user(df):
    active_user = df['user'].value_counts().head()
    df = round((df['user'].value_counts()/df.shape[0])*100, 2).reset_index().rename(columns = {'index': 'name', 'user':'percent'})
    return active_user, df

def create_wordcloud(selected_user, df):
    
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color= '#dcf8c6')
    df_wc = wc.generate(df['message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user, df):

    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] == 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']
    temp = temp[temp['message'] != 'Messages and calls are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them. Tap to learn more.\n']

    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_words_df = pd.DataFrame(Counter(words).most_common(10))
    return most_common_words_df

def most_common_emoji(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend(s for s in message if emoji.is_emoji(s))
        
    emoji_counter = Counter(emojis)
    most_common_emojis = emoji_counter.most_common(len(emoji_counter))

    df_emojis = pd.DataFrame(most_common_emojis, columns=['Emoji', 'Count'])
    return df_emojis

def monthly_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + " - " + str(timeline['year'][i]))
    timeline['time'] = time
    return timeline

def daily_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline_df = df.groupby('only_date').count()['message'].reset_index()

    return daily_timeline_df

def week_activity(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

def time_activity(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]
    time_activity_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc = 'count').fillna(0)

    
    return time_activity_heatmap

