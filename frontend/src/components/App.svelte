<script>
  import Model3D from "@components/Model3D.svelte";
  import { Circle } from "svelte-loading-spinners";
  let data;
  let loading = true;
  let message = "3D graph loading";
  let component = Model3D;
  (async () => {
    let res = await fetch("/assets/data.json");
    data = await res.json();
    console.log(data);
  })();
</script>

{#if loading}
  <div class="loading">
    <Circle size="60" unit="px" color="#E65127" />
    <h1>{message}</h1>
    <p>Best view on desktop</p>
    <p>You might experience performance issue on mobile device</p>
  </div>
{/if}

<svelte:component
  this={component}
  {data}
  on:unloading={() => {
    loading = false;
  }}
/>

<style>
  .loading {
    background-color: #e8e9ed;
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }
  * {
    font-family: sans-serif;
    text-align: center;
  }
  h1 {
    margin-top: 15px;
  }
  p {
    margin-top: 15px;
  }
</style>
