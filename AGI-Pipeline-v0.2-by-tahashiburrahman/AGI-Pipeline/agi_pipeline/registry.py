class AgentRegistry:
    def __init__(self):
        self._agents = {}

    def register(self, agent):
        if not agent.name.strip():
            raise ValueError("Agent name cannot be empty")
        if agent.name in self._agents:
            raise ValueError(f"Agent already registered: {agent.name}")
        self._agents[agent.name] = agent

    def all(self):
        return list(self._agents.values())

    def get(self, name):
        return self._agents.get(name)
