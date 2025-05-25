<script lang="ts">
  import { onMount } from 'svelte';
  import axios from 'axios';

  interface ApiResponse {
    message: string;
    source: string;
  }

  let data: ApiResponse | null = null;
  let error: string | null = null;

  onMount(async () => {
    try {
      // In development, Vite's proxy will handle this.
      // In production, this assumes the API is served under the same domain.
      const response = await axios.get<ApiResponse>('/api/data');
      data = response.data;
    } catch (e: any) {
      error = e.message || "An unknown error occurred";
      console.error("Error fetching data:", e);
    }
  });
</script>

<div>
  <h2>Data from Backend:</h2>
  {#if error}
    <p style="color: red;">Error: {error}</p>
  {/if}
  {#if data}
    <pre>{JSON.stringify(data, null, 2)}</pre>
  {:else if !error}
    <p>Loading data...</p>
  {/if}
</div>

<style>
  div {
    margin-top: 20px;
    padding: 10px;
    border: 1px solid #eee;
    border-radius: 5px;
  }
  pre {
    background-color: #f4f4f4;
    padding: 10px;
    border-radius: 3px;
  }
</style>
