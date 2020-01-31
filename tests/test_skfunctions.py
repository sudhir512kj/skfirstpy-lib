from skpylib import skfunctions


def test_haversine():
    assert skfunctions.haversine(
        52.370216, 4.895168, 52.520008, 13.404954) == 945793.4375088713
