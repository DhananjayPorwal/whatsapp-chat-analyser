import streamlit as st
import preprocessing as pp
import helper as hl
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit Page Configuration

st.set_page_config(
    page_title="WhatsApp Chat Analyser",
    page_icon="📈",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'mailto:dporwal214@gmail.com',
        'Report a bug': "https://www.github.com/DhananjayPorwal/whatsapp-chat-analyser/issues",
        'About': "### Created by [Dhananjay Porwal](https://www.linkedin.com/in/dhananjayporwal/)"
    }
)

# Main Page
st.sidebar.title("WhatsApp Chat Analyser")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode('utf-8')
    df = pp.preprocess(data)
    original_df = df

    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")
    selected_user = st.sidebar.selectbox("Show analysis WRT", user_list)

    if st.sidebar.button("Show Analysis"):
        st.title("Top Statistics")

        # Stats
        num_messages, words, num_media, num_links = hl.fetch_stats(selected_user, df)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Media Shared")
            st.title(num_media)
        with col4:
            st.header("Links Shared")
            st.title(num_links)

        # Timeline
        st.title("Timeline")
        timeline = hl.time_activity(selected_user, df)
        fig, ax = plt.subplots()
        ax = sns.heatmap(timeline, cmap='Greens')
        st.pyplot(fig) 

        # Daily Timeline
        st.title("Daily Timeline")
        daily_timeline = hl.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        plt.plot(daily_timeline['only_date'], daily_timeline['message'], color = '#25D366')
        ax.set_facecolor('#dcf8c6')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)    

        # Monthly Timeline
        st.title("Monthly Timeline")
        monthly_timeline_df = hl.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        plt.plot(monthly_timeline_df['time'], monthly_timeline_df['message'], color = '#25D366')
        ax.set_facecolor('#dcf8c6')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # Activity Map
        st.title("Activity Map")
        
        col1,col2 = st.columns(2)

        with col1:
            st.header("Most Active Day")
            active_day = hl.week_activity(selected_user, df)
            fig,ax = plt.subplots()
            ax.bar(active_day.index, active_day.values, color = '#25D366')
            ax.set_facecolor('#dcf8c6')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.header("Most Month Day")
            active_month = hl.month_activity(selected_user, df)
            fig,ax = plt.subplots()
            ax.bar(active_month.index, active_month.values, color = '#25D366')
            ax.set_facecolor('#dcf8c6')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # Most Active Users
        if selected_user == 'Overall':
            st.title('Most Active User')
            active_user, new_df = hl.most_active_user(df)
            
            col1, col2 = st.columns(2)
            
            fig, ax = plt.subplots()

            with col1:
                ax.bar(active_user.index, active_user.values, color = '#25D366')
                ax.set_facecolor('#dcf8c6')
                plt.xticks(rotation= 'vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)


        # Word Cloud
        st.title("Word Cloud")
        df_wc = hl.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        plt.imshow(df_wc)
        st.pyplot(fig)



        # Most Common Words
        try:
            st.title("Most Common Words")

            col1, col2 = st.columns(2)
            
            most_common_words_df = hl.most_common_words(selected_user, df)
            
            with col1:
                fig, ax = plt.subplots()
                ax.barh(most_common_words_df[0], most_common_words_df[1], color = '#25D366')
                ax.set_facecolor('#dcf8c6')
                plt.xticks(rotation= 'vertical')
                st.pyplot(fig)


            with col2:
                st.dataframe(most_common_words_df)
        except:
            st.write("We cannot compare to oneself.")

        # Emoji Analysis
            
        st.title("Most Used Emojis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            emoji_df = hl.most_common_emoji(selected_user, df)
            st.dataframe(emoji_df)

        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df['Count'].head(), labels = emoji_df['Emoji'].head(), autopct="%0.2f")
            # ax.set_facecolor('#dcf8c6')

            st.pyplot(fig)


    # Original Data Frame

    st.header("Your WhatsApp Chat")
    st.dataframe(original_df)


# Footer Section

footer="""<style>
a:link , a:visited{
color: #075e54;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #dcf8c6;
color: #128c7e;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with 💖 by <a href="https://www.linkedin.com/in/dhananjayporwal/">Dhananjay Porwal</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)