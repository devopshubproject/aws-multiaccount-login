##### Flash Docker container with AWS account switch role URLs #####
from flask import Flask, request, render_template, flash, url_for, redirect
import json
import os

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "your_secret_key")

# Load AWS account details
AWS_ACCOUNTS_FILE = "aws_accounts.json"
try:
    with open(AWS_ACCOUNTS_FILE, "r") as f:
        aws_accounts = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading {AWS_ACCOUNTS_FILE}: {e}")
    aws_accounts = []

@app.route('/')
def home():
    """Render home page with AWS account dropdown."""
    return render_template('index.html', accounts=aws_accounts)

@app.route('/login', methods=['POST'])
def login():
    """Redirect the user to AWS Switch Role URL."""
    account_name = request.form.get('account_name')

    # Find the selected AWS account
    selected_account = next((acc for acc in aws_accounts if acc["name"] == account_name), None)

    if not selected_account:
        flash("Invalid account selection.", "danger")
        return redirect(url_for('home'))

    account_id = selected_account["account_id"]
    role_name = selected_account["role_name"]  # Ensure this is added in aws_accounts.json

    # Construct AWS Switch Role URL
    aws_switch_role_url = f"https://signin.aws.amazon.com/switchrole?roleName={role_name}&account={account_id}"

    return redirect(aws_switch_role_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
