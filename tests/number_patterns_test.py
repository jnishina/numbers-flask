import pytest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from number_patterns import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    rv = client.get("/")
    assert b'Welcome to Finding Patterns in Numbers!' in rv.data

def test_non_int(client):
    rv = client.get("/3.4")
    assert b'<p>Oops! Passed value is not an int.</p>' in rv.data

def test_n_numbers(client):
    rv = client.get("/3")
    for i in range(1, 4):
        assert b'%d' %i in rv.data

def test_even_numbers(client):
    rv = client.get("/6/even")
    for i in range(1, 7):
        if i%2 == 0:
            assert b'%d' %i in rv.data
        if not i%2 == 0:
            assert b'%d' %i not in rv.data

def test_odd_numbers(client):
    rv = client.get("/21/odd")
    for i in range(1, 22):
        if i%2 == 0:
            assert b'<li>%d</li>' %i not in rv.data
        if not i%2 == 0:
            assert b'<li>%d</li>' %i in rv.data

def test_prime_numbers(client):
    rv = client.get("/10/prime")
    numInt = 10
    primes = [1] * (numInt+1)
    primes[0] = primes[1] = 0

    for i in range(2, int((numInt+1)**0.5)+1):
        if primes[i]:
            lowerbound = i**2
            while lowerbound < numInt+1:
                primes[lowerbound] = 0
                lowerbound += i
    
    for i in range(11):
        assert (b'<li>%d</li>' %i in rv.data) == primes[i]