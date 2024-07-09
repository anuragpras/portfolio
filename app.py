import streamlit as st

def main():
    # Custom CSS for styling
    st.markdown("""
        <style>
            .main-title {
                font-size: 36px;
                font-weight: bold;
                text-align: center;
                margin-bottom: 20px;
            }
            .section-header {
                font-size: 28px;
                font-weight: bold;
                margin-top: 40px;
                margin-bottom: 20px;
            }
            .project-subheader {
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .project-details {
                font-size: 16px;
            }
            .horizontal-line {
                margin-top: 10px;
                margin-bottom: 30px;
                border: 0;
                height: 1px;
                background: #333333;
            }
            .contact-info {
                display: flex;
                flex-direction: row;
                justify-content: space-around;
                margin-top: 20px;
            }
            .contact-item {
                flex: 1;
                text-align: center;
                font-size: 16px;
            }
            .contact-item a {
                color: #333333;
                text-decoration: none;
            }
            .footer {
                text-align: center;
                margin-top: 40px;
                font-size: 14px;
                color: #888888;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-title">Anurag Prasad - Portfolio</div>', unsafe_allow_html=True)

    # About Me section
    st.markdown('<div class="section-header">About Me</div>', unsafe_allow_html=True)
    st.write('CS Undergrad at VIT Bhopal, open to all technical roles.')

    # Projects section
    st.markdown('<div class="section-header">Projects</div>', unsafe_allow_html=True)

    # Function to display project details
    def display_project(title, repo_url, description, gif_path):
        st.markdown(f'<div class="project-subheader">{title}</div>', unsafe_allow_html=True)
        col1, col2 = st.columns([4, 1])
        with col1:
            st.markdown(f'<div class="project-details"><a href="{repo_url}" target="_blank">{repo_url.split("/")[-1]}</a></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="project-details">{description}</div>', unsafe_allow_html=True)
        with col2:
            st.image(gif_path, use_column_width=True)
        st.markdown('<hr class="horizontal-line">', unsafe_allow_html=True)

    # Displaying all projects
    display_project('Image Caption Generator', 'https://github.com/anuragpras/image-description-deep-learning', 'Image Caption Generator using Flickr dataset', '1.gif')
    display_project('Cafe Sales Analysis', 'https://github.com/anuragpras/cafe-sales-analysis', 'Detailed cafe sales analysis project using Power BI and MySQL', '2.gif')
    display_project('Amazon India Sales Dashboard (Tableau)', 'https://github.com/anuragpras/amazon-india-sales-dashboard-tableau', 'Interactive Tableau dashboard analyzing Amazon India\'s sales data', '3.gif')
    display_project('Exploratory Data Analysis', 'https://github.com/anuragpras/exploratory-data-analysis', 'E-Commerce Sales Insights: An Exploratory Data Analysis with Python', '4.gif')
    display_project('Pizza Sales Analysis', 'https://github.com/anuragpras/pizza-sales-analysis', 'Analyzing pizza sales data using MySQL and Excel', '5.gif')
    display_project('Not By Gulzar (Random Poetry Generator)', 'https://github.com/anuragpras/not-by-gulzar', 'Capture Gulzar\'s essence with the Random Poetry Generator', '6.gif')
    display_project('COVID-19 Dashboard (Tableau)', 'https://github.com/anuragpras/covid19-tableau', 'Interactive Tableau dashboard tracking COVID-19 statistics', '7.gif')
    display_project('Pomodoro Timer App', 'https://github.com/anuragpras/pomodoro-app', 'Productivity tool for time management using Python', '8.gif')
    display_project('Snake Game', 'https://github.com/anuragpras/snake-game', 'Classic snake game implementation in Python', '9.gif')

    # Contact section
    st.markdown('<div class="section-header">Contact</div>', unsafe_allow_html=True)
    st.markdown('<div class="contact-info">', unsafe_allow_html=True)
    st.markdown('<div class="contact-item">Personal Mail ID:<br><a href="mailto:ianuragprasad@gmail.com">ianuragprasad@gmail.com</a></div>', unsafe_allow_html=True)
    st.markdown('<div class="contact-item">University Mail ID:<br><a href="mailto:anurag.prasad@vitbhopal.ac.in">anurag.prasad@vitbhopal.ac.in</a></div>', unsafe_allow_html=True)
    st.markdown('<div class="contact-item">LinkedIn:<br><a href="https://www.linkedin.com/in/anuragpras">LinkedIn</a></div>', unsafe_allow_html=True)
    st.markdown('<div class="contact-item">GitHub:<br><a href="https://github.com/anuragpras">GitHub</a></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown('<div class="footer">© 2024 Anurag Prasad</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()
