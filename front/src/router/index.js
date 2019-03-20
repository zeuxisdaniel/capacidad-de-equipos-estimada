import Vue from 'vue'
import Router from 'vue-router'
import ProjectPageComponent from '@/components/ProjectPageComponent'
import ProjectListPageComponent from '@/components/ProjectsListPageComponent'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'ProjectPage',
      component: ProjectPageComponent
    },
    {
      path: '/list/',
      name: 'ProjectListPage',
      component: ProjectListPageComponent
    }
  ]
})
