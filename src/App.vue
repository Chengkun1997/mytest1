<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link> |
      <router-link to="/helloWorld">HelloWorld</router-link> |
      <router-link to="/demo1">Demo1</router-link> |
      <router-link to="/demo2">Demo2</router-link> |
      <router-link to="/demo2sample">Demo2sample</router-link> |
      <router-link to="/demo3">Demo3</router-link> |
      <router-link to="/cssTest">CssTest</router-link> |
      <router-link to="/cssAnimate">CssAnimate</router-link> |
      <router-link to="/demo5">Demo5</router-link> |
      <router-link to="/WebAIdemo">WebAIdemo</router-link> |
    </div>
    <router-view />
  </div>
</template>

<style>
  html,
  body,
  #app {
    /* width: 1920px;
    height: 1080px; */
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
  }

  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  #nav {
    position: absolute;
    top: 2%;
    padding: 10px;
    z-index: 99999;
  }

  #nav a {
    font-weight: bold;
    color: #2c3e50;
  }

  #nav a.router-link-exact-active {
    color: #42b983;
  }
</style>