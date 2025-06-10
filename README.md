# :car: Vehicle Diagnostics - Pytest + CI 🚀

This is a simple python project for vehicle diagnostics, built with a focus on **automated testing** using `pytest` and **Continuous Integration** (CI) via **GitHub Actions**.

The diagnostic logic mimics simple real-world automotive scenarios such as:
- Detecting if a vehicle is **stationary**, **moving**, or **overspeeding**
- Classifying vehicle status based on speed thresholds
- Validating diagnostic output using **unit tests**

### 🛠️ Use Case
In modern automotive software, diagnostics play a crucial role in monitoring sensor data, reporting vehicle health, and triggering alerts. This mini-project is a learning-level simulation of how such logic can be:
- Developed with Python
- Verified with automated unit tests
- Integrated into a CI workflow

---
## 📁 Project Structure

```text
vehicle_diagnostics_pytest/
├── diagnostics.py            # Diagnostic logic
├── test_diagnostics.py       # Pytest test cases
├── requirements.txt          # Dependencies
└── .github/
    └── workflows/
        └── pytest.yml        # CI workflow for GitHub Actions
```

## 🧪 How to Run Tests Locally

```bash
# Clone the repository
git clone https://github.com/Saketh1196/vehicle_diagnostics_pytest.git
cd vehicle_diagnostics_pytest

# Install dependencies
pip install -r requirements.txt

# Run Tests
pytest

----
## ⚙️ Technologies Used

- 🐍 Python 3.12.10
- ✅ Pytest
- 🔁 GitHub Actions (CI)
- 🧪 Unit Testing

