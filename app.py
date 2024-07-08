import streamlit as st

# Main function to render the Streamlit app
def main():
    st.title('Anurag Prasad - Portfolio')

    # About Me section
    st.header('About Me')
    st.write('CS Undergrad at VIT Bhopal, open to all technical roles.')

    # Projects section
    st.header('Projects')

    # Project 1 - Image Caption Generator
    st.subheader('Image Caption Generator')
    st.image('1.gif', use_column_width=True)  # Ensure '1.gif' is in the root folder and the correct filename
    st.markdown('[image-description-deep-learning](https://github.com/anuragpras/image-description-deep-learning)', unsafe_allow_html=True)
    st.markdown('Image Caption Generator using Flickr dataset')
    st.markdown('---')  # Horizontal line after the project

    # Project 2 - Cafe Sales Analysis
    st.subheader('Cafe Sales Analysis')
    # st.image('2.gif', use_column_width=True)  # Ensure '2.gif' is in the root folder and the correct filename
    st.markdown('[cafe-sales-analysis](https://github.com/anuragpras/cafe-sales-analysis)', unsafe_allow_html=True)
    st.markdown('Detailed cafe sales analysis using Power BI and MySQL')
    st.markdown('---')  # Horizontal line after the project

    # Project 3 - Amazon India Sales Dashboard
    st.subheader('Amazon India Sales Dashboard')
    # st.image('3.gif', use_column_width=True)  # Ensure '3.gif' is in the root folder and the correct filename
    st.markdown('[amazon-india-sales-dashboard-tableau](https://github.com/anuragpras/amazon-india-sales-dashboard-tableau)', unsafe_allow_html=True)
    st.markdown('Interactive Tableau dashboard analyzing Amazon India\'s sales data')
    st.markdown('---')  # Horizontal line after the project

    # Project 4 - COVID-19 Tableau Dashboard
    st.subheader('COVID-19 Tableau Dashboard')
    # st.image('4.gif', use_column_width=True)  # Ensure '4.gif' is in the root folder and the correct filename
    st.markdown('[covid19-tableau](https://github.com/anuragpras/covid19-tableau)', unsafe_allow_html=True)
    st.markdown('Analyzing COVID-19 data using Tableau')
    st.markdown('---')  # Horizontal line after the project

    # Project 5 - Exploratory Data Analysis
    st.subheader('Exploratory Data Analysis')
    # st.image('5.gif', use_column_width=True)  # Ensure '5.gif' is in the root folder and the correct filename
    st.markdown('[exploratory-data-analysis](https://github.com/anuragpras/exploratory-data-analysis)', unsafe_allow_html=True)
    st.markdown('E-Commerce Sales Insights using Python')
    st.markdown('---')  # Horizontal line after the project

    # Project 6 - Pizza Sales Analysis
    st.subheader('Pizza Sales Analysis')
    # st.image('6.gif', use_column_width=True)  # Ensure '6.gif' is in the root folder and the correct filename
    st.markdown('[pizza-sales-analysis](https://github.com/anuragpras/pizza-sales-analysis)', unsafe_allow_html=True)
    st.markdown('Analyzing pizza sales data using MySQL and Excel')
    st.markdown('---')  # Horizontal line after the project

    # Project 7 - Random Poetry Generator
    st.subheader('Random Poetry Generator')
    # st.image('7.gif', use_column_width=True)  # Ensure '7.gif' is in the root folder and the correct filename
    st.markdown('[not-by-gulzar](https://github.com/anuragpras/not-by-gulzar)', unsafe_allow_html=True)
    st.markdown('Capture Gulzar\'s essence with playful verses')
    st.markdown('---')  # Horizontal line after the project

    # Project 8 - Pomodoro App
    st.subheader('Pomodoro App')
    # st.image('8.gif', use_column_width=True)  # Ensure '8.gif' is in the root folder and the correct filename
    st.markdown('[pomodoro-app](https://github.com/anuragpras/pomodoro-app)', unsafe_allow_html=True)
    st.markdown('Simple Pomodoro timer app')
    st.markdown('---')  # Horizontal line after the project

    # Project 9 - Snake Game
    st.subheader('Snake Game')
    # st.image('9.gif', use_column_width=True)  # Ensure '9.gif' is in the root folder and the correct filename
    st.markdown('[snake-game](https://github.com/anuragpras/snake-game)', unsafe_allow_html=True)
    st.markdown('Classic snake game implemented in Python')
    st.markdown('---')  # Horizontal line after the project

    # Contact section
    st.header('Contact')

    # Contact information with styled hyperlinks and aligned horizontally
    st.markdown('<style> a { text-decoration: none; color: #333333; } </style>', unsafe_allow_html=True)

    st.markdown('<div style="display: flex; flex-direction: row;">', unsafe_allow_html=True)

    st.markdown('<div style="flex: 1;">Personal Mail ID:<br><a href="mailto:ianuragprasad@gmail.com">ianuragprasad@gmail.com</a></div>', unsafe_allow_html=True)

    st.markdown('<div style="flex: 1;">University Mail ID:<br><a href="mailto:anurag.prasad@vitbhopal.ac.in">anurag.prasad@vitbhopal.ac.in</a></div>', unsafe_allow_html=True)

    st.markdown('<div style="flex: 1;">LinkedIn:<br><a href="https://www.linkedin.com/in/anuragpras">LinkedIn</a></div>', unsafe_allow_html=True)

    st.markdown('<div style="flex: 1;">GitHub:<br><a href="https://github.com/anuragpras">GitHub</a></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown('---')
    st.markdown("© 2024 Anurag Prasad")

if __name__ == '__main__':
    main()
