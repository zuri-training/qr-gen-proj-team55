# Repository for Team 55 QR_Generator
<div>
<p align="center">
  <a href="" rel="noopener">
 <img src="Frontend/profiledashboard1/images/qrcode 2.png" alt="Project logo"></a>
</p>
</div>
<h1></h1>

## Table of Contents

* [Project Description](#project-description)
* [Problem statement](#problem-statement)
* [Framework for building](#framework-for-building)
* [Contributors Guide](#contributors-guide)
* [Features of the Website](#features-of-the-website)
* [Product Specification](#product-specialization)
* [Project Status](#project-status)
* [Contributors](#contributors)
* [Deployment Instruction](#deployment-instruction)
* [Relevant Links](#relevant-links)
* [Acknowledgements](#acknowledgements)



## Project Description

This project involve building a web site for generating a (Quick Response) qr_code where user that visit the site can only generate the code after registration. The code generated should also be able to use both on and offline and can be shared via email, can be downloaded in PNG and PDF

* __The repository file arranged in the following order

1. `FrontEnd Folder` contains the HTML,CSS and Javascripts code.
2. `ContributionList` is a folder that contains a txt files of every contributed Team members.
3. `qr_gen folder` contains all the codes use in evecuting this project with subfolder such as
 * `authentication`, Apllication folder for the CustomUser and Profile models as well as other .py files in an app, it also contains templates folder for all jinja related to authentication
 *  `qr_gen_app`, this is the second applcation folder that how all the functionalit of the qr_generation.
 *  `static`, this contains all the static folders such as the CSS; IMAGEs and the JS files.
 *  `templates` contains a based templates file that is extended in all templates file.
 *   `qr_gen` is the the project folder.
4. `requirements.txt` contains the dependencies installed throughout the project.

## Problem statement
With the evolution of Technology, quick access to service using an encrypted method has been evolving over the years, platform for the creating this encryption is what we will be building.


## Framework for building

* __IDE__ </br>
The project is was built using the ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) Editor and the following technologies were used: <br/>
* __Project Management and Version Control__<br/><br/>
        ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
* __Design__<br/><br/>
        ![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)
        
* __FrontEnd__<br/><br/>
      <img src="https://github.com/devicons/devicon/blob/master/icons/css3/css3-plain-wordmark.svg"  title="CSS3" alt="CSS" width="40" height="40"/>&nbsp;
      <img src="https://github.com/devicons/devicon/blob/master/icons/html5/html5-original.svg" title="HTML5" alt="HTML" width="40" height="40"/>&nbsp;
      <img src="https://github.com/devicons/devicon/blob/master/icons/javascript/javascript-original.svg" title="JavaScript" alt="JavaScript" width="40" height="40"/>&nbsp;
* __BackEnd__<br/>
        ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
        ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
* __Database__<br/>
        ![PostqresSQL](https://img.shields.io/badge/PostGresQL-%2300f.svg?style=for-the-badge&logo=postgressql&logoColor=white)

 
## Contributors Guide
1. Visit the Repository to the Project on Github Website `https://github.com/zuri-training/qr-gen-proj-team55`
2. Fork the repository: Click the "Fork" button on the upper right corner of the Repo page.*
3. Make a local clone by: 
     Copying the URL for the forked Repo <br/>
     `https://github.com/zuri-training/qr-gen-proj-team55` <br/>
     Create a Folder on your Local machine for the project <br/>
     Open Command prompt / Terminal in the same folder location <br/>
     In your Terminal, type: <br/>
        `git clone https://github.com/github_username/qr-gen-proj-team55.git`
4. Open terminal and set upstream branch: <br/>
    `git remote add upstream https://github.com/zuri-training/qr-gen-proj-team55`
5. To add install all requirement for contributors to updates packages run on cloned terminal:<br/>
    `pip install -r requirements.txt` 
6. Pull upstream to get up to date with the original repo:<br/>
    `git pull upstream main`
7. Create a new branch for the task you are working on :<br/>
    `git checkout -b branchName`<br/>
    *(Make sure your branchName is descriptive in context to the feature you are working on. Also be sure to check which branch you are on using `git status` before you begin working)*
8. When you're done with your task, do:<br/>
    `git add`<br/>
   - Commit your work with a message:<br/>
   `git commit -m "message"`
9. To avoid conflicts:<br/>
    `git pull upstream main`
10. Then push your branch:<br/>
    `git push origin branchName` - This creates the branch remotely and pushes to that branch on the Github
11. Go to Github and create a new pull request to the main branch. It will then be reviewed and merged into the master.

## Features of the Website
__Unauthenticated users__ - An individual that has not registered to the website would be able to: <br/> 

* Visit the platform to view basic information about it
* View and Interact with the documentation
* Register to view more details
* No access to use until registered

__Authenticated Users__ - A user that has fully registered and has completed all the verification processes in the website: <br/>

* Full access to the platform
* Allow setting on what should happen when qr is scanned - give at least 2 options.
* Allow users to download (allow png, jpg and pdf download format), or share code by email or social media.
* Allow users to save data and come back to it

## Product Specialization
* Mobile Phones
* Tablets
* Laptops

## Project Status
Project is : *in progress*

## Contributors

__Designers__ <br/>
* Itepu precious eden
 `https://github.com/preciousitepu`

* Timileyin Lasisi
`https://github.com/Timileyin21`

* Abimbola Ashonibare
`https://github.com/BimboOni`

* Badamosi Abdullahi Oluwatobi
`https://github.com/Abdooorl`

* Zipporah Badi
`https://github.com/Zeebadi`

* Nnoruka Anthonia
`https://github.com/Antoruka`

* Uduak Oscar
`https://github.com/Udyoscar`

* Barakat Muraina Omolara 
`https://github.com/bara506`

* Ekojawe Efe
`https://github.com/efedivine`

* Falola Samuel
`https://github.com/sammiecode`

* Daniel Ige
`https://github.com/igedaniel96`

* Emediong Ebong 
`https://github.com/Emyebong`

* Oluwabusayo Basirat Atiku
`https://github.com/Busayoatiku`
<br/>

__BackEnd Contributors__ <br/>
* David Ilori
`https://github.com/Ddluwole`

* Awal Umar
`https://github.com/drizla01`

* Joshua Eze
`http://github.com/Allenkeys`

* Dighomanor Jeremiah
`http://github.com/Digho007`
<br/>

__FrontEnd Contributors__ <br/>
* Mark nehemiah
`http://github.com/markben2122`

* Samson Vershima Saaikyaa
`http://github.com/vershima2`

* Awelewa Oluwasanmi Omolade
`http://github.com/Sanmi01`

* Akobi, Mutiat Adeoti
`https://github.com/PhoenixClix`

## Deployment Instruction
1. Create a folder `mkdir folder_name`
2. Change directory to the folder: cd `folder_name`
3. Clone main branch to folder: `git clone --branch main https://github.com/zuri-training/qr-gen-proj-team55`
4. create virtual environment: `python -m virtualenv local`
5. Activate virtual environment: `local\Scripts\activate`
6. Install packages: `pip install -r requirements.txt`
7. Create database, database_user and password  for the project: `PostgreSQL database`
8. To generate a new secret key and add it to ,env file created in the page `python manage.py generate_secret_key`
9. Create a new file .env and copy the contents of .env_template into it and replace:


* {DB} with database name
* {DB_HOST} with localhost
* {DB_PORT} with 5432
* {DB_USERNAME} with database postgres
* {DB_PASSWORD} with database *********



## Relevant Links
* Figma Design - `https://www.figma.com/file/65TGG1OYI0nqPJ4EgMdmgn/Untitled?node-id=0%3A1 `
* BackEnd Schema - `https://drive.google.com/file/d/1try3DiVSOIg-wCeG1_2_TUOyGgY5gvEi/view?usp=sharing `
* Design Documentation


## Acknowledgements
Special thanks to Zuri Team and I4G for giving every member of this Team the privelege to Learn as well
as implement what they have have in a real life settings.



