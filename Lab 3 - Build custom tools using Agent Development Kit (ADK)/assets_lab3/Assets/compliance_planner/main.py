import asyncio
import logging
from pathlib import Path

# Impor fungsi build flow Anda dari file extract_compliance_info.py
from extract_compliance_info import run_full_compliance_check

from ibm_watsonx_orchestrate.flow_builder.flows.flow import FlowRunStatus

logger = logging.getLogger(__name__)

flow_run = None

def on_flow_end(result):
    """
    Callback function yang dipanggil saat flow selesai.
    """
    print("\n✅ HASIL AKHIR FLOW:")
    # Mengakses laporan dari hasil akhir flow
    final_report = result.get('final_report', 'Tidak ada laporan yang dihasilkan.')
    print(final_report)
    print("------------------------------------------")


def on_flow_error(error):
    """
    Callback function yang dipanggil saat flow gagal.
    """
    print(f"❌ CUSTOM HANDLER: Flow `{flow_run.name}` GAGAL: {error}")


async def main():
    """Fungsi untuk menjalankan flow secara programatik dan menyimpannya ke file."""
    
    # 1. Compile dan deploy flow Anda
    print("--- Mengompilasi Flow ---")
    my_flow_definition = await run_full_compliance_check().compile_deploy()

    # (Opsional) Simpan spesifikasi flow yang dihasilkan ke file JSON
    current_folder = Path(__file__).resolve().parent
    generated_folder = current_folder / "generated"
    generated_folder.mkdir(exist_ok=True)
    my_flow_definition.dump_spec(generated_folder / "compliance_check_flow.json")
    print(f"--- Spesifikasi Flow disimpan di {generated_folder / 'compliance_check_flow.json'} ---")

    # 2. Siapkan input untuk flow
    shipment_id_to_test = "SHIPMENT-XYZ-789"
    flow_input = {"shipment_id": shipment_id_to_test}

    # 3. Panggil (invoke) flow dengan input yang sudah disiapkan
    print(f"\n--- Menjalankan Flow untuk ID: {shipment_id_to_test} ---")
    global flow_run
    flow_run = await my_flow_definition.invoke(
        flow_input, 
        on_flow_end_handler=on_flow_end, 
        on_flow_error_handler=on_flow_error, 
        debug=True  # Set ke False jika tidak ingin melihat log detail
    )

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())