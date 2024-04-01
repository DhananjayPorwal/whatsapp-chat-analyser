# WhatsApp Chat Analyser 📈

## Objective 🎯

The objective of this project is to provide a tool for statistical and visual analysis of WhatsApp chat data. It allows users to gain insights into their chat history by analyzing various aspects such as message frequency, word usage, media sharing, links shared, and more.

## Demo Video

[![WhatsApp Chat Analyser Demo Video](https://raw.githubusercontent.com/DhananjayPorwal/whatsapp-chat-analyser/main/demo-screenshot.jpeg)](https://drive.google.com/file/d/1CLglp0d50_7h5RKumreh0X8gzdGpaDbG/view?usp=sharing)



## Installation ⚙️

To use the WhatsApp Chat Analyser, follow these steps:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/DhananjayPorwal/whatsapp-chat-analyser.git
   ```
2. Navigate to the project directory:
   ```bash
   cd whatsapp-chat-analyser
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit web app:
   ```bash
   streamlit run app.py
   ```
5. Upload your WhatsApp chat export file and start analyzing!

## Docker Installation and Usage 🐳

Alternatively, you can run the WhatsApp Chat Analyser using Docker. Follow these steps:

1. Ensure Docker is installed on your machine.
2. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/DhananjayPorwal/whatsapp-chat-analyser.git
   ```

3. Navigate to the project directory:
   ```bash
   cd whatsapp-chat-analyser
   ```
4. Build the Docker image:
   ```bash
   docker build -t whatsapp-chat-analyser .
   ```
5. Run a container using the following command:
   ```bash
   docker run -p 8501:8501 whatsapp-chat-analyser
   ```
6. Access the Streamlit web app from your browser at `http://localhost:8501`.

## WhatsApp Color Palette

<center><img src="https://i.imgur.com/m0w84VM.png" alt="alt-text" style="width:20%;">

| Hex       | RGB           |
| --------- | ------------- |
| `#075e54` | (7,94,84)     |
| `#128c7e` | (18,140,126)  |
| `#25d366` | (37,211,102)  |
| `#dcf8c6` | (220,248,198) |
| `#ece5dd` | (236,229,221) |

</center>

## Learning 📚

This project demonstrates the use of Streamlit for creating interactive web applications in Python. It also involves data preprocessing, statistical analysis, and data visualization techniques using pandas, matplotlib, seaborn, and other libraries.

## Conclusion 🌟

The WhatsApp Chat Analyser provides valuable insights into chat behavior, helping users understand their communication patterns, most active periods, frequently used words and emojis, and more. It can be a useful tool for personal reflection, group analysis, or even research purposes.

## Possible Use Cases 🚀

- Personal reflection and self-analysis of communication habits.
- Team communication analysis for project management or team dynamics assessment.
- Academic research on linguistic patterns, social dynamics, or sentiment analysis.
- Business intelligence for customer support analysis or marketing insights.

## Contribution Guidelines 🤝

Contributions to the WhatsApp Chat Analyser are welcome! If you have ideas for new features, improvements, or bug fixes, please feel free to open an issue or submit a pull request.

## Issues ❗

If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository. We appreciate your feedback and will work to address any concerns promptly.

## Reference 👥

- [Streamlit footer - 🎈 Using Streamlit - Streamlit](https://discuss.streamlit.io/t/streamlit-footer/12181)
- [st.set_page_config - Streamlit Docs](https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config)
- [HTML Link Colors (w3schools.com)](https://www.w3schools.com/html/html_links_colors.asp)
- [How do i change the app title and favicon? - 🎈 Using Streamlit - Streamlit](https://discuss.streamlit.io/t/how-do-i-change-the-app-title-and-favicon/1654/4)
- [Be able to change the title and favicon of a Streamlit app · Issue #1006 · streamlit/streamlit (github.com)](https://github.com/streamlit/streamlit/issues/1006)
- [WhatsApp Color Palette (color-hex.com)](https://www.color-hex.com/color-palette/110833)
- [WhatsApp Colors - Hex, RGB, CMYK, Pantone | Color Codes - U.S. Brand Colors (usbrandcolors.com)](https://usbrandcolors.com/whatsapp-colors/)
- [Hindi and Hinglish stop-words · Issue #2087 · nltk/nltk (github.com)](https://github.com/nltk/nltk/issues/2087)
- [HinglishNLP/data/assets/stop_hinglish at master · TrigonaMinima/HinglishNLP (github.com)](https://github.com/TrigonaMinima/HinglishNLP/blob/master/data/assets/stop_hinglish)
- [python - Find there is an emoji in a string in python3 - Stack Overflow](https://stackoverflow.com/questions/36216665/find-there-is-an-emoji-in-a-string-in-python3)
- [emoji · PyPI](https://pypi.org/project/emoji/)
- [Emoji: Extract, Analyze, and Get Insights — Python (advertools.readthedocs.io)](https://advertools.readthedocs.io/en/master/advertools.emoji.html)
- [Support (first font of) TTC files. by anntzer · Pull Request #9787 · matplotlib/matplotlib (github.com)](https://github.com/matplotlib/matplotlib/pull/9787)
