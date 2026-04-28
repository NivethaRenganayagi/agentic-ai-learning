def react_agent(question):
    print("Question:", question)

    print("\nThought: Find capital of France")
    print("Action: Searching...")
    observation = "Paris"
    print("Observation:", observation)

    print("\nThought: Find population of Paris")
    print("Action: Searching...")
    observation = "2.1 million"
    print("Observation:", observation)

    print("\nFinal Answer: Population is about 2.1 million")


react_agent("What is the population of the capital of France?")
