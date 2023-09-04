from datetime import datetime

from PatientData import PatientData
from Medications import Medications

class Medical_History:
    """
    Class for managing the medical history of patients.

    Args:
        patient_data (Patient_Data): Object of Patient_Data to store patient information.
    """

    def __init__(self, patient_data):
        """
        Constructor for Medical_History.

        Args:
            patient_data (Patient_Data): Object of Patient_Data to store patient information.
        """
        self.patient_data = patient_data

    def inorder_traversal(self):
        """
        Performs an in-order traversal of the patient tree and prints their data.
        """
        self._inorder_traversal_recursive(self.patient_data.root)

    def _inorder_traversal_recursive(self, root):
        """
        Performs a recursive in-order traversal of the patient tree and prints their data.

        Args:
            root (PatientNode): Root node of the current subtree.
        """
        if root:
            self._inorder_traversal_recursive(root.left)
            print("------------------------------------------------------------------------------------")
            print(f"ID Number: {root.id_number}\tName: {root.name}\tGender: {root.gender}\t\tDate of Birth: {root.date_of_birth}")
            print(f"Systolic Blood Pressure: {root.systolic_blood_pressure}\tDiastolic Blood Pressure: {root.diastolic_blood_pressure}")
            print(f"Temperature: {root.temperature}\nOxygen Saturation: {root.oxygen_saturation}\nRespiratory Rate: {root.respiratory_rate}")
            print(f"Progress Note: {root.progress_note}\nDiagnostic Image Code: {root.diagnostic_image_code}\nLab Test Results: {root.lab_test_results}\nPrescribed Medications: {root.prescribed_medications}")
            self.evaluate_state(root)
            print("------------------------------------------------------------------------------------")
            self._inorder_traversal_recursive(root.right)

    def evaluate_state(self, root):
        """
        Evaluates the state of a patient and displays possible alerts.

        Args:
            root (PatientNode): Node of the patient to evaluate.
        """
        medications = Medications()
        i = 0
        current_date = datetime.now()
        age = current_date.year - root.date_of_birth.year - ((current_date.month, current_date.day) < ((root.date_of_birth).month, (root.date_of_birth).day))

        if root.temperature >= 41 or root.temperature <= 35:
            i += 1
            if root.temperature >= 41:
                print("The patient has Hyperthermia")
            else:
                print("The patient has Hypothermia")
            print("------------------------------------------------------------------------------------")
            medications.temperature(root.temperature)
        
        if (root.respiratory_rate > 40 or root.respiratory_rate < 24) and (age == 1 and age <= 5):
            if root.respiratory_rate > 40:
                print("[Respiratory Rate is very high]")
                print("------------------------------------------------------------------------------------")
                medications.respiratory_rate(True)
            else:
                print("[Respiratory Rate is very low]")
                print("------------------------------------------------------------------------------------")
                medications.respiratory_rate(False)
            i += 1
        elif (root.respiratory_rate > 30 or root.respiratory_rate < 18) and (age >= 6 and age <= 13):
            if root.respiratory_rate > 30:
                print("[Respiratory Rate is very high]")
                print("------------------------------------------------------------------------------------")
                medications.respiratory_rate(True)
            else:
                print("[Respiratory Rate is very low]")
                print("------------------------------------------------------------------------------------")
                medications.respiratory_rate(False)
            i += 1
        elif ((root.respiratory_rate > 12 and root.respiratory_rate > 16) or (root.respiratory_rate < 16 and root.respiratory_rate < 12)) and (age >= 14):
            if root.respiratory_rate > 16:
                print("[Respiratory Rate is very high]")
                print("------------------------------------------------------------------------------------")
                medications.respiratory_rate(True)
            else:
                print("[Respiratory Rate is very low]")
                print("------------------------------------------------------------------------------------")
                medications.respiratory_rate(False)
            i += 1

        if (90 > root.systolic_blood_pressure or root.systolic_blood_pressure > 150) and (50 > root.diastolic_blood_pressure or root.diastolic_blood_pressure > 90):
            if (root.systolic_blood_pressure > 150 or root.diastolic_blood_pressure > 90):
                print("[Very high Blood Pressure]")
                i += 1
            else:
                print("[Very low Blood Pressure]")
                i += 1
            print("------------------------------------------------------------------------------------")
            medications.blood_pressure(root.systolic_blood_pressure, root.diastolic_blood_pressure)
        
        if root.oxygen_saturation < 85:
            print(f"[Oxygen Saturation [{root.oxygen_saturation}%] is very low, the patient may have Severe Hypoxia]")
            i += 1
            print("------------------------------------------------------------------------------------")
            medications.oxygen_saturation()

        if i > 0:
            print("The patient may have a chronic disease")
        else:
            print("The patient shows no signs of chronic disease")
