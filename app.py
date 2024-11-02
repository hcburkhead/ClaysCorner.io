import os
import requests
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
app.config['GITHUB_TOKEN'] = os.getenv('GITHUB_TOKEN')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getProjectData', methods=['GET'])
def get_project_data():
    # GitHub username
    username = "hcburkhead"  # Replace with your GitHub username
    url = f"https://api.github.com/users/{username}/repos"
    
    # Headers for authentication
    headers = {
        "Authorization": f"token {app.config['GITHUB_TOKEN']}"
    }
    
    # Send the request
    response = requests.get(url, headers=headers)
    
    # Check for successful response
    if response.status_code == 200:
        # Extract relevant project data
        projects = [
            {
                "name": repo["name"],
                "description": repo["description"],
                "url": repo["html_url"],
                "stars": repo["stargazers_count"],
                "forks": repo["forks_count"],
                "language": repo["language"]
            }
            for repo in response.json()
        ]
        return jsonify({"projects": projects})
    else:
        # Handle errors
        return jsonify({"error": "Failed to fetch data"}), response.status_code

# Form submission route
@app.route('/submitContactForm', methods=['POST'])
def submit_contact_form():
    data = request.json
    # Processes form data
    response = {"message": "Form submitted successfully!"}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
