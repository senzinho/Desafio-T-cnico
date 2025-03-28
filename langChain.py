from langchain.agents import initialize_agent, Tool, AgentType
from langchain.tools import DuckDuckGoSearchResults

# Definindo uma ferramenta (pode ser outras como DuckDuckGo, Wikipedia, etc)
search_tool = DuckDuckGoSearchResults()

# Definindo as ferramentas a serem usadas pelo agente
tools = [
    Tool(
        name="Search",
        func=search_tool.run,
        description="Use esta ferramenta para pesquisar na web"
    )
]

# Inicializando o agente com as ferramentas
agent = initialize_agent(
    tools, 
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
    verbose=True
)

# Função para executar o agente
def execute_agent(query):
    try:
        # Execute a consulta
        resultado = agent.run(query)
        return resultado
    except Exception as e:
        print(f"Erro ao executar agente: {e}")
        return None

# Teste da função
if __name__ == "__main__":
    query = "Qual é a capital do Brasil?"
    resultado = execute_agent(query)
    print(f"Resultado: {resultado}")
