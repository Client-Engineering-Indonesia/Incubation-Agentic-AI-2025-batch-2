orchestrate env activate activate env activateEU-New-Agentic
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

for flow_tool in compliance_checker_tools.py compliance_finish_tools.py compliance_plan_generator_tools.py; do
orchestrate tools import -k python -f ${SCRIPT_DIR}/tools/${flow_tool}
done

for agent in compliance_Checker_Agent.yaml AgentContract_RD_9820Yw.yaml compliance_Finish_Agent.yaml Compliance_Plan_Generator_Agent.yaml; do
orchestrate agents import -f ${SCRIPT_DIR}/agents/${agent}
done

for flow_tool in check_compliance_flow.py; do
orchestrate tools import -k flow -f ${SCRIPT_DIR}/tools/${flow_tool}
done

for agent in compliance_system.yaml; do
orchestrate agents import -f ${SCRIPT_DIR}/agents/${agent}
done