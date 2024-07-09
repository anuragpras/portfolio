import streamlit as st

def main():
    st.title('Anurag Prasad - Portfolio')

    # About Me section
    st.header('About Me')
    st.write('CS Undergrad at VIT Bhopal, open to all technical roles.')

    # Education section
    st.header('Education')
    st.markdown("""
    <table style="width:100%">
      <tr>
        <td>B.Tech, Computer Science</td>
        <td>Vellore Institute of Technology, Bhopal</td>
        <td>2021-2025</td>
      </tr>
      <tr>
        <td>Class XII</td>
        <td>Rukhmani Devi Public School, Bhopal</td>
        <td>2020</td>
      </tr>
      <tr>
        <td>Class X</td>
        <td>Holy Family Convent Sr. Sec. School, Bhopal</td>
        <td>2018</td>
      </tr>
    </table>
    """, unsafe_allow_html=True)

    # Projects section
    st.header('Projects')

    # Function to display project details
    def display_project(title, link, description, gif):
        st.subheader(title)
        col1, col2 = st.columns([4, 1])  # Adjust the ratio as needed
        with col1:
            st.markdown(f'[{link}](https://github.com/anuragpras/{link})', unsafe_allow_html=True)
            st.markdown(description)
            st.markdown('---')  # Horizontal line after the project
        with col2:
            st.image(gif, use_column_width=True)  # Ensure the GIF is in the correct folder and filename

    # List of projects
    projects = [
        ('Image Caption Generator', 'image-description-deep-learning', 'Image Caption Generator using Flickr dataset', '1.gif'),
        ('Cafe Sales Analysis', 'cafe-sales-analysis', 'Detailed cafe sales analysis project using Power BI and MySQL', '2.gif'),
        ('Amazon India Sales Dashboard (Tableau)', 'amazon-india-sales-dashboard-tableau', 'Interactive Tableau dashboard analyzing Amazon India\'s sales data', '3.gif'),
        ('Exploratory Data Analysis', 'exploratory-data-analysis', 'E-Commerce Sales Insights: An Exploratory Data Analysis with Python', '4.gif'),
        ('Pizza Sales Analysis', 'pizza-sales-analysis', 'Analyzing pizza sales data using MySQL and Excel', '5.gif'),
        ('Not By Gulzar (Random Poetry Generator)', 'not-by-gulzar', 'Capture Gulzar\'s essence with the Random Poetry Generator', '6.gif'),
        ('COVID-19 Dashboard (Tableau)', 'covid19-tableau', 'Interactive Tableau dashboard tracking COVID-19 statistics', '7.gif'),
        ('Pomodoro Timer App', 'pomodoro-app', 'Productivity tool for time management using Python', '8.gif'),
        ('Snake Game', 'snake-game', 'Classic snake game implementation in Python', '9.gif')
    ]

    for project in projects:
        display_project(*project)

    # Contact section
    st.header('Contact')
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
