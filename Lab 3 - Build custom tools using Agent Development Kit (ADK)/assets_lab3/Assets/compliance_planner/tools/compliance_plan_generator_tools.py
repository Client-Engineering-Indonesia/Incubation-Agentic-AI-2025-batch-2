from pydantic import BaseModel, Field
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission 
from typing import List


class CompliancePlan(BaseModel):
    """Output from the planner agent: a list of mandatory documents."""
    plan: str = Field(description="A string containing a checklist of all documents required for compliance.")

@tool(
    permission=ToolPermission.READ_ONLY
)
def compliance_plan_generator_tools(plan: str) -> str:
    """
    Retrieves the compliance plan, which is a checklist of mandatory documents.

    Args:
        plan (str): A string containing a checklist of all documents required for compliance.

    Returns:
        str: A formatted string detailing the compliance plan.
    """
    return f"Compliance plan retrieved: {plan}"
