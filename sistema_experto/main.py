import json
from rules.project_recomendation_rules import ProjectConditions
from rules.project_recomendation_rules import TimeProjectConditions
from rules.project_recomendation_rules import ProjectRecomendationRules

engine = ProjectRecomendationRules()
engine.reset()


#Probamos con el caso de prueba 1
engine.declare(
    ProjectConditions('Mongo'),
    ProjectConditions('Polymer'),
    ProjectConditions('Go Lang'),
    ProjectConditions('Networking'),
    TimeProjectConditions(timeProject='10')
    )

engine.run()
message, image = engine.get_recomendation()
print ("message:", message)
print ("image:", image)
