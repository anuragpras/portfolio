import streamlit as st

# Main function to render the Streamlit app
def main():
    st.title('Anurag Prasad - Portfolio')

    # About Me section
    st.header('About Me')
    st.write('CS Undergrad at VIT Bhopal, open to all technical roles.')

    # Projects section
    st.header('Projects')

    # Two columns layout for projects
    col1, col2 = st.columns(2)

    # First block of repositories
    with col1:
        st.subheader('Image Caption Generator')
        st.markdown('[Image Caption Generator](https://github.com/anuragpras/image-description-deep-learning)')
        st.markdown('Image Caption Generator using Flickr dataset')

        st.subheader('Cafe Sales Analysis')
        st.markdown('[Cafe Sales Analysis](https://github.com/anuragpras/cafe-sales-analysis)')
        st.markdown('Detailed cafe sales analysis using Power BI and MySQL')

        st.subheader('Amazon India Sales Dashboard')
        st.markdown('[Amazon India Sales Dashboard](https://github.com/anuragpras/amazon-india-sales-dashboard-tableau)')
        st.markdown('Interactive Tableau dashboard analyzing Amazon India\'s sales data')

        st.subheader('COVID-19 Tableau Dashboard')
        st.markdown('[COVID-19 Tableau Dashboard](https://github.com/anuragpras/covid19-tableau)')
        st.markdown('Analyzing COVID-19 data using Tableau')

    # Second block of repositories
    with col2:
        st.subheader('Exploratory Data Analysis')
        st.markdown('[Exploratory Data Analysis](https://github.com/anuragpras/exploratory-data-analysis)')
        st.markdown('E-Commerce Sales Insights using Python')

        st.subheader('Pizza Sales Analysis')
        st.markdown('[Pizza Sales Analysis](https://github.com/anuragpras/pizza-sales-analysis)')
        st.markdown('Analyzing pizza sales data using MySQL and Excel')

        st.subheader('Random Poetry Generator')
        st.markdown('[Random Poetry Generator](https://github.com/anuragpras/not-by-gulzar)')
        st.markdown('Capture Gulzar\'s essence with playful verses')

        st.subheader('Pomodoro App')
        st.markdown('[Pomodoro App](https://github.com/anuragpras/pomodoro-app)')
        st.markdown('Simple Pomodoro timer app')

        st.subheader('Snake Game')
        st.markdown('[Snake Game](https://github.com/anuragpras/snake-game)')
        st.markdown('Classic snake game implemented in Python')

    # Contact section
    st.header('Contact')
    st.markdown('**Gmail**')
    st.image('assets/gmail-icon.png', width=30)
    st.markdown('[ianuragprasad@gmail.com](mailto:ianuragprasad@gmail.com)')
    st.image('assets/gmail-icon.png', width=30)
    st.markdown('[anurag.prasad@vitbhopal.ac.in](mailto:anurag.prasad@vitbhopal.ac.in)')
    st.markdown('**LinkedIn**')
    st.image('assets/linkedin-icon.png', width=30)
    st.markdown('[LinkedIn](https://www.linkedin.com/in/anuragpras)')
    st.markdown('**GitHub**')
    st.image('assets/github-icon.png', width=30)
    st.markdown('[GitHub](https://github.com/anuragpras)')

    # Footer
    st.markdown('---')
    st.markdown("© 2024 Anurag Prasad")

if __name__ == '__main__':
    main()
