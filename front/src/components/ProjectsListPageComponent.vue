<template lang="pug">
    .projectslist-container
        template(v-for="project in getProjects()")
            .project-card
                .project-card-title
                    h2 {{ project.name }}
                .project-card-content
                    .project-card-text
                        .desc
                            strong Descripción:
                            |  {{ project.desc }}
                        .stats
                            .hrs.tooltip
                                span.tooltiptext Horas semanales
                                p {{ project.hours }} 
                                | HORAS
                            .dur.tooltip
                                span.tooltiptext Duración en meses
                                p {{ project.duration }}
                                | DURACIÓN
                            .rsc.tooltip
                                span.tooltiptext Recursos necesarios
                                p {{ project.resc }}
                                | RECURSOS
                    .tag-container
                            template(v-for="tech in project.techs")
                                span.tag-tec {{ tech.name }}
                    
        
    
</template>

<script>
export default {
    name:'ProjectsList',
    data(){
        return {

        }
    },
    methods:{
        getProjects(){
            var projects =
            [
                {   name: 'PROYECTO 1',
                    desc: `Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book`,
                    duration: 6,
                    hours: 40,
                    resc: 7,
                    techs: [    
                        { name:'Mongo'},
                        { name:'NoSQL'},
                        { name:'Polymer'}, 
                        { name:'JavaScript'}, 
                        { name:'Java'}, 
                        { name:'Python'}
                    ]
                },
                {   name: 'PROYECTO 2',
                    desc: `Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book`,
                    duration: 2,
                    hours: 32,
                    resc: 4,
                    techs: [
                        { name:'C++'},
                        { name:'R'},
                        { name:'C#'},
                        { name:'MVC'},
                        { name:'REST'}
                    ]
                },
                {   name: 'PROYECTO 3',
                    desc: `Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book`,
                    duration: 2,
                    hours: 32,
                    resc: 4,
                    techs: [
                        { name:'Ruby'},
                        { name:'Flask'},
                        { name:'Sprint'},
                        { name:'Security'},
                        { name:'Networking'}
                    ]
                }
            ]
            return projects;
        }
    }
    
}
</script>

<style scoped>

    .projectslist-container{
        display: flex;
    }
    
    .project-card{
        flex: 1;
        display: flex;
        flex-direction: column;
        
        color:#004481;
        cursor: pointer;
        border: none;
        background: #FFFF;
        margin: 10px;
        min-height: 350px;
        text-align: left;
        box-shadow: 0 10px 6px -6px #6666;
        transition: .5s;
    }

    .project-card:hover{
        box-shadow: 0 10px 20px -1px #4C4C4C;
        transform: scale(1.05);
    }

    .project-card-title{
        flex: 1;
        
        
        background: #2DCCC2;
        color: #ffffff;
        padding: 0 15px;
    }
    

    .project-card-content{
        display: flex;

        flex: 4;
    }

    .project-card-text{
        flex: 1.7;
        display: flex;
        flex-direction: column;

        font-size: .9rem;
        color: #666666;
        padding: 25px 15px 15px 15px;
    }

    .project-card-text .desc{
        flex: 2;
    }

    .project-card-text .stats{
        flex: 1;
        display: flex;
        flex-wrap: wrap;
    }

    .project-card-text .stats div{
        flex: 1;

        padding: 10px;
        font-size: .7rem;   
        text-align: center;
    }

    .project-card-text .stats div p{
        font-size: 2rem;
        text-align: center;
        margin: 0;
    }
    
    .tag-container{
        flex: 1;
        display: flex;
        flex-wrap: wrap;
        align-content: start;
        justify-content: flex-start;

        padding-top: 20px;
        padding-left: 10px;
        background: #004481;
    }

    .tag-tec{
        padding: 5px;
        font-size: .85rem;
        color: #FFFF;
        margin: 5px 5px;
        height: 20px;
        border-radius: 5px;
        background: #009EE5;
    }



    /* Tooltip container */
    .tooltip {
        position: relative;
        display: inline-block;
    }

    /* Tooltip text */
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 120px;
        background-color: #555;
        color: #fff;
        text-align: center;
        padding: 5px 0;
        border-radius: 6px;

        /* Position the tooltip text */
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -60px;

        /* Fade in tooltip */
        opacity: 0;
        transition: opacity 0.3s;
    }

    /* Tooltip arrow */
    .tooltip .tooltiptext::after {
        content: "";
        position: absolute;
        top: 100%;
        left: 50%;
        margin-left: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: #555 transparent transparent transparent;
    }

    /* Show the tooltip text when you mouse over the tooltip container */
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }


</style>
