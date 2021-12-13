<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <command/>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
// import Command from '@/components/Command'
import Command from '../components/Command.vue'

export default {
  name: 'Home',
  components: {
    // HelloWorld
    Command
  }
}
</script>
