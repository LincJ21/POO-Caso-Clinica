from datetime import datetime

from PatientData import PatientData
from Medical_History import Medical_History
from Bed import Bed

def validate_number(message):
    """Validates and returns a non-negative integer entered by the user."""
    while True:
        try:
            number = float(input(message))
            if number >= 0:
                return number
            print("Error. It must be a non-negative number.")
        except ValueError:
            print("Error. You must enter a valid number.")

def main():
    patient_data = PatientData()
    bed = Bed()
    medical_history = Medical_History(patient_data)
    i, d, time = 0, 0, 0

    while True:
        print("------------------------------------------------------------------------------------")
        print("Menu\n [1]. Enter patient\n",
            "[2]. Print medical history of Patients\n",
            "[3]. Clinic occupancy information\n",
            "[4]. Exit")
        choice = validate_number("Enter the number: ")
        print("------------------------------------------------------------------------------------")
        while choice < 1 or choice > 4:
            choice = validate_number("Error. Enter the number: ")

        if choice == 4:
            break

        if choice == 1:
            while True:
                id_number = validate_number("Document Number: ")
                name = input("Name: ")
                
                # Validate gender
                gender = input("Gender (M/F): ").upper()
                while gender != "M" and gender != "F":
                    gender = input("Error. Gender (M/F): ").upper()
                
                # Validate date of birth
                while True:
                    try:
                        birthdate_str = input("Enter your date of birth (YYYY-MM-DD): ")
                        date_of_birth = datetime.strptime(birthdate_str, "%Y-%m-%d")
                        break
                    except ValueError:
                        print("Incorrect date format. Please use YYYY-MM-DD format.")
                        continue

                systolic_blood_pressure = validate_number("Systolic Blood Pressure: ")
                diastolic_blood_pressure = validate_number("Diastolic Blood Pressure: ")
                temperature = validate_number("Temperature (°C): ")
                oxygen_saturation = validate_number("Oxygen Saturation (%): ")
                respiratory_rate = validate_number("Respiratory Rate (rpm): ")
                progress_note = input("Progress Note: ")
                diagnostic_image_code = input("Diagnostic Image Code: ") 
                lab_test_results = input("Lab Test Results: ")
                prescribed_medications = input("Prescribed Medications: ")

                # To determine the duration of patient care and whether they are discharged, ask the following question
                status = validate_number("Please confirm if the patient is still in the clinic or not. [1]: True or [2]: False: ")
                while status != 1 and status != 2:
                    status = validate_number("Error. Enter [1]: True or [2]: False: ")
                
                if status == 2:
                    time += float(input("Enter the time taken for care: "))
                    d += 1

                patient_data.insert(id_number, name, gender, date_of_birth, systolic_blood_pressure, diastolic_blood_pressure, temperature, oxygen_saturation, respiratory_rate, progress_note, diagnostic_image_code, lab_test_results, prescribed_medications)
                i += 1

                option = input("Do you want to continue (y/n): ")
                if option.lower() != "y":
                    break

        elif choice == 2:
            print("Print List:")
            medical_history.inorder_traversal()
        elif choice == 3:
            bed.occupancy(i, d)
            bed.average_stay(time, d)
            bed.admissions_discharges_count(i, d)

if __name__ == "__main__":
    main()
