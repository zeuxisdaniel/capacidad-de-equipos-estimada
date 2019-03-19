from pyknow import *

class ProjectConditions(Fact):
    pass

class TimeProjectConditions(Fact):
    pass

class ProjectRecomendationRules(KnowledgeEngine):

    def __init__(self, *args, **kwargs):
        self.numRecomended = 'NO_MESSAGE'
        self.img = 'NO_IMAGE'
        super().__init__(*args, **kwargs)

    @Rule(TimeProjectConditions(timeProject=MATCH.tp),
        AND (
            OR (
                ProjectConditions('Mongo'),
                ProjectConditions('NoSQL'),
                ProjectConditions('SQL')
            ),
            OR (
                ProjectConditions('Polymer'),
                ProjectConditions('JavaScript'),
                ProjectConditions('MVC'),
                ProjectConditions('Sprint')
            ),
            OR (
                ProjectConditions('Java'),
                ProjectConditions('Python'),
                ProjectConditions('.NET'),
                ProjectConditions('Go Lang'),
                ProjectConditions('C++'),
                ProjectConditions('R'),
                ProjectConditions('C#'),
                ProjectConditions('Ruby')
            ),
            OR (
                ProjectConditions('Networking'),
                ProjectConditions('Security')
            )
        )
    )
    def rule_1(self,tp):
        recomendados = 3 + int(int(tp) / 4)
        self.message = 'Te recomendamos tener '+ str(recomendados) + ' recursos en tu equipo'
        self.img = 'png1.png'

    @Rule(TimeProjectConditions(timeProject=MATCH.tp),
        AND (
            OR (
                ProjectConditions('Polymer'),
                ProjectConditions('JavaScript'),
                ProjectConditions('MVC'),
                ProjectConditions('Sprint')
            ),
            OR (
                ProjectConditions('Java'),
                ProjectConditions('Python'),
                ProjectConditions('.NET'),
                ProjectConditions('Go Lang'),
                ProjectConditions('C++'),
                ProjectConditions('R'),
                ProjectConditions('C#'),
                ProjectConditions('Ruby')
            ),
            OR (
                ProjectConditions('Networking'),
                ProjectConditions('Security')
            ),
            OR (
                ProjectConditions('REST'),
                ProjectConditions('Flask')
            )
        )
    )
    def rule_2(self,tp):
        recomendados = 3 + int(int(tp) / 4)
        self.message = 'Te recomendamos tener '+ str(recomendados) + ' recursos en tu equipo'
        self.img = 'png1.png'

    @Rule(TimeProjectConditions(timeProject=MATCH.tp),
        AND (
            OR (
                ProjectConditions('Networking'),
                ProjectConditions('Security')
            ),
            OR (
                ProjectConditions('REST'),
                ProjectConditions('Flask')
            ),
            OR (
                ProjectConditions('AWS'),
                ProjectConditions('GCP'),
                ProjectConditions('Azure')
            ),
            OR (
                ProjectConditions('Mongo'),
                ProjectConditions('NoSQL'),
                ProjectConditions('SQL')
            )
        )
    )
    def rule_3(self,tp):
        recomendados = 4 + int(int(tp) / 4)
        self.message = 'Te recomendamos tener '+ str(recomendados) + ' recursos en tu equipo'
        self.img = 'png1.png'

    @Rule(TimeProjectConditions(timeProject=MATCH.tp),
        AND (
            OR (
                ProjectConditions('REST'),
                ProjectConditions('Flask')
            ),
            OR (
                ProjectConditions('AWS'),
                ProjectConditions('GCP'),
                ProjectConditions('Azure')
            ),
            OR (
                ProjectConditions('Mongo'),
                ProjectConditions('NoSQL'),
                ProjectConditions('SQL')
            ),
            OR (
                ProjectConditions('Polymer'),
                ProjectConditions('JavaScript'),
                ProjectConditions('MVC'),
                ProjectConditions('Sprint')
            )
        )
    )
    def rule_4(self,tp):
        recomendados = 5 + int(int(tp) / 4)
        self.message = 'Te recomendamos tener '+ str(recomendados) + ' recursos en tu equipo'
        self.img = 'png1.png'

    @Rule(TimeProjectConditions(timeProject=MATCH.tp),
        AND (
            OR (
                ProjectConditions('AWS'),
                ProjectConditions('GCP'),
                ProjectConditions('Azure')
            ),
            OR (
                ProjectConditions('Mongo'),
                ProjectConditions('NoSQL'),
                ProjectConditions('SQL')
            ),
            OR (
                ProjectConditions('Polymer'),
                ProjectConditions('JavaScript'),
                ProjectConditions('MVC'),
                ProjectConditions('Sprint')
            ),
            OR (
                ProjectConditions('Java'),
                ProjectConditions('Python'),
                ProjectConditions('.NET'),
                ProjectConditions('Go Lang'),
                ProjectConditions('C++'),
                ProjectConditions('R'),
                ProjectConditions('C#'),
                ProjectConditions('Ruby')
            )
        )
    )
    def rule_5(self,tp):
        recomendados = 4 + int(int(tp) / 4)
        self.message = 'Te recomendamos tener '+ str(recomendados) + ' recursos en tu equipo'
        self.img = 'png1.png'

    @Rule(TimeProjectConditions(timeProject=MATCH.tp),
        AND (
            OR (
                ProjectConditions('Mongo'),
                ProjectConditions('NoSQL'),
                ProjectConditions('SQL')
            ),
            OR (
                ProjectConditions('Java'),
                ProjectConditions('Python'),
                ProjectConditions('.NET'),
                ProjectConditions('Go Lang'),
                ProjectConditions('C++'),
                ProjectConditions('R'),
                ProjectConditions('C#'),
                ProjectConditions('Ruby')
            ),
            OR (
                ProjectConditions('REST'),
                ProjectConditions('Flask')
            ),
            OR (
                ProjectConditions('Networking'),
                ProjectConditions('Security')
            )
        )
    )
    def rule_6(self,tp):
        recomendados = 2 + int(int(tp) / 4)
        self.message = 'Te recomendamos tener '+ str(recomendados) + ' recursos en tu equipo'
        self.img = 'png1.png'

    @Rule(TimeProjectConditions(timeProject=MATCH.tp),
        AND (
            OR (
                ProjectConditions('Java'),
                ProjectConditions('Python'),
                ProjectConditions('.NET'),
                ProjectConditions('Go Lang'),
                ProjectConditions('C++'),
                ProjectConditions('R'),
                ProjectConditions('C#'),
                ProjectConditions('Ruby')
            ),
            OR (
                ProjectConditions('Polymer'),
                ProjectConditions('JavaScript'),
                ProjectConditions('MVC'),
                ProjectConditions('Sprint')
            ),
            OR (
                ProjectConditions('AWS'),
                ProjectConditions('GCP'),
                ProjectConditions('Azure')
            ),
            OR (
                ProjectConditions('REST'),
                ProjectConditions('Flask')
            )
        )
    )
    def rule_7(self,tp):
        recomendados = 6 + int(int(tp) / 4)
        self.message = 'Te recomendamos tener '+ str(recomendados) + ' recursos en tu equipo'
        self.img = 'png1.png'

    @Rule(TimeProjectConditions(timeProject=MATCH.tp),
        AND (
            OR (
                ProjectConditions('Mongo'),
                ProjectConditions('NoSQL'),
                ProjectConditions('SQL')
            ),
            OR (
                ProjectConditions('Polymer'),
                ProjectConditions('JavaScript'),
                ProjectConditions('MVC'),
                ProjectConditions('Sprint')
            ),
            OR (
                ProjectConditions('Networking'),
                ProjectConditions('Security')
            ),
            OR (
                ProjectConditions('AWS'),
                ProjectConditions('GCP'),
                ProjectConditions('Azure')
            )
        )
    )
    def rule_8(self,tp):
        recomendados = 6 + int(int(tp) / 4)
        self.message = 'Te recomendamos tener '+ str(recomendados) + ' recursos en tu equipo'
        self.img = 'png1.png'

    @Rule(TimeProjectConditions(timeProject=MATCH.tp),
        AND (
            OR (
                ProjectConditions('AWS'),
                ProjectConditions('GCP'),
                ProjectConditions('Azure')
            ),
            OR (
                ProjectConditions('Networking'),
                ProjectConditions('Security')
            ),
            OR (
                ProjectConditions('Mongo'),
                ProjectConditions('NoSQL'),
                ProjectConditions('SQL')
            ),
            OR (
                ProjectConditions('Java'),
                ProjectConditions('Python'),
                ProjectConditions('.NET'),
                ProjectConditions('Go Lang'),
                ProjectConditions('C++'),
                ProjectConditions('R'),
                ProjectConditions('C#'),
                ProjectConditions('Ruby')
            )
        )
    )
    def rule_9(self,tp):
        recomendados = 2 + int(int(tp) / 4)
        self.message = 'Te recomendamos tener '+ str(recomendados) + ' recursos en tu equipo'
        self.img = 'png1.png'
    
    @Rule(TimeProjectConditions(timeProject=MATCH.tp),
        AND (
            OR (
                ProjectConditions('Polymer'),
                ProjectConditions('JavaScript'),
                ProjectConditions('MVC'),
                ProjectConditions('Sprint')
            ),
            OR (
                ProjectConditions('REST'),
                ProjectConditions('Flask')
            ),
            OR (
                ProjectConditions('AWS'),
                ProjectConditions('GCP'),
                ProjectConditions('Azure')
            ),
            OR (
                ProjectConditions('REST'),
                ProjectConditions('Flask')
            )
        )
    )
    def rule_10(self,tp):
        recomendados = 4 + int(int(tp) / 4)
        self.message = 'Te recomendamos tener '+ str(recomendados) + ' recursos en tu equipo'
        self.img = 'png1.png'

    def get_recomendation(self):
        return self.message, self.img
