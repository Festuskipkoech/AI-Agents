from phi.agent import Agent
from phi.model.groq import Groq
from  dotenv import load_dotenv
from phi.tools.yfinance import YFinanceTools
load_dotenv()

<<<<<<< HEAD
agent = Agent(
    model = Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=['Use tables to display data.']
)
agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA and Phidata. Show in tables.")
=======
def get_company_symbol(company: str) -> str:
    """Use this function to get the symbol for a company.

    Args:
        company (str): The name of the company.

    Returns:
        str: The symbol for the company.
    """
    symbols = {
        "Phidata" : "GOOGL",
        "Infosys" : "INFY",
        "Tesla" : "TSLA",
        "Apple" : "AAPL",
        "Microsoft" : "MSFT",
        "AMAZON" : "AMZN",
        "Google" : "GOOGL",
    }
    return symbols.get(company, "Uknown")


agent = Agent(
    model = Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True),get_company_symbol],
    show_tool_calls=True,
    markdown=True,
    instructions=[
        "Use tables to display data.",
        "If you need to find the symbol for a company, use the get_company_symbol tool.",
    ],
    debug_mode=True,
    
)
agent.print_response("Summarize and compare analyst recommendations and fundamentals for TSLA and Phidata. Show in tables.", stream=True)
>>>>>>> 3fdd215 (Final agent)
