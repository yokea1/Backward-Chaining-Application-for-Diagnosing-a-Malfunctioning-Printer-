# Lab 5 - Backward Chaining Application for Diagnosing a Malfunctioning Printer
# Define the rules: Hypotheses and their possible causes
rules = {
    "The printer does not turn on": ["Power cord issue", "Power outlet issue", "Power supply issue"],
    "The printer produces blank pages": ["Out of ink or toner", "Clogged print head", "Driver issue"],
    "The printer produces low-quality prints": ["Out of ink or toner", "Clogged print head",
                                                "Low-resolution print settings"],
    "The printer jams frequently": ["Paper feed issue", "Worn-out roller", "Dirty pickup roller", "Wrong paper type"],
    "The printer produces distorted prints": ["Driver issue", "Connectivity issue", "Wrong paper type"],
    "The printer produces smudged prints": ["Dirty print head", "Damaged ink cartridge", "Damaged paper"],
    "The printer prints slowly": ["High-resolution print settings", "Connectivity issue", "Low memory"]
}

def backward_chaining(symptoms, rules):
    """
    Backward chaining function to diagnose printer problems.
    :param symptoms: List of observed symptoms
    :param rules: Dictionary of hypotheses and possible causes
    :return: Diagnosed problem(s)
    """
    diagnoses = []

    for hypothesis, causes in rules.items():
        for cause in causes:
            for symptom in symptoms:
                if symptom.lower() in cause.lower() or symptom.lower() in hypothesis.lower():
                    diagnoses.append((hypothesis, cause))

    return diagnoses

# Example testing
if __name__ == "__main__":
    print("Printer Diagnosis System")
    print("-------------------------")

    # Example input: symptoms observed
    observed_symptoms = input("Enter observed symptoms (separated by commas): ").split(",")
    observed_symptoms = [symptom.strip() for symptom in observed_symptoms]

    # Run backward chaining
    result = backward_chaining(observed_symptoms, rules)

    if result:
        print("\nPossible Diagnoses:")
        for hypothesis, cause in result:
            print(f"- {hypothesis} (Cause: {cause})")
    else:
        print("\nNo matching diagnosis found based on the given symptoms.")

# Simple evaluation:
# Efficiency: Suitable for small sets of rules and symptoms, fast diagnosis.
# Accuracy: Depends on the quality and completeness of the rule definitions.
# Scalability: For a very large number of rules, performance may decrease.

