from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from tools.sec_tools import SECTools
import os
from langchain_openai import ChatOpenAI

from langchain_community.chat_models import ChatOllama
from langchain_community.llms import Ollama

from dotenv import load_dotenv
load_dotenv()

#llm_ollama = ChatOllama(model="llama3.1:latest", base_url="http://localhost:11434")
llm=LLM(model="ollama/llama3.1:latest", base_url="http://localhost:11434")

@CrewBase
class FinancialAnalystCrew():
	"""FinancialAnalystCrew crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	#def __init__(self) -> None:
	#	self.chatollama_llm = ChatOllama(model="llama3.1:latest", base_url="http://localhost:11434")

	@agent
	def company_researcher(self) -> Agent:
		return Agent(
			config = self.agents_config['company_researcher'],
			tools = [SECTools.search_10k, SECTools.search_10q],
			llm = llm
		)

	@agent
	def company_analyst(self) -> Agent:
		return Agent(
			config = self.agents_config['company_analyst'],
			tools = [SECTools.search_10k, SECTools.search_10q],
			llm = llm
		)

	@task
	def research_company_task(self) -> Task:
		return Task(
			config = self.tasks_config['research_company_task'],
			agent = self.company_researcher()
		)

	@task
	def analyze_company_task(self) -> Task:
		return Task(
			config = self.tasks_config['analyze_company_task'],
			agent = self.company_analyst()
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the FinancialAnalystCrew crew"""
		return Crew(
			agents =  self.agents,
			tasks = self.tasks,
			process = Process.sequential,
			verbose = True
		)
	