<script>
  import { onMount, createEventDispatcher } from "svelte";
  import ForceGraph3D from "3d-force-graph";
  import { Mesh, SphereGeometry, MeshBasicMaterial } from "three";
  import SpriteText from "three-spritetext";
  export let data;
  let target;
  let loaded = false;
  const dispatch = createEventDispatcher();

  $: {
    data & init();
  }
  function init() {
    let counter = 0;
    try {
      let graph = ForceGraph3D();
      graph.d3Force("charge").strength(-250);
      graph(target)
        .graphData(data)
        .backgroundColor("#E8E9ED")
        .linkColor(() => "#606060")
        .nodeThreeObject((node) => {
          // use a sphere as a drag handle
          const obj = new Mesh(
            new SphereGeometry(2),
            new MeshBasicMaterial({
              depthWrite: false,
              transparent: true,
              opacity: 1,
            })
          );

          // add text sprite as child
          const sprite = new SpriteText(node.name);
          sprite.color = node.color;
          sprite.backgroundColor = "white";
          sprite.textHeight = node.textHeight;
          obj.add(sprite);

          return obj;
        })
        .onNodeHover((node) => (target.style.cursor = node ? "pointer" : null))
        .onNodeClick((node) => {
          // Aim at node from outside it
          const distance = 200;
          const distRatio = 1 + distance / Math.hypot(node.x, node.y, node.z);

          graph.cameraPosition(
            {
              x: node.x * distRatio,
              y: node.y * distRatio,
              z: node.z * distRatio,
            }, // new position
            node, // lookAt ({ x, y, z })
            3000 // ms transition duration
          );
          setTimeout(() => {
            window.open(node.id);
          }, 3000);
          //
        })
        .onEngineTick(() => {
          counter += 1;
          if (counter >= 80) {
            dispatch("unloading");
            loaded = true;
          }
        });
    } catch (e) {
      dispatch("error", {
        message: "WebGL error, switch to 2D mode.",
      });
    }
    setTimeout(() => {
      if (!loaded) {
        dispatch("error", {
          message: "Switch to 2D mode due to perfomance issue.",
        });
      }
    }, 8000);
  }
</script>

<div bind:this={target} />
