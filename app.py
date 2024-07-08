import streamlit as st

def main():
    st.title('Anurag Prasad - Portfolio')

    # About Me section
    st.header('About Me')
    st.write('CS Undergrad at VIT Bhopal, open to all technical roles.')

    # Projects section
    st.header('Projects')

    # Project 1 - Image Caption Generator
    st.subheader('Image Caption Generator')

    # Display project details and GIF in a single row
    col1, col2 = st.columns([4, 1])  # Adjust the ratio as needed

    # Display project details on the left column
    with col1:
        st.markdown('**[image-description-deep-learning](https://github.com/anuragpras/image-description-deep-learning)**')
        st.markdown('Image Caption Generator using Flickr dataset')

    # Display GIF on the right column
    with col2:
        st.image('1.gif', use_column_width=True)  # Ensure '1.gif' is in the root folder and the correct filename

    st.markdown('---')  # Horizontal line after the project

    # Project 2 - Cafe Sales Analysis
    st.subheader('Cafe Sales Analysis')

    # Display project details and GIF in a single row
    col1, col2 = st.columns([4, 1])  # Adjust the ratio as needed

    # Display project details on the left column
    with col1:
        st.markdown('**[cafe-sales-analysis](https://github.com/anuragpras/cafe-sales-analysis)**')
        st.markdown('Detailed cafe sales analysis project using Power BI and MySQL')

    # Display GIF on the right column
    with col2:
        st.image('2.gif', use_column_width=True)  # Ensure '2.gif' is in the root folder and the correct filename

    st.markdown('---')  # Horizontal line after the project

    # Project 3 - Amazon India Sales Dashboard (Tableau)
    st.subheader('Amazon India Sales Dashboard (Tableau)')

    # Display project details and GIF in a single row
    col1, col2 = st.columns([4, 1])  # Adjust the ratio as needed

    # Display project details on the left column
    with col1:
        st.markdown('**[amazon-india-sales-dashboard-tableau](https://github.com/anuragpras/amazon-india-sales-dashboard-tableau)**')
        st.markdown('Interactive Tableau dashboard analyzing Amazon India\'s sales data')

    # Display GIF on the right column
    with col2:
        st.image('3.gif', use_column_width=True)  # Ensure '3.gif' is in the root folder and the correct filename

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
