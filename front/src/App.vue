<template>
  <div id="app">
    <div class="header">
      <img class="logo" src="@/assets/logoq.png">
      <img class="logo" src="@/assets/logo-next.png">
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
html,body{
  margin: 0 !important;
  padding: 0 !important;
}

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
  background-color: #D8D8D8;
}

.header{
  height:70px;
  background: #043263;
  padding: 15px;
}
.logo{
  height: 100%;
  float: left;
}
</style>
