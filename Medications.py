class Medications:
    """
    Class for providing medical recommendations based on medical parameter values.
    """

    @staticmethod
    def temperature(n):
        """
        Provides recommendations for abnormal body temperature.

        :param n: Body temperature value.
        """
        if n >= 41 or n <= 35:
            if n >= 41:
                print("Recommendations for Hyperthermia:")
                print("Cooler Environment: Place the person in a cooler or lower-temperature environment.")
                print("Light Clothing: Dress in light and loose-fitting clothing to allow better heat dissipation.")
                print("Hydration: Drink water and cool fluids to aid in the cooling process through sweating.")
                print("Fans or Air Conditioning: Use fans or air conditioning to lower the room temperature.")
                print("Cold Compresses or Baths: Apply cold compresses or take a tepid water bath to lower body temperature.")
                print("Rest: Rest and avoid strenuous physical activity that may increase body temperature.")
            else:
                print("Recommendations for Hypothermia:")
                print("Medical Attention: If hypothermia is severe or if the person shows signs of confusion or extreme weakness, seek medical attention immediately.")
                print("In some severe cases of hypothermia, specific medications may be administered in a medical setting.")

    @staticmethod
    def respiratory_rate(n):
        """
        Provides recommendations for abnormal respiratory rate.

        :param n: Boolean value indicating whether the respiratory rate is high (True) or low (False).
        """
        if n:
            print("Recommendations for Elevated Respiratory Rate:")
            print("Bronchodilator Medications: These may help open airways and relieve breathing difficulties.")
            print("Sedatives or Anxiolytics: These may be prescribed to calm the patient and reduce respiratory rate.")
            print("Antibiotics or Antivirals: These may be necessary to treat the underlying infection.")
            print("Cardiac Medications: In cases of heart disease, specific medications may be prescribed to improve cardiac function.")
        else:
            print("Recommendations for Low Respiratory Rate:")
            print("Respiratory Stimulant Medications: These may be prescribed to increase respiratory rate.")
            print("Device Therapy: In some cases, devices such as pacemakers or mechanical ventilators may be used.")
            print("Medication Adjustment: If bradypnea is caused by medication side effects, adjusting the dosage under medical supervision may be necessary.")

    @staticmethod
    def oxygen_saturation():
        """
        Provides recommendations for low oxygen saturation.
        """
        print("Recommendations for Low Oxygen Saturation:")
        print("Oxygen Supplement: Oxygen can be administered through concentrators, tanks, or masks depending on severity.")
        print("Improving Ventilation: Teach breathing exercises and clear airway obstructions.")
        print("Treating the Underlying Cause: Identify and treat the root cause, such as respiratory infections or heart problems.")
        print("Hospitalization: In severe cases or difficulty breathing, hospitalization may be necessary.")
        print("Maintaining Proper Position: Assist the patient in maintaining a position that facilitates breathing.")
        print("Administering Medications: In some cases, bronchodilators or diuretics may be prescribed based on the underlying cause.")

    @staticmethod
    def blood_pressure(n, m):
        """
        Provides recommendations for abnormal blood pressure.

        :param n: Systolic blood pressure value.
        :param m: Diastolic blood pressure value.
        """
        if (90 > n or n > 150) and (50 > m or m > 90):
            if (n > 150 or m > 90):
                print("Recommendations for High Blood Pressure:")
                print("Diuretics: Help eliminate excess salt and water from the body, reducing blood pressure.")
                print("Beta-Blockers: Reduce heart rate and the force of heart contractions.")
                print("Angiotensin-Converting Enzyme Inhibitors (ACEIs): Relax blood vessels and reduce resistance in arteries.")
                print("Angiotensin II Receptor Blockers (ARBs): Function similarly to ACEIs by relaxing blood vessels.")
                print("Calcium Channel Blockers: Relax blood vessels and reduce arterial resistance.")
            else:
                print("Recommendations for Low Blood Pressure:")
                print("Medications: In cases of severe symptomatic hypotension, the doctor may prescribe specific medications to raise blood pressure.")
