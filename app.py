import streamlit as st
import requests

# Page layout configuration
st.set_page_config(
    page_title="Anurag Prasad - Portfolio",
    page_icon=":wave:",
    layout="wide"
)

# Define CSS styles
st.markdown(
    """
    <style>
    .header {
        font-size: 3rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section {
        margin-top: 3rem;
    }
    .contact-info {
        margin-top: 1rem;
    }
    .contact-item {
        margin-bottom: 1rem;
    }
    .contact-item a {
        display: inline-block;
        margin-right: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to fetch GitHub pinned repositories
def fetch_github_pinned_repos(username):
    url = f"https://gh-pinned-repos.egoist.dev/?username={username}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Main content
st.title("Anurag Prasad - Portfolio")
st.header("About Me")
st.write("CS Undergrad at VIT Bhopal, open to all technical roles.")

st.header("Projects")

# Replace 'anuragpras' with your GitHub username
username = 'anuragpras'
pinned_repos = fetch_github_pinned_repos(username)

if pinned_repos:
    for repo in pinned_repos:
        st.write(f"**{repo['repo']}**")
        st.write(repo['description'])
        st.write(f"[View on GitHub]({repo['link']})")
        st.write("---")
else:
    st.error("Error fetching GitHub pinned repositories. Please check your GitHub username.")

st.header("Contact")
st.markdown("""
<div class="contact-info">
    <div class="contact-item">
        <a href="mailto:ianuragprasad@gmail.com">
            <img src="images/gmail-icon.png" alt="Gmail" style="width: 20px; height: 20px; margin-bottom: -5px;">
            ianuragprasad@gmail.com
        </a>
    </div>
    <div class="contact-item">
        <a href="mailto:anurag.prasad@vitbhopal.ac.in">
            <img src="images/gmail-icon.png" alt="Gmail" style="width: 20px; height: 20px; margin-bottom: -5px;">
            anurag.prasad@vitbhopal.ac.in
        </a>
    </div>
    <div class="contact-item">
        <a href="https://www.linkedin.com/in/anuragpras/" target="_blank">
            <img src="images/linkedin-icon.png" alt="LinkedIn" style="width: 20px; height: 20px; margin-bottom: -5px;">
            LinkedIn
        </a>
    </div>
    <div class="contact-item">
        <a href="https://github.com/anuragpras" target="_blank">
            <img src="images/github-icon.png" alt="GitHub" style="width: 20px; height: 20px; margin-bottom: -5px;">
            GitHub
        </a>
    </div>
</div>
""",
unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("&copy; 2024 Anurag Prasad", unsafe_allow_html=True)
