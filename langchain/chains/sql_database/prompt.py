# flake8: noqa
from langchain.prompts.base import CommaSeparatedListOutputParser
from langchain.prompts.prompt import PromptTemplate


DEFAULT_TEMPLATE = """Given an input question, first create a syntactically correct {dialect} query to run, then look at the results of the query and return the answer. Unless the user specifies in his question a specific number of examples he wishes to obtain, always limit your query to at most {top_k} results using the 'LIMIT' clause. You can order the results by a relevant column to return the most interesting examples in the database, but you must place the 'ORDER' clause before the 'LIMIT' clause and never after. The 'LIMIT' clause should always be the last in your query.

Never ask for all the columns in a specific table, only for the few relevant columns given the question. When possible, don't query exactly but use 'LIKE' to make your queries more robust. Pay attention to use only the column names that you can see in the schema description and use exactly the same casing. Be careful not to include columns that do not exist and not to ask for columns in the wrong table.

Use the following format:

Question: "Question here"
SQLQuery: "SQL Query to run"
SQLResult: "Result of the SQLQuery"
Answer: "Final answer here"

Only use the following tables:

{table_info}

Question: {input}"""

PROMPT = PromptTemplate(
    input_variables=["input", "table_info", "dialect", "top_k"],
    template=_DEFAULT_TEMPLATE,
)

_DECIDER_TEMPLATE = """Given the below input question and list of potential tables, output a comma separated list of the table names that may be neccessary to answer this question.

Question: {query}

Table Names: {table_names}

Relevant Table Names:"""
DECIDER_PROMPT = PromptTemplate(
    input_variables=["query", "table_names"],
    template=_DECIDER_TEMPLATE,
    output_parser=CommaSeparatedListOutputParser(),
)
