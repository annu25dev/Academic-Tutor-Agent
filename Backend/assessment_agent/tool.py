from crewai.tools import tool
from RAG_agent.rag_tool import rag_tool


@tool("SWOT Generator")
def generate_swot(strength, weakness, opportunity, threat):
    """
    Formats SWOT analysis.
    """

    return f"""
Strength:
{strength}

Weakness:
{weakness}

Opportunity:
{opportunity}

Threat:
{threat}
"""


@tool("Score Formatter")
def format_score(

    accuracy,

    depth,

    clarity,

    application

):
    """
    Formats the assessment scores into a readable report.

    """

    overall = accuracy + depth + clarity + application

    return f"""
Conceptual Accuracy : {accuracy}/10

Depth of Understanding : {depth}/10

Clarity : {clarity}/10

Application Ability : {application}/10

Overall Score : {overall}/40
"""


@tool("Feedback Generator")
def feedback(

    strengths,

    weaknesses,

    recommendations,

    next_topic

):
    """
    Formats personalized feedback for the student's assessment.

    """

    return f"""
Strengths

{strengths}


Weaknesses

{weaknesses}


Recommendations

{recommendations}


Recommended Next Topic

{next_topic}
"""
assessment_tools=[
    generate_swot,format_score,feedback,rag_tool
]