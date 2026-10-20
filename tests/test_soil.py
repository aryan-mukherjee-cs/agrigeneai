from app import diagnose_soil


def test_strongly_acidic():
    result = diagnose_soil(50, 50, 50, 5.0)
    assert result["ph_class"] == "Strongly Acidic"


def test_moderately_acidic():
    result = diagnose_soil(50, 50, 50, 5.7)
    assert result["ph_class"] == "Moderately Acidic"


def test_optimal_ph():
    result = diagnose_soil(50, 50, 50, 7.0)
    assert result["ph_class"] == "Optimal (Neutral)"


def test_moderately_alkaline():
    result = diagnose_soil(50, 50, 50, 8.0)
    assert result["ph_class"] == "Moderately Alkaline"


def test_strongly_alkaline():
    result = diagnose_soil(50, 50, 50, 9.0)
    assert result["ph_class"] == "Strongly Alkaline"

def test_ph_5_5_boundary():
    result = diagnose_soil(50, 50, 50, 5.5)
    assert result["ph_class"] == "Moderately Acidic"


def test_ph_6_0_boundary():
    result = diagnose_soil(50, 50, 50, 6.0)
    assert result["ph_class"] == "Optimal (Neutral)"


def test_ph_7_5_boundary():
    result = diagnose_soil(50, 50, 50, 7.5)
    assert result["ph_class"] == "Optimal (Neutral)"


def test_ph_8_5_boundary():
    result = diagnose_soil(50, 50, 50, 8.5)
    assert result["ph_class"] == "Moderately Alkaline"

def test_ph_5_5_boundary():
    result = diagnose_soil(50, 50, 50, 5.5)
    assert result["ph_class"] == "Moderately Acidic"


def test_ph_6_0_boundary():
    result = diagnose_soil(50, 50, 50, 6.0)
    assert result["ph_class"] == "Optimal (Neutral)"


def test_ph_7_5_boundary():
    result = diagnose_soil(50, 50, 50, 7.5)
    assert result["ph_class"] == "Optimal (Neutral)"


def test_ph_8_5_boundary():
    result = diagnose_soil(50, 50, 50, 8.5)
    assert result["ph_class"] == "Moderately Alkaline"

def test_nitrogen_critically_low():
    result = diagnose_soil(20, 50, 50, 7.0)
    assert "Nitrogen (N) is critically low." in result["warnings"]


def test_nitrogen_normal():
    result = diagnose_soil(50, 50, 50, 7.0)
    assert not any("Nitrogen (N)" in warning for warning in result["warnings"])


def test_nitrogen_high():
    result = diagnose_soil(120, 50, 50, 7.0)
    assert "Nitrogen (N) is high (potential environmental leaching risk)." in result["warnings"]


def test_phosphorus_critically_low():
    result = diagnose_soil(50, 20, 50, 7.0)
    assert "Phosphorus (P) is critically low." in result["warnings"]


def test_phosphorus_normal():
    result = diagnose_soil(50, 50, 50, 7.0)
    assert not any("Phosphorus (P)" in warning for warning in result["warnings"])


def test_phosphorus_high():
    result = diagnose_soil(50, 100, 50, 7.0)
    assert "Phosphorus (P) is high." in result["warnings"]


def test_potassium_critically_low():
    result = diagnose_soil(50, 50, 20, 7.0)
    assert "Potassium (K) is critically low." in result["warnings"]


def test_potassium_normal():
    result = diagnose_soil(50, 50, 50, 7.0)
    assert not any("Potassium (K)" in warning for warning in result["warnings"])


def test_potassium_high():
    result = diagnose_soil(50, 50, 120, 7.0)
    assert "Potassium (K) is high." in result["warnings"]

