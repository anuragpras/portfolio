import streamlit as st

# Main function to render the Streamlit app
def main():
    st.title('Anurag Prasad - Portfolio')

    # About Me section
    st.header('About Me')
    st.write('CS Undergrad at VIT Bhopal, open to all technical roles.')

    # Projects section
    st.header('Projects')
    st.markdown('### GitHub Pinned Repositories')
    repos = [
        {
            "name": "Repo 1",
            "html_url": "https://github.com/anuragpras/repo1",
            "description": "Description for Repo 1"
        },
        {
            "name": "Repo 2",
            "html_url": "https://github.com/anuragpras/repo2",
            "description": "Description for Repo 2"
        }
        # Add more repositories as needed
    ]

    for repo in repos:
        st.markdown(f"[{repo['name']}]({repo['html_url']}) - {repo['description']}")

    # Contact section
    st.header('Contact')
    st.markdown('**Gmail**')
    st.image('assets/gmail-icon.png', width=30)
    st.markdown('[ianuragprasad@gmail.com](mailto:ianuragprasad@gmail.com)')
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
