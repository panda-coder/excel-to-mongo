<script>
    import Dropzone from "svelte-file-dropzone";
    import axios from "axios";
  let files = [];
  let fileData = [];
  function processRawCSV(data) {
    const output = [];
    const rows = data.split("\n");
    for (let i = 0; i < rows.length; i++) {
      const cells = rows[i].split(",");
      output.push(cells);
    }
    return output;
  }
  function handleFilesSelect(e) {
    files = e.detail.acceptedFiles;
    for (let i = 0; i < files.length; i++) {
      const reader = new FileReader();
      reader.onload = async () => {
        const file = new FormData();

        console.log(files[i])
        file.append('file', files[i], files[i].name);
        const res = await axios.post(
        "http://localhost:8080/save",
        file,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
        );
        alert(res.data.msg)
      };
      console.log(reader.readAsText(files[i]));
    }
  }
</script>


  
<div class="container h-full mx-auto flex justify-center items-center">
	<div class="space-y-10 text-center">
		<h2>Upload CSV file and preview same</h2>
        <Dropzone on:drop={handleFilesSelect} multiple={false} accept=".xlsx" />

        {#each files as item}
        <h2>{item.name}</h2>
        {/each}

        <table border="1">
        {#each fileData as row}
            <tr>
            {#each row as item}
                <td>{item}</td>
            {/each}
            </tr>
        {/each}
        </table>

	</div>

	<style lang="postcss">
		figure {
			@apply flex relative flex-col;
		}
		figure svg,
		.img-bg {
			@apply w-64 h-64 md:w-80 md:h-80;
		}
		.img-bg {
			@apply bg-gradient-to-r from-primary-300 to-warning-300;
			@apply absolute z-[-1] rounded-full blur-[64px];
			animation: pulse 5s cubic-bezier(0, 0, 0, 0.5) infinite;
		}
		@keyframes pulse {
			50% {
				transform: scale(1.5);
			}
		}
	</style>
</div>
