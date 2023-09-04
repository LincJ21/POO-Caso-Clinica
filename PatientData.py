class PatientNode:
    """Class to represent a patient node in an AVL tree."""

    def __init__(self, id_number, name, gender, date_of_birth, systolic_blood_pressure, diastolic_blood_pressure, temperature, oxygen_saturation, respiratory_rate, progress_note, diagnostic_image_code, lab_test_results, prescribed_medications):
        """
        Constructor for PatientNode.

        Args:
            id_number (int): Patient's document number.
            name (str): Patient's name.
            gender (str): Patient's gender ('M' or 'F').
            date_of_birth (datetime): Patient's date of birth.
            systolic_blood_pressure (int): Patient's systolic blood pressure.
            diastolic_blood_pressure (int): Patient's diastolic blood pressure.
            temperature (float): Patient's temperature in degrees Celsius.
            oxygen_saturation (float): Patient's oxygen saturation in percentage.
            respiratory_rate (float): Patient's respiratory rate in seconds.
            progress_note (str): Patient's progress note.
            diagnostic_image_code (str): Patient's diagnostic image code.
            lab_test_results (str): Patient's lab test results.
            prescribed_medications (str): Medications prescribed for the patient.
        """
        self.id_number = id_number
        self.name = name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.systolic_blood_pressure = systolic_blood_pressure
        self.diastolic_blood_pressure = diastolic_blood_pressure
        self.temperature = temperature
        self.oxygen_saturation = oxygen_saturation
        self.respiratory_rate = respiratory_rate
        self.progress_note = progress_note
        self.diagnostic_image_code = diagnostic_image_code
        self.lab_test_results = lab_test_results
        self.prescribed_medications = prescribed_medications
        self.height = 1
        self.left = None
        self.right = None

class PatientData:
    """Class to manage patients in an AVL tree."""

    def __init__(self):
        # Constructor for PatientData. Initializes an empty AVL tree.
        self.root = None

    def insert(self, id_number, name, gender, date_of_birth, systolic_blood_pressure, diastolic_blood_pressure, temperature, oxygen_saturation, respiratory_rate, progress_note, diagnostic_image_code, lab_test_results, prescribed_medications):

        self.root = self._recursive_insert(
            self.root, id_number, name, gender, date_of_birth, systolic_blood_pressure, diastolic_blood_pressure, temperature, oxygen_saturation, respiratory_rate, progress_note, diagnostic_image_code, lab_test_results, prescribed_medications)

    def _height(self, node):
        # Get the height of a node.
        if node is None:
            return 0
        return node.height

    def _balance(self, node):
        # Calculate the balance factor of a node (difference in height between left and right subtrees).
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, z):
        # Perform a right rotation on node z.
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._height(z.left), self._height(z.right))
        y.height = 1 + max(self._height(y.left), self._height(y.right))

        return y

    def _rotate_left(self, y):
        # Perform a left rotation on node y.
        x = y.right
        T2 = x.left

        x.left = y
        y.right = T2

        y.height = 1 + max(self._height(y.left), self._height(y.right))
        x.height = 1 + max(self._height(x.left), self._height(x.right))

        return x

    def _recursive_insert(self, root, id_number, name, gender, date_of_birth, systolic_blood_pressure, diastolic_blood_pressure, temperature, oxygen_saturation, respiratory_rate, progress_note, diagnostic_image_code, lab_test_results, prescribed_medications):
        # Insert a patient recursively into the AVL tree.

        if root is None:
            return PatientNode(id_number, name, gender, date_of_birth, systolic_blood_pressure, diastolic_blood_pressure, temperature, oxygen_saturation, respiratory_rate, progress_note, diagnostic_image_code, lab_test_results, prescribed_medications)

        if id_number < root.id_number:
            root.left = self._recursive_insert(
                root.left, id_number, name, gender, date_of_birth, systolic_blood_pressure, diastolic_blood_pressure, temperature, oxygen_saturation, respiratory_rate, progress_note, diagnostic_image_code, lab_test_results, prescribed_medications)
        else:
            root.right = self._recursive_insert(
                root.right, id_number, name, gender, date_of_birth, systolic_blood_pressure, diastolic_blood_pressure, temperature, oxygen_saturation, respiratory_rate, progress_note, diagnostic_image_code, lab_test_results, prescribed_medications)

        root.height = 1 + max(self._height(root.left),
                              self._height(root.right))

        balance = self._balance(root)

        # Rotation cases to balance the AVL tree
        if balance > 1:
            """Right rotation case: When the left subtree of the left subtree of the root node
            has a balance greater than 1 (single right rotation)."""
            if id_number < root.left.id_number:
                return self._rotate_right(root)
            else:
                root.left = self._rotate_left(root.left)
                return self._rotate_right(root)
            
        if balance < -1:
            """Left rotation case: When the right subtree of the right subtree of the root node
            has a balance less than -1 (single left rotation)."""
            if id_number > root.right.id_number:
                return self._rotate_left(root)
            else:
                root.right = self._rotate_right(root.right)
                return self._rotate_left(root)

        # Returns: PatientNode: Root node of the current subtree after insertion.
        return root
