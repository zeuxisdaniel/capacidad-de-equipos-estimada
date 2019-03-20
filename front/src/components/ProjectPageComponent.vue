<template lang="pug">
  .project-component-container
    .project-form-container
      form#project-form.form-project( @submit='sendCall()')
        .quick-input
          label Proyecto
          input(type='text' v-model="project.name")
        .quick-input
          label Descripción
          input(type='text' v-model="project.desc")
        .quick-input
          label Duración aproximada del Proyecto en meses 
          input(type='number' v-model="project.duration" placeholder="Máximo 24" :change="validate('proctime')")
        .quick-input
          label Hora semanales esperadas
          input(type='number' v-model="project.hours")
        .quick-input
          label Número de recursos
          input(type='number' v-model="project.resc")
        .quick-input
            label Technologías a utilizar
            multiselect(
              v-model="value",
              :max="limitopts",
              :options="getTechs()",
              :multiple="true",
              :close-on-select="false",
              :clear-on-select="false",
              :preserve-search="true",
              placeholder="Elige las tecnologías (Max. 4)"
              label="name",
              track-by="name",
              :preselect-first="true"
            )
              template(
                slot="selection"
                slot-scope="{ values, search, isOpen }"
              )
                span.multiselect__single(v-if="values.length && !isOpen")
                  | {{ values.length }} opciones seleccionadas
              template(slot='maxElements')
                span.multiselect__single
                  | Necesitas borrar un elemento para agregar otro (Presiona "Delete")
        .quick-input
            input.go-input(type='submit' value='Registrar') 
</template>


<script>
import Multiselect from 'vue-multiselect'


export default {
  name: 'Projects',
  components: {
    Multiselect
  },
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      project: {
        name: '',
        desc: '',
        duration: 0,
        hours: 0,
        resc: 0,
        techs: []
      },
      value: [],
      limitopts:4,
      from: '',
      to:''
    }
  },
  methods:{
    sendCall(){
      console.log(this.project);
      return;
    },
    validate(item){
      switch(item)
      {
        case 'proctime':{
          if( this.project.duration <= 0) { this.project.duration = 1 }
          else if(this.project.duration > 24) { this. project.duration = 24 }
        }
      }
    },
    getTechs(){
      var techs = [
        { name:'Mongo'},
        { name:'NoSQL'},
        { name:'Polymer'}, 
        { name:'JavaScript'}, 
        { name:'Java'}, 
        { name:'Python'}, 
        { name:'SQL'}, 
        { name:'AWS'}, 
        { name:'GCP'}, 
        { name:'Azure'},
        { name:'Go Lang'},
        { name:'.NET'},
        { name:'Ruby'},
        { name:'Flask'},
        { name:'Sprint'},
        { name:'Security'},
        { name:'Networking'},
        { name:'C++'},
        { name:'R'},
        { name:'C#'},
        { name:'MVC'},
        { name:'REST'}
      ];

      return techs;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  /** Select Styling **/
  .multiselect{
    margin: 10px;
    width: inherit !important;
  }
  .multiselect__tags{
    border: 0.1px !important;
    border-radius: 0 !important;
    font-size: 18px !important;
    padding: 8px !important;
    box-shadow: 0 10px 6px -6px #6666;
  }
  .multiselect__single{
    position: inherit !important;
  }
  .multiselect__option--selected.multiselect__option--highlight{
    background: #1464A5 !important;
  }
  .multiselect__option.multiselect__option--highlight{
    background: #49A5E6 !important;
  }

</style>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<style scoped>

.project-form-container{
  display: flex;
  /* flex-direction: row; */
  font-size: 18px;
  color: #424242;
  padding: 20px;
  flex-wrap: wrap;
}

.form-project{
  display: flex;
  flex: 1;
  /* flex-direction: column; */
  flex-wrap: wrap;
  /* align-content: center; */
  /* max-width: 600px; */
}
.form-project label{
  margin: 10px 10px 5px 10px;
  text-align: left;
}
.form-project input{
  margin: 10px;
  border: 0.1px;
  padding: 12px;
  font-size: 18px;
  box-shadow: 0 10px 6px -6px #6666;
}
.form-project input[type="number,text"]{
  margin-top: 5px;
}

.form-project input[type=submit]{
  background: #49A5E6;
  color: #ffff;
}

.form-project input[type=submit]:hover{
  background: #2A86CA;
  cursor: pointer;
}

.quick-input{
  display: flex;
  flex-direction: column;
}

@media screen and (max-width:640px) {
  /* reglas CSS */
  .project-form-container{
    justify-content: center;
  }
}
@media screen and (max-width:1024px) and (min-width:640px) {
  /* reglas CSS */
}

@media screen and (min-width:1024px) {
  /* reglas CSS */
  .project-form-container{
  }

  .quick-input{
    flex: 0 0 50%;
  }
}

</style>

