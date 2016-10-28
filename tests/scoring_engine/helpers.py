import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../scoring_engine'))

from models.team import Team
from models.user import User
from models.server import Server
from models.service import Service
from models.property import Property
from models.check import Check


def generate_sample_model_tree(model, db):
    # Team
    team = Team(name="Team 1", color="Blue")
    db.save(team)
    if model == 'Team':
        return team

    # Users
    user = User(username="testuser", password="catdog", team=team)
    db.save(user)
    if model == 'User':
        return user

    # Servers
    server = Server(name="Example Server", team=team)
    db.save(server)
    if model == 'Server':
        return server

    # Services
    service = Service(name="ICMP IPv4", server=server, check_name="ICMP IPv4 Check")
    db.save(service)
    if model == 'Service':
        return service

    # Properties
    property_obj = Property(name="ip", value="127.0.0.1", service=service)
    db.save(property_obj)
    if model == 'Property':
        return property_obj

    # Rounds
    # round_obj = Round(...)

    # Checks
    check = Check(round_num=1, service=service, result=True, output="Sample output", reason="Sample reason")
    db.save(check)
    if model == 'Check':
        return check
