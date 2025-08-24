# adk_forest
My personal forest of Google ADK agents


## Setup the environment

```bash
# Only once to create the virtual enviroment
python3 -m venv .venv

# Run in each new terminal
source .venv/bin/activate

# Only once, or whenever there is a new library to install
pip install -r requirements.txt
```

Create an .env file under the root folder of this repo, using the [.env.example](.env.example) as example.
Follow [this tutorial](https://youtu.be/P4VFL9nIaIA?si=07Ysn70KZYC6LsDp&t=887) to setup an Google Agent.




## Pavia news

This agent finds the latest news and events in Pavia, Italy.

To run the agent:

```bash
# from the adk_forest folder
cd pavia_news

# run the agent as a web service
adk web

# Or run the agent from cli
adk adk run pavia_news_agent
```

