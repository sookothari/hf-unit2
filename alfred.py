"""
    IMPORTANT: SWITCH ON DEVELOPER MODE ON THE LAPTOP BEFORE RUNNING THIS
    go to windows Settings->Developer Settings->Developer Mode
    this will require admin password

"""
import alfred_setup
from smolagents import CodeAgent, HfApiModel

alfred_setup.setup()

agent = CodeAgent(tools=[], model=HfApiModel())
alfred_agent = agent.from_hub('sergiopaniego/AlfredAgent', trust_remote_code=True)
alfred_agent.run("Give me the best playlist for a party at Wayne's mansion. The party idea is a 'villain masquerade' theme")  