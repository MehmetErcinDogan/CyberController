<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <button v-on:click = "sendMessage('Hello World')">Send Message</button>
  <HelloWorld msg="Welcome to Your Vue.js App"/>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  },
  data: function(){
    return{
      connection: null
    }
  },
  methods:{
    sendMessage: function(message){
      console.log(this.connection);
      this.connection.send(message);
      console.log("message sent");
    }
  },
  created: function(){
    console.log("Starting connection to WebSocket Server");
    this.connection = new WebSocket("ws://localhost:5000");

    this.connection.onopen = function(event){
      console.log(event);
      console.log("Sucessfully connected to the echo WebSocket Server");
    }

    this.connection.onmessage = function(event){
      console.log(event);
      console.log(event.data);
      console.log("message recieved");
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
