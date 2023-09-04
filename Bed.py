class Bed:
    """
    Class that manages information related to bed occupancy in a hospital.
    """

    @staticmethod
    def occupancy(n, d):
        """
        Calculates and displays the bed occupancy in the hospital.

        :param n: Number of patients admitted.
        :param d: Number of patients discharged.
        """
        total_beds = 300
        occupied = n - d
        print("The total available beds are:", total_beds - occupied)
        total_occupancy = (occupied * 100) / total_beds
        print(f"The total occupancy is: {total_occupancy:.2f}%")

    @staticmethod
    def average_stay(t, d):
        """
        Calculates and displays the average length of stay per service.

        :param t: Total time of stay for patients.
        :param d: Number of patients discharged.
        """
        if t == 0:
            print("There is no information yet")
        else:
            average_stay = t / d
            print(f"The average length of stay per service is: {average_stay:.2f} hours")

    @staticmethod
    def admissions_discharges_count(n, d):
        """
        Displays the count of hospital admissions and discharges.

        :param n: Number of admissions.
        :param d: Number of patients discharged.
        """
        print("Number of Admissions:", n)
        print("Number of Discharges:", d)
