from pydantic import BaseModel, Field
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission
from typing import List, Optional

class CombinedComplianceInput(BaseModel):
    """
    Input for a combined compliance checker tool.
    Provide either 'plan' and 'documents' for document compliance,
    OR 'procedure_compliance' and 'rag_result' for RAG comparison.
    """
    plan: Optional[str] = Field(
        None, description="The checklist of mandatory documents for a document compliance check (e.g., 'Invoice, Packing List')."
    )
    documents: Optional[str] = Field(
        None, description="A string describing the documents that were successfully found for a document compliance check (e.g., 'The retrieved documents include: Invoice, Packing List, and Bill of Lading.')."
    )
    procedure_compliance: Optional[str] = Field(
        None, description="The string representing the expected procedure compliance for a RAG comparison."
    )
    rag_result: Optional[str] = Field(
        None, description="The RAG (Retrieval-Augmented Generation) result string to be compared with the procedure."
    )

@tool(permission=ToolPermission.READ_ONLY)
def compliance_checker_tools(
    input_data: CombinedComplianceInput
) -> str:
    """
    Performs either a document compliance check or a RAG result compliance check
    based on the provided input.

    If 'plan' and 'documents' are provided, it performs a document compliance check.
    If 'procedure_compliance' and 'rag_result' are provided, it performs a RAG result comparison.
    If an invalid combination of inputs is provided, it returns an error message.

    Args:
        input_data (CombinedComplianceInput): An object containing the necessary
                                              inputs for either check.

    Returns:
        str: A formatted string summarizing the compliance check result.
    """
    plan = input_data.plan
    documents = input_data.documents
    procedure_compliance = input_data.procedure_compliance
    rag_result = input_data.rag_result

    # Determine which check to perform based on provided inputs
    if plan is not None and documents is not None:
        # --- Perform Document Compliance Check (simulated logic) ---
        # Parse the 'plan' string into a list of required document names
        required_docs = [doc.strip().lower() for doc in plan.split(',')]

        missing_documents = []
        # Check if each required document is present as a substring in the 'documents' string
        for req_doc in required_docs:
            if req_doc not in documents.strip().lower():
                missing_documents.append(req_doc)

        is_compliant = not bool(missing_documents)
        status_summary = "All mandatory documents were found." if is_compliant else "Some mandatory documents were not found."

        # Format the output similar to the original compliance_checker_tools
        compliance_status = "compliant" if is_compliant else "not compliant"
        missing_docs_str = ", ".join(missing_documents) if missing_documents else "None"
        return (f"Compliance check result: The shipment is {compliance_status}. "
                f"Missing documents: {missing_docs_str}. "
                f"Technical summary: {status_summary}.")

    elif procedure_compliance is not None and rag_result is not None:
        # --- Perform RAG Result Compliance Check ---
        is_compliant = False
        status_summary = ""
        missing_points = [] # Placeholder for more sophisticated comparison

        # Simple substring check for RAG result alignment with procedure
        if procedure_compliance.strip().lower() in rag_result.strip().lower():
            is_compliant = True
            status_summary = "The RAG result aligns well with the expected procedure compliance."
        else:
            is_compliant = False
            status_summary = "The RAG result does not fully align with the expected procedure compliance."
            # For a simple substring check, identifying specific "missing points" is hard.
            # This is a placeholder; real logic would involve parsing and comparing elements.
            missing_points.append("specific procedure details")

        # Format the output similar to the original compare_procedure_and_rag_compliance
        compliance_status = "compliant" if is_compliant else "not compliant"
        missing_points_str = ", ".join(missing_points) if missing_points else "None"

        return (f"Compliance check result: The RAG result is {compliance_status} with the procedure. "
                f"Missing aspects: {missing_points_str}. "
                f"Technical summary: {status_summary}.")
    else:
        # Handle cases where an invalid combination of inputs is provided
        return "Error: Invalid input. Please provide either 'plan' and 'documents' for a document compliance check, or 'procedure_compliance' and 'rag_result' for a RAG comparison."

# Example of how you might use the new combined function (for testing purposes)
if __name__ == "__main__":
    print("--- Document Compliance Check Examples ---")
    # Example 1: Document Compliance Check (Compliant)
    doc_input_compliant = CombinedComplianceInput(
        plan="Invoice, Packing List, Bill of Lading",
        documents="The retrieved documents include: Invoice, Packing List, and Bill of Lading."
    )
    print("Document Compliance (Compliant):")
    print(compliance_checker_tools(doc_input_compliant))

    print("-" * 50)

    # Example 2: Document Compliance Check (Missing documents)
    doc_input_missing = CombinedComplianceInput(
        plan="Invoice, Packing List, Certificate of Origin",
        documents="The retrieved documents include: Invoice, Packing List."
    )
    print("Document Compliance (Missing):")
    print(compliance_checker_tools(doc_input_missing))

    print("\n--- RAG Compliance Comparison Examples ---")
    # Example 3: RAG Compliance Comparison (Compliant)
    rag_input_compliant = CombinedComplianceInput(
        procedure_compliance="All documents must be checked for completeness: Invoice, Packing List, Bill of Lading.",
        rag_result="The retrieved documents include: Invoice, Packing List, and Bill of Lading. All complete."
    )
    print("RAG Comparison (Compliant):")
    print(compliance_checker_tools(rag_input_compliant))

    print("-" * 50)

    # Example 4: RAG Compliance Comparison (Non-compliant)
    rag_input_non_compliant = CombinedComplianceInput(
        procedure_compliance="Mandatory: Safety Data Sheet and Certificate of Origin.",
        rag_result="Documents found: Invoice, Packing List, Safety Data Sheet."
    )
    print("RAG Comparison (Non-compliant):")
    print(compliance_checker_tools(rag_input_non_compliant))

    print("\n--- Invalid Input Example ---")
    # Example 5: Invalid Input (only one set of parameters provided)
    invalid_input = CombinedComplianceInput(plan="Invoice")
    print("Invalid Input:")
    print(compliance_checker_tools(invalid_input))
