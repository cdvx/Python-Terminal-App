## Simple Terminal APP to consume NEWSAPI

------------------------------------------------------------------------------------------------
## Setup
1. Clone the project `git clone https://github.com/cdvx/Python-Terminal-App.git`
2. cd into the project direcrtory `cd Python-Terminal-App`
3. Create a virtual environment `python3 -m venv venv`
4. Activate the environment `. venv/bi/activate` for linux and 
	`venv\Scripts\activate` for Windows.
5. Install the requirements `pip install -r requirements.txt`


## Usage
1. Entry point -> `app.py`
2. Try out the app with:
 . `python app.py`
 . `python app.py -n bitcoin` or `python app.py -news bitcoin` or `python app.py -new <topic_name>`

---------------------------------------------------------------------------------------------------

## Prerequsites
1. Get a `NewsAPI key from (Here)[https://newsapi.org/docs/get-started]
2. Create a `.env` file and add the key as shown in thw `.env.sample`
