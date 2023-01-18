from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        subject = request.form['subject']
        desired_outcome = request.form['desired_outcome']
        prompt = request.form['prompt']
        example_output = request.form['example_output']
        github_username = request.form['github_username']
        name = request.form['name']
        # save the prompt, subject, and desired outcome to a file
    return render_template('dashboard.html')


import os

def save_to_file(subject, desired_outcome, prompt, example_output, github_username, name):
    file_path = os.path.join('path', 'to', 'file')
    with open(file_path, 'w') as f:
        f.write(subject + '\n')
        f.write(desired_outcome + '\n')
        f.write(prompt + '\n')
        f.write(example_output + '\n')
        f.write(github_username + '\n')
        f.write(name + '\n')


if request.method == 'POST':
    subject = request.form['subject']
    desired_outcome = request.form['desired_outcome']
    prompt = request.form['prompt']
    example_output = request.form['example_output']
    github_username = request.form['github_username']
    name = request.form['name']
    save_to_file(subject, desired_outcome, prompt, example_output, github_username, name)
    # inform user that the form has been submitted
    return render_template('dashboard.html', message="Form submitted successfully")



# Path: dashboard.html
<form action="/dashboard" method="POST">
    <input type="text" name="subject" placeholder="Subject">
    <input type="text" name="desired_outcome" placeholder="Desired Outcome">
    <input type="text" name="prompt" placeholder="Prompt">
    <input type="text" name="example_output" placeholder="Example Output">
    <input type="text" name="github_username" placeholder="Github Username">
    <input type="text" name="name" placeholder="Name">
    <button type="submit">Submit</button>
</form>