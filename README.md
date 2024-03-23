# Quicknote

A python script that allows quick and easy capturing of thoughts in Notion via the Ubuntu terminal

## Installation
The script currently is only supported for Linux (Ubuntu), I am working on versions for Windows as well. 

Follow the following steps to install quicknote: 

1. Make sure you have Python installed on your machine 
2. Clone the repository to your machine
3. Navigate to the project directory `quicknote`
4. Create an .env file inside `quicknote` 
5. Follow this [Youtube video](https://youtu.be/6ATmIyi8Vmg?si=vNsh9z0KH2nNPEP-) to create an Integration in Notion and receive your database_id and secret key
6. Insert the three lines `DATABASE_ID=`, `DATABASE_NAME=` and `SECRET_KEY=` followed by your id, name of your database and key in the `.env` file
7. Change the path of `load_dotenv(...)` to your local `.env` file 

## Create symbolic link (Optional)
You can create a symbolic link to call the script from each directory in the terminal with just `quicknote`

1. Make the script executable `chmod +x quicknote.py`
2. Create a symbolic link `sudo ln -s /path/to/quicknote.py /usr/local/bin/quicknote` where you replace /path/to with the absolute path to quicknote.py

## Usage 
If installed correctly you can use quicknote to capture thought in your terminal and add them to your Notion database. 

If you created the symbolic link you can capture one or multiple thoughts in the following way `quicknote thought1 thought2 thought3`. As you can see you can capture as many thoughts as you want in parallel. Each of the thoughts will be added as an own row in your database.

If you didn't create the symbolic link you can capture one or multiple thoughts in the following way `python3 quicknote.py thought1 thought2 thought3`. Again you can capture as many thoughts as you want in parallel.

