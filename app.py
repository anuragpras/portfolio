import streamlit as st
import requests

# Function to fetch GitHub pinned repositories
def fetch_github_pinned_repos():
    url = 'https://api.github.com/users/anuragpras/repos?type=public&sort=pushed'
    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()
        pinned_repos = [repo for repo in repos if repo['pinned']]
        return pinned_repos
    else:
        st.error('Failed to fetch GitHub repositories')
        return []

# Main function to render the Streamlit app
def main():
    st.title('Anurag Prasad - Portfolio')

    # About Me section
    st.header('About Me')
    st.write('CS Undergrad at VIT Bhopal, open to all technical roles.')

    # Projects section
    st.header('Projects')
    # Fetch GitHub pinned repositories
    repos = fetch_github_pinned_repos()
    if repos:
        st.markdown('### GitHub Pinned Repositories')
        for repo in repos:
            st.markdown(f"[{repo['name']}]({repo['html_url']}) - {repo['description']}")

    # Contact section
    st.header('Contact')
    st.markdown('**Gmail**')
    st.image('assets/gmail_icon.png', width=30)
    st.markdown('[ianuragprasad@gmail.com](mailto:ianuragprasad@gmail.com)')
    st.image('assets/gmail_icon.png', width=30)
    st.markdown('[anurag.prasad@vitbhopal.ac.in](mailto:anurag.prasad@vitbhopal.ac.in)')
    st.markdown('**LinkedIn**')
    st.image('assets/linkedin_icon.png', width=30)
    st.markdown('[LinkedIn](https://www.linkedin.com/your-linkedin-profile)')
    st.markdown('**GitHub**')
    st.image('assets/github_icon.png', width=30)
    st.markdown('[GitHub](https://github.com/anuragpras)')

    # Footer
    st.markdown('---')
    st.markdown("© 2024 Anurag Prasad")

if __name__ == '__main__':
    main()
