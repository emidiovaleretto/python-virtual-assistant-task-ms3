# **Python Virtual Assistant Task**

## How may I assist you today?

![Mockup](./documents/readme-images/mockup.png)

The live link can be found <a href="https://virtual-assistant-task-py.herokuapp.com/" target="_blank" rel="noopener">here</a>.

Python Virtual Assistant Task is a Python terminal application, which runs on a mock terminal on Heroku.

## Contents

- [**Python Virtual Assistant Task**](#python-virtual-assistant-task)
  - [How may I assist you today?](#how-may-i-assist-you-today)
  - [Contents](#contents)
    - [Forking the GitHub Repository and Running this Project Locally](#forking-the-github-repository-and-running-this-project-locally)
    - [Setting up heroku](#setting-up-heroku)
    - [Acknowledgements](#acknowledgements)
  - [Author](#author)


### Forking the GitHub Repository and Running this Project Locally

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original 
repository by using the following steps...

  1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)

  2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.

  3. You should now have a copy of the original repository in your GitHub account.

  4. Run the index.html file in your local browser.


### Setting up heroku

To set up heroku you must:

  1. If your requirements.txt file has not changed you can skip this step. Otherwise, in your terminal type 'pip3 freeze > requirements.txt' then save and push the changes.
  2. Go to Heroku.com and sign in or create a free account.
  3. From the heroku dashboard click the 'Create new app' button.
  4. Name the app something unique and choose what region you are in then click 'Create app'.
  5. Go to the settings tab and find the Config Vars section. Click 'Reveal Config Vars'.
  6. If your project does not use a creds.json file then skip this step. Otherwise, in the field for KEY enter the value CREDS in all capitals. In the field for VALUE copy and paste the entire contents of your creds.json file from your project. Then click 'Add'.
  7. In the field for KEY enter PORT in all capitals, then in the field for VALUE enter 8000. Then click 'Add'.
  8. Scroll down to the Buildpacks section and click 'Add buildpack'.
  9. Click Python then save changes.
  10. Add another buildpack by clicking 'Add buildpack' and this time click Nodejs then save changes.
  11. Make sure that Python appears above Nodejs in the buildpack section. If it does not you can click and drag them to change the order.
  12. Then head over to the deploy section by clicking deploy from the nav bar at the top of the page.
  13. From the 'Deployment method' section select GitHub and click 'Connect to GitHub'.
  14. Enter the repository name as it is in GitHub and click 'search'.
  15. Click the 'connect' button next to the repository to link it to heroku.
  16. To deploy, scroll down and click the 'Deploy Branch' button.
  17. Heroku will notify you that the app was successfully deployed with a button to view the app.
  18. If you want to rebuild your app automatically you can also select the 'Enable Automatic Deploys' button which will then rebuild the app every time you push any changes.

### Acknowledgements

I would like to take the opportunity to thank:

 - My family, friends and colleagues for their advice, support and help with testing.
 - To my mentor Felipe Alarcon for his feedback, advice, support and, above all, for his patience.
 - All Code Institute Tutors and Community on Slack for the peer reviews and advice.

## Author

Made with ❤️ by <b>Emidio Valereto</b> 👋🏽 Get in touch!

[![Linkedin Badge](https://img.shields.io/badge/-Emidio-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/emidiovalereto/)](https://www.linkedin.com/in/emidiovalereto/) [![Gmail Badge](https://img.shields.io/badge/-emidio.valereto@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:emidio.valereto@gmail.com)](mailto:emidio.valereto@gmail.com)

[Back to top ⇧](#table-of-contents)