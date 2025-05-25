<script lang="ts">
  import DataDisplay from './lib/DataDisplay.svelte';
</script>

<main>
  <h1>FastAPI + Svelte Demo</h1>
  <p>This page demonstrates fetching data from a FastAPI backend.</p>
  
  <DataDisplay />
</main>

<style>
  main {
    font-family: Arial, sans-serif;
    padding: 20px;
    max-width: 800px;
    margin: auto;
    text-align: center;
  }
  h1 {
    color: #333;
  }
</style>
