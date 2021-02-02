<template>
  <div class="flex flex-col items-center">
    <img alt="Vue logo" class="bg-black w-64 m-10 rounded-lg" src="./assets/logo.png" />
    <Container />
  </div>
</template>

<script setup>
import "./index.css";
import Container from "./components/Container.vue";
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
