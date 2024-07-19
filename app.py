import streamlit as st

def main():
    st.set_page_config(page_title="Anurag Prasad - Portfolio", layout="centered")

    st.title('Anurag Prasad - Portfolio')

    # Navigation links
    st.markdown(
        """
        [**Certifications**](#certifications) | [**Projects**](#projects) | [**Contact**](#contact)
        """
        , unsafe_allow_html=True
    )

    # About Me section
    st.header('About Me')
    st.write('Computer Science undergraduate at VIT Bhopal with a passion for AI/ML, data science, and software development. I\'m eager to learn and contribute my skills to innovative technical roles.')

    # Education section
    st.header('Education')
    education = """
    | **Degree**                           | **Institution**                                    | **Year**      |
    |:------------------------------------:|:--------------------------------------------------:|:-------------:|
    | B.Tech, Computer Science             | Vellore Institute of Technology, Bhopal            | 2021-2025     |
    | Class XII                            | Rukhmani Devi Public School, Bhopal                | 2020          |
    | Class X                              | Holy Family Convent Sr. Sec. School, Bhopal        | 2018          |
    """
    st.markdown(education, unsafe_allow_html=True)

    # Certifications section
    st.header('Certifications')

    certifications = """
    | **Certification**                                    | **Score** | **Link**                                                                                     |
    |:-----------------------------------------------------:|:---------:|:---------------------------------------------------------------------------------------------:|
    | AWS Certified Cloud Practitioner (CLF-C02)            | 838/1000  | [View Certificate](https://drive.google.com/file/d/1xPKoW9Bc9kh_a3ki2feQ0bGcjWo4I_zu/view?usp=drive_link)         |
    | Microsoft Certified Azure Administrator (AZ-104)      | 836/1000  | [View Certificate](https://drive.google.com/file/d/1F39DA3ledkMapL_AAGUfzsP3tqTL3Btt/view?usp=drive_link)         |
    | Introduction to Internet of Things (NPTEL)            | 90/100    | [View Certificate](https://drive.google.com/file/d/111txAdF5ZiMuCYHVpi9MiKGR-PBP7NrE/view?usp=drive_link)          |
    | The Bits & Bytes of Computer Networking (Coursera)    | 97.25/100 | [View Certificate](https://drive.google.com/file/d/1YCTt65ZIZjKW6rCN2hhXjxNbgVBWVMx0/view?usp=drive_link)        |
    """
    st.markdown(certifications, unsafe_allow_html=True)

    # Projects section
    st.header('Projects')

    projects = [
        {"title": "Image Caption Generator", "link": "https://github.com/anuragpras/image-description-deep-learning", "description": "Image Caption Generator using Flickr dataset", "gif": "1.gif"},
        {"title": "Cafe Sales Analysis", "link": "https://github.com/anuragpras/cafe-sales-analysis", "description": "Detailed cafe sales analysis project using Power BI and MySQL", "gif": "2.gif"},
        {"title": "Forecasting Hotel Booking Cancellations", "link": "https://github.com/anuragpras/forecasting-hotel-booking-cancellations", "description": "Machine learning model to predict hotel booking cancellations", "gif": "11.gif"},
        {"title": "Amazon India Sales Dashboard (Tableau)", "link": "https://github.com/anuragpras/amazon-india-sales-dashboard-tableau", "description": "Interactive Tableau dashboard analyzing Amazon India's sales data", "gif": "3.gif"},
        {"title": "Exploratory Data Analysis", "link": "https://github.com/anuragpras/exploratory-data-analysis", "description": "E-Commerce Sales Insights: An Exploratory Data Analysis with Python", "gif": "4.gif"},
        {"title": "Pizza Sales Analysis", "link": "https://github.com/anuragpras/pizza-sales-analysis", "description": "Analyzing pizza sales data using MySQL and Excel", "gif": "5.gif"},
        {"title": "Not By Gulzar (Random Poetry Generator)", "link": "https://github.com/anuragpras/not-by-gulzar", "description": "Capture Gulzar's essence with the Random Poetry Generator", "gif": "6.gif"},
        {"title": "COVID-19 Dashboard (Tableau)", "link": "https://github.com/anuragpras/covid19-tableau", "description": "Interactive Tableau dashboard tracking COVID-19 statistics", "gif": "7.gif"},
        {"title": "Pomodoro Timer App (Streamlit)", "link": "https://github.com/anuragpras/pomodoro-app", "description": "Productivity tool for time management using Python and Streamlit", "gif": "8.gif"},
        {"title": "Snake Game (Raylib and C++)", "link": "https://github.com/anuragpras/snake-game", "description": "Classic snake game implementation using Raylib library and C++", "gif": "9.gif"},
        {"title": "Task Manager MERN App", "link": "https://github.com/anuragpras/Task-Manager-MERN", "description": "Full-stack MERN application for managing tasks", "gif": "10.gif"},
    ]

    for project in projects:
        st.subheader(project["title"])
        col1, col2 = st.columns([3, 1])  # Adjust the ratio as needed
        with col1:
            st.markdown(f'[{project["title"]}]({project["link"]})', unsafe_allow_html=True)
            st.markdown(project["description"])
        with col2:
            st.image(project["gif"], use_column_width=True)
        st.markdown('---')  # Horizontal line after the project

    # Contact section
    st.header('Contact')
    contact_info = """
    <div style="display: flex; flex-direction: column; align-items: flex-start;">
        <div>Personal Mail ID:<br><a href="mailto:ianuragprasad@gmail.com">ianuragprasad@gmail.com</a></div>
        <div>University Mail ID:<br><a href="mailto:anurag.prasad@vitbhopal.ac.in">anurag.prasad@vitbhopal.ac.in</a></div>
        <div>LinkedIn:<br><a href="https://www.linkedin.com/in/anuragpras">LinkedIn</a></div>
        <div>GitHub:<br><a href="https://github.com/anuragpras">GitHub</a></div>
    </div>
    """
    st.markdown(contact_info, unsafe_allow_html=True)

    # Footer
    st.markdown('---')
    st.markdown("© 2024 Anurag Prasad")

if __name__ == '__main__':
    main()
