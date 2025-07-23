# #!/usr/bin/env bash

# set -x

# # Mengatur direktori script
# SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )


# # Loop untuk mengimpor semua tool Python individual
# for python_tool in get_shipment_data.py check_compliance.py; do
#   orchestrate tools import -k python -f "${SCRIPT_DIR}/tools/${python_tool}"
# done

# # Mengimpor definisi flow utama
# for flow_tool in extract_compliance_info.py; do
#   orchestrate tools import -k flow -f "${SCRIPT_DIR}/${flow_tool}" 
# done

# # Mengimpor agent yang akan menggunakan flow
# for agent in compliance_agent.yaml; do
#   orchestrate agents import -f "${SCRIPT_DIR}/agents/${agent}"
# done


################### yang bawahh bisa ################ 


orchestrate env activate incubation-agent
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

