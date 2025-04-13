from langchain_core.prompts import ChatPromptTemplate


nodes_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Your role is to serve as an automated extractor and identifier of nodes and relationships among the nodes within the provided legal texts, and to build GraphDocument from the nodes and relationships.",
        ),
        (
            "human",
            "Given a piece of legal text, your task is to identify and extract entities and concepts as nodes and the relationships among them. These nodes and relationships will be used to construct a knowledge graph that represents the information in the text."
            "Aim for simplicity and clarity in the knowledge graph to cater to a wide audience."
            "\n"
            "Strive for precision in information extraction without sacrificing accuracy. Only include information explicitly stated in the text."
            "- **Nodes** represent entities and concepts."
            "- **Relationships** denote connections between nodes."
            "- **Labels** are used to categorize nodes."
            "- **Properties** provide additional information about nodes and relationships."
            "- **IDs** are unique identifiers for nodes and relationships."
            "- **GraphDocument** is a collection of nodes and relationships that represent the entities and connections in the text."
            "\n"
            "=> Ensure uniformity and generality in relationship types."
            "=> Utilize available types for node labels and opt for basic or elementary types."
            "For instance, consistently label a person entity as **'person'**, avoiding overly specific terms like 'mathematician' or 'scientist'."
            "=> Avoid integers as node IDs; instead, use names or human-readable identifiers from the text."
            "=> Ensure consistency in referring to entities throughout the knowledge graph."
            "If an entity like 'John Doe' is mentioned using different names or pronouns (e.g., 'Joe', 'he'), consistently use the most complete identifier (e.g., 'John Doe')."
            "Consistency in entity references enhances coherence and understanding in the knowledge graph."
            "\n"
            "For example, given the text 'John Doe is a mathematician. He works at XYZ University.', the nodes and relationships could be:"
            "Nodes: 'John Doe', 'mathematician', 'XYZ University'"
            "Relationships: 'John Doe' is 'mathematician', 'John Doe' works at 'XYZ University'"
            "Or in case of a leagal document, the nodes and relationships could be:"
            "Nodes: 'Organization', 'Person', 'Clause', 'ClauseText'"
            "Relationships: 'Organization' has 'Person', 'Person' works at 'Organization', 'Person' mentioned in 'ClauseText', 'Clause' contains 'ClauseText' and so on.."
            "Follow the guidelines meticulously. Failure to comply will result in termination."
            "\n"
            "A graph document is a collection of nodes and relationships that represent the entities and connections in the text."
            "The nodes and relationships should be accurately extracted from the text and formatted according to the specified format."
            "Similarly, the graph document should be constructed with the nodes and relationships in the correct order and structure."
            "\n"
            "input: {input}",
        ),
    ]
)