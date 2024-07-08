import streamlit as st

# Main function to render the Streamlit app
def main():
    st.title('Anurag Prasad - Portfolio')

    # About Me section
    st.header('About Me')
    st.write('CS Undergrad at VIT Bhopal, Open to technical roles.')

    # Projects section
    st.header('Projects')

    # First block of repositories
    st.subheader('Image Caption Generator')
    st.markdown('[image-description-deep-learning](https://github.com/anuragpras/image-description-deep-learning)', unsafe_allow_html=True)
    st.markdown('Image Caption Generator using Flickr dataset')
    st.markdown('---')  # Horizontal line after the project

    st.subheader('Cafe Sales Analysis')
    st.markdown('[cafe-sales-analysis](https://github.com/anuragpras/cafe-sales-analysis)', unsafe_allow_html=True)
    st.markdown('Detailed cafe sales analysis using Power BI and MySQL')
    st.markdown('---')  # Horizontal line after the project

    st.subheader('Amazon India Sales Dashboard')
    st.markdown('[amazon-india-sales-dashboard-tableau](https://github.com/anuragpras/amazon-india-sales-dashboard-tableau)', unsafe_allow_html=True)
    st.markdown('Interactive Tableau dashboard analyzing Amazon India\'s sales data')
    st.markdown('---')  # Horizontal line after the project

    st.subheader('COVID-19 Tableau Dashboard')
    st.markdown('[covid19-tableau](https://github.com/anuragpras/covid19-tableau)', unsafe_allow_html=True)
    st.markdown('Analyzing COVID-19 data using Tableau')
    st.markdown('---')  # Horizontal line after the project

    st.subheader('Exploratory Data Analysis')
    st.markdown('[exploratory-data-analysis](https://github.com/anuragpras/exploratory-data-analysis)', unsafe_allow_html=True)
    st.markdown('E-Commerce Sales Insights using Python')
    st.markdown('---')  # Horizontal line after the project

    st.subheader('Pizza Sales Analysis')
    st.markdown('[pizza-sales-analysis](https://github.com/anuragpras/pizza-sales-analysis)', unsafe_allow_html=True)
    st.markdown('Analyzing pizza sales data using MySQL and Excel')
    st.markdown('---')  # Horizontal line after the project

    st.subheader('Random Poetry Generator')
    st.markdown('[not-by-gulzar](https://github.com/anuragpras/not-by-gulzar)', unsafe_allow_html=True)
    st.markdown('Capture Gulzar\'s essence with playful verses')
    st.markdown('---')  # Horizontal line after the project

    st.subheader('Pomodoro App')
    st.markdown('[pomodoro-app](https://github.com/anuragpras/pomodoro-app)', unsafe_allow_html=True)
    st.markdown('Simple Pomodoro timer app')
    st.markdown('---')  # Horizontal line after the project

    st.subheader('Snake Game')
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
