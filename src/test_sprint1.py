
from functions.loginfunctions import *


# Selecting any of these skills result in “under construction”
def test_frontendDevelopment():
    assert frontendDevelopment() == "\nunder construction"

def test_backendDevelopment():
    assert backendDevelopment() == "\nunder construction"

def test_databaseDesign():
    assert databaseDesign() == "\nunder construction"

def test_agileMethodologies():
    assert agileMethodologies() == "\nunder construction"

def test_gitVersionControl():
    assert gitVersionControl() == "\nunder construction"

# search for job / internship and find someone you know result in "under construction"

def test_searchForJob():
    assert searchForJob() == "\nunder construction"

def test_findSomeone():
    assert findSomeone() == "\nunder construction"