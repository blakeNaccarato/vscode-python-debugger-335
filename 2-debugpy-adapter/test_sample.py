import json

def test_answer():
    assert json.dumps({'toto': 'tata'}) == "{'toto': 'tata'}"
