from services import app
from flask import Flask, render_template, request, redirect, url_for, Response
from .rules.project_recomendation_rules import ProjectConditions
from .rules.project_recomendation_rules import TimeProjectConditions
from .rules.project_recomendation_rules import ProjectRecomendationRules
import json

@app.route('/services/health-check', methods=['GET'])
def health_check():
  body = {
      'msg': 'Hola Mundo!',
  }
  return Response(json.dumps(body), mimetype='application/json')

@app.route('/services/obtener-recursos', methods=['POST'])
def obtener_resursos():
  contenido = request.get_json()

  engine = ProjectRecomendationRules()
  engine.reset()


  #Probamos con el caso de prueba 1
  engine.declare(
    ProjectConditions(contenido['tecnologia1']),
    ProjectConditions(contenido['tecnologia2']),
    ProjectConditions(contenido['tecnologia3']),
    ProjectConditions(contenido['tecnologia4']),
    TimeProjectConditions(timeProject=contenido['timeProject'])
  )

  engine.run()
  message, image = engine.get_recomendation()
  body = {
      'message': message,
      'image': image
  }

  return Response(json.dumps(body), mimetype='application/json')
